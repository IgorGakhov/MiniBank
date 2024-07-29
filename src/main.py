from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
import uvicorn

from .domain.customers import router as router_customers
from .domain.remittances import router as router_transfers
from .domain.accounts import router as router_accounts
from .domain.currencies import router as router_currencies


app = FastAPI(title="MiniBank")

endpoints = APIRouter(
    prefix="/api/v1",
)
endpoints.include_router(router_customers)
endpoints.include_router(router_transfers)
endpoints.include_router(router_accounts)
endpoints.include_router(router_currencies)

app.include_router(endpoints)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
