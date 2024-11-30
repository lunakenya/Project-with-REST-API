from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Endpoint REST-API con el método GET
def read_root():
    return {"message": "Hola, Mundo desde FastAPI!"}
