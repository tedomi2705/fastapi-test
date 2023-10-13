import asyncio
import random
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import websockets

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://api.tedomi.tk:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


async def send_random_data(websocket: WebSocket):
    while True:
        data = {
            "Hiếu óc con chó": random.randint(1, 10),
            "Hiếu ngu vkl": random.randint(1, 10),
        }
        try:
            await websocket.send_json(data)
            await asyncio.sleep(1)
        except websockets.exceptions.ConnectionClosedOK:
            break


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        await send_random_data(websocket)
    except websockets.exceptions.ConnectionClosedOK:
        pass
