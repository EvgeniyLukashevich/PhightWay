import random

class Person:

    # id[0], name[1], way[2], level[3], exp[4], hp[5], power[6], agility[7], defence[8], matches[9], wins[10], loses[11] 
    person_list = []

    # start level, start exp, hp, power, agility, defence, matches, wins, loses
    _ninja_pattern = ["", "", "", 1, 0, 15, 3, 4, 2, 0, 0, 0]
    _samurai_pattern = ["", "", "", 1, 0, 15, 3.5, 3, 2.5, 0, 0, 0]
    _kamikaze_pattern = ["", "", "", 1, 0, 15, 5, 3, 1, 0, 0, 0]
    _shogun_pattern = ["", "", "", 1, 0, 15, 4, 3, 2, 0, 0, 0]
    _rock_pattern = ["", "", "", 1, 0, 15, 2, 3, 4, 0, 0, 0]

    _hp_coef = [1.67]
    _ninja_coef = [9, 3, 0.22, 0.56, 0.22]
    _samurai_coef = [9, 3, 0.45, 0.22, 0.33]
    _kamikaze_coef = [9, 3, 0.56, 0.22, 0.22]
    _shogun_coef = [9, 3, 0.45, 0.33, 0.22]
    _rock_coef = [9, 3, 0.33, 0.22, 0.45]



    def __init__(self, id: str):
        self.person_list = [id, "", "", 0, 0, 0, 0, 0, 0, 0, 0, 0]        

    def getPersonList(self):
        return self.person_list

    def setId(self, user_id: str):
        self.person_list[0] = user_id
    def getId(self):
        return self.person_list[0]

    def setName(self, user_name: str):
        self.person_list[1] = user_name
    def getName(self):
        return self.person_list[1]
       
    def setWay(self, user_way: str):
        self.person_list[2] = user_way
    def getWay(self):
        return self.person_list[2]
      
    def setLevel(self, user_level: int):
        self.person_list[3] = user_level 
    def getLevel(self):
        return self.person_list[3]

    def setExpa(self, user_exp: int):
        self.person_list[4] = user_exp
    def getExpa(self):
        return self.person_list[4]

    def setHp(self, user_hp: int):
        self.person_list[5] = user_hp
    def getHp(self):
        return self.person_list[5]

    def setPower(self, user_power: int):
        self.person_list[6] = user_power
    def getPower(self):
        return self.person_list[6]

    def setAgility(self, user_agility: int):
        self.person_list[7] = user_agility
    def getAgility(self):
        return self.person_list[7]

    def setDefence(self, user_defence: int):
        self.person_list[8] = user_defence
    def getDefence(self):
        return self.person_list[8]

    def setMatches(self, user_matches: int):
        self.person_list[9] = user_matches
    def getMatches(self):
        return self.person_list[9]

    def setWins(self, user_wins: int):
        self.person_list[10] = user_wins
    def getWins(self):
        return self.person_list[10]

    def setLoses(self, user_loses: int):
        self.person_list[11] = user_loses
    def getLoses(self):
        return self.person_list[11]

   
    def expaWinProgress(self):
        self.person_list[4] += 10 // self.person_list[3]

    def expaLoseProgress(self):
        self.person_list[4] += 5 // self.person_list[3]

    def updateLevelWin(self, pers_list):
        if pers_list[4] > 29:
            pers_list[3] += 1   
            pers_list[9] += 1   
            pers_list[10] += 1                              
            match(pers_list[2]):           
                case "Ниндзя":
                    pers_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (pers_list[3] - 1)) * self._ninja_coef[2], 2) 
                    pers_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (pers_list[3] - 1)) * self._ninja_coef[3], 2) 
                    pers_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (pers_list[3] - 1)) * self._ninja_coef[4], 2) 
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
                case "Самурай":
                    pers_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (pers_list[3] - 1)) * self._samurai_coef[2], 2) 
                    pers_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (pers_list[3] - 1)) * self._samurai_coef[3], 2) 
                    pers_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (pers_list[3] - 1)) * self._samurai_coef[4], 2)   
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)      
                case "Камикадзе":
                    pers_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (pers_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                    pers_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (pers_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                    pers_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (pers_list[3] - 1)) * self._kamikaze_coef[4], 2)      
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)            
                case "Сёгун":
                    pers_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (pers_list[3] - 1)) * self._shogun_coef[2], 2) 
                    pers_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (pers_list[3] - 1)) * self._shogun_coef[3], 2) 
                    pers_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (pers_list[3] - 1)) * self._shogun_coef[4], 2)  
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
                case "Скала":
                    pers_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (pers_list[3] - 1)) * self._rock_coef[2], 2) 
                    pers_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (pers_list[3] - 1)) * self._rock_coef[3], 2) 
                    pers_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (pers_list[3] - 1)) * self._rock_coef[4], 2)
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
            pers_list[4] = 0                                                     
        else: 
            if pers_list[3] > 1:
                pers_list[9] += 1 
                pers_list[10] += 1
                pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)   
            else:
                pers_list[9] += 1 
                pers_list[10] += 1
                pers_list[5] = 15


    def updateLevelLose(self, pers_list):
        if pers_list[4] > 29:
            pers_list[3] += 1   
            pers_list[9] += 1   
            pers_list[11] += 1                              
            match(pers_list[2]):           
                case "Ниндзя":
                    pers_list[6] = round((self._ninja_coef[0] + self._ninja_coef[1] * (pers_list[3] - 1)) * self._ninja_coef[2], 2) 
                    pers_list[7] = round((self._ninja_coef[0] + self._ninja_coef[1] * (pers_list[3] - 1)) * self._ninja_coef[3], 2) 
                    pers_list[8] = round((self._ninja_coef[0] + self._ninja_coef[1] * (pers_list[3] - 1)) * self._ninja_coef[4], 2) 
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
                case "Самурай":
                    pers_list[6] = round((self._samurai_coef[0] + self._samurai_coef[1] * (pers_list[3] - 1)) * self._samurai_coef[2], 2) 
                    pers_list[7] = round((self._samurai_coef[0] + self._samurai_coef[1] * (pers_list[3] - 1)) * self._samurai_coef[3], 2) 
                    pers_list[8] = round((self._samurai_coef[0] + self._samurai_coef[1] * (pers_list[3] - 1)) * self._samurai_coef[4], 2)   
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)      
                case "Камикадзе":
                    pers_list[6] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (pers_list[3] - 1)) * self._kamikaze_coef[2], 2) 
                    pers_list[7] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (pers_list[3] - 1)) * self._kamikaze_coef[3], 2) 
                    pers_list[8] = round((self._kamikaze_coef[0] + self._kamikaze_coef[1] * (pers_list[3] - 1)) * self._kamikaze_coef[4], 2)      
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)            
                case "Сёгун":
                    pers_list[6] = round((self._shogun_coef[0] + self._shogun_coef[1] * (pers_list[3] - 1)) * self._shogun_coef[2], 2) 
                    pers_list[7] = round((self._shogun_coef[0] + self._shogun_coef[1] * (pers_list[3] - 1)) * self._shogun_coef[3], 2) 
                    pers_list[8] = round((self._shogun_coef[0] + self._shogun_coef[1] * (pers_list[3] - 1)) * self._shogun_coef[4], 2)  
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
                case "Скала":
                    pers_list[6] = round((self._rock_coef[0] + self._rock_coef[1] * (pers_list[3] - 1)) * self._rock_coef[2], 2) 
                    pers_list[7] = round((self._rock_coef[0] + self._rock_coef[1] * (pers_list[3] - 1)) * self._rock_coef[3], 2) 
                    pers_list[8] = round((self._rock_coef[0] + self._rock_coef[1] * (pers_list[3] - 1)) * self._rock_coef[4], 2)
                    pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
            pers_list[4] = 0                                                     
        else: 
            if pers_list[3] > 1:
                pers_list[9] += 1 
                pers_list[11] += 1
                pers_list[5] = round((pers_list[6] + pers_list[7] + pers_list[8]) * self._hp_coef[0], 2)
            else:
                pers_list[9] += 1 
                pers_list[11] += 1
                pers_list[5] = 15
    