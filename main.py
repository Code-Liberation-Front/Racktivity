import modules.database
import modules.CSVed as CSVed
import modules.JSONed as JSONed
import modules.selection as selection
import vars

vars.init()

print("______              _     _    _         _  _          \n"
      "| ___ \            | |   | |  (_)       (_)| |         \n"
      "| |_/ / __ _   ___ | | __| |_  _ __   __ _ | |_  _   _ \n"
      "|    / / _` | / __|| |/ /| __|| |\ \ / /| || __|| | | |\n"
      "| |\ \| (_| || (__ |   < | |_ | | \ V / | || |_ | |_| |\n"
      "\_| \_|\__,_| \___||_|\_\ \__||_|  \_/  |_| \__| \__, |\n"
      "                                                  __/ |\n"
      "                                                 |___/ \n")

while True:
    print("Please select an option:\n\n0: Exit\n1: Create a new table for your rack\n2: Print a rack table\n3: Remove"
          " a rack table\n4: Add new rows to your rack\n5: Remove a row of information from a rack\n6: Input a single "
          "server's information\n7: Display a single server's information\n8: Import from a CSV file\n")
    print("Please select an option: ", end="")
    userSelection = input()
    print("")
    if userSelection == "0":
        break
    elif userSelection == "1":
        selection.createTable()
