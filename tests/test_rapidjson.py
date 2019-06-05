import sys
import unittest


class TestWithoutRapidJson(unittest.TestCase):
    def setUp(self):
        self._temp_rapidjson = None
        if sys.modules.get('rapidjson'):
            self._temp_rapidjson = sys.modules['rapidjson']
        sys.modules['rapidjson'] = None

    def tearDown(self):
        if self._temp_rapidjson:
            sys.modules['rapidjson'] = self._temp_rapidjson
        else:
            del sys.modules['rapidjson']

    def tests_using_rapidjson(self):
        flag = True
        try:
            import rapidjson
        except ImportError:
            flag = False
        self.assertFalse(flag)


class TestWithRapidJson(unittest.TestCase):
    def tests_using_rapidjson(self):
        flag = True
        try:
            import rapidjson
        except ImportError:
            flag = False
        self.assertTrue(flag)
