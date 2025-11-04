from aiogram import Router
from .photo import router as photo_router

router = Router()

router.include_routers(photo_router)
