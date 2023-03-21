#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:49:18 2023

@author: C. Martinez-Lombilla

A script to simulate a catalogue of simulated stars around Andromeda galaxy 
"""

import math
import random

NSRC = 1_000_000


def get_radec():
    '''
    Determine Andromeda location in ra/dec degrees

    Returns
    -------
    Tuple with ra and dec values

    '''
    
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    
    return (ra, dec)


def make_stars(ra, dec, NSRC):
    '''
    Make 1000000 stars within 1 degree of Andromeda

    Parameters
    ----------
    ra : float
        ra in degrees
    dec : float
        dec in degrees
    NSRC : int
        number of stars to simulate

    Returns
    -------
    tuple with the lists of ra and dec values

    '''

    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return (ras, decs)



def main():
    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, NSRC)
    
    # now write these to a csv file for use by my other program
    with open('catalog.csv','w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{0:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)


if __name__ ==  '__main__':
    main()