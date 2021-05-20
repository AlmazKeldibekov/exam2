text = '''
Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. 
Sometimes they are mini-dramas and we wait for the next program in the mini-drama. 
Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. 
Without advertising, life is boring and colorless.

But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. 
Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. 
Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.
'''

count_s = 0
count_t = 0
for letter in text.lower():
    if letter == 's':
        count_s += 1
    elif letter == 't':
        count_t += 1
print(count_t)
print(count_s)
text = text.replace('advert','ADVERT')
print(text)

students = [
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agness', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Don', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alexey', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susanne', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Stevie', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktanbek', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]
courses = {'python': [], 'java': [],'javascript:': []}
for i in students:
    if i['course'] in courses:
        courses[i['course']].append(i['name'])
print(courses)

name_age = {x['name']: x['age'] for x in students}

names = ['Janyl', 'Nursultan', 'Meerim', 'Emir', 'Susann', 'Marcus', 'Aidin',
'Aigerim', 'Angela', 'Albert', 'Jyldyz', 'Doe', 'Gloria', 'Aliaskar',
 'Martin', 'John', 'Andrew', 'Steve', 'Johnathan', 'Adyl', 'Chyngyz',
'Michael', 'Atay', 'Mikkel', 'Agnes', 'Aidana', 'Sultan', 'Nash',
 'Nicolas', 'Mirbek', 'Aktan', 'Emirlan', 'Jennifer', 'Eniston', 'Alex', 'Mark']

def func21(lst,dct):
    for i in lst:
        try:
            print(f'{i}--------{dct[i]}')
        except KeyError:
            print(f'Imeni {i} ne sushestvuet!')
            continue

func21(names,students)


def func(*args):
    sum_ = 0
    for i in args:
        try:
            sum_ += i
        except TypeError:
            pass
    return sum_

