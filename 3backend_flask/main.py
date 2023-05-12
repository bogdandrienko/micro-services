import random
import aiohttp
from flask import Flask


app = Flask(__name__)


@app.route("/api")
async def api():
    # todo LOGIC
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8004/api") as response:
            return await response.json()
    # logs: list[dict] = [
    #     {"id": x, "title": f"Title {x}", "value": random.randint(1, 10000)} for x in range(1, 10)
    # ]
    # return logs


if __name__ == "__main__":
    app.run(debug=True)
