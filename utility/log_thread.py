from subprocess import PIPE, Popen

from PyQt6.QtCore import QThread, pyqtSignal


class LogThread(QThread):
    new_log = pyqtSignal(str)

    def run(self):
        process = Popen(
            "journalctl -u wg-quick@* -f",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            bufsize=1,
        )

        for line in process.stdout:
            self.new_log.emit(line.strip())

        process.stdout.close()
        process.wait()
