from aiogram import executor,types,Bot,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datas import add_computer,add_user,get_computers,get_users,start_db
from keyboards import admins_menu,reg_menu
file = open(file='token.txt')

token = file.read()
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot,storage=storage)

class RegState(StatesGroup):
    name = State()
    phone = State()

class CompState(StatesGroup):
    processor = State()
    videokarta = State()
    operativka = State()
    hdd = State()
    ssd = State()
    monitor = State()
    klava = State()
    mishka = State()
    naushnik = State()
    kovrik = State()

async def on_startup(_):
    await start_db()

admin_id = 5570471897
@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer(f'Salem admin xosh keldiniz!',reply_markup=admins_menu)      
    else:
        await message.answer(f'Salem {message.from_user.first_name}',reply_markup=reg_menu)
@dp.message_handler(text="Registration")
async def registration(message:types.Message):
    await message.answer("Atiniz kim")
    await RegState.name.set()


@dp.message_handler(state = RegState.name)
async def handle_start(message: types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Nomerinizdi jiberin")
    await RegState.phone.set()


@dp.message_handler(state = RegState.phone)
async def handle_start(message: types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        data['chat_id'] = message.chat.id
    await message.answer("Successfully finished")
    await add_user(first_name=data['name'],phone_num=data['phone'],id=data['chat_id'],nickname=message.from_user.first_name)
    await message.answer(text=f'''Sizdin magliwmatlariniz:
atiniz:{data["name"]},
telefon nomeriniz:{data["phone"]},
Eger magliwmatlarinizda qatelik ketken bolsa qaytaldan Registraciyadan otseniz boladi.''')


@dp.message_handler(text='Users')
async def get_all_users(message:types.Message):
    users = await get_users()
    for i in users:
        await message.answer(i)

@dp.message_handler(text='Share adds')
async def adds(message:types.Message):
    if admin_id==message.from_user.id:
        users_ids = await get_users()
        for i in users_ids:
            await bot.send_message(chat_id=i[0],text=f'Salem bul, reklkama,{message.from_user.first_name}')


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
