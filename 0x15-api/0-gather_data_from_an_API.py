#!/usr/bin/python3
"""Using REST API.

Returns info about employees TODO list progress
"""


import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com"

users = requests.get(
    "{}/users/?id={}".format(url, argv[1])
)

todo_total = requests.get(
    "{}/todos?userId={}".format(url, argv[1])
)

todo_completed = requests.get(
    "{}/todos?userId={}&&completed=true".format(url, argv[1])
)


users_dict = users.json()
todo_dict_total = todo_total.json()
todo_completed_dict = todo_completed.json()

EMPLOYEE_NAME = users_dict[0]['name']
NUMBER_OF_DONE_TASKS = len(todo_completed_dict)
TOTAL_NUMBER_OF_TASKS = len(todo_dict_total)
text = "Employee {} is done with tasks({}/{}):".format(
    EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
)
print(text)
for task in todo_completed_dict:
    print("\t {}".format(task['title']))
