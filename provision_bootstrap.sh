#!/usr/bin/env bash
# Root level script to set up environment for Django development on Vagrant.
# Target box: ubuntu/trusty64

echo "---------------------------------------------"
echo "Setting fastest repo"
echo "---------------------------------------------"
wget https://raw.githubusercontent.com/geoenvo/apt-select/master/apt-select.py https://raw.githubusercontent.com/geoenvo/apt-select/master/arguments.py https://raw.githubusercontent.com/geoenvo/apt-select/master/mirrors.py https://raw.githubusercontent.com/geoenvo/apt-select/master/update.sh https://raw.githubusercontent.com/geoenvo/apt-select/master/util_funcs.py
chmod u+x *.py update.sh
apt-get update
apt-get install -y python-bs4
./apt-select.py
./update.sh

echo "---------------------------------------------"
echo "Adding PostgreSQL repo"
echo "---------------------------------------------"
echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >> /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

echo "---------------------------------------------"
echo "Upgrading packages"
echo "---------------------------------------------"
apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade

echo "---------------------------------------------"
echo "Installing dependencies"
echo "---------------------------------------------"
apt-get install -y build-essential python-pip python-dev python-software-properties git-core

apt-get install -y postgresql-9.3 postgresql-contrib-9.3

pip install virtualenv virtualenvwrapper

echo 'export WORKON_HOME=$HOME/.virtualenvs' >> /home/vagrant/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc
