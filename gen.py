from jinja2 import Template
f = open('template.jinja', 'r', encoding='utf-8')
t = f.read()
f.close()
template = Template(t)

todo_list = [
    'Endless homework',
]

data_dict = {
    "todo_list": todo_list
}

res = template.render(data_dict)
f2 = open('index.html','w+',encoding='utf-8')
f2.write(res)
f2.close()
