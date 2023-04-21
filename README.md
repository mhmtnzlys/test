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
If running Flask app in a GitHub Codespaces web browser, click the link you see in terminal after running the previous command. The link looks like in the following line.\
http://<your-codespace-name>.githubpreview.dev:8080/ \
If running Flask app in a GitHub Codespaces local VS Code, go to the link in the following line.\
http://localhost:5000 \