import re

#задание 1
def email_parse(email):
 e_pattern = re.compile(r'^\w{2,}@\w*\.\w{1,3}')
 valid_email = e_pattern.findall(email)
 if not valid_email:
     raise ValueError("Not valid e-mail")
 user_domain = "".join(valid_email).split("@")
 return {"username":user_domain[0],
         "domain":user_domain[1]}


#задание 2
def parse_nginx():

    # разбиваю на блоки что бы можно было норм читать
    ip_pattern = re.compile(r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    date_patern = re.compile(r'\[(.*)\]')
    request_pattern = re.compile(r'GET')
    response_pattern = re.compile(r'[^\d]\/\w+\/\w+')
    code_pattern = re.compile(r'.+HTTP\/1\.1" (\d{3}\s\d{1,4})')
    with open("nginx_logs", "r", encoding="utf-8") as nginx:
        for line in nginx:
            remote_addr = "".join(ip_pattern.findall(line))
            request_datetime = "".join(date_patern.findall(line))
            request_type = "".join(request_pattern.findall(line))
            requested_resource = "".join(response_pattern.findall(line))
            code_size = code_pattern.findall(line)
            response_size = "".join(code_size).split()[-1]
            code = "".join(code_size).split()[0]
            text =  (f'{remote_addr}, {request_datetime}, {request_type}, {requested_resource}, ' \
                   f'{code}, {response_size}')
            print(text)


if __name__ == "__main__":
    print(email_parse("someone@geekbrains.ru"))
    parse_nginx()
