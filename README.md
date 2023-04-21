### Usage

- Create a .env file inside the "azureFunctions" folder.
- Fill the following variables and add inside the .env 
```
SECRET_KEY="<secret_key>"
DB_NAME="<db_name>"
DB_USER="<db_username>"
DB_PASSWORD="<db_password>"
DB_HOST="<db_host>"
DB_PORT="<db_port>"
DB_TEST_NAME="<db_test_name>"
```

Run the following command in the terminal.
```
$ export FLASK_APP=src/azureFunctions/flaskr.app
$ flask run
```
If you're running a Flask app in a GitHub Codespaces web browser, click the link displayed in the terminal after running the previous command. The link will be in the following format:\
```
http://{your-codespace-name}.githubpreview.dev:8080/
```
If you're running a Flask app in a GitHub Codespaces local VS Code, go to the following link:\
```
http://localhost:5000
```
Note that the link for the web browser version and the link for the local VS Code version may be different, so be sure to use the correct link depending on which environment you're using to run your Flask app.