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

**3- Install Requirements**

You need to install the requirements of the file.

`pip install -r requirements.txt`

**4-Make migrations and migrate them

You also need migrations. You can do this by following up codes:

`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py makemigrations albums`
`python manage.py migrate albums`

**5-CelerySettings

You need to set the cellery setting via admin panel. If you need help, visit http://docs.celeryproject.org/en/latest/ or create an issue.
##The other Settings

**jango Broker Install**

To install it, run the following command:

`python manage.py migrate kombu_transport_django`

**Run Worker**

Run the following command:

`python manage.py celery worker`

Note: It runs in every 20 minutes and indexes the first 100 results.

**Email Server**

You must edit **\#E-mail Settings** part in `the_project/the_project/settings.py`

**Twitter API Settings**

You need to change **\#Twitter API settings** in  `the_project/the_project/settings.py`. You get them from https://apps.twitter.com/

**Facebook AppID**

you need to get an Facebook App  ID from https://developers.facebook.com/apps. And add it to templates/albums/base.html.
