from PyQt6.QtWidgets import QTableWidgetItem

from apps.task_manager.ui import TaskManagerUI

from core.process_manager import ProcessManager


class TaskManagerApp(TaskManagerUI):

    def __init__(self):
        super().__init__()

        self.process_manager = ProcessManager()

        self.load_processes()

        self.kill_button.clicked.connect(
            self.kill_selected_process
        )

    # =========================
    # LOAD PROCESSES
    # =========================

    def load_processes(self):

        processes = self.process_manager.get_processes()

        self.table.setRowCount(len(processes))

        for row, process in enumerate(processes):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(str(process["pid"]))
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(process["name"])
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(process["status"])
            )

    # =========================
    # KILL PROCESS
    # =========================

    def kill_selected_process(self):

        selected_row = self.table.currentRow()

        if selected_row < 0:
            return

        pid_item = self.table.item(selected_row, 0)

        pid = int(pid_item.text())

        self.process_manager.kill_process(pid)

        self.load_processes()