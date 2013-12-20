def create_class(debug):
    class Foo(object):
        def __init__(self, v):
            self.v = v

        if debug:
            def __repr__(self):
                return 'debug'
        else:
            def __repr__(self):
                return 'normal'
    return Foo


if __name__ == '__main__':
    assert 'debug' == repr(create_class(True)('debug=True'))
    assert 'normal' == repr(create_class(False)('debug=False'))


