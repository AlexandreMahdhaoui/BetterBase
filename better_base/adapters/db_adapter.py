from better_base.adapters.mongo_db_adapter import MongoDbAdapter
from better_base.utils.subscriptable_class import Subscriptable


class DbAdapter(Subscriptable):
    mongo_db = MongoDbAdapter

    def __iter__(self):
        self._n_iter = -1
        self._max_iter = len(self._dict())
        return self

    def __next__(self):
        self._n_iter += 1
        if self._n_iter <= self._max_iter:
            return list(self._dict().keys())[self._n_iter]
        raise StopIteration
