# This file contains functions related to creating pandas dataframes
import pandas as pd


# pandaTable creates a new dataframe for the specific rack we are working with
def pandaTable(items, slots):
    # First it creates a new dictionary for the rack
    newrack = {}

    # Then it populates the dictionary with empty items for each of the slots
    for cnt in range(0, len(items)):
        newrack[items[cnt]] = [None] * int(slots)

    # Once that's done, it returns the dataframe
    return pd.DataFrame(newrack)
