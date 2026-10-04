import { useState } from "react";

import Header from "./components/Header";
import AnalysisResult from "./components/AnalysisResult";
import { analyzeTraffic } from "./services/api";


function App() {

  const [input, setInput] = useState(
    `{
  "Flow_Duration": 1000,
  "Total_Fwd_Packets": 10,
  "Total_Backward_Packets": 5,
  "Total_Length_of_Fwd_Packets": 500,
  "Total_Length_of_Bwd_Packets": 300
}`
  );

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");


  const handleAnalyze = async () => {

    setLoading(true);
    setError("");

    try {

      const features = JSON.parse(input);

      const response = await analyzeTraffic(
        features
      );

      setResult(response);

    } catch (error) {

      setError(
        error.response?.data?.detail ||
        error.message ||
        "Unable to analyze traffic."
      );

    } finally {

      setLoading(false);

    }
  };


  return (
    <div className="app">

      <Header />

      <main>

        <section className="hero">

          <h2>
            AI-Powered Cybersecurity Analysis
          </h2>

          <p>
            Detect threats, understand model decisions,
            retrieve trusted cybersecurity knowledge,
            and generate explainable security recommendations.
          </p>

        </section>


        <section className="card">

          <h2>Network Traffic Input</h2>

          <p>
            Enter CIC-IDS2017 feature values as JSON.
          </p>

          <textarea
            value={input}
            onChange={(event) =>
              setInput(event.target.value)
            }
          />

          <button
            onClick={handleAnalyze}
            disabled={loading}
          >
            {loading
              ? "Analyzing..."
              : "Analyze Traffic"}
          </button>

          {error && (
            <div className="error">
              {error}
            </div>
          )}

        </section>


        <AnalysisResult
          result={result}
        />

      </main>

    </div>
  );
}

export default App;