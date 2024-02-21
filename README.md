# Image-Store-App 
This app has registration, login, and image(or any data) upload features. It is created using the Python-Flask Framework.

## APIs

#### /register - users can register 
#### /login    - The users can log in only after registration
#### /logout   - logout after uploading the images
#### /dashboard   - page for users to upload the files after login


## Installation and Setup

```
pip install --user flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator pytest
```

## Execution

```
python app.py
```


## Docker and YML file attached (CircieCI build Successful)
[Docker Image](https://hub.docker.com/repository/docker/charulsjsu/img-store-app/general)


