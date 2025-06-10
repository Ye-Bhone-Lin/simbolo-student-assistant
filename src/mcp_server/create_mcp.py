from mcp.server.fastmcp import FastMCP
from search_engine import SearchEngine, GenerateOutput

mcp = FastMCP("Simbolo-Student-Assistant")

# Tool: retrieve information from the knowledge base 
@mcp.tool()
def retrieve_information_and_generating_output(user_input: str):
    """Retrieve information from the index knowledge base and generate output based on index knowledge base."""
    result = GenerateOutput.model_generate(user_input)
    return result

if __name__ == "__main__":
    mcp.run()