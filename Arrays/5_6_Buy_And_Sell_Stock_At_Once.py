

def buy_and_sell_stock_once(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        max_profit_today = price - min_price
        max_profit = max(max_profit, max_profit_today)

        min_price = min(min_price, price)


    return max_profit

prices = [310,315,275,295,260,270,290,230,255,250]

print(buy_and_sell_stock_once(prices))