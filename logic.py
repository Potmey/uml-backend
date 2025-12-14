import re


def extract_agents(text: str) -> list[str]:
    keywords = [
        "employee", "manager", "customer", "client",
        "department", "service", "system", "team"
    ]

    agents = set()

    sentences = re.split(r"[.,]", text.lower())
    for s in sentences:
        for kw in keywords:
            if kw in s:
                agent = s.strip().split()[:3]
                agents.add(" ".join(agent).title())

    return list(agents) or ["User", "System"]


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
