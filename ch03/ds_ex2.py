from typing import List

orders = [
    ['VIEW', '10', 'p1'],
    ['PURCHASE', '7', 'p4'],
    ['PURCHASE', '2', 'p2'],
    ['VIEW', '5', 'p1'],
    ['PURCHASE', '3', 'p3'],
    ['VIEW', '3', 'p2'],
    ['VIEW', '6', 'p2'],
    ['PURCHASE', '10', 'p2'],
    ['PURCHASE', '8', 'p1'],
    ['VIEW', '4', 'p1'],
    ['VIEW', '6', 'p1'],
    ['VIEW', '9', 'p4'],
    ['PURCHASE', '10', 'p4'],
    ['VIEW', '1', 'p1'],
    ['VIEW', '11', 'p1'],
    ['PURCHASE', '13', 'p1'],
    ['VIEW', '14', 'p1'],
    ['VIEW', '15', 'p3'],
    ['PURCHASE', '16', 'p3'],
    ['VIEW', '17', 'p3'],
]


def get_num_of_views_before_purchase(orders: List[List[str]]) -> dict:
    # get the number of views before the purchase
    views = {}
    
    # convert the second element to int using map for all the orders
    orders = list(map(lambda x: [x[0], int(x[1]), x[2]], orders))
    # order orders based on the time stamp and the type of the order
    orders.sort(key=lambda x: (x[1], x[2]))
    
    # group the orders by the product id
    id_set = list(set(list(map(lambda x: x[2], orders))))
    
    # order the orders by the product id
    id_set.sort()
    
    grouped_orders = []
    for product_id in id_set:
        grouped_orders.append([order for order in orders if order[2] == product_id])
        
    # for each group drop all elements after the last purchase
    for group in grouped_orders:
        last_purchase = None
        for order in group:
            if order[0] == 'PURCHASE':
                last_purchase = order
        if last_purchase:
            last_purchase_index = group.index(last_purchase)
            group = group[:last_purchase_index + 1]
        
        # count all the views
        view_count = 0
        for order in group:
            if order[0] == 'VIEW':
                view_count += 1
        
        views[group[0][2]] = view_count
        
    
    return views

if __name__ == "__main__":
    view = get_num_of_views_before_purchase(orders)
    print(view)