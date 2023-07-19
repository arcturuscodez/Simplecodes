import datetime
import csv
import os
from main import get_ip_address

def collect_user_data(username, action):
    timestamp = datetime.datetime.now()
    ip_address = get_ip_address()

    data = {
        'timestamp': timestamp,
        'username': username,
        'action': action,
        'ip_address': ip_address,
    }

    save_data_to_csv(data)

def save_data_to_csv(data):

    file_path = 'user_data.csv'

    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

collect_user_data('user', 'access')