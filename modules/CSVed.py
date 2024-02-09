# This file contains functions relating to output and input to a CSV
import csv


def importCSVFile():
    csv.reader()
    return


def exportRackCSV(rack, rackname):
    rack.to_csv(f"{rackname}.csv", index=True)
