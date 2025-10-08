import os  #gives acess to the os
from pathlib import Path #easy,objevt orient to handle file system paths
import logging #display log messages 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #configures the logging system (2025-10-08 10:12:45 - INFO - Something happened)

project_name = "mlProject"

list_of_files = [
    ".github/workflows/.gitkeep", #to keep the folder in git,
    f"src/{project_name}/__init__.py", #to make the folder a package
    f"src/{project_name}/components/__init__.py", #to make the folder a package
    f"src/{project_name}/utils/__init__.py", #to make the folder a package
    f"src/{project_name}/utils/common.py", #common utility functions
    f"src/{project_name}/config/__init__.py", #to make the folder a package
    f"src/{project_name}/config/configuration.py", #to handle the config
    f"src/{project_name}/pipeline/__init__.py", #to make the folder a package
    f"src/{project_name}/entity/__init__.py", #to make the folder a package
    f"src/{project_name}/entity/config_entity.py", #to handle the config entity
    f"src/{project_name}/constants/__init__.py", #to make the folder a package
    "config/config.yaml", #yaml config file
    "params.yaml", #parameters file
    "schema.yaml", #schema file
    "main.py", #entry point of the project
    "app.py", #to run the app
    "requirements.txt", #to list the dependencies
    "dockerfile", #to containerize the app
    "research/trials.ipynb", #jupyter notebook for research
    "setup.py", #to make the project pip installable
    "templates/index.html"#html template for the app
]



for filepath in list_of_files:
    filepath = Path(filepath) #convert to Path object
    filedir, filename = os.path.split(filepath) #split the path into directory and file name

    if filedir != "": #if there is a directory
        os.makedirs(filedir, exist_ok=True) #create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for file: {filename}") #log the creation of the directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if the file doesn't exist or is empty
        with open(filepath, "w") as fp: #create the file
            pass #do nothing, just create an empty file
        logging.info(f"Creating file: {filepath}") #log the creation of the file
    else:
        logging.info(f"File already exists: {filepath}, skipping...") #log that the file already exists and is being skipped