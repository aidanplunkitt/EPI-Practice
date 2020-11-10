from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_net = 0.0
    min_price = prices[0]

    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_net = max(max_net, prices[i] - min_price)

    return max_net


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
