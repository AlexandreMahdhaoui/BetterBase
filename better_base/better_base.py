import typing

from better_base.adapters.db_adapter_type import DbAdapterType
from better_manager.meta_conf.base_meta_conf import BaseMetaConf
from better_base.bootstrap import Bootstrap
from better_base.namespace_model import NamespaceModel


class BetterBase(Bootstrap):
    """
    Provides namespace for abstraction of database
    BetterBase bootstrap BetterManager initialization by providing configs of all microservices

    Bootstrap helps BetterBase at providing its own configuration
    >> Bootstrapping could help us fetching MetaConfigs and bootstrap other AppManagers
    >> Bootstrap's meta_conf is mandatory atm. However, other meta_configs could be retrieved while bootstrapping\
       BetterBase.
    """
    _name = 'base'
    _private_namespace = typing.Mapping[str, typing.Any]

    def __init__(
            self,
            name,
            namespace
    ):
        self._name = name
        self._meta_conf: BaseMetaConf = namespace[name]['meta_conf']

    def __getitem__(self, item) -> NamespaceModel:
        return self._private_namespace.get(item)

    def init(self):
        """
        BetterBase's initialization Called by BetterManager after the config bootstrapping process
        Init _private_namespace with config provided in bootstrap
        """
        for v in self._namespace[self._name]['config'].values():
            self._private_namespace[v['name']] = dict()

    def get_adapter(self, microservice, collection) -> DbAdapterType:
        return self._get_adapter(
            cnx_str=self._meta_conf['bootstrap']['cnx_str'],
            db_type=self._meta_conf['bootstrap']['db_type'],
            db_name=microservice,
            collection=collection
        )

    def set_adapter(self, microservice, collection) -> None:
        self._private_namespace[microservice][collection] = self._get_adapter(
            cnx_str=self._meta_conf['bootstrap']['cnx_str'],
            db_type=self._meta_conf['bootstrap']['db_type'],
            db_name=microservice,
            collection=collection
        )
