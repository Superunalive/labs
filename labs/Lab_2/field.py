#This Python file uses the following encoding: utf-8
import sys

def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        for i in items:
            if i[args[0]] != "None":
                yield i[args[0]]
    else:
        for i in items:
            yield {args[j] : i[args[j]] for j in range(len(args)) if i[args[j]] != "None"}


goods = [{'title': 'Ковёр', 'price': 2000, 'color': 'green'}, {'title': 'Диван', 'price': 5300, 'color': 'black'}, {'title': 'диван', 'price': 'None', 'color': 'black'}]

for i in field(goods, 'title'):
    print(i, end=' ')

print('\n')
for j in field(goods, 'title', 'price'):
    print(j, end=' ')