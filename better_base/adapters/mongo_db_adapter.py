from pymongo import MongoClient

from better_base.adapters.db_adapter_type import DbAdapterType


class MongoDbAdapter(metaclass=DbAdapterType):
    def __init__(
            self,
            cnx_str,
            db_name,
            collection
    ):
        self._db_client: MongoClient = MongoClient(cnx_str)
        self._db_client = self._db_client[db_name]
        self._db_client = self._db_client[collection]

    def find(self, document):
        return self._db_client.find(document)

    def find_one(self, document):
        return self._db_client.find_one(document)

    def insert_one(self, document):
        return self._db_client.insert_one(document)

    def update_one(self, filter_, update):
        return self._db_client.update_one(filter_, update)

    def delete_one(self, filter_):
        return self._db_client.delete_one(filter_)
