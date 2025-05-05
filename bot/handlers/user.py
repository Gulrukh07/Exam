from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.buttons.inline import admin_contact
from bot.buttons.reply import back_text, admin_cont, r_menu, restaurant_menu, salats_text, salat_menu, \
    fast_food_text, fast_food_menu, hot_meal_menu
from bot.states import Food

user_router = Router()

@user_router.message(Food.main_menu, F.text == __(admin_cont))
async def contact_us(message:Message):
    await message.answer(_("Press admin button to contact us"), reply_markup=admin_contact())


@user_router.message(Food.hot_meal, F.text == __(back_text))
@user_router.message(Food.fast_food, F.text == __(back_text))
@user_router.message(Food.salat, F.text == __(back_text))
@user_router.message(Food.main_menu, F.text == __(r_menu))
async def main_panel(message:Message, state:FSMContext):
    await state.set_state(Food.res_menu)
    await message.answer(_("🍽 Restaurant Menu"), reply_markup=restaurant_menu())


@user_router.message(Food.res_menu, F.text == __(salats_text))
async def salat_panel(message:Message, state:FSMContext):
    await state.set_state(Food.salat)
    await message.answer(_("🥗 Salats"), reply_markup=salat_menu())

@user_router.message(Food.res_menu, F.text == __(fast_food_text))
async def fast_food_panel(message:Message, state:FSMContext):
    await state.set_state(Food.fast_food)
    await message.answer(_(" Fast Food"), reply_markup=fast_food_menu())

@user_router.message(Food.res_menu, F.text == __(salats_text))
async def hot_meal_panel(message:Message, state:FSMContext):
    await state.set_state(Food.hot_meal)
    await message.answer(_("🥗 Hor Meals"), reply_markup=hot_meal_menu())

