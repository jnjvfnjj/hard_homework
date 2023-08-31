import schedule
import time
import requests
import argparse
import logging

logging.basicConfig(filename='request_logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def perform_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Request to {url} successful. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")


def main(url, initial_delay, interval):
    schedule.every(initial_delay).seconds.do(perform_request, url)
    schedule.every(interval).seconds.do(perform_request, url)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
delay = 1
url = 'https://youtube.com/'
val = 1

main( url,delay, val)