from aiogram import Router, F, types

router = Router()


@router.message(F.photo & F.caption)
async def handle_photo_w_caption(message: types.Message):
    await message.copy_to(
        chat_id=message.chat.id,
    )


@router.message(F.photo & ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    await message.answer(text="I cant read a photo")


@router.message(F.text == "hello")
async def handle_text(message: types.Message):
    await message.answer(
        text=f"hello {message.from_user.full_name} your id {message.from_user.id}"
    )


@router.message(F.text.contains("hello"))
async def handle_conatains(message: types.Message):
    await message.answer(text="hi")
