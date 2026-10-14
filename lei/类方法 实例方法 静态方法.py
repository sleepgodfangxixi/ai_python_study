from datetime import datetime

class Person:
  planet='月球'
  def __init__(self,age,name,gender,habit):
    self.age=age
    self.name=name
    self.gender=gender
    self.habit=habit
#实例方法
  def introduce(self,msg):
   print(f'我的名字是{self.name}，今年{self.age},性别是{self.gender},爱好是{self.habit},我说：{msg}')
#类方法 通过类名直接调用
  @classmethod
  def modify_planet(cls,fcx):
      print(fcx)
      cls.planet=fcx
  @classmethod
  def create(cls,info_str):
      name,year,gender,habit=info_str.split('-')
      #获取当前年份
      now_time=datetime.now().year
      age=now_time-int(year)
      return cls(age,name,gender,habit)
  @staticmethod
  def is_adult(year):
      now_time=datetime.now().year
      age=now_time-year
      return age>=18

p1=Person('17','fcx','男','打游戏')
p1.introduce('哈哈哈哈哈')
print(p1.__dict__)
p2=Person.create('dqy-2005-女-学习')
p2.introduce('我太美了')
print(p2.__dict__)
Person.modify_planet('地球')
print(Person.__dict__)
print(Person.is_adult(2009))