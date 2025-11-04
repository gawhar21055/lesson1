from aiogram import Router
from .common import router as common_router
from .documents import router as documents_router

router = Router()

router.include_routers(common_router, documents_router)
