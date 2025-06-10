# Simbolo Student Assistant

This repository contains a Streamlit application designed to assist students with information about Simbolo, a training school. The application uses Elasticsearch for data retrieval and Groq for generating responses.

## Project Structure

- `src/main.py`: The main entry point for the Streamlit application.
- `src/search_engine.py`: Contains the logic for interacting with Elasticsearch and generating responses.
- `data/Simbolo_Information.json`: JSON file containing the data used by Elasticsearch.

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Elasticsearch
- Streamlit
- Groq

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Running the Application
To run the Streamlit application, use the following command:

```
streamlit run src/main.py
```

## MCP Server

The `create_mcp.py` file is part of the MCP server implementation. It initializes the FastMCP server and defines tools for retrieving information and generating output based on the knowledge base.

### Usage

To run the MCP server, execute the following command:

```bash
fastmcp dev src/mcp_server/create_mcp.py
```

In order to test the MCP Server, you can use the following link: erver, you can use the following link: http://127.0.0.1:6274

Connect the MCP Server at this website and test it out in tools section. 

### Functionality
- retrieve_information_and_generating_output : This tool retrieves information from the index knowledge base and generates output based on the input provided.

## Docker
To build and run the application using Docker, use the following commands:

```
docker build -t 
simbolo-student-assistant .
docker run -p 8501:8501 
simbolo-student-assistant
```
Access the application at http://localhost:8501 .

## Docker Pull

If you prefer to use a pre-built Docker image, you can pull it from Docker Hub using the following command:

```bash
docker pull yebhonelin102273442/simbolo-student-assistant
```

## Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.