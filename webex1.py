# Import necessary libraries
import requests
import json

# Function to test the connection to the Webex server
def test_connection(headers):
    url = 'https://webexapis.com/v1/people/me'
    response = requests.get(url, headers=headers)
    
    # Check if the response status code is 200 (success)
    if response.status_code == 200:
        print("\nConnection to Webex server successful")
    else:
        print("\nConnection to Webex server failed")

# Function to display user information
def display_user_information(headers):
    url = 'https://webexapis.com/v1/people/me'
    response = requests.get(url, headers=headers)
    
    # Check if the response status code is 200 (success)
    if response.status_code == 200:
        user_info = response.json()
        print("\nUSER INFORMATION")
        print("*" * 130)
        print(f"User Displayed name: {user_info['displayName']}")
        print(f"User Nickname: {user_info['nickName']}")
        print(f"User email: {', '.join(user_info['emails'])}")
        print("*" * 130)
    else:
        print("\nFailed to retrieve user information")

# Function to display a list of rooms
def display_rooms(headers):
    url = 'https://webexapis.com/v1/rooms'
    params = {'max': '5'}
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the response status code is 200 (success)
    if response.status_code == 200:
        room_info = response.json()
        if 'items' in room_info:
            print("\nROOM INFORMATION")
            print("*" * 120)
            for room in room_info['items']:
                print(f"Room Id: {room['id']}")
                print(f"Room name: {room['title']}")
                print(f"Room's date created: {room['created']}")
                print(f"Last activity: {', '.join(room['lastActivity'])}")
                print("*" * 120)
    else:
        print("\nFailed to retrieve room information")

# Function to create a new room
def create_room(headers):
    url = 'https://webexapis.com/v1/rooms'
    room_name = input("Enter the room name you want to create: ")
    params = {'title': room_name}
    response = requests.post(url, headers=headers, json=params)
    
    # Check if the response status code is 200 (success)
    if response.status_code == 200:
        print(f"\nRoom '{room_name}' has been created")
    else:
        print(f"\nFailed to create the room due to error: {response.status_code}")

# Function to send a message to a room
def send_message_to_room(headers):
    url = 'https://webexapis.com/v1/rooms'
    params = {'max': '5'}
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the response status code is 200 (success)
    if response.status_code == 200:
        room_info = response.json()
        print("\nROOMS")
        print("*" * 120)
        for i, room in enumerate(room_info['items']):
            print(f"({i + 1}) {room['title']}")
            print("*" * 120)
        room_choice = int(input("\nPlease choose a room to send a message: ")) - 1

        if 0 <= room_choice < len(room_info['items']):
            room_id_selected = room_info['items'][room_choice]['id']
            room_name_selected = room_info['items'][room_choice]['title']
            message_to_room = input("Enter the message you want to send: ")
            params = {'roomId': room_id_selected, 'markdown': message_to_room}
            url = 'https://webexapis.com/v1/messages'
            response = requests.post(url, headers=headers, json=params)

            # Check if the response status code is 200 (success)
            if response.status_code == 200:
                print(f"\nMessage: '{message_to_room}' is sent successfully to room: '{room_name_selected}'")
            else:
                print(f"\nFailed to send the message due to error: {response.status_code}")
    else:
        print("\nFailed to retrieve room information")

# Main menu with options
print("-" * 130)
print("MENU OPTIONS")
print("-" * 130)
print("Test connection (0)")
print("Display User Information (1)")
print("Display 5 Rooms (2)")
print("Create a room (3)")
print("Send a message to a room (4)")
print("-" * 130)

# Input access token for Webex API
acc_token = input("Please enter your access token: ")
headers = {
    'Authorization': 'Bearer {}'.format(acc_token),
    'Content-Type': 'application/json'
}

# Choose an option based on user input
option = input("\nPlease choose an option: ")

if option == "0":
    test_connection(headers)
elif option == "1":
    display_user_information(headers)
elif option == "2":
    display_rooms(headers)
elif option == "3":
    create_room(headers)
elif option == "4":
    send_message_to_room(headers)
else:
    print("\nPlease choose the right option")

# Wait for user input to return to the main menu
user_input = input("\nPress Enter to return to the main menu...")

