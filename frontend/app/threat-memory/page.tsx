import Sidebar from "../../components/Sidebar";
import { api } from "../../lib/api";

export default async function ThreatMemoryPage() {
  let memories: any[] = [];
  let error: string | null = null;

  try {
    memories = await api.listThreatMemory();
  } catch (e) {
    error = "Could not reach the LN1 backend.";
  }

  return (
    <main className="layout">
      <Sidebar />
      <section className="content">
        <div className="topbar">
          <div>
            <h1>Threat Memory</h1>
            <p>Recurring risks and trends Lix has tracked over time.</p>
          </div>
        </div>

        {error && <div className="panel error">{error}</div>}

        <div className="finding-list">
          {memories.map((m) => (
            <div className="panel finding" key={m.id}>
              <div className="finding-head">
                <h3>{m.title}</h3>
                <span className={`pill ${m.severity}`}>{m.severity}</span>
              </div>
              <p>{m.summary}</p>
              <p className="muted"><strong>Type:</strong> {m.memory_type} · <strong>Trend:</strong> {m.trend}</p>
            </div>
          ))}
          {memories.length === 0 && !error && (
            <div className="panel">No threat memory entries yet.</div>
          )}
        </div>
      </section>
    </main>
  );
}
