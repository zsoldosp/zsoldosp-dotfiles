#/bin/bash
function init-env() {
    export MANAGE_PY=~/$DJANGO_PROJECT/manage.py
    export DJANGO_CONFIG=$DJANGO_PROJECT.settings
}

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
    (echo "postgres"; echo "postgres") | sudo passwd postgres
    
}

function init-heroku-project() {
    # as per https://devcenter.heroku.com/articles/django
    rm -rf ~/$DJANGO_PROJECT; mkdir ~/$DJANGO_PROJECT; cd ~/$DJANGO_PROJECT
    init-env
    virtualenv venv --distribute
    source venv/bin/activate
    git init
    for to_ignore in venv "*.pyc" "*~" "*.swp" clerybeat-schedule; do
        echo "$to_ignore" >> .gitignore
    done
    git init
    git add .gitignore
    git commit -m"basic gitignore file"
    pip install Django psycopg2 django-celery
    django-admin.py startproject $DJANGO_PROJECT ~/$DJANGO_PROJECT
    git add manage.py $DJANGO_PROJECT
    git commit -m"django skeleton"
    update_settings_file_variable
    echo  "INSTALLED_APPS += ('kombu.transport.django', 'djcelery', '$DJANGO_PROJECT')" >> $DJANGO_CONFIG_FILE
    echo  "BROKER_BACKEND = 'django'" >> $DJANGO_CONFIG_FILE
    git commit $DJANGO_CONFIG_FILE -m"installed celery/kombu"
    echo  "DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'" >> $DJANGO_CONFIG_FILE
    echo  "DATABASES['default']['NAME'] = '/tmp/${DJANGO_PROJECT}.sqlite3'" >> $DJANGO_CONFIG_FILE
    PIP_REQ=requirements.txt
    pip freeze > $PIP_REQ # TODO: unlike the tutorial, this has wsgi & distribute as well
    git add $PIP_REQ
    git commit $PIP_REQ -m"pip requirements"
    PROCFILE=Procfile
    echo "celeryd: python manage.py celeryd -E -B --loglevel=INFO" > $PROCFILE
    git add $PROCFILE
    git commit $PROCFILE -m"procfile configured for just celery"
    django-initdb
}

function djcelery-add-sample() {
    update_settings_file_variable

    task_file=~/$DJANGO_PROJECT/$DJANGO_PROJECT/tasks.py
    echo "from celery.decorators import task" > $task_file
    echo "from datetime import datetime" >> $task_file
    echo "@task(name='tasks.helloworld')" >> $task_file
    echo "def helloworld():" >> $task_file
    echo "    print 'hello world @ %s' % datetime.now()" >> $task_file

    
    echo "from datetime import timedelta" >> $DJANGO_CONFIG_FILE
    echo "CELERYBEAT_SCHEDULE = { 'helloworld-schedule-name': { 'task': 'tasks.helloworld', 'schedule': timedelta(seconds=10), 'args': tuple() },}" >> $DJANGO_CONFIG_FILE
}
init-env
