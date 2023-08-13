import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(ascitime)s]: [%(message)s]:')

project_name ="textSummarizer"

list_of_files =[
    ".github/workflows/.gitkeep",
    "app.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.yaml",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    file = Path(file)
    filedirectory,filename = os.path.split(file)
    
    if filedirectory != '':
        os.makedirs(filedirectory,exist_ok=True)
        logging.info(f"Creating directory {filedirectory} for the file {filename}")

    if(not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,'w') as f:
            pass
            logging.info(f"Creating file {filename} in the directory {filedirectory}")
    else:
        logging.info(f"File {filename} already exists in the directory {filedirectory}")
