import asyncio
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types.input_file import FSInputFile, BufferedInputFile
from aiogram.utils.chat_action import ChatActionSender

from aiogram.enums import ChatAction

router = Router()


async def send_file(message: types.Message):
    await asyncio.sleep(5)
    url = "https://images.unsplash.com/photo-1760556415132-533affdd9ccf?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=687"
    await message.reply_document(
        document=url,
        caption="some doc",
    )


@router.message(Command("pic"))
async def handle_pic_command(message: types.Message):
    text_file = types.BufferedInputFile(b"Hello, world!", filename="file.txt")
    # await message.bot.send_chat_action(
    #     chat_id=message.chat.id,
    #     action=ChatAction.UPLOAD_PHOTO,
    # )
    # await asyncio.sleep(10)

    # sender = ChatActionSender(
    #     bot=message.bot,
    #     chat_id=message.chat.id,
    #     action=ChatAction.UPLOAD_DOCUMENT,
    # )
    async with ChatActionSender.upload_document(
        bot=message.bot, chat_id=message.chat.id
    ):
        await asyncio.sleep(3)
        await message.reply_document(
            document=text_file,
        )


@router.message(Command("pic_file"))
async def handle_pic_file_command(message: types.Message):
    path = "/home/alien/Pictures/Icon.png"
    file = FSInputFile(
        path=path,
        filename="my photo",
    )
    await message.reply_photo(
        photo=file,
    )
    await message.reply_document(
        document=file,
    )


@router.message(Command("txt"))
async def handle_txt_command(message: types.Message):
    # file_io = io.BytesIO()
    # file_io.write(message.text)
    text_file = BufferedInputFile(b"Hello, world!", filename="file.txt")
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.CHOOSE_STICKER,
    )
    await message.reply_document(
        document=text_file,
    )
