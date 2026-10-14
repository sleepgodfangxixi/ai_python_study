
class Person:

  def __init__(self,age,name,gender):
    self.age=age             #公有属性：都可以访问
    self._name=name          #受保护的属性：仅仅在类,子类 访问
    self.__gender=gender     #私有属性：只能在类里面访问

  def __str__(self):
      return f'{self.age}-{self._name}-{self.__gender}'
  def __lt__(self,other):
      return self.age<other.age
  def __gt__(self,other):
      return self.age>other.age
  def __eq__(self,other):
      return self.__dict__==other.__dict__
  def __getattr__(self,item):
      return f'您访问的{item}属性不存在'

p1=Person(18,'fcx','男')
p2=Person(20,'dqy','女')
print(p1)
# print(p1<p2)
# print(p1>p2)
# print(p1==p2)
# print(p1!=p2)
# print(p1.id_card)
# print(p1.age)

