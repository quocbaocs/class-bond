#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ClassPriceOfBond.py Get yield-to-maturity of a bond
__author__      = "Le Quoc Bao KHMT11A "
__university__ = "Industrial university of Ho Chi Minh City"
__copyright__   = "Copyright 2020"

__email__ = "quocbaole.cs@gmail.com"
__status__ = "Production"
"""

import scipy.optimize as optimize
from scipy import optimize, special



class CalculatingBond:
    def __init__(self,price, par, T, coup, freq=2):
        self.price = price
        self.par = par
        self.T = T
        self.coup = coup
        self.freq = freq

    def getData(self):
        print("{}\n{}\n{}\n{}\n{}\n{}\n".format(self.price,
                                                self.par, self.T, self.ytm, self.coup, self.freq))
    
    def bond_ytm(self, guess=0.05):
        freq = float(self.freq)
        periods = self.T*freq
        coupon = self.coup/100.*self.par/freq
        dt = [(i+1)/freq for i in range(int(periods))]
        def ytm_func((y)): return \
            sum([coupon/(1+y/freq)**(freq*t) for t in dt]) + \
            self.par/(1+y/freq)**(freq*t) - self.price
        return optimize.newton(ytm_func, guess)
    

    def bond_price(self,ytm):
        freq = float(self.freq)
        periods = self.T*freq
        coupon = self.coup/100.*self.par/freq
        dt = [(i+1)/freq for i in range(int(periods))]
        price = sum([coupon/(1+ytm/freq)**(freq*t) for t in dt]) + \
            self.par/(1+ytm/freq)**(freq*self.T)
        return price

    def bond_mod_duration(self, ytm, dy=0.01):

        ytm_minus = ytm - dy    
        price_minus = self.bond_price(ytm_minus)
        
        ytm_plus = ytm + dy
        price_plus = self.bond_price(ytm_plus)
        
        mduration = (price_minus-price_plus)/(2.*self.price*dy)
        return mduration

    def bond_convexity(self,ytm,dy=0.01):
        ytm_minus = ytm - dy    
        price_minus = self.bond_price(ytm_minus)
        
        ytm_plus = ytm + dy
        price_plus = self.bond_price(ytm_plus)
        
        convexity = (price_minus+price_plus-2*self.price)/(self.price*dy**2)
        return convexity
