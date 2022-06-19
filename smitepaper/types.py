from sqlalchemy import types

from smitepaper.utils import get_fqn


class IntEnum(types.TypeDecorator):
    impl = types.Integer

    def __init__(self, enumtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enumtype = enumtype

    def process_bind_param(self, value, dialect):
        try:
            return value.value
        except Exception:
            return value

    def process_result_value(self, value, dialect):
        try:
            return self.enumtype(value)
        except Exception:
            return value

    def __repr__(self):
        return "{}({})".format(get_fqn(self.__class__), get_fqn(self.enumtype))
