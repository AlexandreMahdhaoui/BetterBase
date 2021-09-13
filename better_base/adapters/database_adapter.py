from better_base.adapters.db_adapter_type import DbAdapterType
from better_base.adapters.mongo_db_adapter import MongoDbAdapter
from better_base.utils.subscriptable_class import Subscriptable


class DatabaseAdapter(Subscriptable):
    mongo_db = MongoDbAdapter

    def __class_getitem__(cls, item) -> DbAdapterType:
        return cls._dict()[item]

    def __iter__(self):
        self._n_iter = 0
        self._max_iter = len(self._dict())
        return self

    def __next__(self):
        if self._n_iter <= self._max_iter:
            return self._dict().items()[self._n_iter]
        raise StopIteration
