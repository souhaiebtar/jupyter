email = {
    "From": "j.smith@example.com",
    "To": "zed.shaw.example.com",
    "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU!!!"
};

print(email["To"])

messages = [
    {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
    {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
    {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
    {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'}
];

print(messages[2]['message'])

fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
];

cars = [
    {'type': 'Cadillac', 'color': 'Black',
    'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red',
    'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue',
    'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White',
    'size': 'Baby', 'miles': 7890}
];

languages = [
    {'name': 'Python', 'speed': 'Slow',
    'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate',
    'opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate',
    'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast',
    'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast',
    'opinion': ['Fun', 'Difficult']},
];

print(fruit[0]['rating'])

print(messages[0]['to'])

print(messages[2]['message'])

print(languages[0]['speed'])
print(languages[1]['opinion'][0])

def print_number(x):
    print("NUMBER IS", x)

rename_print = print_number
rename_print(100)
print_number(100)

x = 10 
y = x
print(y)

color = "Red"
corvette = {
    "color": color
}

print("LITTLE", corvette["color"], "CORVETTE")
print(corvette)