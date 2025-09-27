balance = 1000  # USD
btc_price = 50000
btc_amount = 0

while True:
    action = input("Buy, Sell, or Exit: ").lower()
    if action == "buy":
        usd = float(input("Enter amount in USD: "))
        if usd <= balance:
            btc = usd / btc_price
            btc_amount += btc
            balance -= usd
            print(f"Bought {btc:.6f} BTC")
        else:
            print("Not enough balance.")
    elif action == "sell":
        btc = float(input("Enter amount in BTC: "))
        if btc <= btc_amount:
            usd = btc * btc_price
            btc_amount -= btc
            balance += usd
            print(f"Sold {btc:.6f} BTC for ${usd:.2f}")
        else:
            print("Not enough BTC.")
    elif action == "exit":
        print("Final Balance:", balance, "USD,", btc_amount, "BTC")
        break
    else:
        print("Invalid action")
