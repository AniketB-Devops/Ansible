from fastapi import FastAPI

app= FastAPI()

users=[{'id':101,'uname':'admin','email':'admin@mail.com'}]
@app.get('/users')
def loadUsers():
    return {'message': users}

@app.get('/')
def welcome():
    return {'Hey Aniket'}