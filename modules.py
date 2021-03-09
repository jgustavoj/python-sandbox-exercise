# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules 

import datetime 
from datetime import date
import time
from time import time

# Pip module
import camelcase

# Custom module
import validator 
from validator import validate_email

# today = datetime.date.today()
today = date.today()

# timestamp = time.time()
timestamp = time()

# camel = camelcase.CamelCase()
# text = 'hello there world'
# print(camel.hump(text))

email = 'test@test.com'
# email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Not valid email')
