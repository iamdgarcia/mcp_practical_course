import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Cambia a "servidor_bd.py" si quieres probar la herramienta de BD
server_params = StdioServerParameters(command="python", args=["src/servidor.py"])

async def main():
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("=== Herramientas disponibles ===")
            for t in tools.tools:
                print(f"- {t.name}: {t.description}")
            print("===============================\n")

            # Demo: invocar "sumar"
            result = await session.call_tool("sumar", {"a": 5, "b": 7})
            print(f"Resultado sumar 5 + 7 = {result}")

if __name__ == "__main__":
    asyncio.run(main())
