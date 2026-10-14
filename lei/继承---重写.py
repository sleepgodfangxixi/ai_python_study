class Person:

  def __init__(self,age,name,gender,habit):
    self.age=age
    self.name=name
    self.gender=gender
    self.habit=habit
#实例方法
  def introduce(self,msg):
   print(f'我的名字是{self.name}，今年{self.age},性别是{self.gender},爱好是{self.habit},我说：{msg}')

class Student(Person):
    def __init__(self,age,name,gender,habit,positions):
        self.positions=positions
        #调用父类的初始化方法，来实现对属性继承：age,name,gender,
        #方法一
        super().__init__(age,name,gender,habit)
        #方法二
        Person.__init__(self,age,name,gender,habit)
    def study(self,msg):
       print(f'我要学{msg},我的职位是{self.positions}')

    def introduce(self, msg):
        super().introduce(msg) 
        print(f'{self.name},{self.age}岁,{self.gender},爱好是{self.habit},说：{msg}')


p1=Student('12','fcx','男','打游戏','班长')

p1.study('English')

p1.introduce('谢谢')