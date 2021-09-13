import json

import dotenv
import pytest
import os

from better_base.adapters.database_adapter import DatabaseAdapter
from better_base.adapters.db_adapter_type import DbAdapterType


class DbAdapterTest:
    _methods = ['insert_one', 'insert_many'
                'find_one', 'find_all',
                'update_one', 'update_many',
                'delete_one', 'delete_many']

    def test_adapters(self):
        for db_type in DatabaseAdapter():
            self._get_config(db_type)
            [self._test(x) for x in self._methods]

    def _test(self, method: str):
        assert getattr(self._adapter, method)(self.test_data[method]) == self.assertion_data[method]

    @pytest.fixture()
    def fixture(self):
        self.setup()
        yield
        self.teardown()

    def setup(self):
        with open('test/adapters/db_adapter_test.json') as file:
            data = json.load(file)
        self.test_data = data['test_data']
        self.assertion_data = data['assertion_data']

    def teardown(self):
        pass

    def _get_config(self, db_type: str):
        dotenv.load_dotenv('.env.test.{}'.format(db_type))
        self.cnx_str = os.getenv('CNX_STR')
        self.db_name = os.getenv('DB_NAME')
        self.collection = os.getenv('COLLECTION')
        self._adapter: DbAdapterType = DatabaseAdapter.__class_getitem__(db_type)
