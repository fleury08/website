import unittest
from datetime import datetime

from . import mongodb_tool


class TestMongoDBTool(unittest.TestCase):

    def test_parse(self):
        valid_modbo = mongodb_tool.MongoDbContainer(object_id="654575eeeb4cdcc6ccc65f08")
        valid_dt = datetime(2023, 11, 3, 23, 36, 30, 0, None)
        self.assertEqual(mongodb_tool.mongo_id_parse(valid_modbo),valid_dt)

        invalid_modbo = mongodb_tool.MongoDbContainer(object_id="")
        self.assertRaises(ValueError, mongodb_tool.mongo_id_parse, invalid_modbo)

        short_modbo = mongodb_tool.MongoDbContainer(object_id="654575eeeb4cdcc6ccc65f")
        self.assertRaises(ValueError, mongodb_tool.mongo_id_parse, short_modbo)

        long_modbo = mongodb_tool.MongoDbContainer(object_id="654575eeeb4cdcc6ccc65f080")
        self.assertRaises(ValueError, mongodb_tool.mongo_id_parse, long_modbo)

        none_modbo = mongodb_tool.MongoDbContainer(object_id=None)
        self.assertRaises(ValueError, mongodb_tool.mongo_id_parse, none_modbo)
        self.assertRaises(ValueError, mongodb_tool.mongo_id_parse, None)

