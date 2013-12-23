$ manage.py schemamigration app_name --auto
"You cannot use automatic detection, since the previous migration does not have this whole app frozen."
$ manage.py schemamigration app_name freezing_the_models --freeze=app_name
.... ERROR ... USAGE ....
$ manage.py datamigration app_name freezing_the_models --freeze=app_name
$ manage.py migrate
$ manage.py schemamigration app_name --auto

