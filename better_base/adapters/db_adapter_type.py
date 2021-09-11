from abc import ABC


class DbAdapterType(ABC):
    def __init__(
            self,
            cnx_str: str,
            db_name: str,
            collection: str
    ):
        pass

    # _one
    def find_one(self, *args, **kwargs):
        pass

    def insert_one(self, *args, **kwargs):
        pass

    def update_one(self, *args, **kwargs):
        pass

    def delete_one(self, *args, **kwargs):
        pass

    # _many
    def find(self, *args, **kwargs):
        pass

    def insert_many(self, *args, **kwargs):
        pass

    def update_many(self, *args, **kwargs):
        pass

    def delete_many(self, *args, **kwargs):
        pass
