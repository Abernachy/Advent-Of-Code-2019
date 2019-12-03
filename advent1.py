#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2019/day/1
This is the code for Advent day 1 puzzle.
Basically it will take in a list of values, the mass, and calculates the fuel
required for each one, then spits out the total compbined fuel requirement
"""

module_list = [103450,107815,53774,124794,90372,98169,106910,50087,104958,
        71936,118379,122284,55871,91714,120685,117684,146047,60332,72034,
        127689,117575,101714,121018,86073,73764,100533,104443,113037,79474,
        123364,128367,63620,54004,124093,133256,95915,97442,64267,70823,143108,
        86422,118962,66129,69445,51804,56436,117587,64632,104564,67514,108782,
        123991,110932,122201,98816,126708,69821,66902,96993,55032,109143,67678,
        58009,50232,69841,101922,95832,122820,72056,102557,68727,85192,74694,
        142252,140332,53783,123036,88197,148727,138393,87427,65693,88448,51044,
        95470,97336,121463,91997,149518,66967,119301,112022,57363,128247,107454,
        77260,126346,97658,137578,134743]


def advent1(values):
    fuelmodule_list = []
    totalfuel = 0
    for item in values:
        fuelpermodule = int((item / 3) - 2)
        fuelmodule_list.append(fuelpermodule)
        totalfuel += fuelpermodule
    
    print("List of fuel required per module: \n" , fuelmodule_list)
    print("Total Required fuel:  " , totalfuel)

'Advent 1'

print('Advent 1: \n\n')
advent1(module_list)

"""
For Advent 1.5, it runs the same way, however, while the total fuel value 
remains above 0, it appends it to the module list, then takes that value,
runs the math, and appends that.  It does that loop until it hits a value of
0 or below.
"""
'I got lazy retyping the math problem over and over'
def calcmasstofuel(value):
    calcvalue = int((value/ 3)-2)
    return calcvalue

def advent1point5(values):
    fuelmodule_list = []
    finaltotal = 0
    for item in values:
        fuelpermodule = calcmasstofuel(item)
        fuelmodule_list.append(fuelpermodule)
        while fuelmodule_list[-1] > 3:
                fuelpermod = calcmasstofuel(fuelmodule_list[-1])
                fuelmodule_list.append(fuelpermod)
        
    'Get the complete total'
    for item in fuelmodule_list:
        finaltotal += item

    'Advent 1.5'
    print('Advent1.5: \n\n')
    print('Values:\n\n', fuelmodule_list)
    print('Total number of modules: ', len(fuelmodule_list), '\n\n')
    print('Final Total of fuel: ', finaltotal)

advent1point5(module_list)

