import json
from fastapi.openapi.utils import get_openapi
from src.main import app

def export_openapi(output: str = "openapi.json"):
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    with open(output, "w") as f:
        json.dump(schema, f, indent=2)

if __name__ == "__main__":
    export_openapi()
