from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(x: int, y: int) -> int:
    """
    Add two numbers together.
    
    :param x: First number to add
    :type x: int
    :param y: Second number to add
    :type y: int
    :return: Sum of x and y
    :rtype: int
    """
    return x + y