from django.test import TestCase
from django.utils.decorators import classonlymethod
from django.db.utils import DatabaseError
from django.db.models.loading import load_app, register_models
from django.core.management import sql, color
from django.db import connection, models
from django.conf import settings
from django.core import management


def create_model_at_runtime(app_name, *model_classes):
    """creates a dynamic model for testing purposes. For technical details, see https://code.djangoproject.com/wiki/DynamicModels"""
    for model_cls in model_classes:
        try:
            model_cls.objects.count()
        except:
            style = color.no_style()
            cursor = connection.cursor()
            statements, pending = connection.creation.sql_create_model(model_cls, style)
        for sql in statements:
            try:
                cursor.execute(sql)
            except Exception as e:
                raise Exception('%s\nSQL was:\n%s' % (e, sql))
    register_models(app_name, *model_classes)


class ThisTestCaseRegistersItsOwnModels(TestCase):
    class models:
        class SampleModel(models.Model):
            text = models.CharField(max_length=100)

    @classonlymethod 
    def setUpClass(cls):
        cls.app_name = cls.__module__
        create_model_at_runtime(cls.app_name, *cls.class_models())
        super(ThisTestCaseRegistersItsOwnModels, cls).setUpClass()

    @classonlymethod 
    def class_models(cls):
        return [cls.models.SampleModel]

    def test__create_one_model_instance(self):
        self.models.SampleModel.objects.create(text='Hello')
        self.assertEquals(1, self.models.SampleModel.objects.all().count())

    def test__create_two_model_instances(self):
        self.models.SampleModel.objects.create(text='Hello')
        self.models.SampleModel.objects.create(text='Bye')
        self.assertEquals(2, self.models.SampleModel.objects.all().count())

    @classonlymethod 
    def tearDownClass(cls):
        super(ThisTestCaseRegistersItsOwnModels, cls).tearDownClass()
        for model in cls.class_models():
            connection.creation.sql_destroy_model(model, [], color.no_style())
