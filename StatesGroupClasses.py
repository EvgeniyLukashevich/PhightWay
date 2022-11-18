from aiogram.dispatcher.filters.state import State, StatesGroup


class HeroCreate(StatesGroup):
    hero_name: str 
    gettingName = State()  
    gettingWay = State() 
    

class Fight(StatesGroup):
    chooseHero = State()
    chooseHit = State()

class HeroRemove(StatesGroup):
    chooseHero = State()
    removeHero = State()

class HeroInfo(StatesGroup):
    chooseHero = State()
    infoHero = State()