# django-testapps - testing made easy for reusable django libraries


## Initial Scope:

* provide mixins for
    * model creation
        * per testfile (appname is test's full path lowercased)
        * per class (appname is classname)
        * per method (appname is method name)
        * interface:
            * ideal would be if we could use a single testcase to inherit from
            * but if it doesn't work otherwise, make a modelmixin
    * view/url creation
    * app creation (nesting classes into foo.models, etc.)
* setup TravisCI for supported matrix builds (python2/3 & supported django versions (matrix)
* setup PyPI with automatic version bumps

## TODO:

* write blog post/description
* figure out code organization structure

    * https://github.com/ramusus/django-email-html/blob/master/quicktest.py
    * https://github.com/jtauber/django-email-confirmation/tree/master/devproject
    * read: http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app

* review existing libs

    * https://pypi.python.org/pypi?%3Aaction=search&term=django-test&submit=search
    * and of course, django 1.6/1.7 itself
