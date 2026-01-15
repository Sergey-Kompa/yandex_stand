import requests
from configuration import BASE_URL

def create_order(order_data):
    return requests.post(f"{BASE_URL}/orders", json=order_data)

def get_order_by_track(track):
    return requests.get(f"{BASE_URL}/orders/track?t={track}")
