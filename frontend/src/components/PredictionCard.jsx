function PredictionCard({ prediction }) {
  if (!prediction) {
    return null;
  }

  return (
    <section className="card prediction-card">
      <h2>Threat Detection</h2>

      <div className="prediction">
        {prediction.prediction}
      </div>

      <p>
        Confidence:{" "}
        {(prediction.confidence * 100).toFixed(2)}%
      </p>
    </section>
  );
}

export default PredictionCard;