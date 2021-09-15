from pymongo import MongoClient

from better_base.adapters.db_adapter_type import DbAdapterType


class MongoDbAdapter(DbAdapterType):

    def __init__(self, cnx_str, db_name, collection):
        self._db_client: MongoClient = MongoClient(cnx_str)
        self._db_client = self._db_client[db_name]
        self._db_client = self._db_client[collection]

    def find_one(self, filter_, projection):
        return self._db_client.find_one(projection, filter_)

    def insert_one(self, document):
        result = self._db_client.insert_one(document)
        return {
            'id': result.inserted_id,
            'acknowledged': result.acknowledged
        }

    def update_one(self, filter_, update):
        return self._db_client.update_one(filter_, update)

    def delete_one(self, filter_):
        return self._db_client.delete_one(filter_)

    # many:

    def find(self, filter_, projection):
        return self._db_client.find(projection, filter_)

    def insert_many(self, documents):
        result = self._db_client.insert_many(documents)
        return {
            'ids': result.inserted_ids,
            'acknowledged': result.acknowledged
        }

    def update_many(self, filter_, update):
        return self._db_client.update_many(filter_, update)

    def delete_many(self, filter_):
        return self._db_client.delete_many(filter_)
