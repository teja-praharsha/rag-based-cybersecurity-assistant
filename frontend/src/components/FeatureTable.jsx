function FeatureTable({ features }) {
  if (!features || features.length === 0) {
    return null;
  }

  return (
    <section className="card">
      <h2>Model Explanation</h2>

      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>Value</th>
            <th>Importance</th>
          </tr>
        </thead>

        <tbody>
          {features.map((item, index) => (
            <tr key={index}>
              <td>{item.feature}</td>
              <td>{Number(item.value).toFixed(4)}</td>
              <td>
                {Number(item.importance).toFixed(4)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default FeatureTable;