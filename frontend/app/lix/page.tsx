"use client";

import { useState } from "react";
import Sidebar from "../../components/Sidebar";
import { api } from "../../lib/api";

type Message = { role: "user" | "lix"; content: string };

export default function LixPage() {
  const [messages, setMessages] = useState<Message[]>([
    { role: "lix", content: "Lix is online. Ask about risks, findings, reports, assets, or remediation priorities." },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function send() {
    const question = input.trim();
    if (!question || loading) return;

    setMessages((m) => [...m, { role: "user", content: question }]);
    setInput("");
    setLoading(true);

    try {
      const res = await api.askLix(question);
      setMessages((m) => [...m, { role: "lix", content: res.answer }]);
    } catch (e) {
      setMessages((m) => [
        ...m,
        { role: "lix", content: "Lix could not reach the backend. Make sure the API is running." },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="layout">
      <Sidebar />
      <section className="content">
        <div className="topbar">
          <div>
            <h1>Ask Lix</h1>
            <p>Your defensive security intelligence assistant.</p>
          </div>
        </div>

        <div className="panel large chat-panel">
          <div className="chat-log">
            {messages.map((m, i) => (
              <div key={i} className={`chat-bubble ${m.role}`}>
                <strong>{m.role === "lix" ? "Lix" : "You"}</strong>
                <p>{m.content}</p>
              </div>
            ))}
            {loading && <div className="chat-bubble lix"><strong>Lix</strong><p>Thinking…</p></div>}
          </div>

          <div className="chat-input-row">
            <input
              placeholder="Ask Lix about risks, findings, attack paths, or reports..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && send()}
            />
            <button onClick={send} disabled={loading}>Send</button>
          </div>
        </div>
      </section>
    </main>
  );
}
