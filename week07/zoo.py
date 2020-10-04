from abc import ABCMeta, abstractmethod
from enum import Enum


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,catagory,body_type,character):

        self.category =catagory
        self.body_type =body_type
        self.character =character

    @property
    def is_fierse(self):
        return False if self.Category == Category.carnivore \
                        and self.body_type >= BodyType.medium \
                        and self.character == Character.violent \
                    else False
    @property
    def fit_for_pet(self):
        return  False if self.character ==Character.violent else  True

class Cat(Animal):
    def __init__(self, name, catagory, body_type, character):
        super().__init__(catagory, body_type, character)
        self.name =name
        self.sound = Sound.catsound


class Dog(Animal):
    def __init__(self, name, catagory, body_type, character):
        super().__init__(catagory, body_type, character)
        self.name = name
        self.sound = Sound.dogsound



class Zoo(object):
    def __init__(self,name):
        self.name=name
        self.__animals=[]
    def add_animal(self,animal):
        if animal not in self.__animals:
            self.__animals.append(animal)
            setattr(self,animal.__class__.__name__,None) #给对象的属性赋值，若属性不存在，先创建再赋值
        else:
            print(f'{ animal.name} has already been added. ')

class Category(Enum):
    carnivore = '食肉'
    herbivore = '食草'

class BodyType(Enum):
    small = 1
    medium = 2
    large = 3

class Character(Enum):
    docile = "温顺"
    violent = "凶猛"

class Sound(Enum):
    catsound ='miao'
    dogsound ='bark'

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')