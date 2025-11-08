# JourneyToTheEye Backend

FastAPI backend for star visualization with pathfinding algorithms (Dijkstra's & A*) using KD-tree spatial queries.

## Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

```bash
uvicorn main:app --reload
```

Server runs at: `http://localhost:8000`

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/stars` - Get star count
- `GET /api/stars/all` - Get all stars with KD-tree data
- `GET /api/dijkstra?fuel=30&start=0&end=1` - Dijkstra's pathfinding
- `GET /api/astar?fuel=30&start=0&end=1` - A* pathfinding
