from better_base.adapters.db_adapter_type import DbAdapterType
from better_base.adapters.mongo_db_adapter import MongoDbAdapter
from better_base.utils.subscriptable_class import Subscriptable


class DatabaseAdapter(Subscriptable):
    mongo_db = MongoDbAdapter

    def __class_getitem__(cls, item) -> DbAdapterType:
        return cls._dict()[item]
