from fastapi import APIRouter
from . import auth, workflows, nodes

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(workflows.router, prefix="/workflows", tags=["workflows"])
router.include_router(nodes.router, prefix="/nodes", tags=["nodes"])
# chat.py добавим позже (WebSocket)