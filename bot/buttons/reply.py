from aiogram.types import KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

back_text = "⬅️ Back"
r_menu = "🍽 Restaurant Menu"
admin_cont = "📞 Contact Us"
salats_text = "🥗 Salats"
fast_food_text = "🍕 Fast Food"
hot_meals_text = "🍜 Hot Meals"
olive_text = "🥗 Olive"
sezar_text = "🥗 Sezar"
burger_text = "🍔 Burger"
hot_dog_text = "🌭 Hot Dog"
soup_text = "🍲 Soup"
osh_text = "🍛 Osh"


def make_reply_button(buttons:list, sizes:list, repeat=False):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*buttons)
    if repeat:
        rkb.adjust(sizes[0], repeat=True)
    else:
        rkb.adjust(*sizes)
    return rkb.as_markup(resize_keyboard=True)

def back_button():
    btn = [KeyboardButton(text=_(back_text))]
    size = [1]
    return make_reply_button(buttons=btn, sizes=size)

def main_menu():
    btn1 = KeyboardButton(text=_(r_menu))
    btn2 = KeyboardButton(text=_(admin_cont))

    btns = [btn1,btn2]
    size = [2]
    return make_reply_button(buttons=btns,sizes=size)

def restaurant_menu():
    btn1 = KeyboardButton(text=_(salats_text))
    btn2 = KeyboardButton(text=_(fast_food_text))
    btn3 = KeyboardButton(text=_(hot_meals_text))
    btn4 = KeyboardButton(text=_(back_text))

    btns = [btn1,btn2,btn3,btn4]
    sizes = [2]

    return make_reply_button(buttons=btns, sizes=sizes, repeat=True)


def salat_menu():
    btn1 = KeyboardButton(text=_(olive_text))
    btn2 = KeyboardButton(text=_(sezar_text))
    btn3 = KeyboardButton(text=_(back_text))

    btns = [btn1,btn2,btn3]
    sizes = [2]

    return make_reply_button(buttons=btns, sizes=sizes, repeat=True)

def fast_food_menu():
    btn1 = KeyboardButton(text=_(burger_text))
    btn2 = KeyboardButton(text=_(hot_dog_text))
    btn3 = KeyboardButton(text=_(back_text))

    btns = [btn1,btn2,btn3]
    sizes = [2]

    return make_reply_button(buttons=btns, sizes=sizes, repeat=True)

def hot_meal_menu():
    btn1 = KeyboardButton(text=_(osh_text))
    btn2 = KeyboardButton(text=_(soup_text))
    btn3 = KeyboardButton(text=_(back_text))

    btns = [btn1,btn2,btn3]
    sizes = [2]

    return make_reply_button(buttons=btns, sizes=sizes, repeat=True)
