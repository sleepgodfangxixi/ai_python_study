class Person:
    def speak(self):
      print('何人在此喧嚣')
class dqy(Person):
    def speak(self):
        print('喵喵喵')
class fcx(Person):
    def speak(self):
        print('嘿嘿嘿')

def make_sound(person:Person):
    person.speak()

s1=Person()
d1=dqy()
f1=fcx()

make_sound(s1)
make_sound(d1)
make_sound(f1)