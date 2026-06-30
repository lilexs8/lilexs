import Sidebar from "../../components/Sidebar";
import { api } from "../../lib/api";

export default async function AttackPathsPage() {
  let paths: any[] = [];
  let error: string | null = null;

  try {
    paths = await api.listAttackPaths();
  } catch (e) {
    error = "Could not reach the LN1 backend.";
  }

  return (
    <main className="layout">
      <Sidebar />
      <section className="content">
        <div className="topbar">
          <div>
            <h1>Attack Paths</h1>
            <p>How individual weaknesses connect into business risk.</p>
          </div>
        </div>

        {error && <div className="panel error">{error}</div>}

        <div className="finding-list">
          {paths.map((p) => (
            <div className="panel finding" key={p.id}>
              <div className="finding-head">
                <h3>{p.name}</h3>
                <span className={`pill ${p.risk_level}`}>{p.risk_level}</span>
              </div>
              <p>{p.path_summary}</p>
              {p.business_impact && <p className="muted"><strong>Business impact:</strong> {p.business_impact}</p>}
              {p.lix_analysis && <p className="muted"><strong>Lix analysis:</strong> {p.lix_analysis}</p>}
              <span className="status">{p.status}</span>
            </div>
          ))}
          {paths.length === 0 && !error && (
            <div className="panel">No attack paths recorded yet.</div>
          )}
        </div>
      </section>
    </main>
  );
}
