from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.buttons.inline import language_button
from bot.buttons.reply import main_menu, back_text
from bot.states import Food
from db.models import User

main_router = Router()

@main_router.message(Food.res_menu, F.text == __(back_text))
@main_router.message(CommandStart())
async def lang_handler(message:Message, state:FSMContext):
    chat_id = message.from_user.id
    tg_first_name = message.from_user.first_name
    username = message.from_user.username
    user = await User.get(id_=chat_id)
    if not user:
        await User.create(id=chat_id, tg_first_name=tg_first_name, username=username)
        await message.answer("Please choose the language\n"
                             "Iltimos, tilni tanlang\n"
                             "Пожалуйста, выберите язык",
                             reply_markup=language_button())
    else:
        await state.set_state(Food.main_menu)
        await message.answer(_("🏠Welcome to the main menu"), reply_markup=main_menu())


@main_router.callback_query(F.data.in_(('ru', 'uz', 'en')))
async def start_handler(callback:CallbackQuery):
    await callback.message.answer(_("🏠Welcome to the main menu"), reply_markup=main_menu())

