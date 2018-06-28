from typing import Any, Optional, Deque
from . import log

proxies: Any = ...

def manage(module, **params): ...
def clear_managers(): ...

reset_rollback: Any = ...
reset_commit: Any = ...
reset_none: Any = ...

class _ConnDialect(object):
    def do_rollback(self, dbapi_connection): ...
    def do_commit(self, dbapi_connection): ...
    def do_close(self, dbapi_connection): ...

class Pool(log.Identified):
    logging_name: str = ...
    echo: Any
    def __init__(self, creator, recycle: int = ..., echo: Optional[Any] = ..., use_threadlocal: bool = ...,
                 logging_name: Optional[Any] = ..., reset_on_return: bool = ..., listeners: Optional[Any] = ...,
                 events: Optional[Any] = ..., dialect: Optional[Any] = ...,
                 _dispatch: Optional[Any] = ...) -> None: ...
    def add_listener(self, listener): ...
    def unique_connection(self): ...
    def recreate(self): ...
    def dispose(self): ...
    def connect(self): ...
    def status(self): ...

class _ConnectionRecord(object):
    finalize_callback: Deque[Any]
    def __init__(self, pool, connect: bool = ...) -> None: ...
    fairy_ref: Any = ...
    starttime: Any = ...
    connection: Any = ...
    @property
    def info(self): ...
    @property
    def record_info(self): ...
    @classmethod
    def checkout(cls, pool): ...
    def checkin(self): ...
    @property
    def in_use(self): ...
    @property
    def last_connect_time(self): ...
    def close(self): ...
    def invalidate(self, e: Optional[Any] = ..., soft: bool = ...): ...
    def get_connection(self): ...

class _ConnectionFairy(object):
    connection: Any = ...
    def __init__(self, dbapi_connection, connection_record, echo) -> None: ...
    @property
    def is_valid(self): ...
    @property
    def record_info(self): ...
    def invalidate(self, e: Optional[Any] = ..., soft: bool = ...): ...
    def cursor(self, *args, **kwargs): ...
    def __getattr__(self, key): ...
    info: Any = ...
    def detach(self): ...
    def close(self): ...

class SingletonThreadPool(Pool):
    size: int = ...
    def __init__(self, creator, pool_size: int = ..., **kw) -> None: ...
    def recreate(self): ...
    def dispose(self): ...
    def status(self): ...

class QueuePool(Pool):
    def __init__(self, creator, pool_size: int = ..., max_overflow: int = ...,
                 timeout: int = ..., **kw) -> None: ...
    def recreate(self): ...
    def dispose(self): ...
    def status(self): ...
    def size(self): ...
    def checkedin(self): ...
    def overflow(self): ...
    def checkedout(self): ...

class NullPool(Pool):
    def status(self): ...
    def recreate(self): ...
    def dispose(self): ...

class StaticPool(Pool):
    def connection(self): ...
    def status(self): ...
    def dispose(self): ...
    def recreate(self): ...

class AssertionPool(Pool):
    def __init__(self, *args, **kw) -> None: ...
    def status(self): ...
    def dispose(self): ...
    def recreate(self): ...

class _DBProxy(object):
    module: Any = ...
    kw: Any = ...
    poolclass: Any = ...
    pools: Any
    def __init__(self, module, poolclass: Any = ..., **kw) -> None: ...
    def close(self): ...
    def __del__(self): ...
    def __getattr__(self, key): ...
    def get_pool(self, *args, **kw): ...
    def connect(self, *args, **kw): ...
    def dispose(self, *args, **kw): ...
