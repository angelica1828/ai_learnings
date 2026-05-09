from fastmcp import FastMCP

@mcp.tool()
def multiply(x: int, y: int) -> int:
    """ 
    Multiply two numbers
    args:
        x: The first number
        y: The second number
    returns:
        The product of x and y
    """
    return x * y

@mcp.tool()
def add(x: int, y: int) -> int:
    """ 
    Add two numbers
    args:
        x: The first number
        y: The second number
    returns:
        The sum of x and y
    """
    return x + y 

@mcp.tool()
def subtract(x: int, y: int) -> int:
    """ 
    Subtract two numbers
    args:
        x: The first number
        y: The second number
    returns:
        The difference of x and y
    """
    return x - y

@mcp.tool()
def divide(x: int, y: int) -> int:
    """ 
    Divide two numbers
    args:
        x: The first number
        y: The second number
    returns:
        The quotient of x and y
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x // y

if __name__ == "__main__":
    mcp.run() #STDIO by default