from app.core.config import settings

SYSTEM_PROMPT = (
    "You are Lix, the defensive security intelligence assistant inside LN1, "
    "a security posture management platform built by Lilexs. "
    "You help authorized users understand findings, attack paths, asset risk, "
    "and remediation priorities. Stay strictly within authorized defensive "
    "security guidance: risk explanation, prioritization, remediation advice, "
    "and reporting. Never provide exploit code or offensive attack instructions. "
    "Keep answers concise and actionable."
)


def _rule_based_answer(question: str) -> str:
    """Fallback used when no Claude API key is configured."""
    q = question.lower()

    if "priority" in q or "fix" in q:
        return "Priority One: address critical findings connected to identity, exposed services, and sensitive assets."
    if "attack path" in q:
        return "Attack Path Intelligence links assets and findings to show how weaknesses may combine into business risk."
    if "report" in q:
        return "Lix can generate executive and technical reports with business impact and remediation guidance."
    return "Lix is online. Ask about risks, findings, reports, assets, or remediation priorities."


def _claude_answer(question: str, context: str | None) -> str | None:
    """Calls the real Claude API if a key is configured. Returns None on any failure
    so the caller can fall back to rule-based mode instead of breaking the request."""
    if not settings.claude_api_key or settings.claude_api_key == "replace_later":
        return None

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=settings.claude_api_key)

        user_content = question
        if context:
            user_content = f"Context:\n{context}\n\nQuestion:\n{question}"

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_content}],
        )

        parts = [block.text for block in response.content if getattr(block, "type", None) == "text"]
        text = "\n".join(parts).strip()
        return text or None
    except Exception:
        # Any SDK/network/auth error: fail safe to rule-based mode rather than 500.
        return None


def ask_lix(question: str, context: str | None = None) -> dict:
    answer = _claude_answer(question, context)
    mode = "claude"

    if answer is None:
        answer = _rule_based_answer(question)
        mode = "rule-based"

    return {
        "assistant": "Lix",
        "answer": answer,
        "mode": mode,
        "scope": "authorized defensive security intelligence",
    }
