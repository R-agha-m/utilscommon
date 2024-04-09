from unittest import TestCase, main

try:
    from .detect_boolean import detect_boolean, FALSE_STRINGS
except ImportError:
    from detect_boolean import detect_boolean, FALSE_STRINGS


class DetectBooleanTest(TestCase):

    def test_detect_boolean_by_false_strings(self):
        for false_string in FALSE_STRINGS:
            with self.subTest(false_string=false_string):
                self.assertFalse(detect_boolean(false_string))

    def test_detect_boolean_by_true_strings(self):
        self.assertTrue(detect_boolean('true'))

    def test_detect_boolean_by_false_things(self):
        self.assertFalse(detect_boolean(0))

    def test_detect_boolean_by_true_things(self):
        self.assertTrue(detect_boolean(1))


if __name__ == "__main__":
    main()
