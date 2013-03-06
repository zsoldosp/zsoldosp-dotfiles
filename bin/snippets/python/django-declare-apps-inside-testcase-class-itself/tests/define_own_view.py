from django.test import TestCase
from django.utils.decorators import classonlymethod
from django.views.generic.base import View
from django.conf.urls.defaults import patterns
from django.http import HttpResponse

class DefineViewForTestCaseInSameFileSample(TestCase):
    class views:
        class HelloWorldView(View):
            def get(self, request, *args, **kwargs):
                return HttpResponse('Hello world!')

    # cannot move it into class urls due to the import uglyness
    urlpatterns = patterns('',
        (r'^helloworld/$', views.HelloWorldView.as_view()),
    )

    @classonlymethod 
    def setUpClass(cls):
        cls.urls = cls
        super(DefineViewForTestCaseInSameFileSample, cls).setUpClass()

    def test__can_use_view_and_url_defined_within_test(self):
        self.assertEqual('Hello world!', self.client.get('/helloworld/').content)
