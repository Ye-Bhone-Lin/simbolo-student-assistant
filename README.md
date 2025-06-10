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

## Docker
To build and run the application using Docker, use the following commands:

```
docker build -t 
simbolo-student-assistant .
docker run -p 8501:8501 
simbolo-student-assistant
```
Access the application at http://localhost:8501 .


## Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.