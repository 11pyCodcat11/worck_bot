import asyncio
import datetime
import sqlite3
from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from keyboards.ikb import boost_ikb, back_to_boost_list_ikb, me_keyboard, create_spam_ikb, create_sub_ikb, scheck_sub_btn, back_to_profil_ikb
from untils import AddSpamBanner, AddSpamChenal, Check_sub
from keyboards.rkb import menu_keyboard
from apscheduler.schedulers.blocking import BlockingScheduler

router = Router()

def del_chenal(id_chenal):
    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM admin_database WHERE chenal_id = (?)", (id_chenal))
    conn.commit()
    conn.close()


def boost_batary(bd_name, rows):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT agges_index FROM database_{bd_name}""")
    agges_index = cur.fetchone()
    conn.close()
    new_index = None
    if agges_index > 0:
        conn = sqlite3.connect('database_egg_bot.db')
        cur = conn.cursor()
        cur.execute(f"""SELECT cash_index FROM database_{bd_name}""")
        rows = cur.fetchone()

        new_index = agges_index - rows
        conn.close
        if new_index > 0:
            conn = sqlite3.connect('database_eggBOOST_bot.db')
            cur = conn.cursor()
            cur.execute(f"""
            UPDATE database_{bd_name}
            SET agges_index = ?,
                win_index = ?,
                change_index = ?,
                all_ags = ?,
                date_of_reg = ?
            """, (new_index, list(rows)[0][1], list(rows)[0][2], list(rows)[0][3], list(rows)[0][4]))
            conn.close()

            return new_index

@router.callback_query(F.data == "boost")
async def present_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    await bot.edit_message_text(f'⬆️Прокачка⬆️\nЯиц: {list(rows)[0][0]} шт.\n\n🔋 Производительность: {list(rows)[0][1]} ур.\n Цена следующего уровня: {list(rows)[0][1] * 4} шт.\n🥵 Выносливость: {list(rows)[0][2]} ур.\n Цена следующего уровня: {list(rows)[0][2] * 4} шт.\n🦾 Сила: {list(rows)[0][3]}\n Цена следующего уровня: {list(rows)[0][3] * 4} шт.',call.from_user.id, call.message.message_id,
                           reply_markup=boost_ikb
                           )
    
@router.callback_query(F.data == 'boost_info')
async def boost_info_funck(call: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(text='''
ℹ️ <b>Информация о прокачке</b> ℹ️

🔋 <b>Производительность</b> - увеличивает количество яиц которые ты можешь получить

🥵 <b>Выносливость</b> - ускоряет перезарядку на следующий бросок яица

🦾 <b>Сила</b> - увеличивает дальность броска яица''', chat_id=call.message.chat.id, message_id=call.message.message_id, 
parse_mode='html',
reply_markup=back_to_boost_list_ikb
)
    
@router.callback_query(F.data == "back_to_boost_list")
async def present_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    await bot.edit_message_text(text=f'⬆️Прокачка⬆️\nЯиц: {list(rows)[0][0]} шт.\n\n🔋 Производительность: {list(rows)[0][1]} ур.\n Цена следующего уровня: {list(rows)[0][1] * 4} шт.\n🥵 Выносливость: {list(rows)[0][2]} ур.\n Цена следующего уровня: {list(rows)[0][2] * 4} шт.\n🦾 Сила: {list(rows)[0][3]}\n Цена следующего уровня: {list(rows)[0][3] * 4} шт.', chat_id=call.message.chat.id, message_id=call.message.message_id,
                           reply_markup=boost_ikb
                           )
    
@router.callback_query(F.data == 'boost_1')
async def boost_1_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    if list(rows)[0][0] >= list(rows)[0][1] * 4:
        new_cash_index = list(rows)[0][0] - list(rows)[0][1] * 4
        new_proizvod = list(rows)[0][1] + 1
        vinosliv = list(rows)[0][2]
        stong = list(rows)[0][3]
        update_query = f"UPDATE database_{call.from_user.id} SET cash_index = ?, proizvod = ?, vinosliv = ?, stong = ?"
        values = (new_cash_index, new_proizvod, vinosliv, stong)

        # Выполняем SQL-запрос с передачей значений
        cur.execute(update_query, values)
        conn.commit()
        cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
        rows = cur.fetchall()

        
        await bot.edit_message_text(text=f'⬆️Прокачка⬆️\nЯиц: {list(rows)[0][0]} шт.\n\n🔋 Производительность: {list(rows)[0][1]} ур.\n Цена следующего уровня: {list(rows)[0][1] * 4} шт.\n🥵 Выносливость: {list(rows)[0][2]} ур.\n Цена следующего уровня: {list(rows)[0][2] * 4} шт.\n🦾 Сила: {list(rows)[0][3]}\n Цена следующего уровня: {list(rows)[0][3] * 4} шт.',chat_id=call.from_user.id, message_id=call.message.message_id,
                           reply_markup=boost_ikb
                           )
    else:
        print('else')
        await call.answer(f'Тебе не хватает 🥚яиц!\nНе хватает {list(rows)[0][1] * 4 - list(rows)[0][0]}🥚 шт.')
    conn.close()

@router.callback_query(F.data == 'boost_2')
async def boost_2_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    if list(rows)[0][0] >= list(rows)[0][2] * 4:
        new_cash_index = list(rows)[0][0] - list(rows)[0][2] * 4
        proizvod = list(rows)[0][1]
        new_vinosliv = list(rows)[0][2] + 1
        stong = list(rows)[0][3]
        update_query = f"UPDATE database_{call.from_user.id} SET cash_index = ?, proizvod = ?, vinosliv = ?, stong = ?"
        values = (new_cash_index, proizvod, new_vinosliv, stong)

        # Выполняем SQL-запрос с передачей значений
                # Выполняем SQL-запрос с передачей значений
        cur.execute(update_query, values)
        conn.commit()
        cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
        rows = cur.fetchall()
        await bot.edit_message_text(call.from_user.id, call.message.message_id, f'⬆️Прокачка⬆️\nЯиц: {list(rows)[0][0]} шт.\n\n🔋 Производительность: {list(rows)[0][1]} ур.\n Цена следующего уровня: {list(rows)[0][1] * 4} шт.\n🥵 Выносливость: {list(rows)[0][2]} ур.\n Цена следующего уровня: {list(rows)[0][2] * 4} шт.\n🦾 Сила: {list(rows)[0][3]}\n Цена следующего уровня: {list(rows)[0][3] * 4} шт.',
                           )
    else:
        await call.answer(f'Тебе не хватает 🥚яиц!\nНе хватает {list(rows)[0][2] * 4 - list(rows)[0][0]}🥚 шт.')
    conn.close()


@router.callback_query(F.data == 'boost_3')
async def boost_3_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    if list(rows)[0][0] >= list(rows)[0][3] * 4:
        new_cash_index = list(rows)[0][0] - list(rows)[0][2] * 4
        proizvod = list(rows)[0][1]
        vinosliv = list(rows)[0][2] 
        new_stong = list(rows)[0][3] + 1
        update_query = f"UPDATE database_{call.from_user.id} SET cash_index = ?, proizvod = ?, vinosliv = ?, stong = ?"
        values = (new_cash_index, proizvod, vinosliv, new_stong)

        # Выполняем SQL-запрос с передачей значений
                # Выполняем SQL-запрос с передачей значений
        cur.execute(update_query, values)
        conn.commit()
        cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
        rows = cur.fetchall()
        await bot.edit_message_text(call.from_user.id, call.message.message_id, f'⬆️Прокачка⬆️\nЯиц: {list(rows)[0][0]} шт.\n\n🔋 Производительность: {list(rows)[0][1]} ур.\n Цена следующего уровня: {list(rows)[0][1] * 4} шт.\n🥵 Выносливость: {list(rows)[0][2]} ур.\n Цена следующего уровня: {list(rows)[0][2] * 4} шт.\n🦾 Сила: {list(rows)[0][3]}\n Цена следующего уровня: {list(rows)[0][3] * 4} шт.',
                           reply_markup=boost_ikb
                           )
    else:
        await call.answer(f'Тебе не хватает 🥚яиц!\nНе хватает {list(rows)[0][3] * 4 - list(rows)[0][0]}🥚 шт.')
    conn.close()



@router.callback_query(F.data == 'back_profil')
async def back_profil_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    r = list(rows)
    print(f'https://t.me/{call.from_user.username}')
    cur.execute(f"SELECT SUM(agges_index) FROM database_{call.from_user.id}")
    total_agges_index = cur.fetchone()[0]
    await bot.edit_message_text(text=f'<a href="https://t.me/{call.from_user.username}">{call.from_user.first_name}</a>\n'
                                                 f'🥚 Брошено яиц: {r[0][0]} шт.\n'
                                                 f'⚔️ Побед: {r[0][1]}\n'
                                                 f'🔥 Попытки: {r[0][2]}\n'
                                                 f'📊 Всего брошено яиц: {total_agges_index}\n'
                                                 f'📅 Дата регистрации: <b>{r[0][4]}</b>',
                                                 chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                 parse_mode='html',
                                                 reply_markup=me_keyboard,
                                                 disable_web_page_preview=True
                                                 )
    conn.close()

#8
    
@router.callback_query(F.data == 'Kwests')
async def Kwests_funck(call: types.CallbackQuery, bot: Bot):
    first_Kwests = '❌'
    second_Kwests = '❌'
    therd_Kwests = '❌'
    fours_Kwests = '❌'
    fives_Kwests = '❌'
    sixt_Kwests = '❌'

    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM database_{call.from_user.id}")
    result = cur.fetchall()
    if len(result) > 0:
        if result[0] == 1:
            first_Kwests = '🟢'
        if result[0] == 1:
            second_Kwests = '🟢'
        if result[0] == 1:
            therd_Kwests = '🟢'
        if result[0] == 1:
            fours_Kwests = '🟢'
        if result[0] == 1:
            fives_Kwests = '🟢'
        if result[0] == 1:
            sixt_Kwests = '🟢'
        if result[0] == 1:
            sevens_Kwests = '🟢'
        if result[0] == 1:
            eights_Kwests = '🟢'
    conn.close()

    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT chenal_id, subscriptio_chanal FROM admin_database")
    result = cur.fetchall()
    print(result)
    id_for_checl_sub = []
    text_list = []
    status_dict = {}
    for id, linck in result:
        cur.execute("SELECT sub_user FROM admin_database WHERE chenal_id = ?", (id))
        users = cur.fetchall()
        if str(call.from_user.id) in list(users[0]):
            imoge = '🟢'
            id_for_checl_sub.append(id[0])
            text = f'{imoge} Подписаться на <a href="{linck}">канал</a>👑\nНаграда - 50 яиц. 🥚\n\n'
            text_list.append(text)
            status_dict[id[0]] = imoge
        else:
            imoge = '❌'
            id_for_checl_sub.append(id[0])
            status_dict[id[0]] = imoge
            text = f'{imoge} Подписаться на <a href="{linck}">канал</a>👑\nНаграда - 50 яиц. 🥚\n\n'
            text_list.append(text)
    chenal_text = ''.join(text_list)
    await bot.edit_message_text(f'{first_Kwests} Достичь 10 ур. Производительности 🔋\nНаграда - 200 яиц. 🥚\n\n{second_Kwests} Достичь 10 ур. Выносливости 🥵\nНаграда - 200 яиц. 🥚\n\n{therd_Kwests} Достичь 10 ур. Силы 🦾\nНаграда - 200 яиц. 🥚\n\n{fours_Kwests} Выиграть 20 сражений ⚔️\nНаграда - 10 попыток\n\n{fives_Kwests} Накопить 1,000 яиц. 🥚\nНаграда - 5 попыток\n\n{sixt_Kwests} Кинуть яйцо 50 раз 🐣\nНаграда - 5 попыток\n\n{chenal_text}',call.from_user.id, call.message.message_id,
                           reply_markup=back_to_profil_ikb,
                           parse_mode="html"
                           )

@router.callback_query(F.data == 'send_spam_banner')
async def send_spam_banner_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    await bot.send_message(call.from_user.id, '🏞Отравьте фото для баннера:')
    await state.set_state(AddSpamBanner.photo)






@router.callback_query(F.data == 'add_spam_chenal')
async def add_spam_chenal_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    await bot.send_message(call.from_user.id, '🌐Отправьте пожалуйста ссылку на необходимый канал:')
    await state.set_state(AddSpamChenal.chenal_url)

    

@router.callback_query(AddSpamBanner.send_for_chat, F.data == 'Ok1')
async def send_for_chat_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CHAT")
    rows = cur.fetchall()
    i = []
    i.append(data['text_for_btn_list'])
    i.append(data['url_for_btn_list'])
    ikb = create_spam_ikb(i)
    for row in rows:
        await bot.send_photo(row, photo=data['photo'], caption=data['desc'], reply_markup=ikb, parse_mode='html')
    await bot.send_message(call.from_user.id, 'Банер успешно разослан🤑\nМожете вернуться в главное меню⚙️',
                           reply_markup=menu_keyboard
                           )
    await state.clear()

@router.callback_query(AddSpamBanner.send_for_chat, F.data == 'Ok0')
async def send_for_chat_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CHAT")
    rows = cur.fetchall()
    for row in rows:
        await bot.send_photo(row, photo=data['photo'], caption=data['desc'], parse_mode='html')
    await bot.send_message(call.from_user.id, 'Банер успешно разослан🤑\nМожете вернуться в главное меню⚙️', 
                           reply_markup=menu_keyboard
                           )
    await state.clear()


@router.callback_query(F.data == 'Non_ok')
async def send_spam_banner_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    await bot.send_message(call.from_user.id, 'Заполним баннер заново.\n🏞Отравьте фото для баннера:')
    await state.set_state(AddSpamBanner.photo)

    
@router.callback_query(AddSpamChenal.time_url, F.data)
async def one_hour_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    now = datetime.datetime.now()
    after_one_day = None
    print(call.data)
    if call.data == 'One_hour':
        after_one_day = now + datetime.timedelta(hours=1)
    elif call.data == 'One_day':
        after_one_day = now + datetime.timedelta(days=1)
    elif call.data == 'Three_day':
         after_one_day = now + datetime.timedelta(days=3)
    elif call.data == 'One_week':
         after_one_day = now + datetime.timedelta(days=7)
    scheduler = BlockingScheduler()
    scheduler.add_job(del_chenal(data['id_chenal']), 'date', run_date=after_one_day)
    scheduler.start()


    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO admin_database (subscriptio_chanal, chenal_id) VALUES (?, ?)", (data['chenal_url'], data['id_chenal']))
    conn.commit()
    conn.close()
        
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CHAT")
    rows = cur.fetchall()
    for row in rows:
        await bot.send_message(row[0], '<b>❗️Новое задание❗️</b>\nХочень получить <b>50 яиц</b>🥚?', reply_markup=create_sub_ikb(data['chenal_url']), parse_mode='html')
    await bot.send_message(call.from_user.id, 'Канал успешно добавлен🤑\nОбъявление разосланно пользователям', reply_markup=menu_keyboard)
    await state.clear()
    conn.close()


@router.callback_query(F.data.startswith('I_wand_agg;'))
async def I_wand_agg_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    print(call.data)
    await bot.send_message(call.from_user.id, f'Что бы получить <b>50 яиц</b>🥚 нужно подписаться на <a href="{call.data.split(";")[1]}">канал</a>\nКак только подпишешься нажми на кнопку ниже:',
                           reply_markup=scheck_sub_btn,
                           parse_mode="html"
                           )
    await state.update_data(link = call.data.split(";")[1])
    await state.set_state(Check_sub.scheck_sub_btn)

@router.callback_query(Check_sub.scheck_sub_btn, F.data == 'I_sub')
async def I_sub_funck(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    data = await state.get_data()
    cur.execute(f"SELECT chenal_id FROM admin_database WHERE subscriptio_chanal = ?", (str(data['link']),))
    result = cur.fetchall()
    print(result)
    print(result[0])
    print(result[0][0])
    is_subscribed = await bot.get_chat_member(chat_id=result[0][0], user_id=call.from_user.id)
    print(is_subscribed.status)
    conn.close()

    if is_subscribed.status != 'left':
        conn = sqlite3.connect('database_eggBOOST_bot.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM database_{call.from_user.id}")
        result = cur.fetchall()
        print(result[0][0])
        one = list(result[0])
        one = int(one[0]) + 50
        two = result[0][1]
        three = result[0][2]
        four = result[0][3]
        cur.execute(f"UPDATE database_{call.from_user.id} SET cash_index = ?, proizvod= ?, vinosliv= ?, stong= ?", (one, two, three, four))
        conn.commit()
        conn.close()
        conn = sqlite3.connect('database_achiv_bot.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM admin_database")
        rows = cur.fetchall()
        cur.execute(f"UPDATE admin_database SET sub_user = ?", (str(rows[0]) + "|" + str(call.from_user.id)))


        result = cur.fetchall()
        await call.answer('Вам зачисленно 50 яиц🥚')
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await state.clear()
    else:
        await call.answer('❗️Вы не подписанны❗️')
        return
    

@router.callback_query(F.data == 'back_to_profil')
async def me_funck(call: types.CallbackQuery, bot: Bot):
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM database_{call.from_user.id}""")
    rows = cur.fetchall()
    r = list(rows)
    cur.execute(f"SELECT SUM(agges_index) FROM database_{call.from_user.id}")
    total_agges_index = cur.fetchone()[0]
    await bot.edit_message_text(f'<a href="https://t.me/{call.from_user.username}">{call.from_user.first_name}</a>\n'
                                                     f'🥚 Брошено яиц: {r[0][0]} шт.\n'
                                                     f'⚔️ Побед: {r[0][1]}\n'
                                                     f'🔥 Попытки: {r[0][2]}\n'
                                                     f'📊 Всего брошено яиц: {total_agges_index}\n'
                                                     f'📅 Дата регистрации: <b>{r[0][4]}</b>', call.from_user.id, call.message.message_id,
                                                     parse_mode='html',
                                                     reply_markup=me_keyboard,
                                                     disable_web_page_preview=True
                                                     )