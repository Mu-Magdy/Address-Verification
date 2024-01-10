import requests
import time

server_url = "http://127.0.0.1:5000/verify_address"

test_data = {"address": "حلوان"}


num_requests = 10

execution_times = []

for _ in range(num_requests):
    start_time = time.time()

    response = requests.post(server_url, json=test_data)

    end_time = time.time()

    execution_time = (end_time - start_time) * 1000
    execution_times.append(execution_time)

    print(f"Result: {response.json()}, Execution Time: {execution_time:.2f} ms")

average_execution_time = sum(execution_times) / num_requests
print(f"Average Execution Time: {average_execution_time:.2f} ms")
