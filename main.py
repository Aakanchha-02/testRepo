from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask_app import flask_app  # Import your Flask app

app = FastAPI()

# Mount your Flask app at a specific path
app.mount("/flask", WSGIMiddleware(flask_app))

@app.get("/fastapi")
def fastapi_endpoint():
    return "Hello from FastAPI!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)