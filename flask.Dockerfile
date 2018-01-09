FROM python:alpine 

MAINTAINER Giovanni Mosconi

RUN pip install flask
RUN pip install SQLAlchemy
RUN pip install flask-sqlalchemy
RUN pip install python-dateutil
RUN pip install flask-restless
RUN pip install pymysql

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/api/api.py"]