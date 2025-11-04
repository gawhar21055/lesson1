from aiogram import Router,F,types
from aiogram.types.callback_query import CallbackQuery
router=Router()

@router.callback_query(F.data=="1")
async def handle_info_online_btn(callback_query: CallbackQuery):
    await callback_query.message.answer(text="1")
    await callback_query.answer(
        text="1"
        show_alert=True
    )