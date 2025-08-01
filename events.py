from aiogram.types import Message
from aiogram.enums.content_type import ContentType
from aiogram import Router

event = Router()

@event.message()
async def join_chat_member(message: Message):
    if ContentType.NEW_CHAT_MEMBERS:
        await message.delete()
        await message.answer(f"Привет, {message.from_user.username}")

@event.message()
async def left_chat_member(message: Message):
    if ContentType.LEFT_CHAT_MEMBER:
        await message.delete()
        await message.answer(f"Пользователь {message.from_user.username} покинул группу")

@event.message()
async def main(message: Message):
    if ContentType.TEXT:
        return