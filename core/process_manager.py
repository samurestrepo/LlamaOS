class ProcessManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.processes = []
            cls._instance.next_pid = 1000

        return cls._instance

    # =========================
    # REGISTER PROCESS
    # =========================

    def register_process(self, name, window):

        process = {
            "pid": self.next_pid,
            "name": name,
            "status": "Running",
            "window": window
        }

        self.processes.append(process)

        self.next_pid += 1

        return process

    # =========================
    # GET PROCESSES
    # =========================

    def get_processes(self):
        return self.processes

    # =========================
    # KILL PROCESS
    # =========================

    def kill_process(self, pid):

        for process in self.processes:

            if process["pid"] == pid:

                process["window"].close()

                self.processes.remove(process)

                return True

        return False