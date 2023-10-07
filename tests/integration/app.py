from typing import Dict

from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette.requests import Request

from src import Cache, CacheType

app = FastAPI()

@app.on_event("startup")
def run_apscheduler():
    Cache.init()


@app.get("/")
@Cache.cache(cache_type=CacheType.LIST)
async def read_main(request: Request):
    return {"msg": "Hello World"}


router = InferringRouter()


@cbv(router)
class ProductController:

    @router.get("/{id}", status_code=200)
    @Cache.cache(cache_type=CacheType.LIST)
    async def get_by_id(self, request: Request) -> Dict[str, str]:
        result: Dict[str, str] = {"bla": "bla"}
        return result


app.include_router(router)


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_cbv_endpoint():
    response = client.get("/10")
    assert response.status_code == 200
    assert response.json() == {"bla": "bla"}
