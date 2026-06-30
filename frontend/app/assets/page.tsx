import Sidebar from "../../components/Sidebar";
import { api } from "../../lib/api";

export default async function AssetsPage() {
  let assets: any[] = [];
  let error: string | null = null;

  try {
    assets = await api.listAssets();
  } catch (e) {
    error = "Could not reach the LN1 backend.";
  }

  return (
    <main className="layout">
      <Sidebar />
      <section className="content">
        <div className="topbar">
          <div>
            <h1>Assets</h1>
            <p>Tracked systems across your organization.</p>
          </div>
        </div>

        {error && <div className="panel error">{error}</div>}

        <div className="panel large">
          <table className="data-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Type</th>
                <th>IP / Domain</th>
                <th>Criticality</th>
                <th>Risk Level</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {assets.map((a) => (
                <tr key={a.id}>
                  <td>{a.name}</td>
                  <td>{a.asset_type}</td>
                  <td>{a.ip_address || a.domain || "—"}</td>
                  <td><span className={`pill ${a.criticality}`}>{a.criticality}</span></td>
                  <td><span className={`pill ${a.risk_level}`}>{a.risk_level}</span></td>
                  <td>{a.status}</td>
                </tr>
              ))}
              {assets.length === 0 && !error && (
                <tr><td colSpan={6}>No assets yet. Seed the database or add one via the API.</td></tr>
              )}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  );
}
