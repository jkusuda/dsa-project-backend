from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from backend import *
from pathlib import Path

app = FastAPI(
    title="JourneyToTheEye Backend",
    description="FastAPI backend for our star visualization.",
    version="1.0.0",
)


# Load star nodes once
def get_star_nodes():
    base_dir = Path(__file__).parent
    filepath = base_dir / "stars.csv"
    star_nodes = load_stars(str(filepath))
    print(f"Loaded {len(star_nodes)} stars")
    return star_nodes


# Cache graphs by fuel range
def get_graph(fuel: float):
    return build_graph(get_star_nodes(), fuel)


@app.get("/api/health")
def health():
    return { 
            "running" 
        }


@app.get("/api/dijkstra")
def dijkstra_call(fuel: float = 30, start: int = 0, end: int = 1):
    nodes = get_star_nodes()
    graph = get_graph(fuel)
    index_sequence, distance = djikstras(nodes, graph, start, end)
    
    return {
        "sequence": [nodes[i].id for i in index_sequence],
        "distance": distance,
        "algorithm": "dijkstra"
    }


@app.get("/api/astar")
def astar_call(fuel: float = 30, start: int = 0, end: int = 1):
    nodes = get_star_nodes()
    graph = get_graph(fuel)
    index_sequence, distance = astar(nodes, graph, start, end)
    
    return {
        "sequence": [nodes[i].id for i in index_sequence],
        "distance": distance,
        "algorithm": "astar"
    }


@app.get("/api/stars")
def get_sample_stars():
    try:
        nodes = get_star_nodes()
        return {
            "status": "running",
            "star_count": len(nodes)
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


@app.get("/api/stars/all")
def get_all_stars():

    return {
        "data": build_kdtree_data(get_star_nodes()),
        "total": len(get_star_nodes())
    }