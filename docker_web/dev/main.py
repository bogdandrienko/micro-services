import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return "Index Page"


@app.get("/api")
async def api():
    logs: list[dict] = [
        {"id": x, "title": f"Title {x}", "value": random.randint(1, 10000)} for x in range(1, 100)
    ]
    return logs


if __name__ == "__main__":
    pass
