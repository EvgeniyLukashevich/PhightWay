import os



def writePerson(person_list):
    try:
        os.mkdir(f"data/persons/{person_list[0]}")
        with open(f"data/persons/{person_list[0]}/{person_list[1]}_{person_list[2]}.ini", "w+", encoding='UTF-8') as file:
            print(*person_list, file=file, sep="\n")
    except:
        with open(f"data/persons/{person_list[0]}/{person_list[1]}_{person_list[2]}.ini", "w+", encoding='UTF-8') as file:
            print(*person_list, file=file, sep="\n")


def writeEnemy(id, enemy_list):
    try:
        os.mkdir(f"data/persons/{enemy_list[0]}")
        with open(f"data/persons/{enemy_list[0]}/{id}_{enemy_list[1]}_{enemy_list[2]}.ini", "w+", encoding='UTF-8') as file:
            print(*enemy_list, file=file, sep="\n")
    except:
        with open(f"data/persons/{enemy_list[0]}/{id}_{enemy_list[1]}_{enemy_list[2]}.ini", "w+", encoding='UTF-8') as file:
            print(*enemy_list, file=file, sep="\n")


def writeEnemyStats(enemy_list: list):
    matches = 0
    wins = 0
    statistic_list = []

    with open(f"data/persons/{enemy_list[0]}/{enemy_list[2]}.ini", "r", encoding='UTF-8') as file:
        for i in file.readlines():
            try:
                statistic_list.append(int(i.replace("\n", "").replace(" матчей", "").replace(" побед", "").replace(" поражений", "").replace(" % ПОБЕД", "")))
            except:
                statistic_list.append(float(i.replace("\n", "").replace(" матчей", "").replace(" побед", "").replace(" поражений", "").replace(" % ПОБЕД", "")))
    
        
        statistic_list[0] +=1
        matches = int(statistic_list[0])
        wins = int(statistic_list[1])
        loses = int(statistic_list[2])
        if enemy_list[5] > 0:
            wins += 1
            statistic_list[1] = wins
            statistic_list[3] = round(wins / matches * 100, 2)
        else:
            loses += 1
            statistic_list[2] = loses
            statistic_list[3] = round(wins / matches * 100, 2)
        statistic_list[0] = f"{statistic_list[0]} матчей"
        statistic_list[1] = f"{statistic_list[1]} побед"
        statistic_list[2] = f"{statistic_list[2]} поражений"
        statistic_list[3] = f"{statistic_list[3]} % ПОБЕД"
            
    with open(f"data/persons/{enemy_list[0]}/{enemy_list[2]}.ini", "w+", encoding='UTF-8') as file:
        print(*statistic_list, file=file, sep="\n")
        


def getFileNames(user_id):
    file_list = []
    try:
        with os.scandir(f"data/persons/{user_id}") as entries:  
            for entry in entries:
                if entry.is_file():
                    file_name_for_button = entry.name.replace("_Ниндзя", " Ниндзя").replace("_Самурай", " Самурай").replace("_Камикадзе", " Камикадзе").replace("_Сёгун", " Сёгун").replace("_Скала", " Скала").replace(".ini", "")
                    file_list.append(file_name_for_button)
        return file_list
    except: return file_list


def loadFromFileName(id, name_button:str):
    person_list = []
    j = 0
    file_name = name_button.replace(" Ниндзя", "_Ниндзя").replace(" Самурай", "_Самурай").replace(" Камикадзе", "_Камикадзе").replace(" Сёгун", "_Сёгун").replace(" Скала", "_Скала")
    try:
        with open(f"data/persons/{id}/{file_name}.ini", "r", encoding='UTF-8') as file:
            for i in file.readlines():
                string = i.strip()
                if j > 0:
                    try:
                        person_list.append(int(string))
                    except: 
                        try:
                            person_list.append(float(string))
                        except:
                            person_list.append(string)
                else: person_list.append(string)
                j+=1
        return person_list
    except: return person_list

def removeFromFileName(id, name_button:str):
    file_name = name_button.replace(" Ниндзя", "_Ниндзя").replace(" Самурай", "_Самурай").replace(" Камикадзе", "_Камикадзе").replace(" Сёгун", "_Сёгун").replace(" Скала", "_Скала")
    os.remove(f"data/persons/{id}/{file_name}.ini")
