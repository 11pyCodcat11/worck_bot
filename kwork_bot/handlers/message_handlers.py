#AddSpamBanner.photo
import sqlite3
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
from untils import AddSpamBanner, AddSpamChenal
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
import asyncio
from keyboards.rkb import phone_keyboard
from keyboards.ikb import create_spam_ikb, admin_chtck_baner1, admin_chtck_baner0, time_to_chenal_ikb

#   await state.update_data(phone_number=message.text)
#   user_data = await state.get_data()
router = Router()



@router.message(AddSpamBanner.photo, F.photo)
async def AddSpamBanner_photo_funck(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(photo = message.photo[0].file_id)
    await bot.send_message(message.from_user.id, '📝Введите описание для баннера:\n(Если вы хотите поместить в тексты ссылку, сделайте это сейчас через форматирование telegram)')
    await state.set_state(AddSpamBanner.desc)

@router.message(AddSpamBanner.desc, F.text)
async def AddSpamBanner_desc_funck(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(desc = message.html_text)
    await bot.send_message(message.from_user.id, 'В банере будут кнопки?\n<i>(Кнопки подразумивают налиие ссылок)</i>', reply_markup=phone_keyboard, parse_mode='html')
    await state.set_state(AddSpamBanner.butn)

@router.message(AddSpamBanner.butn, F.text)
async def AddSpamBanner_butn_funck(message: Message, bot: Bot, state: FSMContext):
    if message.text == 'Да✅':
        await bot.send_message(message.from_user.id, 'Введите текст на кнопках без пробелов в фонмате <i>(Кнопака1:Кнопка2:Кнопка3)</i>:', parse_mode='html')
        await state.set_state(AddSpamBanner.bytton_text)
    else:
        data = await state.get_data()
        await message.answer_photo(photo=data['photo'], caption=data['desc'], reply_markup=admin_chtck_baner0, parse_mode='html', disable_web_page_preview=True)
        await state.set_state(AddSpamBanner.send_for_chat)


@router.message(AddSpamBanner.bytton_text, F.text)
async def AddSpamBanner_bytton_text_funck(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(text_for_btn_list = message.text.split(':'))
    await bot.send_message(message.from_user.id, 'Введите ссылки для кнопок в формате <i>(Ссылка1:Ссылка2:Ссылка3)</i>\n<b>ВАЖНО! Количество ссылок должно быть равно количеству текстов и ссылки должны быть в той же последовательности и текты к которым эти ссылки должны прилагаться.</b>:', reply_markup=phone_keyboard, parse_mode='html')
    await state.set_state(AddSpamBanner.button_url)

@router.message(AddSpamBanner.button_url, F.text)
async def AddSpamBanner_button_url_funck(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(url_for_btn_list = message.text.split(':'))
    data = await state.get_data()
    i = []
    i.append(data['text_for_btn_list'])
    i.append(data['url_for_btn_list'])
    ikb = create_spam_ikb(i)
    await message.answer_photo(photo=data['photo'], caption=data['desc'], reply_markup=ikb, disable_web_page_preview=True, parse_mode='html')
    await bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=admin_chtck_baner1)
    await state.set_state(AddSpamBanner.send_for_chat)
    
    
@router.message(AddSpamChenal.chenal_url, F.text)
async def AddSpamChenal_chenal_url_funck(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(chenal_url=message.html_text)
    await bot.send_message(message.from_user.id, '💬Введите id рекламного канала:\n(id канала можно получить по <a href="https://t.me/username_to_id_bot">ссылке</a>)', parse_mode="html")
    await state.set_state(AddSpamChenal.id_chenal)



@router.message(AddSpamChenal.id_chenal, F.text)
async def AddSpamChenal_id_chenal_funck(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(id_chenal=message.text)
    await bot.send_message(message.from_user.id, '⏳Выберите время на которое канал будет размещён в боте:', reply_markup=time_to_chenal_ikb)
    await state.set_state(AddSpamChenal.time_url)
