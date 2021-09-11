from better_base.utils.subscriptable_class import Subscriptable


class NamespaceModel(Subscriptable):
    meta_conf: dict
    config: dict
    instance: object
