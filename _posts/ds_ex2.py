from typing import List

orders = [
    ['VIEW', '10', 'p1'],
    ['PURCHASE', '7', 'p4'],
    ['PURCHASE', '2', 'p2'],
    ['VIEW', '5', 'P1'],
    ['PURCHASE', '3', 'p3'],
    ['PURCHASE', '8', 'p1'],
    ['VIEW', '4', 'p1'],
    ['VIEW', '6', 'p1'],
    ['VIEW', '9', 'p4'],
    ['PURCHASE', '10', 'p4'],
    ['VIEW', '1', 'p1'],
    ['VIEW', '11', 'p1'],
    ['PURCHASE', '13', 'p1'],
    ['VIEW', '14', 'p1'],
]


def get_num_of_views_before_purchase(orders: List[List[str]]) -> dict:
    # get the number of views before the purchase
    views = {}
    
    # convert the second element to int using map for all the orders
    orders = list(map(lambda x: [x[0], int(x[1]), x[2]], orders))