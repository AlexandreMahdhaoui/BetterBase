import json

import dotenv
import pytest
import os

from better_base.adapters.db_adapter import DbAdapter
from better_base.adapters.db_adapter_type import DbAdapterType


class TestDbAdapters:
    _methods = ['insert_one', 'insert_many',
                'find_one', 'find_all',
                'update_one', 'update_many',
                'delete_one', 'delete_many']

    def test_adapters(self):
        for k in DbAdapter():
            self._get_config(k)
            [self._test(x) for x in self._methods]

    def _test(self, method: str):
        test = getattr(self._adapter, method)(self._adapter, self.test_data[method])
        assertion = self.assertion_data[method]
        assert test == assertion

    def _get_config(self, db_type: str):
        dotenv.load_dotenv('.env.test.{}'.format(db_type))
        cnx_str = os.getenv('CNX_STR')
        db_name = os.getenv('DB_NAME')
        collection = os.getenv('COLLECTION')
        self._adapter: DbAdapterType = DbAdapter[db_type]
        self._adapter.__init__(self._adapter, cnx_str, db_name, collection)

    @pytest.fixture()
    def fixture(self):
        self.setup()
        yield
        self.teardown()

    def setup(self):
        with open('test/adapters/test_db_adapter.json') as file:
            data = json.load(file)
        self.test_data = data['test_data']
        self.assertion_data = data['assertion_data']

    def teardown(self):
        pass
