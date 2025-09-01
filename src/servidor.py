from mcp.server.fastmcp import FastMCP
from utils import get_port

server = FastMCP("Mi Servidor de Ejemplo")

@server.tool(name="sumar", description="Suma dos números enteros y devuelve el resultado")
def sumar(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    # Leer puerto de $PORT para compatibilidad con PaaS (fallback 8080)
    server.run()
