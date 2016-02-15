#!/usr/bin/env bash
# User level script to set up environment for Django development on Vagrant.
# Target box: ubuntu/trusty64

DB_NAME='opendims'
DB_USERNAME='vagrant'
DB_PASSWORD='password'

echo "---------------------------------------------"
echo "Creating database"
echo "---------------------------------------------"
sudo su - postgres << START
createdb $DB_NAME
psql -c "CREATE ROLE $DB_USERNAME WITH LOGIN ENCRYPTED PASSWORD '$DB_PASSWORD';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USERNAME;"
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
    cdvirtualenv
    ln -s /vagrant/ src
fi

workon opendims
cdvirtualenv
cd src

echo "---------------------------------------------"
echo "Setting up Django"
echo "---------------------------------------------"
pip install -r requirements.txt

echo "---------------------------------------------"
echo "Provisioning complete"
echo "---------------------------------------------"
printf "Use the following database connection settings in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '$DB_NAME',
        'USER': '$DB_USERNAME',
        'PASSWORD': '$DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"
