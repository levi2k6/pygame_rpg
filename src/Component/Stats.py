

class Stats:

    strength: int = 0
    agility: int = 0
    intelligence: int = 0

    strPerPoint = {
       "maxHealth": 100,
       "damage": 10
    }
    agiPerPoint = {
        "evasion": 15,
        "critChance": 15 
    }
    intPerPoint = {
        "strategy": 15,
        "opportunity": 15,
    }

    maxHealth: float = 0
    damage: float = 0
    evasion: int = 0
    critChance: int = 0
    strategy: int  = 0
    opportunity: int = 0

    maxMana: float = 100 
    absorb: int = 0


    def __init__(self):
        self.updateStats()
        
    def updateStats(self):
        self.currentHealth = self.strPerPoint["maxHealth"] * self.strength 
        self.damage = self.strPerPoint["damage"] * self.strength

        self.evasion = self.agiPerPoint["evasion"] * self.agility
        self.dexterity = self.agiPerPoint["critChance"] * self.agility

        self.strategy = self.intPerPoint["strategy"] * self.intelligence
        self.opportunity = self.intPerpoint["opportunity"] * self.intelligence 





    

