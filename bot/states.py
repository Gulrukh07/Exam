from aiogram.fsm.state import StatesGroup, State


class Food(StatesGroup):
    main_menu = State()
    res_menu =State()
    salat = State()
    fast_food = State()
    hot_meal = State()