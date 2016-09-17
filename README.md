# esphotos

esphotos is a Django application to store photos in photo albums

## Installation Steps
**NOTE:**

* You need to install pip in your machine firstly

**1- Install virtualenv**

Firstly you need to install virtualenv.

Prefered method:
`pip install virtualenv`

**2- Create your enviorement**

You need to create your enviorement by using virtualenv and python3. 

method:
`virtualenv -p python3 esphotos`(the name can be changed)

**Email Server**

You must edit the following-up part in `the_project/the_project/.py`

`#E-mail Settings
EMAIL_HOST = '' # Host

EMAIL_HOST_USER = '' # Username

EMAIL_HOST_PASSWORD = '' # Password

EMAIL_PORT = 0 # Port Number`
