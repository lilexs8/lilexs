const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

async function request(path: string, options: RequestInit = {}) {
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error(`API error ${res.status} on ${path}`);
  }
  return res.json();
}

export const api = {
  missionControl: (organizationId = 1) =>
    request(`/mission-control?organization_id=${organizationId}`),

  listAssets: () => request(`/assets`),
  createAsset: (payload: any) =>
    request(`/assets`, { method: "POST", body: JSON.stringify(payload) }),

  listFindings: () => request(`/findings`),
  createFinding: (payload: any) =>
    request(`/findings`, { method: "POST", body: JSON.stringify(payload) }),

  listAttackPaths: () => request(`/attack-paths`),
  createAttackPath: (payload: any) =>
    request(`/attack-paths`, { method: "POST", body: JSON.stringify(payload) }),

  listThreatMemory: () => request(`/threat-memory`),
  createThreatMemory: (payload: any) =>
    request(`/threat-memory`, { method: "POST", body: JSON.stringify(payload) }),

  listReports: () => request(`/reports`),
  createReport: (payload: any) =>
    request(`/reports`, { method: "POST", body: JSON.stringify(payload) }),

  askLix: (question: string, context?: string) =>
    request(`/lix/chat`, {
      method: "POST",
      body: JSON.stringify({ question, context }),
    }),
};
