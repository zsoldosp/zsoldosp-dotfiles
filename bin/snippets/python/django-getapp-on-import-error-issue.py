myapp/
    models.py:
        import nonexistent
        from django.db import models
        class MyModel(models.Model):
            foo = models.CharField(lenght=10)


>>> from django.db import models
>>> models.get_model('myapp', 'MyModel')
None, None
>>> from myapp.models import MyModel
Traceback (most recent call last):
...
ImportError: No module named nonexistent


# TODO: check whether there is a force/failfast switch
