from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "FIN DE LA DEMO DEVOPS"}


