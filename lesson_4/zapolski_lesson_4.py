import utils

def main():

    print(utils.currency_rates("USD", True))
    print(utils.Decimal.from_float(utils.currency_rates("USD")))
    print(utils.currency_rates("EUR"))
    print(utils.Decimal.from_float(utils.currency_rates("EUR")))



if __name__ == "__main__":
    main()
