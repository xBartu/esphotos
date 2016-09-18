# esphotos

esphotos is a Django application to store photos in photo albums

## Installation Steps
**NOTE:**

* You need to install pip in your machine firstly
* I use Django-Database-broker. If you use it on production, I suggest using more robust and advanced broker. In this case, do not forget to change BROKER_URL in `the_project/the_project/settings.py`

**1- Install virtualenv**

Firstly you need to install virtualenv.

Prefered method:
`pip install virtualenv`

**2- Create your enviorement**

You need to create your enviorement by using virtualenv and python3. 

method:
`virtualenv -p python3 esphotos`(the name can be changed)

** Django Broker Install **

To install it, run the following command:

`python manage.py migrate kombu_transport_django`

**Email Server**

You must edit **\#E-mail Settings** part in `the_project/the_project/settings.py`

**Twitter API Settings**

You need to change **\#Twitter API settings** in  `the_project/the_project/settings.py`. You get them from https://apps.twitter.com/
