# moodle_dash

Get the App running:
- Clone the repo to a folder of your choice
- Open the project in an IDE (e.g. PyCharm, VS Code)
- If you work in PyCharm, it should set up a virtual environment by itself, otherwise create one manually by typing the following command in the command line/ terminal:
  - Mac/Linux: virtualenv venv
  - Windows: virtualenv --python C:\Path\To\Python\python.exe venv
    -> if it doesn't work, check the following paths:
      - C:\Users\%username%\AppData\Local\Programs\Python\Python36\python.exe
      - C:\Users\%username%\AppData\Local\Programs\Python\Python36-32\python.exe
- Activate the virtual envioronment: 
  - Mac/Linux: source/venv/binActivate
  - Windows: venvironment\Scripts\activate or .\venv\Scripts\activate
- Install requirements:
  - pip install -r requirements.txt
- Start the App with the command:
  - python index.py
- Dash should be running on:
  - http://127.0.0.1:8050/
- Log in with the credentials:
  - username: anon1
  - password: restored
