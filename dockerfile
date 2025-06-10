FROM python:3.11.4-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]