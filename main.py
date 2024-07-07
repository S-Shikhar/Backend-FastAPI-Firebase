from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from DB import get_db


app = FastAPI()
db = get_db()

# Endpoint to return a greeting message
@app.get("/hello")
async def hello():
    return {"message": "Hey Hello From Here Also"}

# Endpoint to return a list of to-do items
@app.get("/todo")
async def get_todo():
    todos = [
        {"id": 1, "task": "Learn FastAPI"},
        {"id": 2, "task": "Build a REST API"},
        {"id": 3, "task": "Test the API",},
    ]
    return {"todos": todos}

# Optional: Endpoint to upload a file
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    file_size = len(content)
    file_type = file.content_type
    return {"filename": file.filename, "size": file_size, "type": file_type}

# Endpoint to add two numbers provided by the user
# @app.get("/add")
# async def add(a: int, b: int):
#     result = a + b
#     return {"result": result}

@app.post("/add")
async def add_numbers(a: int, b: int):
    try:
        sum_result = a + b
        # Save the sum to Firebase Realtime Database
        ref = db.reference('result')
        ref.set(sum_result)
        return {"a": a, "b": b,"result": sum_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# uvicorn main:app --reload
