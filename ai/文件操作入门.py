#1.打开文件(读r/写w)

# f=open('resource/败者食尘.txt','r',encoding='utf-8')



#2.读写文件
# content=f.read()
# print(content)
# f.write('败者\n')
# f.write('食尘')



#3.关闭文件
# f.close()

with open('resource/败者食尘.txt','r',encoding='utf-8') as f:
    content = f.read()
    print(content)