import json
import vars


def createTable():
    attributes = ["Name", "StartSlot", "EndSlot"]
    print("What is the name of the Rack?: ", end="")
    name = input()
    print("How many slots are in the Rack?: ", end="")
    slots = input()
    print("How many attributes do you want in the Rack? (Default comes with Name, Starting Slot, and Ending Slot): ",
          end="")
    attrib = int(input())
    for count in range(0, attrib):
        print("Please write the name of the attribute: ", end="")
        attributes.append(input())
    vars.racks[name] = {}
    vars.racks[name]["Slots"] = int(slots)
    vars.racks[name]["Attributes"] = attributes
    print(json.dumps(vars.racks, indent=4))
