#This Python file uses the following encoding: utf-8
import sys

class House:
    
    def __init__(self, number, owner, size, address):
        self.n = number
        self.owner = owner
        self.size = size
        self.address = address        
        
        # n = which house on this street, address = name of street
        # owner and size are self-explanatory.
        
    def get_address(self):
        return {self.address, self.n}

class Street:
    
    def __init__(self, name):
        self.name = name
        self.n = 0
        self.area = 0
        
        # n = number of houses, name is name, area is a sum of sizes from houses
        
        # here, house ID is a combination of address and house number, while street ID is just the name. Hope this qualifies.
        
    def add_house(self, s):
        self.n += 1
        self.area += s
        
class HouseList:
    
    def __init__(self, house):
        self.name = house.address
        self.houses = [house]
        
    def add_house(self, house):
        self.houses.append(house)
        
    #A list of houses on the street. A house COULD be on multiple streets, but only in the last task.
        
def main():
    StreetData = dict()
    HouseData = dict()
    HouseListData = dict()
    for i in range(5):
        
        print("Please input data (house number, owner, house size, street name):")
        n = int(input())
        owner = input()
        size = int(input())
        address = input()
        
        house = House(n, owner, size, address)
        street = Street(address)
        HouseData[(address, n)] = house
        
        if address not in StreetData:
            StreetData[address] = street
        StreetData[address].add_house(house.size)
        
        if address not in HouseListData:
            HouseListData[address] = HouseList(house)
        HouseListData[address].add_house(house)
        
        i += 1
    
    #Задание 1 - вывести дома, фамилии владельцев которых заканчиваются на "ов", а также их улицы
    
    for i in HouseData:
        if HouseData[i].owner[-2:] == "ов":
            print(HouseData[i].owner, HouseData[i].address)
    
    # Задание 2 - вывести отсортированный список улиц по средней площади домов
    
    for j in sorted(StreetData.items(), key = lambda StreetData: (StreetData[1].area / StreetData[1].n)):
        print(j[0], j[1].area / j[1].n)
        
    # Задание 3 - вывести список улиц, которые начинаются с буквы "А" и список владельцев
    
    temp = set()
    print("Список улиц:")
    for l in HouseListData:
        if HouseListData[l].name[0] == "А":
            print(HouseListData[l].name)
            for elem in HouseListData[l].houses:
                temp.add(elem.owner)
    print("Список владельцев:")
    for name in temp:
        print(name)
    
    
main()

"""
1
Александров
20
Жуковская
2
Шадрин
25
Жуковская
11
Зверева
21
Зверева
2
Кислов
40
Зверева
1
Александров
1
Аде-то
"""
