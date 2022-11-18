from aiogram import types

    
startButtons = ["Создать Героя", "Удалить Героя", "Инфа о Герое", "Инфа об игре", "Бой с Соперником"]
wayButtons = ['Ниндзя', 'Самурай', 'Камикадзе', 'Сёгун', 'Скала', "/Выход в Меню"]    
hitButtons = ["Захват", "Удар в голову", "Удар по корпусу", "Удар по ногам"]
exit_command = "/Выход в Меню"
exit_button = types.KeyboardButton(exit_command)   
waiting = "Ходит соперник"
waiting_button = types.KeyboardButton(waiting) 
fight_ending = "Схватка заканчивается"
fight_ending_button = types.KeyboardButton(fight_ending) 


def buttonsFromFile(name_list: list):
    name_buttons_list = []
    names_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(len(name_list)):
        name_buttons_list.append(types.KeyboardButton(name_list[i]))
        names_menu.row(name_buttons_list[i])
    names_exitbtn = types.KeyboardButton(exit_command)  
    names_menu.row(names_exitbtn)
    return names_menu

  
start_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_way_button1 = types.KeyboardButton(startButtons[0])
start_way_button2 = types.KeyboardButton(startButtons[1])
start_way_button3 = types.KeyboardButton(startButtons[2])
start_way_button4 = types.KeyboardButton(startButtons[3])
start_way_button5 = types.KeyboardButton(startButtons[4])    
start_menu.row(start_way_button1, start_way_button2)
start_menu.row(start_way_button3, start_way_button4)
start_menu.row(start_way_button5)

ways_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
way_button1 = types.KeyboardButton(wayButtons[0])
way_button2 = types.KeyboardButton(wayButtons[1])
way_button3 = types.KeyboardButton(wayButtons[2])
way_button4 = types.KeyboardButton(wayButtons[3])    
way_button5 = types.KeyboardButton(wayButtons[4])  
ways_menu.row(way_button1, way_button2)
ways_menu.row(way_button3, way_button4, way_button5)
ways_menu.row(exit_button)


hits_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
hit_button1 = types.KeyboardButton(hitButtons[0])
hit_button2 = types.KeyboardButton(hitButtons[1])
hit_button3 = types.KeyboardButton(hitButtons[2])
hit_button4 = types.KeyboardButton(hitButtons[3])
hits_menu.row(hit_button1, hit_button2)
hits_menu.row(hit_button3, hit_button4)
hits_menu.row(exit_button)

yesno_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
yes_btn = types.KeyboardButton('ДА')
no_btn = types.KeyboardButton('НЕТ')
yesno_menu.row(yes_btn, no_btn)
yesno_menu.row(exit_button)

one_btn_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
one_btn_1 = types.KeyboardButton(exit_command)
one_btn_menu.row(one_btn_1)

waiting_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
waiting_menu.row(waiting_button)
waiting_menu.row(exit_button)

fight_end_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
fight_end_menu.row(fight_ending_button)
fight_end_menu.row(exit_button)