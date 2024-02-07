from typing import Optional

from aiogram import Router, F, html
from aiogram.types import InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultCachedPhoto

router = Router()


@router.inline_query()
async def show_user_links(inline_query: InlineQuery):
    if inline_query.query.startswith('@'):
        print(inline_query.query)
        username = inline_query.query[1:]
        # Obtain the user objects of both users
        user_sender = await inline_query.bot.get_chat_member(inline_query.from_user.id, inline_query.from_user.id)
        user_receiver = await inline_query.bot.get_chat_member(inline_query.from_user.id, username)

        if user_sender and user_receiver:
            # Create the message content
            message_text = f"{user_sender.user.first_name} кинул яйцо в {user_receiver.user.first_name}"

            results = [
                InlineQueryResultArticle(
                    id=inline_query.id,
                    title=f"Отправить яйцо в {user_receiver.user.first_name}",
                    input_message_content=InputTextMessageContent(
                        message_text=message_text
                    )
                )
            ]
            await inline_query.answer(results, is_personal=True)
        else:
            results = [
                InlineQueryResultArticle(
                    id=inline_query.id,
                    title='Пользователь не найден',
                    description='Введите сюда @username пользователя',
                    input_message_content=InputTextMessageContent(
                        message_text='text'
                    )
                )
            ]
            await inline_query.answer(results, is_personal=True)
    else:
        results = [
            InlineQueryResultArticle(
                id=inline_query.id,
                title='Пользователь не найден',
                description='Введите сюда @username пользователя',
                input_message_content=InputTextMessageContent(
                    message_text='text'
                )
            )
        ]
        await inline_query.answer(results, is_personal=True)