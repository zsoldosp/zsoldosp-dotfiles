#!/bin/bash
function env_or_default() {
    # thanks a ton to Dieter for sharing this trick with me!
    name=$1
    default=$2
    if [[ ${!name} == "" ]]; then
        echo "no value set for $name, setting it to default value $default"
        export $name=$default
    else
        echo "value for $name was passed in from the environment, it's value is ${!name}"
    fi

}

env_or_default SITE_ROOT /path/to/my/django/project/root
env_or_default MANAGE_PY_FOLDER $SITE_ROOT/django-sites/
env_or_default SETTINGS_NAME devel
