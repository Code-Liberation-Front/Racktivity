# main.py contains the code to start the Racktivity Program. It contains a menu for the user to choose the option they
# want
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

# Loops through the menu until the options are finished
while True:
    userSelection = input("0: Exit\n1: Create a new table for your rack\n2: Remove a rack table\n3: Add new rows to "
                          "your rack\n4: Remove a row of information from a rack\n5: Input a single server's "
                          "information\n6: Import from a CSV file\n7: Output a single rack's information to a CSV file"
                          "\n\nPlease select an option: ")
    print("")
    if userSelection == "0":
        break
    elif userSelection == "1":
        selection.createTable()
    elif userSelection == "7":
        selection.exportCSV()
