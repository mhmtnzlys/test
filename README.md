## Large File Storage
To add a file larger than 100 mb, git lfs (large file storage) must be installed.

To install:
```
$ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
$ sudo apt-get install git-lfs
```

To track the files which we add:

```
$ git lfs track ".csv" (git lfs track "data/.csv")```

After tracking csv files in the path, we may upload our file or files.
Note: Uploading files to codespaces depends on our internet connection.

Uploading 500 MB file to codespaces: 58 sec
Pushing it to GitHub: 30 seconds

Uploading 1 GB file to codespaces: 1 min 49 sec
Pushing it to GitHub: 40 sec

To add the files to repo:

```
$ git add path/file.csv
$ git commit -m "add file.csv"
$ git push```

## Azure Functions Flask-Todo App
Flask-Todo app consists of registeration, authentication, login part of an app.
