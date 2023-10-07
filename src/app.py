import enum
import json
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, Callable, Coroutine, Dict, Optional, ParamSpec, Tuple, TypeVar
from fastapi.dependencies.utils import get_typed_signature, get_typed_return_annotation, get_typed_annotation

P = ParamSpec("P")
R = TypeVar("R")

TWrappedFunk = Callable[[Tuple[Any, ...], Dict[str, Any]], Coroutine[Any, Any, Dict[str, Any] | Any]]
TFunc = Callable[[Any], TWrappedFunk]


class CacheType(enum.Enum):
    LIST = "List"
    CATALOGS = "Catalogs"


class CacheKeyPayload:
    namespace: str
    query_string: str

    def __init__(self, namespace: str, query_string: str):
        self.namespace = namespace
        self.query_string = query_string


class CacheKey:
    payload: CacheKeyPayload
    expire: float
    cache_type: CacheType

    def __init__(
        self,
        payload: CacheKeyPayload,
        expire: float,
        cache_type: CacheType,
    ):
        self.payload = payload
        self.cache_type = cache_type
        self.expire = expire


class Cache:
    __cache: Dict[CacheKey, Dict[str, Any]] = {}

    @classmethod
    def init(cls) -> None:
        cls.__cache = {}

    @classmethod
    def cache(cls, cache_type: CacheType, expire: Optional[int] = None) -> TFunc:
        def decorator(func: TFunc) -> TWrappedFunk:
            @wraps(func)
            async def wrapper(*args: Tuple[Any], **kwargs: Any | None) -> Any:
                # typed_signature = get_typed_signature(func)
                # typed_return_annotation = get_typed_return_annotation(func)
                # typed_annotation = get_typed_annotation(func)
                key_payload = CacheKeyPayload(
                    namespace=kwargs.get("self").base_route,
                    query_string=json.loads(kwargs.get("request").query_params.get("list_request"))
                    if cache_type == CacheType.LIST
                    else None,
                )
                key = CacheKey(
                    payload=key_payload,
                    expire=(datetime.now() + timedelta(seconds=expire)).timestamp() if expire else None,
                    cache_type=cache_type,
                )

                existing_key = next((i for i in cls.__cache if key.payload.__dict__ == i.payload.__dict__), None)
                if existing_key is not None and (
                    existing_key.expire is None or existing_key.expire > datetime.now().timestamp()
                ):
                    response = cls.__cache[existing_key]
                else:
                    if existing_key is not None and existing_key.expire < datetime.now().timestamp():
                        del cls.__cache[existing_key]
                    response = await func(*args, **kwargs)
                    cls.__cache[key] = response
                return response

            return wrapper

        return decorator

    @classmethod
    def clear_cache(cls, namespace: str, cache_type: CacheType):
        keys_to_deletion = []
        for key in cls.__cache:
            if key.payload.namespace == namespace and key.cache_type == cache_type:
                keys_to_deletion.append(key)
        for key in keys_to_deletion:
            cls.__cache.pop(key)
