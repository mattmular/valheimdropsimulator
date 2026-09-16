import math
import random

# Mock classes and variables to make the translated code syntactically valid and runnable
class DropData:
    def __init__(self, item, weight, stack_min=1, stack_max=1):
        self.m_item = item
        self.m_weight = weight
        self.m_stackMin = stack_min
        self.m_stackMax = stack_max

class DropResult:
    def __init__(self, item, count):
        self.m_item = item
        self.m_count = count

class Game:
    m_resourceRate = 1.0

class DropTable:
    dropsTemp = []

# The translated method
def get_drop_list(amount: int, m_drops: list, m_oneOfEach: bool):
    res_list = []
    if len(m_drops) == 0:
        print("list is empty")
        return res_list
    
    num = float(math.ceil(Game.m_resourceRate))
    num2 = 0
    
    while float(num2) < num:
        DropTable.dropsTemp.clear()
        DropTable.dropsTemp.extend(m_drops)
        
        flag = float(num2 + 1) == num
        num3 = Game.m_resourceRate % 1.0
        if num3 == 0.0:
            num3 = 1.0
            
        num4 = (1.0 if num3 == 0.0 else num3) if flag else 1.0
        num5 = 0.0
        
        for dropData in DropTable.dropsTemp:
            num5 += dropData.m_weight
                
        if num4 < 1.0 and amount > len(DropTable.dropsTemp):
            amount = int(max(1.0, round(float(amount) * num4)))
            
        for i in range(amount):
            num6 = random.uniform(0.0, num5)
            flag2 = False
            num7 = 0.0
            
            for dropData2 in DropTable.dropsTemp:
                num7 += dropData2.m_weight
                if num6 <= num7:
                    flag2 = True
                    min_scaled = round(float(dropData2.m_stackMin) * num4)
                    max_scaled = round(float(dropData2.m_stackMax) * num4)
                    num8 = int(max(1.0, round(random.uniform(min_scaled, max_scaled))))
                        
                    for j in range(num8):
                        res_list.append(dropData2.m_item)
                        
                    if m_oneOfEach:
                        DropTable.dropsTemp.remove(dropData2)
                        num5 -= dropData2.m_weight
                        break
                    break
                    
            if not flag2 and len(DropTable.dropsTemp) > 0:
                res_list.append(DropTable.dropsTemp[0].m_item)
                
        num2 += 1
        
    return res_list

def runSimulation(iterations: int, drop_min: int, drop_max: int, m_drops: list, m_oneOfEach: bool, onlyDisplay=[]):
    counts = {}
    totalitems = 0
    for dropdata in m_drops:
        counts[dropdata.m_item] = 0

    for i in range(iterations):
        amount = random.randint(drop_min, drop_max)
        drops = get_drop_list(amount=amount, m_drops=m_drops, m_oneOfEach=m_oneOfEach)
        #print(drops)
        for d in drops:
            counts[d] = counts[d]+1
            totalitems += 1

    print(f"___________________\ncounts\n{counts}")
    percentPerItem = {}
    for key, value in counts.items():
        if (len(onlyDisplay) == 0 or key in onlyDisplay):
            percentPerItem[key] = f"{value/totalitems*100}%"
    print(f"___________________\n% per item\n{percentPerItem}")

    avgCountPerContainer = {}
    for key, value in counts.items():
        if (len(onlyDisplay) == 0 or key in onlyDisplay):
            avgCountPerContainer[key] = f"{value/iterations}"
    print(f"___________________\nAverage count per container\n{avgCountPerContainer}")

    percentPerContainer = {}
    for key, value in counts.items():
        if (len(onlyDisplay) == 0 or key in onlyDisplay):
            percentPerContainer[key] = f"{value/iterations*100}%"
    print(f"___________________\n% per container\n{percentPerContainer}")
    


if __name__ == "__main__":
    # MorkhallaJotunChest
    drops = [
        DropData("AncientCoin", 1.0, 4, 10),
        DropData("MeadStaminaMedium", 1.0, 1, 1),
        DropData("MeadHealthMedium", 1.0, 1, 1),
        DropData("MeadEitrMinor", 1.0, 1, 1),
        DropData("ArrowCharred", 1.0, 5, 11),
        DropData("Upgrader6Armor", 0.05, 1, 1),
        DropData("Upgrader6Weapon", 0.025, 1, 1),
        DropData("Upgrader7Armor", 0.01, 1, 1), # 0.8%
        DropData("Upgrader7Weapon", 0.01, 1, 1), # 0.8%
    ]
    drop_min = 2
    drop_max = 4
    m_oneOfEach = True
    onlyDisplay = ["Upgrader7Armor", "Upgrader7Weapon"]

    runSimulation(iterations=20000, drop_min=drop_min, drop_max=drop_max, m_drops=drops, m_oneOfEach=m_oneOfEach, onlyDisplay=onlyDisplay)

