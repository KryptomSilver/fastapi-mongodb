from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import conn
from models.user import User
from schemas.user import userEntity, usersEntity
from passlib.hash import sha256_crypt

user = APIRouter()


@user.get("/user", response_model=list[User], tags=["Users"])
def find_all_users():
    return usersEntity(conn.fastapi.user.find())


@user.post("/user", response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.fastapi.user.insert_one(new_user).inserted_id
    user = conn.fastapi.user.find_one({"_id": id})
    return userEntity(user)


@user.get("/user/{id}", response_model=User, tags=["Users"])
def find_user(id: str):
    user = conn.fastapi.user.find_one({"_id": ObjectId(id)})
    if(not user):
        return "User not found"
    return userEntity(user)


@user.delete("/user/{id}", response_model=User, tags=["Users"])
def delete_user(id: str):
    user = conn.fastapi.user.find_one({"_id": ObjectId(id)})
    if(not user):
        return "User not found"
    user_deleted = conn.fastapi.user.find_one_and_delete({"_id": ObjectId(id)})
    return userEntity(user_deleted)


@user.put("/user/{id}", response_model=User, tags=["Users"])
def update_user(id: str, user: User):
    new_User = dict(user)
    user_Found = conn.fastapi.user.find_one({"_id": ObjectId(id)})
    if(not user_Found):
        return "User not found"
    new_User["password"] = sha256_crypt.encrypt(new_User["password"])
    del new_User["id"]
    conn.fastapi.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": new_User})
    return userEntity(conn.fastapi.user.find_one({"_id": ObjectId(id)}))
