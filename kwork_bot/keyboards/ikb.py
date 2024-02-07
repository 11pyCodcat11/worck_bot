from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить в группу🥚", url="https://t.me/DOCTOT_HERBS_URL_BOT?startgroup")
        ],
        [
            InlineKeyboardButton(text="Официальный чат🥰", url="https://t.me/harcha_chat")
        ]
    ]
)

help_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇦UA", callback_data="UA_lang"),
            InlineKeyboardButton(text="🇷🇺RU", callback_data="RU_lang")
        ],
        [
            InlineKeyboardButton(text="🇺🇸US", callback_data="US_lang"),
            InlineKeyboardButton(text="🇮🇱IL", callback_data="IL_lang")

        ],
        [
            InlineKeyboardButton(text="🇮🇳IN", callback_data="IN_lang")
        ]
    ]
)

me_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="😎Прокачка", callback_data="boost"),
            InlineKeyboardButton(text="📝Задания", callback_data="Kwests")
        ],
        [
            InlineKeyboardButton(text="📜Истории", callback_data="Stories")
        ]
    ]
)

top1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐Глобальный топ", callback_data="global_top")
        ]
    ]
)

donate_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="20 попыток = 1.99$", callback_data="pay_1.99")
        ],
        [
            InlineKeyboardButton(text="50 попыток = 2.99$", callback_data="pay_2.99")
        ],
        [
            InlineKeyboardButton(text="100 попыток = 4.99$", callback_data="pay_4.99")
        ],
        [
            InlineKeyboardButton(text="200 попыток = 8.99$", callback_data="pay_8.99")
        ]
    ]
)

boost_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ℹ️Информацияℹ️", callback_data="boost_info")
        ],
        [
            InlineKeyboardButton(text="Улучшить🔋", callback_data="boost_1"),
            InlineKeyboardButton(text="Улучшить🥵", callback_data="boost_2")
        ],
        [
            InlineKeyboardButton(text="Улучшить🦾", callback_data="boost_3")
        ],
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_profil")
        ]
    ]
)

back_to_boost_list_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_boost_list")
        ]
    ]
)


admin_first_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Разослать рекламный баннер📨💰", callback_data="send_spam_banner")
        ],
        [
            InlineKeyboardButton(text="Добавить рекламный канал📈💸", callback_data="add_spam_chenal")
        ]
    ]
)

def create_spam_ikb(ikb):
    inline_keyboard = []
    print(ikb)
    print(ikb[0])
    print(ikb[1])

    for text, link in zip(ikb[0], ikb[1]):
        inline_keyboard.append([InlineKeyboardButton(text=text, url=link)])
    print(inline_keyboard)
    spam_ikb = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return spam_ikb

admin_chtck_baner1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Всё верно✅", callback_data="Ok1")
        ],
        [
            InlineKeyboardButton(text="Неверно❌", callback_data="Non_ok")
        ]
    ]
)

admin_chtck_baner0 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Всё верно✅", callback_data="Ok0")
        ],
        [
            InlineKeyboardButton(text="Неверно❌", callback_data="Non_ok")
        ]
    ]
)

time_to_chenal_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⏱На час", callback_data="One_hour")
        ],
        [
            InlineKeyboardButton(text="⏲На сутки", callback_data="One_day")
        ],
        [
            InlineKeyboardButton(text="⏰На 3 дня", callback_data="Three_day")
        ],
        [
            InlineKeyboardButton(text="🕰На неделю", callback_data="One_week")
        ]
    ]
)

def create_sub_ikb(chenal_url):
    sub_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да, конечно хочу🥚", callback_data=f"I_wand_agg;{chenal_url}")
        ],
        [
            InlineKeyboardButton(text="Нет, я не хочу 50 яиц🍳", callback_data="No_i_nowont")
        ]
    ]
)
    return sub_ikb

scheck_sub_btn =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Я подписался✅", callback_data=f"I_sub")
        ]
    ]
)


back_to_profil_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_profil")
        ]
    ]
)