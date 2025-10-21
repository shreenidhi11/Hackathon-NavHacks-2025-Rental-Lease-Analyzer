import json
import os
import io
import uvicorn
import PyPDF2
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware


from models.lease import Lease
from prompts.prompt import PROMPT_TEMPLATE

#load the variables from the environment to the main file
load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Initialize the instance of fastAPI and configure the CORS policy
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.post("/summarize", response_model=Lease)
async def summarize_lease(file: UploadFile = File(...)):
    """
    Receives a lease file (PDF or TXT or DOCX), extracts text, queries Gemini,
    and returns a structured report.
    """
    lease_text = ""
    contents = await file.read()

    # --- File Processing Logic ---
    if file.filename.endswith('.pdf'):
        try:
            # Read PDF from in-memory bytes
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
            for page in pdf_reader.pages:
                lease_text += page.extract_text()
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error parsing PDF: {e}")

    elif file.filename.endswith('.txt'):
        try:
            # Decode text file from bytes
            lease_text = contents.decode('utf-8')
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error parsing TXT file: {e}")
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a .pdf or .txt file.")

    if not lease_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract any text from the file.")

    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
        )
    )

    schema_string = json.dumps(Lease.model_json_schema(), indent=2)

    prompt = PROMPT_TEMPLATE.format(
        lease_text=lease_text,
        schema=schema_string
    )

    response = await model.generate_content_async(prompt)
    print(response.text)

    return Lease.model_validate_json(response.text)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
