import re
import json
from hashlib import sha256
from dataclasses import dataclass
from dataclasses_json import dataclass_json
USER_DATABASE_PATH = "database/users.json"

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email: str) -> bool:
    if (re.fullmatch(email_regex, email)):
        return True
    return False


@dataclass_json
@dataclass
class User:
    name: str
    email: str
    password: str

def user_exists(name: str) -> bool:
    with open(USER_DATABASE_PATH, "r") as user_db:
        loaded_db = json.loads(user_db.read())
    if name in loaded_db["usernames"]:
        return True
    return False


def create_user(name: str, email: str, password: str) -> User:
    return User(
        name=name,
        email=email,
        password=sha256(password.encode()).hexdigest()
    )

def get_user(name: str) -> User:
    if not user_exists(name):
        return False
    index = 0
    with open(USER_DATABASE_PATH, "r") as user_db:
        loaded_db = json.loads(user_db.read())
        for counter in range(len(loaded_db["users"])):
            if name == loaded_db["users"][counter][name]:
                index = counter
                break
        return User(
            loaded_db["users"][index][name]["name"],
            loaded_db["users"][index][name]["email"],
            loaded_db["users"][index][name]["password"]
        )

def register(user: User) -> None:
    user = create_user(user.name, user.email, user.password)
    previous = ""
    with open(USER_DATABASE_PATH, "r") as user_db:
        previous = json.loads(user_db.read())

    with open(USER_DATABASE_PATH, "w") as user_db:
        previous["usernames"].append(user.name)
        previous["users"].append({
            user.name: {
                "name":  user.name,
                "email": user.email,
                "password": user.password
            }
        })
        user_db.write(json.dumps(previous))

def login(name: str, password: str):
    result = []

    print(sha256(password.encode()).hexdigest())
    print(get_user(name).password)
    if get_user(name).password == sha256(password.encode()).hexdigest():
        result.append(True)
        result.append(sha256(name.encode()).hexdigest())
        return result
    result =[False, "failed"]
    return result