from netunicorn.base.task import Task, Result
from .slowloris import main
from .smbloris import smbloris


class SlowLoris(Task):
    def __init__(
        self,
        host: str,
        port: int,
        sockets: int,
        https: bool,
        sleeptime: int,
        slowloris_iterations: int,
    ):
        self.host = host
        self.port = port
        self.sockets = sockets
        self.https = https
        self.sleeptime = sleeptime
        self.slowloris_iterations = slowloris_iterations
        super().__init__()

    def run(self):
        return main(
            self.host,
            self.port,
            self.sockets,
            self.https,
            self.sleeptime,
            self.slowloris_iterations,
        )


class SMBLoris(Task):
    requirements = ["pip install scapy"]

    def __init__(self, host: str, starting_source_port: int, number_of_ports: int):
        self.host = host
        self.starting_source_port = starting_source_port
        self.number_of_ports = number_of_ports
        super().__init__()

    def run(self):
        return smbloris(self.host, self.starting_source_port, self.number_of_ports)
