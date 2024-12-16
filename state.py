from aiogram.fsm.state import State, StatesGroup


class US(StatesGroup):
    ism_k = State()
    Yosh_k = State()
    Til_k = State()
    Tel_k = State()
    Vil_k = State()




class SHeK(StatesGroup):
    ism_y = State()
    Yosh_y = State()
    Til_y = State()
    Tel_y = State()
    Vil_y = State()




class  HK(StatesGroup):
    ism_h = State()
    Yosh_h = State()
    Til_h = State()
    Tel_h = State()
    Vil_h = State()



class  UK(StatesGroup):
    ism_u = State()
    Yosh_u = State()
    Til_u = State()
    Tel_u = State()
    Vil_u = State()



class  SHK(StatesGroup):
    ism_sh = State()
    Yosh_sh = State()
    Til_sh = State()
    Tel_sh = State()
    Vil_sh = State()