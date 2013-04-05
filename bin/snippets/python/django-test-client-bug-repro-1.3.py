from django.test import TestCase
from django.utils.decorators import classonlymethod
from django.views.generic.base import View
from django.conf.urls.defaults import patterns
from django.http import HttpResponse

class TestClientDoesNotClearRaisedExceptions(TestCase):
    class views:
        class RaiseExceptionView(View):
            def get(self, request, should_raise=None):
                if should_raise:
                    raise ValueError('This view was configured to raise an exception')
                return HttpResponse('Hello world!')

    urlpatterns = patterns('',
        (r'raise-exception', views.RaiseExceptionView.as_view(), dict(should_raise=True), 'raise'),
        (r'no-exception', views.RaiseExceptionView.as_view(), dict(should_raise=False), 'noraise'),
    )

    @classonlymethod
    def setUpClass(cls):
        cls.urls = cls
        super(TestClientDoesNotClearRaisedExceptions, cls).setUpClass()

    def test_repro_from_the_end_users_perspective(self):
        self.assertEquals(200, self.client.get('/no-exception/').status_code, 'as a first request, no exception is raised')
        self.assertRaises(ValueError, lambda: self.client.get('/raise-exception/'))
        self.assertEquals(200, self.client.get('/no-exception/').status_code, 'despite the previous request raising an exception, I should be able to perform another request')

    def test__root_cause(self):
        self.assertRaises(ValueError, lambda: self.client.get('/raise-exception/'))
        self.assertEquals(None, self.client.exc_info, 'should have cleared client.exc_info, but did not - it is %s' % self.client.exc_info)


