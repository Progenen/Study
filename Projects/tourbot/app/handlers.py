from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class User_data(StatesGroup):
    currentCity = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я TourAcBot, я создан для туристов которые ищут достопремичательности и маршруты в популярных городах мира!",
                         reply_markup=kb.main)
    await message.reply("Чем могу помочь?")

@router.message(F.text == "Саня?")
async def cmd_help(message: Message):
    await message.answer("Пидор!")

@router.message(F.text == "Покажи мне Великого Гойдмастера")
async def cmd_help(message: Message):
    await message.answer_photo(
        photo="https://cs14.pikabu.ru/post_img/2023/09/22/7/1695379130192561029.jpg",
        caption="Это приблизительный портрет. Компьютерные технологии еще не дошли то того чтобы передать в точности столь обширную, великую фигуру. \n ГОЙДА ГОЙДА ГОЙДА \n Саня пидор")

@router.message(F.text == 'О каких городах ты знаешь?')
async def cities(message: Message):
    await message.answer('Города которые я знаю:', reply_markup=kb.cities)

@router.message(F.text == 'Выбрать другой город')
async def cities(message: Message):
    await message.answer('Города которые я знаю:', reply_markup=kb.cities)

@router.callback_query(F.data == 'moscow')
async def moscow(callback: CallbackQuery, state: FSMContext):
    await callback.answer("#")
    await state.update_data(currentCity='moscow')
    await callback.message.answer_photo(
        photo="https://horosho-tam.ru/thumb/1600/pics/75/69/59a18064d895b120c4366975/moskva-o-stolitse-rossii-6975.jpg",
        caption="Москва прекрасный город! Что бы вы хотели о нем узнать?", reply_markup=kb.abis)

@router.callback_query(F.data == 'astana')
async def moscow(callback: CallbackQuery, state: FSMContext):
    await callback.answer("#")
    await state.update_data(currentCity='astana')
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikivoyage/ru/thumb/5/5a/Talan_Towers_9.jpg/1200px-Talan_Towers_9.jpg",
        caption="Астана прекрасный город! Что бы вы хотели о нем узнать?", reply_markup=kb.abis)

@router.callback_query(F.data == 'newyork')
async def moscow(callback: CallbackQuery, state: FSMContext):
    await callback.answer("#")
    await state.update_data(currentCity='newyork')
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/1200px-New_york_times_square-terabass.jpg",
        caption="Нью-Йокр прекрасный город! Что бы вы хотели о нем узнать?", reply_markup=kb.abis)
    
@router.message(F.text == 'Достопримечательности')
async def sights(message: Message, state: FSMContext):
    city = await state.get_data()

    if city.get('currentCity') == 'moscow':
        await message.answer_photo(
            photo="https://www.sutochno.ru/doc/images/galleries/182/msk4.jpg",
            caption="Красная площадь это символ Мосвы, ее визитная карточка. Здорово что в нашем городе эта визитная карточка мирового масштаба. Думаю любой иностранец хоть раз побывав тут, пропитался духом восхищения и величия и до сих пор рассказывает о ней, своим знакомым именно с этим чувством. Европейские площади не могут дать такой энергетики. Величественный Собор Василия Блаженного завораживает своим цветом и формами. Место с богатой историей и потрясающей архитектурой."
        )     
        await message.answer_photo(
            photo="https://moscowexcursion.com/wp-content/uploads/2019/09/sobor-vasiliya-blazhennogo-v-moskve-940x1200.jpg",
            caption="Собор Василия Блаженного одна из визитных карточек Москвы. Расположений на Красной Площади. Невероятная архитектура. Разные купола , как по цвету так и по стилю. Всегда прихожу к нему чтоб хотя бы 5 минут постоять и посмотреть."
        )     
    elif city.get('currentCity') == 'astana':
        await message.answer_photo(
            photo="https://avatars.mds.yandex.net/get-altay/10285614/2a0000018fb43713a1d76503f6f21c41c0fd/L_height",
            caption="Одна из основных достопримечательностей Казахстана – монумент Байтерек является главным символом Астаны, олицетворяющий представление казахского народа о мироздании. По преданию Байтерек – это древо жизни, к которому стремится священная птица Самрук."
        )     
        await message.answer_photo(
            photo="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/4c/d5/60/khan-shaty-exterior.jpg?w=2000&h=-1&s=1",
            caption="Хан Шатыр» — крупный торгово-развлекательный центр в столице Казахстана Астане. Открыт 6 июля 2010 года. Является самым большим шатром в мире. «Хан Шатыр» вошёл в Книгу рекордов Гиннесса Общая площадь Хан Шатыра — 127 тысяч квадратных метров. В помещении размещены рознично-торговые и развлекательные комплексы"
        )     
    elif city.get('currentCity') == 'newyork':
        await message.answer_photo(
            photo="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/9d/74/9f/photo0jpg.jpg?w=2000&h=-1&s=1",
            caption="Классический образ Нью-Йорка, каким его представляет большинство посетителей, перед тем как попасть сюда: впечатляющие небоскребы, такие как Крайслер-билдинг и Эмпайр-стейт-билдинг, культовые общественные здания, такие как Центральный вокзал Нью-Йорка и Нью-Йоркская публичная библиотека, и бесконечный шум и суета улиц большого города. Пятая авеню – это просто настоящий рай для шопоголиков, где можно найти магазины на самый взыскательный вкус, с модными марками, начиная от самых доступных и заканчивая самыми элитными. Посетите Рокфеллеровский центр, чтобы ощутить величественную роскошь стиля ар-деко. Гурманам непременно понравятся рестораны с множеством посетителей в Корейском квартале, которые работают допоздна. С приходом ночи ритм жизни в Мидтауне немного затихает, но даже несмотря на это в любое время дня и ночи, находясь здесь, ты понимаешь, что это настоящий Нью-Йорк."
        )     
        await message.answer_photo(
            photo="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/90/ab/88/central-park-manhattan.jpg?w=1400&h=-1&s=1",
            caption="В парке расположенном среди небоскребов впечатляет уют и забота о посетителях. Здесь бесплатно предоставлены туалеты, фонтанчики, скамейки и столики для отдыха, а также всё очень чисто."
        )     

@router.message(F.text == 'Маршруты')
async def sights(message: Message, state: FSMContext):
    city = await state.get_data()

    if city.get('currentCity') == 'moscow':
        await message.answer(f"Маршрут до центра Москвы - 1 час 5 минут \n https://yandex.kz/maps/-/CDd8JZ8k")  
    elif city.get('currentCity') == 'astana':
        await message.answer(f"Маршрут через президентский парк - 40 минут \n https://yandex.kz/maps/-/CDd8NBz9")    
    elif city.get('currentCity') == 'newyork':
        await message.answer(f"Маршрут до Гров-стрит - 41 минута \n https://yandex.kz/maps/-/CDd8NP~J")