class Person:

  def __init__(self,age,name,gender):
    self.age=age             #公有属性：都可以访问
    self._name=name          #受保护的属性：仅仅在类,子类 访问
    self.__gender=gender     #私有属性：只能在类里面访问

#注册name属性getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
  @property
  def name(self):
    return self._name
#注册name属性setter方法，当修改Person实例的age属性时，下面的age方法就会被自动调用
  @name.setter
  def name(self,value):
      if value!='dqy':
          print('不是dqy不要')
      else:
        self._name=value


p1=Person(18,'fcx','男')
print(p1.name)
p1.name='dqy'
print(p1.name)