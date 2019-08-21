
##############################################################################
###################   s v g _ g r a y s c a l e r . p y   ####################
##############################################################################
# Author: Dan Lynch
# Date: 08/10/2019
# Decription:
# This program takes in a .svg file, reads the colors of fill used, changes 
# those colors to grays, and writes a new "grayscale" .svg file. This program
# was started to practice usingn regular expressions with Python.
##############################################################################
##############################################################################
##############################################################################

import re
import sys

def main():
    # Check the file arguments
    inputFilename = sys.argv[1]
    outputFilename = sys.argv[2]
    print("The input filename is " + inputFilename + ".\n")
    print("The output filename is " +outputFilename + ".\n")
    # Open input file
    fill = re.compile(r'fill=\"#[a-zA-z0-9]*\"')
    colors = []
    with(open(inputFilename)) as inFile:
        lineOne = inFile.readline()
        # Regular expression for the fill values
        result = fill.finditer(lineOne)
        if (result):
            for r in result:
                colors.append(r.group())
                #print(r.group())
        else:
            print("No match in this line.")
    for i, c in enumerate(colors):
        temp = c[5:]
        print(temp)
        c = temp
        print(c)
        print(i)
    print(colors)

# Takes in a string that represents a hex value and returns an 8-bit gray
# scale value. Assumes original RGB values were gamma corrected. Takes an
# optional "original gamma value" parameter. If this is 0, it assumes 
# the original RGB values were linear (i.e. not gamma corrected). If para-
# meter i not specified, it assumed the default value of gamma (gamma = 2.2)
# Info for color space transformation from:
# https://stackoverflow.com/questions/687261
def rgbHexToGray(hexValue):
    # Check to make sure it is a valid hex RGB value
    pass
    # Rlin = R^gamma
    # Glin = G^gamma
    # Blin = B^gamma
    # Y = 0.2126Rlin + 0.7152Glin + 0.0722Blin
    # L = 116 * ( Y ^ (1/3)) - 16
    # Convert L into a RGB value for a gray color
    # return gray hex RGB Value


if __name__ == "__main__":
    main()