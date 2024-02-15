FROM python:3.12.1-bookworm

RUN mkdir -p /home/app

COPY . /home/app/

WORKDIR /home/app/

RUN pip3 install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator pytest

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["/home/app/app.py" ]