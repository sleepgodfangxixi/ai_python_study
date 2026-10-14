from abc import ABC,abstractmethod
class Must (ABC):
    @abstractmethod
    def introduce(self):
        pass

    # def introduce2(self):
    #     print(f'你好，我叫{self.name}')
class Person(Must):
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def introduce(self):
        print(f'我是{self.name},{self.age}岁')

p1=Person(18,'fcx')
p1.introduce()
# p1.introduce2()

