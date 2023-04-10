from enum import Enum

from product.models import Product, Category


class ImplementedModelsEnum(Enum):
    PRODUCT = Product.__class__, 'Product'
    CATEGORY = Category.__class__, 'Category'

    def __new__(cls, *values):
        obj = object.__new__(cls)
        obj._value_ = values[0]
        for other_value in values[1:]:
            cls._value2member_map_[other_value] = obj
        obj._values = values
        return obj

    def __repr__(self):
        return '<%s.%s: %s>' % (
                self.__class__.__name__,
                self._name_,
                ', '.join([repr(v) for v in self._values]),
                )

    def __str__(self) -> str:
        return self.name

    @classmethod
    def choices(cls) -> tuple:
        return tuple((i.name, i.value) for i in cls)
