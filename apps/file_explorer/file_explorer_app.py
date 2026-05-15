import os

from PyQt6.QtWidgets import (
    QMessageBox,
    QInputDialog
)

from apps.file_explorer.ui import FileExplorerUI


class FileExplorerApp(FileExplorerUI):
    def __init__(self, username, role):
        super().__init__()

        self.username = username
        self.role = role

        self.user_path = f"users/{self.username}/files"

        self.path_label.setText(f"📂 {self.user_path}")

        self.load_files()

        self.connect_events()

        self.apply_permissions()

    # =========================
    # EVENTS
    # =========================

    def connect_events(self):
        self.create_button.clicked.connect(self.create_file)
        self.delete_button.clicked.connect(self.delete_file)

    # =========================
    # LOAD FILES
    # =========================

    def load_files(self):
        self.file_list.clear()

        if not os.path.exists(self.user_path):
            os.makedirs(self.user_path)

        files = os.listdir(self.user_path)

        for file in files:
            self.file_list.addItem(file)

    # =========================
    # CREATE FILE
    # =========================

    def create_file(self):
        file_name, ok = QInputDialog.getText(
            self,
            "Crear archivo",
            "Nombre del archivo:"
        )

        if ok and file_name:
            file_path = os.path.join(
                self.user_path,
                file_name
            )

            with open(file_path, "w") as f:
                f.write("")

            self.load_files()

    # =========================
    # DELETE FILE
    # =========================

    def delete_file(self):
        selected_item = self.file_list.currentItem()

        if not selected_item:
            return

        file_name = selected_item.text()

        file_path = os.path.join(
            self.user_path,
            file_name
        )

        if self.role != "admin":
            QMessageBox.warning(
                self,
                "Permiso denegado",
                "Solo admin puede eliminar archivos."
            )
            return

        os.remove(file_path)

        self.load_files()

    # =========================
    # PERMISSIONS
    # =========================

    def apply_permissions(self):
        """
        Escalable:
        aquí luego podrás agregar:
        - lectura
        - escritura
        - ejecución
        - ownership
        - ACLs
        """

        if self.role != "admin":
            self.delete_button.setEnabled(False)