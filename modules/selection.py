import vars
import modules.tables as tables
import modules.CSVed as CSVed
import numpy as np


# Creates a table and places it in the dictionary of Racks for a local copy
def createTable():
    # First it creates a list for attributes and asks the user to input the attributes
    attributes = ["Name", "Slots"]
    print("What is the name of the Rack?: ", end="")
    name = input()
    print("How many slots are in the Rack?: ", end="")
    slots = input()
    print("How many attributes do you want in the Rack? (Default comes with Name and the Slots the server is in): ",
          end="")
    attrib = int(input())
    for count in range(0, attrib):
        print("Please write the name of the attribute: ", end="")
        attributes.append(input())

    # Then it creates a dataframe for the rack
    vars.racks[name] = tables.pandaTable(attributes, slots)

    # It then changes the dataframe to start from slot number 1
    vars.racks[name].index = np.arange(1, len(vars.racks[name]) + 1)

    # Then it flips indexes, so they are from the top to 1
    vars.racks[name] = vars.racks[name].iloc[::-1]
    print(vars.racks)


# This function outputs a single rack's information into a CSV file
def exportCSV():

    # Prompts the user to input a rack name
    rackname = input("What is the name of the rack you want to export: ")
    # It checks if the rack exists and if it doesn't it notifies the user that it doesn't exist
    rack = vars.racks.get(rackname, None)
    if rack is not None:
        CSVed.exportRackCSV(rack, rackname)
        print("Exported CSV successfully\n")
    else:
        print(f"There was no rack with the name \"{rackname}\"\n")
