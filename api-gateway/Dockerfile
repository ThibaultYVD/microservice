FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn httpx
CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "8000"]