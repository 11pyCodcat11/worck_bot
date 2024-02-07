from aiogram.fsm.state import StatesGroup, State

class AddSpamBanner(StatesGroup):
    photo = State()
    desc = State()
    butn = State()
    bytton_text = State()
    button_url = State()
    send_for_chat = State()

class AddSpamChenal(StatesGroup):
    chenal_url = State()
    id_chenal = State()
    time_url = State()

class Check_sub(StatesGroup):
    scheck_sub_btn  = State()


