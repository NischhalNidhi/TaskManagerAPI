from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() ## constructor, app instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

tasklist = { }

@app.get('/')
def welcome_message():

    return{"message": "This is a task manager :)"}

@app.get('/task/')
def task():
    return tasklist

@app.get('/task/{taskid}')
def taskById(taskid: int):
    return {taskid : tasklist[taskid]}

@app.post('/task/add/')
def addtask(text : str):
    tasklist[len(tasklist)] = text
    return {"message":"task added", "taskid":len(tasklist)-1}

@app.delete('/task/{taskid}/')
def deletetask(taskid : int):
    del tasklist[taskid]
    return {"message":"task deleted", "taskid":len(tasklist)-1}
#add errorhandeling

