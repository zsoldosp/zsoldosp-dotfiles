import unittest
""" I wanted to learn more about how one would go about
    extending unittest functionality. I learn best when I
    set a functional target, so I tried to implement parameterized
    tests (*) similar to NUnit's attributes. 

    And this proof of concept/spike is successful too!

    (*) I know there are already existing solutions, such as 
            http://pytest.org/latest/example/parametrize.html
            https://github.com/msabramo/python_unittest_parameterized_test_case
        but 
            a) the primary motivation here is learning
            b) I prefer NUnit's composition style over these inheritance 
               based ones"""


class params(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.rmethod = None
        self.method_to_call = None
        self.test_index = 0

    def __repr__(self):
        return repr(dict(
            hasnext=(self.rmethod!=None),
            args=self.args,
            kwargs=self.kwargs,
            test_index=self.test_index
        ))

    def __call__(self, rmethod):
        if type(rmethod) == type(self):
            self.rmethod = rmethod
            self.test_index = rmethod.test_index + 1
        else:
            self.method_to_call = rmethod
        return self

    def __iter__(self, method_to_call=None):
        if self.rmethod is not None:
            for x in self.rmethod:
                yield x
        yield self

class ParamTests(unittest.TestCase):
    @params(2, 9, 11)
    @params(-3, 8, 5)
    @params(0, 9, 9)
    def test_addition(self, a, b, expected_result):
        self.assertEquals(expected_result, a + b)


class ParamsTestSuite(unittest.TestSuite):
    def __iter__(self):
        for test in unittest.TestSuite.__iter__(self):
            test_method = getattr(test, test._testMethodName)
            if type(test_method) != params:
                yield test
                continue
            test_cls = type(test)
            orig_test_method = getattr(test_cls, test._testMethodName)
            while orig_test_method.method_to_call is None:
                orig_test_method = orig_test_method.rmethod
            orig_test_method = orig_test_method.method_to_call
            for p in test_method:
                new_test_method_name = '%s_%s' % (test._testMethodName, p.test_index)
                # TestSuite.__call__/TestSuite.__run__ is too complex
                # to try to reproduce. And since there is no hook to
                # modify the testname, because it's used to derive
                # values in the constructor, the easiest thing to do
                # is to create a new instance and ensure the class has
                # the new methods 
                # 
                # I don't quite like TestSuite's dual nature, but hey, 
                # I don't always like gravity neither!
                setattr(test_cls, new_test_method_name, lambda self: orig_test_method(self, *p.args, **p.kwargs))
                yield type(test)(new_test_method_name) 

runner = unittest.TextTestRunner()
suite = ParamsTestSuite([ParamTests('test_addition')])
result = runner.run(suite)
