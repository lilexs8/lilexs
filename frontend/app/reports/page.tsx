import Sidebar from "../../components/Sidebar";
import { api } from "../../lib/api";

export default async function ReportsPage() {
  let reports: any[] = [];
  let error: string | null = null;

  try {
    reports = await api.listReports();
  } catch (e) {
    error = "Could not reach the LN1 backend.";
  }

  return (
    <main className="layout">
      <Sidebar />
      <section className="content">
        <div className="topbar">
          <div>
            <h1>Reports</h1>
            <p>Executive and technical reports generated for your organization.</p>
          </div>
        </div>

        {error && <div className="panel error">{error}</div>}

        <div className="finding-list">
          {reports.map((r) => (
            <div className="panel finding" key={r.id}>
              <div className="finding-head">
                <h3>{r.title}</h3>
                <span className="pill">{r.report_type}</span>
              </div>
              <p>{r.content}</p>
              <p className="muted">Language: {r.language}</p>
            </div>
          ))}
          {reports.length === 0 && !error && (
            <div className="panel">No reports generated yet.</div>
          )}
        </div>
      </section>
    </main>
  );
}
