# -*- coding: utf-8 -*-
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
SQLALCHEMY_ECHO=True

# Define the database - we are working with
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:chcm_2010@192.168.10.60/prueba_napsis_tasks?charset=utf8"

SQLALCHEMY_TRACK_MODIFICATIONS = False
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# THREADS_PER_PAGE = 100

# Enable protection agains *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
# CSRF_SESSION_KEY = "123Dsdsdk9d8sdd-O"

# Secret key for signing cookies
SECRET_KEY = "99809ausdfjklmfd-9djfk2"

# Static folder
# STATIC_FOLDER = os.path.abspath( os.path.dirname(__file__)+'../public' )