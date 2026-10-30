"""Synthetic, read-only MCP tools used only in the Cloe integration example."""

from mcp.server import MCPServer
from mcp.types import ToolAnnotations


mcp = MCPServer("cloe-readonly-demo")

ORDERS = {
    "demo-1001": {"status": "preparing", "eta_minutes": 18},
    "demo-1002": {"status": "out_for_delivery", "eta_minutes": 7},
}

MENU = (
    {"name": "Veggie bowl", "category": "bowls"},
    {"name": "Chicken wrap", "category": "wraps"},
    {"name": "Mushroom pasta", "category": "pasta"},
)


@mcp.tool(
    title="Look up a demo order",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def lookup_order_status(order_id: str) -> dict[str, str | int]:
    """Return the status of a synthetic demo order by its ID."""
    order = ORDERS.get(order_id)
    if order is None:
        return {"status": "not_found", "eta_minutes": 0}
    return {"order_id": order_id, **order}


@mcp.tool(
    title="Search the demo menu",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def search_demo_menu(query: str) -> list[dict[str, str]]:
    """Search a small synthetic menu by item name or category."""
    normalized_query = query.casefold().strip()
    return [
        item
        for item in MENU
        if normalized_query in item["name"].casefold()
        or normalized_query in item["category"].casefold()
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")
