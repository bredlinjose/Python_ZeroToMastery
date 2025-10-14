people = [{'name': 'Alice', 'age': 25, 'city': 'New York'},
          {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
          {'name': 'Charlie', 'age': 25, 'city': 'New York'},
          {'name': 'David', 'age': 35, 'city': 'Chicago'}]


def categories_by_city():
    grouped_data = {}
    for person in people:
        keys = person['city']
        # print(key)
        if keys not in grouped_data:
            grouped_data[keys] = []
        grouped_data[keys].append(person)
    print(grouped_data)
# {
#     'New York': [{'name': 'Alice', 'age': 25, 'city': 'New York'},
#                  {'name': 'Charlie', 'age': 25, 'city': 'New York'}],
#     'Chicago': [{'name': 'Bob', 'age': 30, 'city': 'Chicago'},
#                 {'name': 'David', 'age': 35, 'city': 'Chicago'}]
# }


def get_all_name():
    name = []
    for peo in people:
        name.append(peo['name'])
    print(name)
# ['Alice', 'Bob', 'Charlie', 'David']


def get_all_name_by_city():
    name = []
    for peo in people:
        if peo['city'] == 'Chicago':
            name.append(peo['name'])
    print(name)


categories_by_city()
get_all_name()
get_all_name_by_city()
