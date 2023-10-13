from fastapi.responses import HTMLResponse
import main

html = ""

with open("src/index.html", "r") as f:
    html = f.read()


@app.get("/")
async def get():
    return HTMLResponse(html)