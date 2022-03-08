# Digital Diary App

***This app will help you to 'free' your memory about important events in your life. You can save your diary here.***

## Project setup
### Requirements:
- python 3 and pip
- mysql server and my sql workbench to generate database

### Set up instructions
- Go to db folder and run init.sql to generate database in your sql. Come to diary folder and replace database config in app.py with your username, password and host. 
- Then run 
```shell
pip install -r requirements.txt
```
- After installation, run below command from the root of the project (DIARY_APP)
```shell
python diary/app.py
```
OR run below from diary folder
```shell
python app.py
```
The application is accessible on http://192.168.0.5:5000 or http://localhost:5000

- Folder myvenv is the virtual environment for the project and user can run the project by activate myvenv and run python diary/app.py without installations of requirement.txt
