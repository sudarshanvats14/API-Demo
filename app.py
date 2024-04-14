from fastapi import FastAPI
from services.order.router import router as order_router
from services.Return.router import router as Return_router
from services.people.router import router as people_router


app = FastAPI()

app.include_router(order_router)
app.include_router(Return_router)
app.include_router(people_router)



@app.get("/ping")
async def ping():
    return {"res": "whasdkljaskld adl;asld;klas; dlasl;askdlask d"}

