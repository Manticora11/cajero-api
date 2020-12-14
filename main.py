from fastapi import FastAPI, HTTPException

from db.user_db import database_users, UserInDB

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/")
async def users():
    return {"users": database_users}


@app.get("/users/{username}")
async def get_user_by_username(username: str):
    if username in database_users.keys():
        return {"user": database_users[username]}
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users/")
async def create_user(new_user: UserInDB):
    database_users[new_user.username] = new_user


@app.delete("/users/")
async def delete_user(user: UserInDB):
    del database_users[user.username]


@app.put("/users/")
async def update_user(user: UserInDB):
    database_users[user.username] = user
