print("Welcome to Elite 101 Chatbot")
user_name = input("Please Enter Your Name: ")
user_age = input(f"Hello {user_name}! I'm glad you're here. How old are you?: ")
print(f"Wow! {user_name} I wish I was {user_age} again!. How can I help you? today\n")

is_exit = False
while(not is_exit):
  print("Please select from the following options: ")
  print("1. Placeholder option 1")
  print("2. Placeholder option 2")
  print("3. Placeholder option 3")
  print("4. Exit the Conversation")
  user_input = input("Please enter the number of your choice: ")

  if user_input == "1":
    print("Placeholder option 1\n")
  elif user_input == "2":
    print("Placeholder option 2\n")
  elif user_input == "3":
    print("Placeholder option 3\n")
  elif user_input == "4":
    print("Exiting the conversation")
    print(f"Goodbye {user_name}! I hope you have a great day!")
    is_exit = True