import re

ROLE_KEYWORDS = [
    "employee", "manager", "customer", "client",
    "user", "system", "department", "service",
    "team", "hr", "finance", "support"
]

ACTION_VERBS = [
    "submit", "submits",
    "approve", "approves",
    "review", "reviews",
    "process", "processes",
    "reject", "rejects",
    "inform", "informs",
    "check", "checks",
    "analyze", "analyzes",
]

def extract_agents(text: str) -> list[str]:
    agents = set()

    sentences = re.split(r"[.]", text.lower())

    for sentence in sentences:
        words = sentence.strip().split()
        if not words:
            continue

        # ищем роль как первое существительное
        for word in words[:4]:
            if word in ROLE_KEYWORDS:
                agents.add(word.capitalize())
                break

    return list(agents)


def extract_actions(text: str) -> list[str]:
    actions = []

    sentences = re.split(r"[.]", text.lower())
    for s in sentences:
        for verb in ACTION_VERBS:
            if verb in s:
                actions.append(s.strip())
                break

    return actions


def extract_entities(text: str) -> list[str]:
    words = re.findall(r"\b\w+\b", text.lower())

    entities = set()
    for w in words:
        if w in {"submit", "review", "approve", "reject", "process"}:
            entities.add(w)

    return list(entities)


def generate_plantuml(text: str, agents: list[str]) -> str:
    uml = ["@startuml"]

    for i, a in enumerate(agents):
        uml.append(f"participant \"{a}\" as P{i}")

    if len(agents) >= 2:
        uml.append(f"P0 -> P1 : {text[:50]}")

    uml.append("@enduml")
    return "\n".join(uml)
