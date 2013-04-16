from functools import wraps

print 'file being loaded'

class Foo:
    def __init__(self):
        print 'init'

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        print 'call'
        return wrapped


@Foo()
def foomethod():
    print 'foomethod'

print 'declarations over, calling foomethod()'
foomethod()
print 'done'
