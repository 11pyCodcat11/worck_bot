import datetime
import sqlite3
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.ikb import start_keyboard, help_keyboard, me_keyboard, top1, donate_keyboard, admin_first_btn
from data.data_base import create_bd_profil, create_bd_boost, create_bd_admin


router = Router()

@router.message(Command('start'))
async def start_funck(message: Message, bot: Bot):
    create_bd_profil(message.from_user.id)
    create_bd_boost(message.from_user.id)
    create_bd_admin()
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CHAT")
    rows = cur.fetchall()
    print(rows)
    result = []
    for i in rows:
        result.extend(i)
    print(result)
    if message.from_user.id not in result:
        cur.execute("INSERT INTO CHAT (id_chat) VALUES (?)", (message.from_user.id,))
        conn.commit()
    if message.from_user.id == 6491212354:
        await bot.send_message(message.from_user.id, 'Допро пожаловать в <b>⚙️админ-панель⚙️</b>.\nЗдесь вы можете выбрать <b>следующие действия:</b>', parse_mode="html", reply_markup=admin_first_btn)
    else:
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        conn = sqlite3.connect('database_egg_bot.db')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO database_{message.from_user.id} (agges_index, win_index, change_index, all_ags, date_of_reg) VALUES (?, ?, ?, ?, ?)", (0, 0, 0, 0, today_date))
        conn.commit()
        conn.close()
        conn = sqlite3.connect('database_eggBOOST_bot.db')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO database_{message.from_user.id} (cash_index, proizvod, vinosliv, stong) VALUES (?, ?, ?, ?)", (0, 0, 0, 0))
        conn.commit()
        conn.close()
        await bot.send_message(message.from_user.id, '<b>Привет 👋🏼 Я - БросьЯйцоБот  🥚</b>\n\n'
                                                    '<b>🟢Добавляй меня в чат и бросай яйца в своих друзей!🟢</b>\n\n'
                                                    '😎 Так же за полученные л. 🥚 ты можешь прокачивать себя!\n\n'
                                                    '<i>Если тебе скучно, можешь ещё зайти в</i>\n'
                                                    '<i>наш <a href="https://t.me/harcha_chat">Официальный чатик</a></i>🥰\n'
                                                    '<b>Есть вопросы? Пиши команду /help</b>',
                                                    parse_mode='html',
                                                    reply_markup=start_keyboard,    
                                                    disable_web_page_preview=True
                                )
    
@router.message(Command('help'))
async def help_funck(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
    f'<a href="https://t.me/{message.from_user.first_name}">{message.from_user.first_name}</a>\n'
    'Команды\n\n'
    '/me - Профиль\n'
    '/spit - Харкнуть\n'
    '/duel - Дуэль\n'
    '/top - Топ игроков\n'
    '/pay - Донат\n\n'
    '😎 Заходи в наш чат, и\n бросай яйца там - @harcha_chat\n'
    '🥰 Пиши @harcha_gamebot в\n любом чате и бросай яйца',
    parse_mode='html',
    reply_markup=help_keyboard,
    disable_web_page_preview=True
        )

@router.message(Command('me'))
async def me_funck(message: Message, bot: Bot):
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{message.from_user.id}""")
    rows = cur.fetchall()
    r = list(rows)
    print(f'https://t.me/{message.from_user.username}')
    cur.execute(f"SELECT SUM(agges_index) FROM database_{message.from_user.id}")
    total_agges_index = cur.fetchone()[0]
    await bot.send_message(message.from_user.id, f'<a href="https://t.me/{message.from_user.username}">{message.from_user.first_name}</a>\n'
                                                     f'🥚 Брошено яиц: {r[0][0]} шт.\n'
                                                     f'⚔️ Побед: {r[0][1]}\n'
                                                     f'🔥 Попытки: {r[0][2]}\n'
                                                     f'📊 Всего брошено яиц: {total_agges_index}\n'
                                                     f'📅 Дата регистрации: <b>{r[0][4]}</b>',
                                                     parse_mode='html',
                                                     reply_markup=me_keyboard,
                                                     disable_web_page_preview=True
                                                     )
    conn.close()

@router.message(Command('spit'))
async def spit_funck(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, '💬 Эта команда работает только в чатах 😔\nДобавь меня в свой чат и играй 🥚',
                           reply_markup=start_keyboard
                           )

@router.message(Command('duel'))
async def spit_funck(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, '💬 Эта команда работает только в чатах 😔\nДобавь меня в свой чат и играй 🥚',
                           reply_markup=start_keyboard
                           )
    
@router.message(Command('top'))
async def top_funck(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, какой топ хочешь посмотреть? 📊',
                           reply_markup=top1
                           )
    
@router.message(Command('pay'))
async def top_funck(message: Message, bot: Bot): 
    await bot.send_message(message.from_user.id, f'💰 Меню пожертвований 💎\n\n🤖 Помогите боту стать еще лучше! 🚀\n\nВыберите количество попыток, которые вы хотите приобрести:👇',
                           reply_markup=donate_keyboard
                           )






