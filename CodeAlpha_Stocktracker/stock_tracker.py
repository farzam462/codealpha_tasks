stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0
portfolio = []

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    value = price * quantity

    total_investment += value
    portfolio.append(f"{stock} - {quantity} shares - ${value}")

    print(f"Added {stock}: ${value}")

print("\n📊 Portfolio Summary:")
for item in portfolio:
    print(item)

print("\nTotal Investment Value: $", total_investment)

save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("----------------------\n")
        for item in portfolio:
            file.write(item + "\n")
        file.write(f"\nTotal Investment: ${total_investment}")

    print("✅ Saved to portfolio.txt")
