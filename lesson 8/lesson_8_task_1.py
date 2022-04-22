import re

# pattern = re.compile(r'(\d{2,3}.)')

ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
date_patern = re.compile(r'\[(.*?)\]')
request_pattern = re.compile(r'[A-Z]{3}\s')
# response_pattern = re.compile(r'\"(GET|POST) )(?P<url>.+)(http\/1\.1")
code_pattern = re.compile(r'.+HTTP\/1\.1" (\d{3})')

response_pattern = re.compile(
    r"""  (http\/1\.1")""",
    re.IGNORECASE)

""

with open("nginx_logs", "r", encoding="utf-8") as nginx:
    for line in nginx:
        remote_addr = ip_pattern.findall(line)
        request_datetime = date_patern.findall(line)
        request_type = request_pattern.findall(line)
        requested_resource = response_pattern.findall(line)
        code = code_pattern.findall(line)
        print(remote_addr, request_datetime, request_type, requested_resource, code)
        break
        # print(lineformat.findall(line))
        # for res in result_iter:
        # print(res.groups())  # найденные группы
        # print(res.group(0))  # всё, что на сработала регулярка
        # # print(res.group(1))  # первая группа, нумерация с 1
        # # print(res.group(2))
        # # print(res.group(3))
        # # print(res.groupdict())
