import platform
import os
import psutil
import socket
import subprocess
import re

class Trojan():
    def __init__(self): 
        self.os = platform.system()
        self.processor = platform.processor()
        self.architecture = platform.machine()
        self.ram = psutil.virtual_memory().total
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
    
    def get_hostname(self):
        return self.hostname
    def get_ip(self):
        return self.ip
    def get_system_info(self):
        system_info = f'{self.hostname} \n {self.ip} \n {self.os} \n {self.architecture} \n {self.processor} \n {self.ram}'
        print(system_info)
        return system_info
