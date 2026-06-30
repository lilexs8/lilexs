import Sidebar from "../../components/Sidebar";
import { api } from "../../lib/api";

export default async function FindingsPage() {
  let findings: any[] = [];
  let error: string | null = null;

  try {
    findings = await api.listFindings();
  } catch (e) {
    error = "Could not reach the LN1 backend.";
  }

  return (
    <main className="layout">
      <Sidebar />
      <section className="content">
        <div className="topbar">
          <div>
            <h1>Findings</h1>
            <p>Open security risks identified across your environment.</p>
          </div>
        </div>

        {error && <div className="panel error">{error}</div>}

        <div className="finding-list">
          {findings.map((f) => (
            <div className="panel finding" key={f.id}>
              <div className="finding-head">
                <h3>{f.title}</h3>
                <span className={`pill ${f.severity}`}>{f.severity}</span>
              </div>
              <p>{f.description}</p>
              {f.business_impact && <p className="muted"><strong>Business impact:</strong> {f.business_impact}</p>}
              {f.recommendation && <p className="muted"><strong>Recommendation:</strong> {f.recommendation}</p>}
              <span className="status">{f.status}</span>
            </div>
          ))}
          {findings.length === 0 && !error && (
            <div className="panel">No findings yet.</div>
          )}
        </div>
      </section>
    </main>
  );
}
