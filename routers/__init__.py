from aiogram import Router
from .command_router import router as command_router
from .photo_handlers import router as photo_handlers_router

router = Router()
router.include_routers(command_router, photo_handlers_router)
