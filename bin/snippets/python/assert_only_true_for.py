import unittest

class TestCasePlusPlus(unittest.TestCase):
    def assert_only_true_for(self, objects_should_be_true_for, all_other_objects, predicate_fn, error_msg_when_true_fails, error_msg_when_others_fail):
        self.assert_predicate_result(
            expected_predicate_result = True,
            objects_should_be_true_for = objects_should_be_true_for,
            predicate_fn = predicate_fn,
            error_msg = error_msg_when_true_fails
        )

        self.assert_predicate_result(
            expected_predicate_result = False,
            objects_should_be_true_for = set(all_other_objects) - set(objects_should_be_true_for),
            predicate_fn = predicate_fn,
            error_msg = error_msg_when_others_fail
        )

    def assert_predicate_result(self, expected_predicate_result, objects_should_be_true_for, predicate_fn, error_msg):
        cls_to_predicate_result = ((cls, predicate_fn(cls)) for cls in objects_should_be_true_for)
        failures = list(cls for cls, predicate_result in cls_to_predicate_result if predicate_result != expected_predicate_result)
        self.assertTrue(len(failures) == 0, '%s - %s' % (error_msg, failures))


class Example(unittest.TestCase):
    pass

class ExamplePlusPlus(TestCasePlusPlus):
    def test__only_exampleplusplus_is_subclass(self):
        self.assert_only_true_for(
            objects_should_be_true_for = [ExamplePlusPlus],
            all_other_objects = [ExamplePlusPlus, Example],
            predicate_fn = lambda cls: issubclass(cls, TestCasePlusPlus),
            error_msg_when_true_fails = 'should implement TestCasePlusPlus',
            error_msg_when_others_fail = 'should NOT implement TestCasePlusPlus'
        )


if __name__ == "__main__":
    unittest.main()

