from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from StatesGroupClasses import HeroCreate
from StatesGroupClasses import Fight
from StatesGroupClasses import HeroInfo
from StatesGroupClasses import HeroRemove
from aiogram.types import ReplyKeyboardRemove
import random as rand
import time

from Enemy import Enemy
from Person import Person

import messages as mess
import dataBase as db
import markups
import battle as batt

bot = Bot(token = 'здесь был токен')

dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_):
    print("EBoBot is activated")


@dp.message_handler(commands=['start', 'Выход в Меню'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"{mess.startMessage(message.from_user.first_name)}", reply_markup=markups.start_menu)
    

@dp.message_handler(text="Создать Героя")
async def createHero(message: types.Message, state: FSMContext):
    if len(db.getFileNames(message.from_user.id)) >= 3:
        await message.reply("Стоп ⛔\nУ тебя уже есть 3 Героя:\n - Развивай их!\n - Или удали кого-то из них и создай нового Героя.", reply_markup=markups.start_menu)
    else:
        await bot.send_message(message.from_user.id, f"Ок, {message.from_user.first_name}!\nСейчас мы создадим тебе нового героя! 💪", reply_markup=markups.one_btn_menu)
        await bot.send_message(message.from_user.id, "Введи имя героя ✏")
        await state.set_state(HeroCreate.gettingName)

@dp.message_handler(state=HeroCreate.gettingName)
async def setHeroName(message: types.Message, state: FSMContext):
    if message.text == markups.exit_command:
        await bot.send_message(message.from_user.id, f"Мы в Меню", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
    else:
        await state.update_data(hero_name=message.text)
        user_data = await state.get_data()
        await bot.send_message(message.from_user.id, f"Хорошо!\nВыбери Путь Воина для героя по имени {user_data['hero_name']} ⚔", reply_markup=markups.ways_menu)
        await state.set_state(HeroCreate.gettingWay)    

@dp.message_handler(state=HeroCreate.gettingWay, text=markups.wayButtons)
async def setHeroWay(message: types.Message, state: FSMContext):
    if message.text == markups.exit_command:
        await bot.send_message(message.from_user.id, f"Мы в Меню", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
    else:
        user_data = await state.get_data()
        fighter = Person(message.from_user.id)
        fighter.person_list[1] = user_data['hero_name']
        fighter.person_list[2] = message.text
        match(message.text):
            case "Ниндзя":
                for i in range(3, len(fighter._ninja_pattern)):
                    fighter.person_list[i] = fighter._ninja_pattern[i]
            case "Самурай":
                for i in range(3, len(fighter._samurai_pattern)):
                    fighter.person_list[i] = fighter._samurai_pattern[i]
            case "Камикадзе":
                for i in range(3, len(fighter._kamikaze_pattern)):
                    fighter.person_list[i] = fighter._kamikaze_pattern[i]
            case "Сёгун":
                for i in range(3, len(fighter._shogun_pattern)):
                    fighter.person_list[i] = fighter._shogun_pattern[i]
            case "Скала":
                for i in range(3, len(fighter._rock_pattern)):
                    fighter.person_list[i] = fighter._rock_pattern[i] 
        db.writePerson(fighter.getPersonList())
        await bot.send_message(message.from_user.id, f"Герой успешно создан! 💥\n\n{mess.showPersonInfo(fighter.getPersonList())}", reply_markup=markups.start_menu)
        # await state.reset_data()
        await state.finish()

@dp.message_handler(state=HeroCreate.gettingWay)
async def setWrongHeroWay(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, f"Слушай, {message.from_user.first_name}... \nТы делаешь что-то не так ⛔\nПросто выбери Боевой Путь твоего героя ⬇", reply_markup=markups.ways_menu)




@dp.message_handler(text="Бой с Соперником")
async def sstart(message: types.Message, state: FSMContext):
    if len(db.getFileNames(message.from_user.id)) < 1:
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, у тебя нет Героев\nСоздай героя в Меню", reply_markup=markups.start_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, "Нужно выбрать, кого из героев отправить в бой ⬇",reply_markup=markups.buttonsFromFile(db.getFileNames(message.from_user.id)))
        await state.set_state(Fight.chooseHero)
        await state.update_data(id=message.from_user.id)
@dp.message_handler(state = Fight.chooseHero)
async def chooseName(message: types.Message, state: FSMContext):
    if message.text in db.getFileNames(message.from_user.id):
        fighter = Person(message.from_user.id)
        fighter.person_list = db.loadFromFileName(message.from_user.id, message.text)
        await state.update_data(person_list=db.loadFromFileName(message.from_user.id, message.text))
        user_data = await state.get_data()
        enemy = Enemy(user_data['person_list'][3])
        await state.update_data(enemy_list = enemy.enemy_list)
        user_data = await state.get_data()
        await bot.send_message(message.from_user.id, f'''Схватка обещает быть зрелищной!\n
{user_data['person_list'][2]} {user_data['person_list'][1]} ({user_data['person_list'][3]} уровень)
        🆚
{user_data['enemy_list'][2]} {user_data['enemy_list'][1]} ({user_data['enemy_list'][3]} уровень)\n
Твой ход, {message.from_user.first_name}. В бой!''', reply_markup=markups.hits_menu)
        await state.set_state(Fight.chooseHit)
    elif message.text == markups.exit_command:
        await bot.send_message(message.from_user.id, f"Мы в Меню", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
    else:
        await message.reply(f"Слушай, {message.from_user.first_name}... \nТы делаешь что-то не так ⛔\nПросто выбери Героя для битвы ⬇",reply_markup=markups.buttonsFromFile(db.getFileNames(message.from_user.id)))
@dp.message_handler(state = Fight.chooseHit)
async def battle(message: types.Message, state: FSMContext):
    if message.text in markups.hitButtons:
        fighter = Person(message.from_user.id)
        user_data = await state.get_data()
        
        hit_list = batt.personHit(user_data['person_list'], user_data['enemy_list'], message.text)
        user_data['enemy_list'][5] = round(user_data['enemy_list'][5]- hit_list[3], 2)
        await state.update_data(enemy_list =  user_data['enemy_list'])
        user_data = await state.get_data()
    
        await bot.send_message(message.from_user.id, f"👊 {mess.hitString(hit_list)}", reply_markup=markups.waiting_menu)
        
        if user_data['enemy_list'][5] <= 0:
            user_data['person_list'][4] += 10 // user_data['person_list'][3]
            fighter.updateLevelWin(user_data['person_list'])
            db.writePerson(user_data['person_list'])
            db.writeEnemyStats(user_data['enemy_list'])
            photoWin = open("data\materials\win.gif", 'rb')
            await bot.send_message(message.from_user.id, mess.winMessage(user_data['person_list'], user_data['enemy_list']), reply_markup=markups.fight_end_menu)
            await bot.send_animation(message.chat.id, photoWin, reply_markup=markups.start_menu)
            await state.finish()
            return

        hit_list = batt.personHit(user_data['enemy_list'], user_data['person_list'], rand.choice(markups.hitButtons))
        user_data['person_list'][5] = round(user_data['person_list'][5] - hit_list[3])
        await state.update_data(person_list =  user_data['person_list'])
        user_data = await state.get_data()
        time.sleep(1)
        await bot.send_message(message.from_user.id, f"👹 {mess.hitString(hit_list)}", reply_markup=markups.hits_menu)
        

        if user_data['person_list'][5] <= 0:
            user_data['person_list'][4] += 5 // user_data['person_list'][3]
            fighter.updateLevelLose(user_data['person_list'])
            db.writePerson(user_data['person_list'])
            db.writeEnemyStats(user_data['enemy_list'])
            photoLose = open("data\materials\lose.gif", 'rb')
            await bot.send_message(message.from_user.id, f"ТЫ ПРОИГРАЛ В ЭТОЙ СХВАТКЕ! 👎👎👎\nВозвращайся, когда будешь готов побеждать!", reply_markup=markups.fight_end_menu)
            await bot.send_animation(message.chat.id, photoLose, reply_markup=markups.start_menu)
            await state.finish()
            return
    elif message.text == markups.exit_command:
        await bot.send_message(message.from_user.id, f"Надеюсь, у тебя была веская причина уйти! \nВозвращайся, когда будешь готов побеждать!", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
    elif message.text == markups.waiting:
        await bot.send_message(message.from_user.id, f"Как только соперник завершит ход, у тебя будет возможность нанести удар")   
    elif message.text == markups.fight_ending:
        await bot.send_message(message.from_user.id, f"Дождись финальной анимации, и тебе откроется главное меню")   
    else:
        await message.reply(f"Слушай, {message.from_user.first_name}... \nТы делаешь что-то не так ⛔\nПросто выбери Боевой Приём ⬇", reply_markup=markups.hits_menu)




@dp.message_handler(text="Инфа о Герое")
async def infStart(message: types.Message, state: FSMContext):
    if len(db.getFileNames(message.from_user.id)) < 1:
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, у тебя нет Героев\nСоздай героя в Меню", reply_markup=markups.start_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, "Инфу о каком герое ты хочешь получить? ⬇",reply_markup=markups.buttonsFromFile(db.getFileNames(message.from_user.id)))
        await state.set_state(HeroInfo.chooseHero)
@dp.message_handler(state = HeroInfo.chooseHero)
async def chooseName(message: types.Message, state: FSMContext):
    if message.text in db.getFileNames(message.from_user.id):
        person_list = db.loadFromFileName(message.from_user.id, message.text)
        await bot.send_message(message.from_user.id, f"Вот инфа об этом герое 💥\n\n{mess.showPersonInfo(person_list)}", reply_markup=markups.start_menu)
        await state.finish()
    elif message.text == markups.exit_command:
        await bot.send_message(message.from_user.id, f"Мы в Меню", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
    else:
        await message.reply(f"Слушай, {message.from_user.first_name}... \nТы делаешь что-то не так ⛔\nПросто выбери Героя из списка ниже ⬇",reply_markup=markups.buttonsFromFile(db.getFileNames(message.from_user.id)))





@dp.message_handler(text="Удалить Героя")
async def delStart(message: types.Message, state: FSMContext):
    if len(db.getFileNames(message.from_user.id)) < 1:
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, у тебя нет Героев\nСоздай героя в Меню", reply_markup=markups.start_menu)
        await state.finish()
    else:
        await message.reply("Какого героя ты хочешь прогнать? ⬇",reply_markup=markups.buttonsFromFile(db.getFileNames(message.from_user.id)))
        await state.set_state(HeroRemove.chooseHero)
@dp.message_handler(state = HeroRemove.chooseHero)
async def choName(message: types.Message, state: FSMContext):
    if message.text in db.getFileNames(message.from_user.id):
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, твоё решение обдуманное и твёрдое?", reply_markup=markups.yesno_menu)
        await state.update_data(rem_name = message.text)
        await state.set_state(HeroRemove.removeHero)
    elif message.text == markups.exit_command:
        await bot.send_message(message.from_user.id, f"И не пришлось никого выгонять :)", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
    else:
        await message.reply(f"Наверное не стоит никого удалять ;)", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()
@dp.message_handler(state = HeroRemove.removeHero)
async def choName(message: types.Message, state: FSMContext):
    if message.text == 'ДА':
        user_data = await state.get_data()
        db.removeFromFileName(message.from_user.id, user_data['rem_name'])
        await bot.send_message(message.from_user.id, f"Этот Герой больше не с нами", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()    
    else:
        await message.reply(f"Любой ответ, кроме 'ДА' трактуется в пользу сохранения Героя", reply_markup=markups.start_menu)
        await state.reset_data()
        await state.finish()    


@dp.message_handler(text="Инфа об игре")
async def infGame(message: types.Message):
    await bot.send_message(message.from_user.id, f"{mess.gameInfo(message.from_user.first_name)}", reply_markup=markups.start_menu)



@dp.message_handler()
async def other(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"Выбирай из кнопок меню, {msg.from_user.first_name} ⬇", reply_markup=markups.start_menu)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)