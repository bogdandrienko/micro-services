import random
import aiohttp
from fastapi import FastAPI


app = FastAPI()


@app.get("/api")
async def api():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8005/api") as response:
            return await response.json()
    # logs: list[dict] = [
    #     {"id": x, "title": f"Title {x}", "value": random.randint(1, 10000)} for x in range(1, 10)
    # ]
    # name = "Sholpan"
    # return name


if __name__ == "__main__":
    pass
