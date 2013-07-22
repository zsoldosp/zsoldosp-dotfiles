from django.test import TestCase
from django.db import models 


class ExploringDjangoModelRegistrationBehavior(TestCase):
    def test_when_model_is_declared_it_is_registerd_but_not_in_installed_app(self):
        models_before_declaring_class = set(models.get_models())
        class FooModel(models.Model):
            pass
        models_after_declaring_class = set(models.get_models())
        self.assertEquals(len(models_before_declaring_class) + 1, len(models_after_declaring_class))
        self.assertEquals(set([FooModel]), models_after_declaring_class - models_before_declaring_class)
