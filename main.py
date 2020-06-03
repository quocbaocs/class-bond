#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ClassPriceOfBond.py Get yield-to-maturity of a bond
__author__      = "Le Quoc Bao KHMT11A "
__university__ = "Industrial university of Ho Chi Minh City"
__copyright__   = "Copyright 2020"

__email__ = "quocbaole.cs@gmail.com"
__status__ = "Production"
"""

from ClassPriceOfBond import CalculatingBond


def main():

    bond1 = CalculatingBond(95.0428,100, 1.5, 5.75, 2)
    ytm = bond1.bond_ytm()
    print("ytm bond: ",ytm)
    print("bond price : ",bond1.bond_price(ytm))
    print("bond mod ration: ",bond1.bond_mod_duration(ytm))
    print("bond convexity: ", bond1.bond_convexity(ytm))

if __name__ == "__main__":
    main()