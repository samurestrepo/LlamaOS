import json
from pathlib import Path


class AuthService:
    def __init__(self):
        self.users_file = Path("data/users.json")
        self.users = self.load_users()

    def load_users(self):
        """
        Carga usuarios desde users.json
        """

        try:
            with open(self.users_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("users", [])

        except FileNotFoundError:
            print("Archivo users.json no encontrado")
            return []

    def login(self, username: str, password: str):
        """
        Retorna:
        - dict usuario si login correcto
        - None si falla
        """

        for user in self.users:

            if (
                user["username"] == username
                and user["password"] == password
            ):
                return user

        return None