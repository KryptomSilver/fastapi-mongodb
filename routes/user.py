from fastapi import APIRouter

user = APIRouter()


@user.get("/user")
def find_all_users():
    print("get users")


@user.post("/user")
def create_user():
    print("create user")


@user.get("/user/{id}")
def find_user():
    print("get user")


@user.delete("/user/{id}")
def delete_user():
    print("delete user")


@user.put("/user")
def update_user():
    print("update user")
