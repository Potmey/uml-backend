from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from logic import extract_agents, extract_entities, generate_plantuml

app = FastAPI(title="UML Backend API")

# 🔓 CORS (обязательно для GitHub Pages)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProcessRequest(BaseModel):
    text: str

class ProcessResponse(BaseModel):
    plantuml: str
    entities: list[str]
    agents: list[str]

@app.post("/analyze")
def analyze_process(data: ProcessRequest):
    text = data.text

    agents = extract_agents(text)
    entities = extract_entities(text)
    plantuml = generate_plantuml(text, agents)

    return {
        "plantuml": plantuml,
        "entities": entities,
        "agents": agents
    }

