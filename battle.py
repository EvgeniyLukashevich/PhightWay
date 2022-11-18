
import random as r

hit_kinds_list = ["Захват", "Удар в голову", "Удар по корпусу", "Удар по ногам"]
damage_modify = [2.5, 2, 1, 0.75]
agility_modify = [1, 1.25, 1.8, 2]
damage = 0

def firstMoveRight(user_agility, enemy_agility):
    if user_agility < enemy_agility:
        return False
    else:
        return True

def nextMoveRight(user_agility, enemy_agility):
    dice = 0
    if user_agility >= enemy_agility:
        dice = int(round(user_agility))
    else: dice = int(round(enemy_agility))

    if user_agility + r.randint(1, dice) > enemy_agility + r.randint(1, dice):
        return True
    else: return False

# Знаю, что много повторений. Позже добавлю несколько функций, чтобы убрать повторения.    
def personHit(user_list: list, enemy_list: list, kind_of_hit: str):
    global hit_kinds_list
    global damage_modify
    global agility_modify
    damage = 0
    dice = 0
    user_luck = 0
    enemy_luck = 0
    result = []
    if user_list[7] >= enemy_list[7]:
        dice = int(round(user_list[7]))
    else: dice = int(round(enemy_list[7]))  
   
    match(kind_of_hit):
        case "Захват":
            if user_list[7] * agility_modify[0] + r.randint(1, dice) > enemy_list[7] + r.randint(1, dice):
                if user_list[6] >= enemy_list[8]:
                    dice = int(round(user_list[6]))
                else: dice = int(round(enemy_list[8]))                    
                user_luck = r.randint(1, dice)    
                enemy_luck = r.randint(1, dice)  
                if user_luck == 1:
                    damage = 0.1
                    result = [user_list[1], enemy_list[1], 'Критическая неудача при захвате', damage, enemy_list[5] ]
                    return result
                elif user_luck == dice:
                    damage = round(user_list[6] * 1.7, 2)
                    result = [user_list[1], enemy_list[1], 'Критическая удача при захвате', damage, enemy_list[5] ]
                    return result
                else:
                    damage = round(damage_modify[0] * ((user_list[6] + user_luck) - (enemy_list[8] + enemy_luck))) 
                    if damage <= 0:
                        damage = 0.5
                    result = [user_list[1], enemy_list[1], 'Успешный захват', damage, enemy_list[5] ]
                    return result
            else: 
                result = [user_list[1], enemy_list[1], 'Захват не удался', 0, enemy_list[5] ]
                return result
        
        case "Удар в голову":
            if user_list[7] * agility_modify[1] + r.randint(1, dice) > enemy_list[7] + r.randint(1, dice):
                if user_list[6] >= enemy_list[8]:
                    dice = int(round(user_list[6]))
                else: dice = int(round(enemy_list[8]))                    
                user_luck = r.randint(1, dice)    
                enemy_luck = r.randint(1, dice)  
                if user_luck == 1:
                    damage = 0.1
                    result = [user_list[1], enemy_list[1], 'Критическая неудача при ударе в голову', damage, enemy_list[5] ]
                    return result
                elif user_luck == dice:
                    damage = round(user_list[6] * 1.5, 2)
                    result = [user_list[1], enemy_list[1], 'Критическая удача при ударе в голову', damage, enemy_list[5] ]
                    return result
                else:
                    damage = round(damage_modify[1] * ((user_list[6] + user_luck) - (enemy_list[8] + enemy_luck))) 
                    if damage <= 0:
                        damage = 0.5
                    result = [user_list[1], enemy_list[1], 'Успешный удар в голову', damage, enemy_list[5] ]
                    return result
            else: 
                result = [user_list[1], enemy_list[1], 'Удар в голову не удался', 0, enemy_list[5] ]
                return result

        case "Удар по корпусу":
            if user_list[7] * agility_modify[2] + r.randint(1, dice) > enemy_list[7] + r.randint(1, dice):
                if user_list[6] >= enemy_list[8]:
                    dice = int(round(user_list[6]))
                else: dice = int(round(enemy_list[8]))                    
                user_luck = r.randint(1, dice)    
                enemy_luck = r.randint(1, dice)  
                if user_luck == 1:
                    damage = 0.1
                    result = [user_list[1], enemy_list[1], 'Критическая неудача при ударе по корпусу', damage, enemy_list[5] ]
                    return result
                elif user_luck == dice:
                    damage = round(user_list[6] * 1.1, 2)
                    result = [user_list[1], enemy_list[1], 'Критическая удача при ударе по корпусу', damage, enemy_list[5] ]
                    return result
                else:
                    damage = round(damage_modify[2] * ((user_list[6] + user_luck) - (enemy_list[8] + enemy_luck))) 
                    if damage <= 0:
                        damage = 0.5
                    result = [user_list[1], enemy_list[1], 'Успешный удар по корпусу', damage, enemy_list[5] ]
                    return result
            else: 
                result = [user_list[1], enemy_list[1], 'Удар по корпусу не удался', 0, enemy_list[5] ]
                return result

        case "Удар по ногам":
            if user_list[7] * agility_modify[3] + r.randint(1, dice) > enemy_list[7] + r.randint(1, dice):
                if user_list[6] >= enemy_list[8]:
                    dice = int(round(user_list[6]))
                else: dice = int(round(enemy_list[8]))                    
                user_luck = r.randint(1, dice)    
                enemy_luck = r.randint(1, dice)  
                if user_luck == 1:
                    damage = 0.1
                    result = [user_list[1], enemy_list[1], 'Критическая неудача при ударе по ногам', damage, enemy_list[5] ]
                    return result
                elif user_luck == dice:
                    damage = round(user_list[6] * 0.8, 2)
                    result = [user_list[1], enemy_list[1], 'Критическая удача при ударе по ногам', damage, enemy_list[5] ]
                    return result
                else:
                    damage = round(damage_modify[3] * ((user_list[6] + user_luck) - (enemy_list[8] + enemy_luck))) 
                    if damage <= 0:
                        damage = 0.5
                    result = [user_list[1], enemy_list[1], 'Успешный удар по ногам', damage, enemy_list[5] ]
                    return result
            else: 
                result = [user_list[1], enemy_list[1], 'Удар по ногам не удался', 0, enemy_list[5] ]
                return result 
        



