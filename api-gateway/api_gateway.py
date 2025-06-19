from fastapi import FastAPI
import httpx

app = FastAPI()

USER_SERVICE_URL = "http://127.0.0.1:8001"
PRODUCT_SERVICE_URL = "http://127.0.0.1:8002"
INTERNAL_API_KEY = "gateway-secret"

@app.get("/api/users/{user_id}")
async def proxy_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{USER_SERVICE_URL}/users/{user_id}",
            headers={"x-internal-key": INTERNAL_API_KEY}
        )
        return response.json()

@app.get("/api/products/{product_id}")
async def proxy_product(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        return response.json()