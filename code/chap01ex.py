"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ValidatePregnum():

    # read pregnancy dataframe
    preg = nsfg.ReadFemPreg()

    # get count of number of pregnancies per respondent (pregnum)
    pregnum_counts = preg.pregnum.value_counts().sort_index()
    print(pregnum_counts)

    preg_map = nsfg.MakePregMap(preg)

    for index, pregnum in preg.pregnum.iteritems():
        caseid = preg.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum in respondent file equals
        # number of pregancy records
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True



ValidatePregnum()
