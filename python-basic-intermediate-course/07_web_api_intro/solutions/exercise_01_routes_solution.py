from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/departments")
def departments() -> list[str]:
    return ["Engineering", "Sales", "Support"]

