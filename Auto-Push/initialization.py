import getpass
import json

username = input('Enter your Leetcode username: ')
session_id = getpass.getpass('Enter your leetcode session ID: ')

user_info = {
    "username": username,
    "session_id": session_id
}

with open("user_info.json", "w") as f:
    json.dump(user_info, f, indent=2)

print('User info is saved to user_info.json')


