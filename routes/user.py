from fastapi import APIRouter
from config.db import conn
from models.user import User
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.get("/user")
def find_all_users():
    return usersEntity(conn.fastapi.user.find())


@user.post("/user")
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    id = conn.fastapi.user.insert_one(new_user).inserted_id
    user = conn.fastapi.user.find_one({"_id": id})
    return userEntity(user)


@user.get("/user/{id}")
def find_user():
    return "get user"


@user.delete("/user/{id}")
def delete_user():
    return "delete user"


@user.put("/user")
def update_user():
    return "update user"
