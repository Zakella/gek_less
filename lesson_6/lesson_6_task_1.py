import requests
from collections import Counter


def parse_log():
    with open('nginx_logs.txt', "r", encoding="utf-8") as logs:
        for line in logs:
            split_log = line.split()
            yield (split_log[0], split_log[5], split_log[6])

def load_logs_in_file():
    response = requests.get(
        "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
    if response.status_code == 200:
        with open('nginx_logs.txt', "w", encoding="utf-8") as logs:
            logs.write(response.text)


if __name__ == "__main__":
    load_logs_in_file()
    data = Counter(parse_log())
    most_common = data.most_common(1)
    spammer_ip = most_common[0][0][0]
    req_times = most_common[0][-1]
    print(f"Spammer IP is {spammer_ip}, number of requests {req_times}")
