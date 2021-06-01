import argparse
import json

with open("access.log") as file:
    requests = file.readlines()
    requests = [request.split() for request in requests]


def count_total():
    return len(requests)


def count_by_type():
    temp_dict = {}
    for request in requests:
        request_type = request[5][1:]
        if request_type in temp_dict:
            temp_dict[request_type] += 1
        elif len(request_type) < 7:
            temp_dict[request_type] = 1
    return temp_dict


def top_10():
    temp_dict = {}
    for request in requests:
        url = request[6]
        if url in temp_dict:
            temp_dict[url] += 1
        else:
            temp_dict[url] = 1
    return temp_dict


def top_5_4xx_requests():
    temp_data = []
    for request in requests:
        url = request[6]
        status = request[8]
        size = request[9]
        ip = request[0]
        if status[0] == '4':
            item = (url, status, int(size), ip)
            temp_data.append(item)
    return [f'url: {item[0]}' \
            f' code: {item[1]}' \
            f' size: {item[2]}' \
            f' ip: {item[3]}'
            for item in sorted(temp_data,
                               key=lambda x: x[2],
                               reverse=True)][:5]


def top_5_5xx_users():
    temp_dict = {}
    for request in requests:
        ip = request[0]
        status = request[8]
        if status[0] == '5':
            if ip in temp_dict:
                temp_dict[ip] += 1
            else:
                temp_dict[ip] = 1
    return temp_dict


def print_data(header, outfile, data):
    print(header,
          *data,
          sep='\n',
          file=outfile,
          end='\n\n')
