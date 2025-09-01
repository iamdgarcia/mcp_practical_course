from mcp.server.fastmcp import FastMCP
import sqlite3
from pathlib import Path
from utils import get_port

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "community.db"

mcp = FastMCP("Servidor BaseDatos")

@mcp.tool(
    name="get_top_chatters",
    description="Obtiene la lista de usuarios ordenados por mensajes enviados (desc).",
)
def get_top_chatters():
    conn = sqlite3.connect(DB_PATH.as_posix())
    cursor = conn.cursor()
    cursor.execute("SELECT name, messages FROM chatters ORDER BY messages DESC")
    results = cursor.fetchall()
    conn.close()
    return [{"name": n, "messages": m} for (n, m) in results]

if __name__ == "__main__":
    mcp.run()
