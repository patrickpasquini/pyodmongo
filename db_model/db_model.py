from .main_model import MainModel
from .db_model_init import resolve_indexes, resolve_lookup_and_set
from .id_model import Id
from datetime import datetime
from pprint import pprint


class DbModel(MainModel):
    id: Id = None
    created_at: datetime = None
    updated_at: datetime = None
    _pipeline: list = []

    def __init__(self, **attrs):
        if attrs.get('_id') is not None:
            attrs['id'] = attrs.pop('_id')
        super().__init__(**attrs)

    def __init_subclass__(cls):
        ref_pipeline = resolve_lookup_and_set(cls=cls, pipeline=[], path='')
        pprint(ref_pipeline)
        print()
        indexes = []
        for key in cls.__fields__.keys():
            extra = cls.__fields__[key].field_info.extra
            idx = resolve_indexes(key=key, extra=extra)
            indexes += idx
        setattr(cls, '_indexes', indexes)
        setattr(cls, '_reference_pipeline', ref_pipeline)

    class Config:
        anystr_strip_whitespace = True
