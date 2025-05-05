from aiogram.types import InlineKeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder

uzb_text = "🇺🇿uz"
ru_text = "🇷🇺ru"
en_text = "🇺🇸en"


def make_inline_button(buttons: list, sizes: list, repeat = False):
    ikb = InlineKeyboardBuilder()
    ikb.add(*buttons)
    if repeat:
        ikb.adjust(sizes[0], repeat=True)
    else:
        ikb.adjust(*sizes)
    return ikb.as_markup()

def language_button():
    btn1 = InlineKeyboardButton(text=_(uzb_text), callback_data="uz")
    btn2 = InlineKeyboardButton(text=_(ru_text), callback_data="ru")
    btn3 = InlineKeyboardButton(text=_(en_text), callback_data="en")

    btns = [btn1,btn2,btn3]
    size = [3]
    return make_inline_button(buttons=btns,sizes=size)

def admin_contact():
    ikb = InlineKeyboardBuilder()
    ikb.add(*[InlineKeyboardButton(text='Admin', url='https://t.me/KhalilovnaG')])
    ikb.adjust(1)
    return ikb.as_markup(resize_keyboard=True)
