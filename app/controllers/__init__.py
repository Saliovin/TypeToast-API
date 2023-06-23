from starlite import Router

from . import records

__all__ = ["router"]

router = Router(path="/v1", route_handlers=[records.Record])
