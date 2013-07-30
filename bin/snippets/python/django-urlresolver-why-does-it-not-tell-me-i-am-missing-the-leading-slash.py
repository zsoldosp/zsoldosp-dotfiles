from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect
"""
GET index.html HTTP/1.1
Host: www.example.com

==> HTTP/1.1 400 Bad Request


GET /index.html HTTP/1.1
Host: www.example.com

==> HTTP/1.1 200
"""
class myurlpatterns:
    urlpatterns = patterns('',
        url(r'^hello', lambda *a, **kw: HttpResponseRedirect('/'), {}, 'foo'),
    )

from django.core import urlresolvers 
from paessler.activation import urls
orig_root_urlconf = settings.ROOT_URLCONF
settings.ROOT_URLCONF = 'paessler.activation.urls'
urlresolvers.clear_url_caches()
should_match = urlresolvers.resolve('/hello')
assert should_match is not None
try:
    unexpected_match = urlresolvers.resolve('hello')
    assert Falase, 'should have raised, but got %r' % unexpected_match
except urlresolvers.Resolver404:
    # why not a meaningful text?
    

