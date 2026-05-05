# services/auth_service.py

import json
from pathlib import Path


class AuthService:
    def __init__(self):
        # Ruta al archivo JSON
        self.users_file = Path("data/users.json")
        self.users = self.load_users()

    def load_users(self):
        """
        Carga los usuarios desde el archivo JSON
        """
        try:
            with open(self.users_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("users", [])
        except FileNotFoundError:
            print("Archivo users.json no encontrado")
            return []

    def login(self, username: str, password: str) -> bool:
        """
        Valida credenciales contra el JSON
        """
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return True

        return False
