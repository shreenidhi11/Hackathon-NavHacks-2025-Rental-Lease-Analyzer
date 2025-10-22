import React, { useState } from "react";

function FileSummarizer() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setSummary(null);
    setError("");
  };

  const handleSummarize = async () => {
    if (!file) {
      setError("Please upload a file first!");
      return;
    }

    setLoading(true);
    setError("");
    setSummary(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/summarize", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }

      const data = await response.json();
      setSummary(data);
    } catch (err) {
      setError(`Failed to summarize: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.page}>
      <div
        style={{
          ...styles.container,
          transform: summary ? "translateY(-6px)" : "translateY(0)",
          transition: "transform 0.6s ease",
        }}
      >
        <h1 style={styles.title}>Renter Summarizer</h1>
        <p>Upload your lease file (.pdf, .txt, or .docx)</p>

        <input type="file" accept=".pdf,.txt,.docx" onChange={handleFileChange} />
        <button onClick={handleSummarize} disabled={loading} style={styles.button}>
          {loading ? "Summarizing..." : "Get Summary"}
        </button>

        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>

      {summary && (
        <div style={styles.resultsSection}>
          {/* <h2 style={styles.subtitle}>Summary</h2> */}
          <div style={styles.gridContainer}>
            {Object.entries(summary).map(([key, value]) => (
              <div key={key} className="card" style={styles.card}>
                <h3 style={styles.cardTitle}>
                  {key.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase())}
                </h3>
                <p style={styles.cardText}>{value}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

const styles = {
  page: {
    fontFamily: "Arial, sans-serif",
    textAlign: "center",
    backgroundColor: "#f4f6f9",
    minHeight: "100vh",
    padding: "40px 20px",
    boxSizing: "border-box",
  },
  container: {
    background: "white",
    borderRadius: "12px",
    padding: "25px 30px",
    width: "100%",
    maxWidth: "700px",
    margin: "0 auto",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
  },
  title: {
    fontSize: "26px",
    marginBottom: "8px",
  },
  subtitle: {
    marginTop: "40px",
    fontSize: "22px",
  },

  button : {
  background: "linear-gradient(135deg, #34d399, #059669)",
  color: "white",
  fontSize: "1rem",
  padding: "12px 24px",
  border: "none",
  borderRadius: "10px",
  cursor: "pointer",
  transition: "all 0.3s ease",
  boxShadow: "0 4px 12px rgba(5, 150, 105, 0.2)"
},
input : {
  background: "linear-gradient(135deg, #34d399, #059669)",
  color: "white",
  fontSize: "1rem",
  padding: "12px 24px",
  border: "none",
  borderRadius: "10px",
  cursor: "pointer",
  transition: "all 0.3s ease",
  boxShadow: "0 4px 12px rgba(5, 150, 105, 0.2)"
},

  
//   button: {
//     marginTop: "12px",
//     padding: "10px 18px",
//     fontSize: "16px",
//     borderRadius: "8px",
//     cursor: "pointer",
//     backgroundColor: "#4CAF50",
//     color: "white",
//     border: "none",
//     transition: "background-color 0.3s ease",
//   },
  resultsSection: {
    marginTop: "50px",
    textAlign: "center",
  },
  gridContainer: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)", // 3 per row
    gap: "20px",
    marginTop: "20px",
    maxWidth: "1000px",
    marginLeft: "auto",
    marginRight: "auto",
  },
  card: {
    backgroundColor: "#fff",
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "15px 20px",
    textAlign: "left",
    boxShadow: "0px 4px 6px rgba(0,0,0,0.1)",
    transition: "transform 0.3s ease, box-shadow 0.3s ease",
  },
  cardTitle: {
    marginBottom: "10px",
    fontSize: "17px",
    color: "#333",
  },
  cardText: {
    fontSize: "15px",
    color: "#555",
    lineHeight: "1.5",
  },
};

// Add hover effect for cards
const styleSheet = document.createElement("style");
styleSheet.innerHTML = `
  .card:hover {
    transform: translateY(-5px);
  }
`;
document.head.appendChild(styleSheet);

export default FileSummarizer;