#! /usr/bin/env python

#  glance.py was generated by yup.py (yupp) 1.0c5
#  out of glance.yu-py

import time
from ConfigParser import ConfigParser

FILE = 'glance.ini'
SEC = 'General'

ini_step = 0
ini_greeting = 'Hello! Improving Pi...'
ini_Pi = 0.0
ini_flag = True
ini_date = time.strftime( '%c' )

def ini_load( fn ):
    global ini_step
    global ini_greeting
    global ini_Pi
    global ini_flag
    global ini_date

    ini = ConfigParser()

    ini.read( fn )
    if ini.has_section( SEC ):
        if ini.has_option( SEC, 'step' ):
            ini_step = ini.getint( SEC, 'step' )
        if ini.has_option( SEC, 'greeting' ):
            ini_greeting = ini.get( SEC, 'greeting' )
        if ini.has_option( SEC, 'Pi' ):
            ini_Pi = ini.getfloat( SEC, 'Pi' )
        if ini.has_option( SEC, 'flag' ):
            ini_flag = ini.getboolean( SEC, 'flag' )
        if ini.has_option( SEC, 'date' ):
            ini_date = ini.get( SEC, 'date' )

def ini_save( fn ):
    global ini_step
    global ini_greeting
    global ini_Pi
    global ini_flag
    global ini_date

    ini = ConfigParser()

    if not ini.has_section( SEC ):
        ini.add_section( SEC )

    ini.set( SEC, 'step', str( ini_step ) )
    ini.set( SEC, 'greeting', ini_greeting )
    ini.set( SEC, 'Pi', str( ini_Pi ) )
    ini.set( SEC, 'flag', str( ini_flag ) )
    ini.set( SEC, 'date', ini_date )

    with open( fn, 'wb' ) as f:
        ini.write( f )

if __name__ == '__main__':
    ini_load( FILE )

    # Calc Pi using Leibniz formula, add one term of the series
    ini_Pi += pow( -1, ini_step ) * 4.0 / ( ini_step * 2 + 1 )
    ini_step += 1

    print 'ini_step =', ini_step
    print 'ini_greeting =', ini_greeting
    print 'ini_Pi =', ini_Pi
    print 'ini_flag =', ini_flag
    print 'ini_date =', ini_date

    ini_save( FILE )