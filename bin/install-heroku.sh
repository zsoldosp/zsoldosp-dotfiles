#/bin/bash
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
heroku_install_file=/tmp/heroku-toolbelt.sh
wget -q https://toolbelt.heroku.com/install.sh -O $heroku_install_file
chmod 755 $heroku_install_file
$heroku_install_file
heroku login
