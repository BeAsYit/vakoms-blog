**Blog**

*Install:*


- sudo apt-get install python3-dev
- sudo apt-get install python3-dev libmysqlclient-dev
- pip install mysqlclient
- sudo apt-get install mysql-server

*Connect to mysql and create database blog_data*

*Then use*


- sudo nano /etc/mysql/my.cnf

Set db_name, db_user, db_password to yours.

```
[client]
database = db_name
user = db_user
password = db_password
default-character-set = utf8*
```

- systemctl daemon-reload
- systemctl restart mysql
- pip install -r req.txt


### Runserver:
#### - python3 manage.py makemigrations
#### - python3 manage.py migrate
#### - python3 manage.py runserver