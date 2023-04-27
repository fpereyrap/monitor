import argparse
import json
import requests
from time import sleep
import sys

webhook_url = "https://hookb.in/VGL7P7y9ZECDrgoorYZq"

def send_alert(path, user_agent):
    url= f"{webhook_url}?path={path}&useragent={user_agent}"
    try:
        requests.post(url)
    except requests.exceptions.RequestException as e:
        print(f"Error sending alert: {e}")
        sys.exit(1)

def process_logs(logfile, tail=False):
    processed_lines = 0
    while True:
        try:
            with open(logfile, "r") as log_file:
                lines = log_file.readlines()
                new_lines = lines[processed_lines:]

                for line in new_lines:
                    try:
                        log = json.loads(line)
                    except json.JSONDecodeError as e:
                        print(f"Error parsing log line: {e}")

                    status = log["http"]["status"]
                    if 500 <= status <= 599:
                        path = log["http"]["path"]
                        user_agent = log["http"]["headers"]["User-Agent"]
                        send_alert(path, user_agent)

                processed_lines = len(lines)
                if not tail:
                    break

        except FileNotFoundError as e:
            print(f"Error opening log file: {e}")
            sys.exit(1)

        if tail:
            sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Monitor and alert on 5XX HTTP status codes in logs")
    parser.add_argument("logfile", help="Log file to process")
    parser.add_argument("--tail", action="store_true", help="Continuously monitor the log file for changes")
    args = parser.parse_args()
    process_logs(args.logfile, args.tail)

if __name__ == "__main__":
    main()