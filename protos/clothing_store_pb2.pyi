from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArticleSearchRequest(_message.Message):
    __slots__ = ("barcode",)
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    barcode: str
    def __init__(self, barcode: _Optional[str] = ...) -> None: ...

class Offer(_message.Message):
    __slots__ = ("discount_percent", "max_discoutn", "min_original_price")
    DISCOUNT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MAX_DISCOUTN_FIELD_NUMBER: _ClassVar[int]
    MIN_ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    discount_percent: float
    max_discoutn: float
    min_original_price: float
    def __init__(self, discount_percent: _Optional[float] = ..., max_discoutn: _Optional[float] = ..., min_original_price: _Optional[float] = ...) -> None: ...

class ArticleSearchResponse(_message.Message):
    __slots__ = ("item_type", "size", "colour", "image_url", "stock", "price", "offers")
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    OFFERS_FIELD_NUMBER: _ClassVar[int]
    item_type: str
    size: str
    colour: str
    image_url: str
    stock: int
    price: float
    offers: _containers.RepeatedCompositeFieldContainer[Offer]
    def __init__(self, item_type: _Optional[str] = ..., size: _Optional[str] = ..., colour: _Optional[str] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ..., price: _Optional[float] = ..., offers: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ...) -> None: ...
