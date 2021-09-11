import typing
from abc import ABC

from better_base.adapters.database_adapter import DatabaseAdapter
from better_base.adapters.db_adapter_type import DbAdapterType
from better_manager.meta_conf.base_meta_conf import BaseMetaConf


class Bootstrap(ABC):
    _name: str
    _db_adapter: DatabaseAdapter = DatabaseAdapter
    _meta_conf: BaseMetaConf
    _namespace = typing.Mapping[str, typing.Any]

    @classmethod
    def config_new_app(cls, *default_conf):
        adapter = cls._get_config_adapter()
        adapter.insert_many(default_conf)

    @classmethod
    def bootstrap(cls):
        """
        Bootstrap.bootstrap() will assume configs already exists in db.
        Default config will be provided by BetterManager
        """
        adapter = cls._get_config_adapter()
        cursor = adapter.find()
        for config in cursor:
            cls._namespace[config['name']]['config'] = config

    @classmethod
    def _get_adapter(cls, cnx_str, db_type, db_name, collection) -> DbAdapterType:
        adapter: DbAdapterType = cls._db_adapter[db_type]
        return adapter.__init__(cnx_str=cnx_str, db_name=db_name, collection=collection)

    @classmethod
    def _get_config_adapter(cls):
        return cls._get_adapter(**cls._meta_conf['bootstrap'])
