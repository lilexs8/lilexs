import Sidebar from "../components/Sidebar";
import { api } from "../lib/api";

export default async function Page() {
  let data: any = null;
  let error: string | null = null;

  try {
    data = await api.missionControl();
  } catch (e: any) {
    error = "Could not reach the LN1 backend. Make sure the API is running.";
  }

  return (
    <main className="layout">
      <Sidebar />

      <section className="content">
        <div className="topbar">
          <div>
            <h1>Mission Control</h1>
            <p>Security intelligence powered by Lix.</p>
          </div>
          <button>Start New Scan</button>
        </div>

        {error && <div className="panel error">{error}</div>}

        {data && (
          <>
            <div className="cards">
              <div className="card"><span>Security Score</span><strong className="lime">{data.security_score}/100</strong><small>Current posture</small></div>
              <div className="card"><span>Assets</span><strong>{data.assets}</strong><small>Tracked systems</small></div>
              <div className="card"><span>Findings</span><strong>{data.open_findings}</strong><small>Open risks</small></div>
              <div className="card"><span>Attack Paths</span><strong>{data.attack_paths}</strong><small>Connected paths</small></div>
            </div>

            <div className="grid">
              <div className="panel large">
                <h2>Attack Path Intelligence</h2>
                <div className="path">
                  <div>Internet</div><span>→</span><div>Web Server</div><span>→</span><div>Identity</div><span>→</span><div>Database</div>
                </div>
              </div>
              <div className="panel">
                <h2>Lix</h2>
                <p>{data.lix_priority}</p>
                <a href="/lix"><button style={{ marginTop: 12 }}>Open Lix Chat</button></a>
              </div>
            </div>
          </>
        )}
      </section>
    </main>
  );
}
