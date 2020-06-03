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