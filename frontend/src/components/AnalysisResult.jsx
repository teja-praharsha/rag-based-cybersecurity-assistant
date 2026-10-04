import PredictionCard from "./PredictionCard";
import FeatureTable from "./FeatureTable";
import SourceList from "./SourceList";

function AnalysisResult({ result }) {
  if (!result) {
    return null;
  }

  return (
    <div className="results">

      <PredictionCard
        prediction={result.prediction}
      />

      <FeatureTable
        features={result.feature_explanations}
      />

      <SourceList
        sources={result.retrieved_sources}
      />

      <section className="card">
        <h2>AI Security Analysis</h2>

        <div className="explanation">
          {result.ai_explanation}
        </div>
      </section>

    </div>
  );
}

export default AnalysisResult;