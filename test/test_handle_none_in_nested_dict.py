from unittest import TestCase, main

try:
    from utilscommon.handle_none_in_nested_dict import handle_none_in_nested_dict
except ImportError:
    from handle_none_in_nested_dict import handle_none_in_nested_dict


class HandleNoneInNestedDictTest(TestCase):

    def test_handle_str(self):
        data = handle_none_in_nested_dict(dict_data={1: {2: {3: "hi"}}},
                                          keys=(1, 2, 3,))
        self.assertEqual(data, 'hi')

    def test_handle_dict(self):
        data = handle_none_in_nested_dict(dict_data={1: {2: {3: {4:"hi"}}}},
                                          keys=(1, 2, 3,))
        self.assertEqual(data, {4:"hi"})

    def test_handle_none(self):
        data = handle_none_in_nested_dict(dict_data={1: {2: {3: None}}},
                                          keys=(1, 2, 3,))
        self.assertEqual(data, None)

    def test_handle_not_exist_key(self):
        data = handle_none_in_nested_dict(dict_data={1: {2: None}},
                                          keys=(1, 2, 3,))
        self.assertEqual(data, None)


if __name__ == "__main__":
    main()
