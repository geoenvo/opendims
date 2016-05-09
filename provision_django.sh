#!/usr/bin/env bash
# User level script to set up environment for Django development on Vagrant.
# Target box: ubuntu/trusty64

DB_NAME='opendims'
DB2_NAME='geolevels'
DB_USERNAME='vagrant'
DB_PASSWORD='password'
POSTGRES_PASSWORD='postgres'

echo "---------------------------------------------"
echo "Creating PostGIS database"
echo "---------------------------------------------"
sudo su - postgres << START
psql -c "ALTER USER postgres WITH PASSWORD '$POSTGRES_PASSWORD';"
createdb $DB_NAME
psql -c "CREATE ROLE $DB_USERNAME WITH LOGIN ENCRYPTED PASSWORD '$DB_PASSWORD';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USERNAME;"
psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" $DB_NAME
createdb $DB2_NAME
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB2_NAME TO $DB_USERNAME;"
psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" $DB2_NAME
START

echo "---------------------------------------------"
echo "Creating virtualenv"
echo "---------------------------------------------"
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    source /usr/local/bin/virtualenvwrapper.sh
elif [ -f /usr/share/virtualenvwrapper/virtualenvwrapper.sh ]; then
    source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
else
    source /usr/bin/virtualenvwrapper.sh
fi

if [ ! -d /home/vagrant/.virtualenvs/opendims ]; then
    mkvirtualenv --no-site-packages opendims
fi

workon opendims
cd opendims

echo "---------------------------------------------"
echo "Setting up Django"
echo "---------------------------------------------"
pip install -r requirements.txt
nodeenv -p --prebuilt
workon opendims
npm install -g bower
npm install -g phantomjs-prebuilt@2.1.7
npm install -g casperjs@1.1.1

echo "---------------------------------------------"
echo "Provisioning complete"
echo "---------------------------------------------"
printf "Use the following database connection settings in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '$DB_NAME',
        'USER': '$DB_USERNAME',
        'PASSWORD': '$DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"
