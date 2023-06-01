import subprocess
import re
import socket

class Wifi_Extractor:
    def __init__(self):
        self.hostname = socket.gethostname()

    #MAIN FUNCTION
    def main(self):
        wifi_networks = self._get_wifi_profiles()
        wifi_passwords = {}

        for network in wifi_networks:
            key_content = self._get_wifi_key_content(network)
            if key_content is not None:
                wifi_passwords[network] = key_content

        return wifi_passwords
    #MAIN FUNCTION
    
    def _get_wifi_profiles(self):
        command = "netsh wlan show profile"
        networks = subprocess.check_output(command, shell=True)
        output_str = networks.decode("utf-8")
        profiles = re.findall(r"(?:Profile\s*:\s)(.*)", output_str)
        return profiles

    def _get_wifi_key_content(self, profile):
        command = f'netsh wlan show profile "{profile}" key=clear'
        try:
            current_result = subprocess.check_output(command, shell=True)
            output_str = current_result.decode("utf-8")
        except (subprocess.CalledProcessError, UnicodeDecodeError):
            return None
        try:
            key_content = re.search(r"Key Content\s+:\s(.+)\r", output_str).group(1)
            return key_content
        except AttributeError:
            return None
