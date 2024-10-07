import unittest
from parse_data import parse_yaml, parse_json, parse_xml


class test_json(unittest.IsolatedAsyncioTestCase):
    async def test_search(self):
        condition = await parse_json()
        self.assertTrue(type(condition) is str)


class test_xml(unittest.IsolatedAsyncioTestCase):
    async def test_search(self):
        condition = await parse_xml()
        self.assertTrue(type(condition) is str)


class test_yaml(unittest.IsolatedAsyncioTestCase):
    async def test_search(self):
        condition = await parse_yaml()
        self.assertTrue(type(condition) is str)


if __name__ == '__main__':
    test_json.main()
    test_xml.main()
    test_json.main()
