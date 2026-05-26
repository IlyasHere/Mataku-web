from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dry Eye Fuzzy API Running"}