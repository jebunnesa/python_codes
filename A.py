yes_vote = 1_000_000

no_vote = 1_000

yes_percentage = (yes_vote)/(yes_vote + no_vote)

print('{:-9} yes vots {:2.2%}'.format(yes_vote, yes_percentage))

print(str("hello world \n"))
print(repr("hello world \n"))
x = 10.09
y = 20
print(repr((x, y, ('spam', 'eggs'))))



dict1 = {'name':'jemi', 'age':10}
for item in dict1:
    print(item, dict1[item], end=', ')
for item in dict1.keys():
    if item == 'name':
        dict1
    print(item)
for key, val in dict1.items():
    print(key)
    print(val)