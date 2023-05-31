import subprocess

class NetworkScanner:
    def __init__(self, target_subnet):
        self.target_subnet = target_subnet
        self.results = []

    def scan_network(self):
        print(f"Scanning network {self.target_subnet}...\n")
        for host in self.get_hosts():
            if self.is_host_up(host):
                self.results.append(host)

    def get_hosts(self):
        hosts = []
        for i in range(1, 255):
            ip = f"{self.target_subnet}.{i}"
            hosts.append(ip)
        return hosts

    def is_host_up(self, host):
        try:
            result = subprocess.call(['ping', '-n', '1', '-w', '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result == 0:
                return True
            return False
        except subprocess.CalledProcessError:
            return False

    def print_results(self):
        print("Hosts that are UP:")
        for host in self.results:
            print(host)



