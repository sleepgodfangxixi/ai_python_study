import json

user={
    'name':'壳子',
    'age':18,
    'gender':'男',
    'hobby':['coding','gaming','reading']
}
with open('resource/user.json','w',encoding='utf-8') as f:
    #ensure_ascii 转义ASCII
    #indent 缩进
    json.dump(user,f,ensure_ascii=False,indent=2)

#读取json数据文件
with open('resource/user.json','r',encoding='utf-8') as f:
    user=json.load(f)
    print(user)
