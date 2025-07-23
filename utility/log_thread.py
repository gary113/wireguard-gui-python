from subprocess import PIPE, Popen

from PyQt6.QtCore import QThread, pyqtSignal


class LogThread(QThread):
    new_log = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        process = Popen(
            ["journalctl", "-u", "wg-quick@*", "-f"],
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            bufsize=1,
        )

        while self._running:
            line = process.stdout.readline()
            if not line:
                break
            self.new_log.emit(line.strip())

        process.terminate()
        process.wait()

    def stop(self):
        self._running = False
