from datetime import datetime



class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count=0
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        Student.count += 1
        self.stu_id=f'{datetime.now().year}{Student.count:03d}'
        self.score= {}

    def add_score(self,subject,score):
        self.score[subject]=score
    def calculate_score(self):
        if self.score:
            return sum(self.score.values())/len(self.score)
        else:
            return 0
    def __str__(self):
        return f'({self.name}-{self.age}-{self.gender}-{self.stu_id})\n成绩：{self.score},平均分：{self.calculate_score():.1f}'

class Operate:
    def __init__(self):
        self.stu_list=[]
    def add_student(self):
        name=input('请输入学生姓名:')
        age = input('请输入学生年龄:')
        gender = input('请输入学生性别:')
        stu = Student(name,age,gender)
        self.stu_list.append(stu)
    def del_student(self):
        found=False
        sid=input('删除的学生学号是:')
        for i in self.stu_list:
            if i.stu_id==sid:
                self.stu_list.remove(i)
                print(f'删除成功！')
                found=True
                break
        if not found:
            print('学生不存在')
    def show_student(self):
        if self.stu_list:
            for i in self.stu_list:
                print(i)
        else:
            print('暂无学生!')
    def set_score(self):
        sid=input('请输入学生学号：')
        for i in self.stu_list:
            if i.stu_id==sid:
                score_str=input('请输入学生成绩（科目-成绩,科目-成绩）：')
                score_list=score_str.split(',')
                for j in score_list:
                    subject,score=j.split('-')
                    score=float(score)
                    i.add_score(subject,score)
                print('添加成功！')
                return
        print('学号有误')

    def run_ui(self):

        while True:
            print('*****************************学生管理系统*******************************')
            print('1.添加学生')
            print('2.删除学生')
            print('3.查看学生')
            print('4.录入学生成绩')
            print('5.退出系统')
            choice=input('请输入操作序号：')
            if choice=='1':
                 self.add_student()
            elif choice=='2':
                self.del_student()
            elif choice=='3':
                self.show_student()
            elif choice=='4':
                self.set_score()
            elif choice=='5':
                print('系统已经退出')
                break
            else:
                print('输入序号有误')

o1=Operate()
o1.run_ui()










# p1=Student('fcx',18,'男')
# p2=Student('dqy',13,'女')
# p1.add_score('数学',93)
# p1.add_score('英语',90)
# p1.add_score('语文',88)
# print(p1.calculate_score())
# print(p1)
# print(p1.__dict__)
# print(p2.__dict__)

