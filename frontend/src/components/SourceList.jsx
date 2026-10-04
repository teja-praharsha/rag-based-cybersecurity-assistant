function SourceList({ sources }) {
  if (!sources || sources.length === 0) {
    return null;
  }

  return (
    <section className="card">
      <h2>Retrieved Knowledge</h2>

      <ul>
        {sources.map((source, index) => (
          <li key={index}>
            <strong>{source.source}</strong>
            {" — "}
            {source.file}
          </li>
        ))}
      </ul>
    </section>
  );
}

export default SourceList;