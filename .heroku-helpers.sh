#/bin/bash
function init-heroku-env() {
    sudo apt-get install python-pip python-dev build-essential 
    sudo pip install --upgrade pip 
    sudo pip install --upgrade virtualenv 
    heroku_install_file=/tmp/heroku-toolbelt.sh
    wget -q https://toolbelt.heroku.com/install.sh -O $heroku_install_file
    chmod 755 $heroku_install_file
    $heroku_install_file
    heroku login
    sudo apt-get install postgresql libpq-dev
}

function init-heroku-project() {
    rm -rf ~/$DJANGO_PROJECT; mkdir ~/$DJANGO_PROJECT; cd ~/$DJANGO_PROJECT
    virtualenv venv --distribute
    source venv/bin/activate
    git init
    for to_ignore in venv "*.pyc" "*~" "*.swp"; do
        echo "$to_ignore" >> .gitignore
    done
    git init
    git add .gitignore
    git commit -m"basic gitignore file"
    pip install Django psycopg2
}
