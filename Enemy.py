import random

class Enemy:

    # id[0], name[1], way[2], level[3], exp[4], hp[5], power[6], agility[7], defence[8], matches[9], wins[10], loses[11] 
    enemy_list = ["", "", "", 0, 0, 0, 0, 0, 0, 0, 0, 0]

    _way_list = ["Ниндзя", "Самурай", "Камикадзе", "Сёгун", "Скала"]

    _ninja_names = ["Нисияма", "Накаяма", "Накахара", "Нагата", "Нисимура", "Нарадзаки", "Наканэ"]
    _samurai_names = ["Симидзу", "Сакахара", "Судзуки", "Сурияма", "Сайто", "Сиракава", "Сато"]
    _kamikaze_names = ["Кагава", "Канэхара", "Кирисима", "Китадзава", "Кобаяси", "Кодзима", "Куросава"]
    _shogun_names = ["Ёсимура", "Ёсиока", "Ёсида", "Ёсикава", "Ёкояма", "Ёката", "Ёкодзава"]
    _rock_names = ["Арнольд", "Сильвестр", "Джейсон", "Дуэйн", "Стивен", "Брюс", "Чак"]

    _hp_coef = [1.8]
    _ninja_coef = [9, 3, 0.22, 0.56, 0.22]
    _samurai_coef = [9, 3, 0.45, 0.22, 0.33]
    _kamikaze_coef = [9, 3, 0.56, 0.22, 0.22]
    _shogun_coef = [9, 3, 0.45, 0.33, 0.22]
    _rock_coef = [9, 3, 0.33, 0.22, 0.45]
    
    # id[0], name[1], way[2], level[3], exp[4], hp[5], power[6], agility[7], defence[8], matches[9], wins[10], loses[11]     
    _ninja_pattern = ["__enemy_stats", random.choice(_ninja_names), "Ниндзя", 1, 0, 15, 3, 3.7, 2, 0, 0, 0]               # 15, 3, 4, 2
    _samurai_pattern = ["__enemy_stats", random.choice(_samurai_names), "Самурай", 1, 0, 15, 2.8, 3, 3, 0, 0, 0]          # 15, 3, 3, 3
    _kamikaze_pattern = ["__enemy_stats", random.choice(_kamikaze_names), "Камикадзе", 1, 0, 15, 4.6, 3, 1, 0, 0, 0]      # 15, 5, 3, 1
    _shogun_pattern = ["__enemy_stats", random.choice(_shogun_names), "Сёгун", 1, 0, 15, 3.7, 3, 2, 0, 0, 0]              # 15, 4, 3, 2
    _rock_pattern = ["__enemy_stats", random.choice(_rock_names), "Скала", 1, 0, 15, 2, 2.8, 4, 0, 0, 0]                  # 15, 2, 3, 4

    def __init__(self, user_level):
        self.enemy_list[2] = random.choice(self._way_list)            
        match(self.enemy_list[2]):           
            case "Ниндзя":  
                for i in range(len(self._ninja_pattern)):
                    self.enemy_list[i] = self._ninja_pattern[i]    
                self.enemy_list[1] = random.choice(self._ninja_names)                
                match(user_level):
                    case 1:
                        self.enemy_list[3] = 1
                        if self.enemy_list[3] > 1:
                            self.enemy_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[2], 2) 
                            self.enemy_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[3], 2) 
                            self.enemy_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[4], 2) 
                            self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 2:
                        self.enemy_list[3] = 2
                        self.enemy_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[2], 2) 
                        self.enemy_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[3], 2) 
                        self.enemy_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[4], 2) 
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 3:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[2], 2) 
                        self.enemy_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[3], 2) 
                        self.enemy_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[4], 2)    
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2) 
                    case 4:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[2], 2) 
                        self.enemy_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[3], 2) 
                        self.enemy_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[4], 2)  
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2) 
                    case 5:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[2], 2) 
                        self.enemy_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[3], 2) 
                        self.enemy_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case _:
                        self.enemy_list[3] = random.randint(user_level, user_level+2)
                        self.enemy_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[2], 2) 
                        self.enemy_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[3], 2) 
                        self.enemy_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (self.enemy_list[3] - 1)) * self._ninja_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
            case "Самурай":
                for i in range(len(self._samurai_pattern)):
                    self.enemy_list[i] = self._samurai_pattern[i] 
                self.enemy_list[1] = random.choice(self._samurai_names)                   
                match(user_level):
                    case 1:
                        self.enemy_list[3] = 1
                        if self.enemy_list[3] > 1:
                            self.enemy_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[2], 2) 
                            self.enemy_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[3], 2) 
                            self.enemy_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[4], 2) 
                            self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 2:
                        self.enemy_list[3] = 2
                        self.enemy_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[2], 2) 
                        self.enemy_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[3], 2) 
                        self.enemy_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[4], 2) 
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 3:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[2], 2) 
                        self.enemy_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[3], 2) 
                        self.enemy_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[4], 2)     
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2) 
                    case 4:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[2], 2) 
                        self.enemy_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[3], 2) 
                        self.enemy_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[4], 2)  
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 5:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[2], 2) 
                        self.enemy_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[3], 2) 
                        self.enemy_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case _:
                        self.enemy_list[3] = random.randint(user_level, user_level+2)
                        self.enemy_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[2], 2) 
                        self.enemy_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[3], 2) 
                        self.enemy_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (self.enemy_list[3] - 1)) * self._samurai_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
            case "Камикадзе":
                for i in range(len(self._kamikaze_pattern)):
                    self.enemy_list[i] = self._kamikaze_pattern[i]   
                self.enemy_list[1] = random.choice(self._kamikaze_names)                 
                match(user_level):
                    case 1:
                        self.enemy_list[3] = 1
                        if self.enemy_list[3] > 1:
                            self.enemy_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                            self.enemy_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                            self.enemy_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[4], 2) 
                            self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 2:
                        self.enemy_list[3] = 2
                        self.enemy_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                        self.enemy_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                        self.enemy_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[4], 2) 
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 3:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                        self.enemy_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                        self.enemy_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[4], 2)  
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)  
                    case 4:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                        self.enemy_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                        self.enemy_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[4], 2)    
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 5:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                        self.enemy_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                        self.enemy_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2) 
                    case _:
                        self.enemy_list[3] = random.randint(user_level, user_level+2)
                        self.enemy_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                        self.enemy_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                        self.enemy_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (self.enemy_list[3] - 1)) * self._kamikaze_coef[4], 2) 
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)   
            case "Сёгун":
                for i in range(len(self._shogun_pattern)):
                    self.enemy_list[i] = self._shogun_pattern[i]  
                self.enemy_list[1] = random.choice(self._shogun_names)                  
                match(user_level):
                    case 1:
                        self.enemy_list[3] = 1
                        if self.enemy_list[3] > 1:
                            self.enemy_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[2], 2) 
                            self.enemy_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[3], 2) 
                            self.enemy_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[4], 2) 
                            self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 2:
                        self.enemy_list[3] = 2
                        self.enemy_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[2], 2) 
                        self.enemy_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[3], 2) 
                        self.enemy_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[4], 2) 
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 3:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1) 
                        self.enemy_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[2], 2) 
                        self.enemy_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[3], 2) 
                        self.enemy_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[4], 2)  
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2) 
                    case 4:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[2], 2) 
                        self.enemy_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[3], 2) 
                        self.enemy_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[4], 2)  
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2) 
                    case 5:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[2], 2) 
                        self.enemy_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[3], 2) 
                        self.enemy_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case _:
                        self.enemy_list[3] = random.randint(user_level, user_level+2)
                        self.enemy_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[2], 2) 
                        self.enemy_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[3], 2) 
                        self.enemy_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (self.enemy_list[3] - 1)) * self._shogun_coef[4], 2)   
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
            case "Скала":
                for i in range(len(self._rock_pattern)):
                    self.enemy_list[i] = self._rock_pattern[i] 
                self.enemy_list[1] = random.choice(self._rock_names)                   
                match(user_level):
                    case 1:
                        self.enemy_list[3] = 1
                        if self.enemy_list[3] > 1:
                            self.enemy_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[2], 2) 
                            self.enemy_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[3], 2) 
                            self.enemy_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[4], 2) 
                            self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 2:
                        self.enemy_list[3] = 2
                        self.enemy_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[2], 2) 
                        self.enemy_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[3], 2) 
                        self.enemy_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[4], 2) 
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 3:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[2], 2) 
                        self.enemy_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[3], 2) 
                        self.enemy_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[4], 2)  
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 4:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[2], 2) 
                        self.enemy_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[3], 2) 
                        self.enemy_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[4], 2)
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case 5:
                        self.enemy_list[3] = random.randint(user_level-1, user_level+1)
                        self.enemy_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[2], 2) 
                        self.enemy_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[3], 2) 
                        self.enemy_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[4], 2)
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)
                    case _:
                        self.enemy_list[3] = random.randint(user_level, user_level+2)
                        self.enemy_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[2], 2) 
                        self.enemy_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[3], 2) 
                        self.enemy_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (self.enemy_list[3] - 1)) * self._rock_coef[4], 2)
                        self.enemy_list[5] = round((self.enemy_list[6] + self.enemy_list[7] + self.enemy_list[8]) * self._hp_coef[0], 2)

            
    def getEnemyList(self):
        return self.enemy_list


                   

     
     
     