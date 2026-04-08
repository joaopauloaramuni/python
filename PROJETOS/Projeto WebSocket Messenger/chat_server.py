import asyncio
import websockets

clientes = {}

async def broadcast(msg):
    for ws in list(clientes.keys()):
        try:
            await ws.send(msg)
        except:
            pass

async def handler(websocket):
    try:
        # Primeiro recebe o nickname
        nickname = await websocket.recv()
        clientes[websocket] = nickname

        await broadcast(f"🔵 {nickname} entrou no chat")

        async for mensagem in websocket:
            nome = clientes[websocket]
            
            if mensagem == "__typing__":
                await broadcast(f"__typing__:{nome}")
            else:
                await broadcast(f"{nome}: {mensagem}")

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        if websocket in clientes:
            nome = clientes[websocket]
            del clientes[websocket]
            await broadcast(f"🔴 {nome} saiu do chat")

async def main():
    servidor = await websockets.serve(handler, "0.0.0.0", 8765)
    print("Servidor rodando em ws://0.0.0.0:8765")
    await servidor.wait_closed()

asyncio.run(main())
