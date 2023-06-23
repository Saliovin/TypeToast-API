from starlite import Starlite
import uvicorn
from app.controllers import router
from app.database import sqlalchemy_plugin


app = Starlite(
    route_handlers=[router],
    plugins=[sqlalchemy_plugin]
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
