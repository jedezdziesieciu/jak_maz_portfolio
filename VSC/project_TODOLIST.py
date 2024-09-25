header = """

  _____          _         _     _        _____
 |_   _|__    __| | ___   | |   |_|  ___ |_   _|
   | |/ _ \  / _` |/ _ \  | |   | | / __|  | |
   | | (_) | |(_| | (_) | | |__ | | \__ \  | |
   |_|\___/  \__,_|\___/  |____||_|_|___/  |_|

                            
"""
print(header)
todos = []
#completed list
completed = []
while True:
    # for todo in todos:
    #     print(f"* {todo}")
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
    print("*" * 20)
    print("Enter a command. Type 'h' for help: ")
    command = input("> ")
    if command == "q":
        break
    elif command == "h":
        print("TO DO LIST:")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")
    elif command.isnumeric():
        idx = int(command) - 1
        if idx >= len(todos):
            print("THERE IS NO TO DO WITH THIS NUMBER")
        else:
            #todos.pop(idx)
            done_todo = todos.pop(idx)
            completed.append(done_todo)
    else:
        todos.append(command)
#print("Good bye")
if completed:
    print(f"You completed your {len(completed)} list today: ")
    for todo in completed:
        print(f"* {todo}")