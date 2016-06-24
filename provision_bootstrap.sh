#!/usr/bin/env bash
# Root level script to set up environment for Django development on Vagrant.
# Target box: ubuntu/trusty64

#echo "---------------------------------------------"
#echo "Setting fastest repo"
#echo "---------------------------------------------"
#wget https://raw.githubusercontent.com/geoenvo/apt-select/master/apt-select.py https://raw.githubusercontent.com/geoenvo/apt-select/master/arguments.py https://raw.githubusercontent.com/geoenvo/apt-select/master/mirrors.py https://raw.githubusercontent.com/geoenvo/apt-select/master/update.sh https://raw.githubusercontent.com/geoenvo/apt-select/master/util_funcs.py
#chmod u+x *.py update.sh
#apt-get update
#apt-get install -y python-bs4
#./apt-select.py
#./update.sh

echo "---------------------------------------------"
echo "Adding PostgreSQL repo"
echo "---------------------------------------------"
if [ ! -f /etc/apt/sources.list.d/pgdg.list ]; then
    echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >> /etc/apt/sources.list.d/pgdg.list
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
fi

echo "---------------------------------------------"
echo "Upgrading packages"
echo "---------------------------------------------"
apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade

echo "---------------------------------------------"
echo "Installing dependencies (build libs, Git, PostgreSQL, PostGIS)"
echo "---------------------------------------------"
apt-get install -y build-essential python-pip python-dev libpq-dev python-software-properties git-core libjpeg8-dev libfreetype6-dev libz-dev libjpeg-dev gettext redis-server

# Install PostgreSQL with PostGIS
apt-get install -y postgresql-9.3 postgresql-contrib-9.3 postgresql-9.3-postgis-2.1

# Install GeoDjango dependencies (GDAL, GEOS, PROJ.4)
apt-get install -y binutils libgeoip1 libproj-dev gdal-bin python-gdal

echo "---------------------------------------------"
echo "Configure PostgreSQL for MD5 authentication"
echo "---------------------------------------------"
if [ -f /etc/postgresql/9.3/main/pg_hba.conf ]; then
    cp /etc/postgresql/9.3/main/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf.orig
    echo 'local all all md5' >> /etc/postgresql/9.3/main/pg_hba.conf
    echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.3/main/pg_hba.conf
fi

if [ -f /etc/postgresql/9.3/main/postgresql.conf ]; then
    cp /etc/postgresql/9.3/main/postgresql.conf /etc/postgresql/9.3/main/postgresql.conf.orig
    echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf
fi

service postgresql restart

echo "---------------------------------------------"
echo "Installing virtualenv"
echo "---------------------------------------------"
pip install virtualenv virtualenvwrapper

if ! grep -Fq "WORKON_HOME" /home/vagrant/.bashrc; then
    echo 'export WORKON_HOME=$HOME/.virtualenvs' >> /home/vagrant/.bashrc
    echo 'source /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc
fi
