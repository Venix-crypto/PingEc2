import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        response = os.system(f"ping {self.server_ip}")
        if response == 0:
            return f"{self.server_ip} is up!"
        else:
            return f"{self.server_ip} is down!"

def print_program_info():
    print("Server Automator v0.1 by FarriusDean")

if __name__ == '__main__':
    print_program_info()
    server = Server('18.223.158.88')
    print(server.ping())