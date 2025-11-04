from aiogram import Router 
from.info import router as callback_data_router
router=Router()
router.include_routers(callback_data_router)