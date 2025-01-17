# SC-server-auth
Authentication server for sc-machine repository

To install poetry run command:
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - 
```
or just do it with pip3 (not recommended):
```sh
pip3 install poetry
```

To install dependencies run command:
```sh
poetry env use 3.8
poetry shell
poetry install
```

Activate the virtual environment is to create a new shell with **_poetry shell_**. 
To deactivate the virtual environment and **_exit_** this new shell type exit. 
To deactivate the virtual environment without leaving the shell use **_deactivate_**.

## PostgreSQL (optional)

```shell
sudo apt install postgresql postgresql-contrib
```

Commands to create database and user for it.

```shell
sudo -u postgres psql
```

```postgresql
create database sc_auth;
create user sc_auth with encrypted password 'sc_auth';
grant all privileges on database sc_auth to sc_auth;
```

**Activation**

Set postgres in sc_server_auth/configs/settings.toml or as argument in server run script

**Insert default values (after server running)**

```shell
psql -U sc_auth -h localhost -d sc_auth
```

Write password "sc_auth" and run command:

```postgresql
insert into "user"(id, name, password)
values (1, 'admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');
```

## Local-CI tool

For check your branch before pushing just run next command:
```sh
scripts/local_ci.sh -a
```
With option -a local_ci runs all checks, which included black, isort, pylint and unittest. 

If you want to run only certain checks, see help for this command:

```sh
scripts/local_ci.sh -h
```

To start auth-server:
```
python3 -m sc_server_auth [-h] [-H HOST] [-p PORT] [-d DATABASE] [-l LOG_LEVEL] [-r] [-e DOT_ENV]
```

You can check current endpoints in swagger docs by url:
```
http://127.0.0.1:5000/docs
```

If you dont have keys in sc-server-auth folder you can generate them by making a request to generate token. After that keys will generate automatically.

Current credentials to test: 
login - admin, password - a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3 (SHA256 hash)
