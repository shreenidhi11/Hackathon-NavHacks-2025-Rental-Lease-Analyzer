# This is a simple template with placeholders to give to the LLM
PROMPT_TEMPLATE = """
You are an expert legal assistant specializing in rental agreements.
Your task is to extract specific, critical information from the lease text provided.
Analyze the text and populate *all* fields in the JSON object.

**CRITICAL RULES:**
1.  **Strictly Adhere to Schema:** Each field's summary must *only* contain information directly related to that field's description from the schema.
2.  **Handle Missing Information:** If information for a specific field is not present in the text, the value for that field must be *only* the string "Not found".
3.  **No Data Contamination:** Do *not* mention the absence of information for one field (e.g., "Guest policy was not found") in the summary of *another* field.

**Field Instructions:**
* For policies (like 'pet_policy' or 'guest_policy'), summarize the rule.
* For fees (like 'late_fee_policy'), state the cost and conditions.

Return *only* a JSON object that strictly follows this Pydantic schema:
{schema}

Here is the lease text:
---
{lease_text}
---

Return *only* the JSON. Do not add any conversational text or markdown.
"""

