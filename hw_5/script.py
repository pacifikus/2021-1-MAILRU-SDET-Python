import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('--total', action='store_true')
parser.add_argument('--by-type', dest='by_type')
parser.add_argument('--top10', action='store_true')
parser.add_argument('--top4xx', action='store_true')
parser.add_argument('--top5xx', action='store_true')
parser.add_argument('--json', action='store_true')

args = parser.parse_args()

with open(args.path) as file:
    requests = file.readlines()
    requests = [request.split() for request in requests]


def count_total():
    return str(len(requests))


def count_by_type(request_type):
    count = 1
    for request in requests:
        if request[5][1:] == request_type:
            count += 1
    return f'{request_type} - {count}'


def top_10():
    temp_dict = {}
    for request in requests:
        url = request[6]
        if url in temp_dict:
            temp_dict[url] += 1
        else:
            temp_dict[url] = 1
    return [f'{url} - {count}'
            for url, count in sorted(temp_dict.items(),
                                     key=lambda x: x[1],
                                     reverse=True)][:10]


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
    return [f'{ip} - {count}'
            for ip, count in sorted(temp_dict.items(),
                                    key=lambda x: x[1],
                                    reverse=True)][:5]


def print_data(header, outfile, data):
    print(header,
          *data,
          sep='\n',
          file=outfile,
          end='\n\n')


result = {}
if args.total:
    result['Total'] = count_total()
if args.by_type:
    result['By type'] = count_by_type(args.by_type)
if args.top10:
    result['top10'] = top_10()
if args.top4xx:
    result['top4xx'] = top_5_4xx_requests()
if args.top5xx:
    result['top5xx'] = top_5_5xx_users()

if args.json:
    with open('result.json', 'w') as out:
        json.dump(result, out, indent=4)
else:
    with open('output.txt', 'w') as out:
        if 'Total' in result:
            print_data('Total requests count:\n', out, [str(result['Total'])])
        if 'By type' in result:
            print_data(f'Requests count by type {args.by_type}:\n', out, [str(result['By type'])])
        if 'top10' in result:
            print_data(f'Top 10 most frequent:', out, result['top10'])
        if 'top4xx' in result:
            print_data(f'Top 5 by size with 4XX code:', out, result['top4xx'])
        if 'top5xx' in result:
            print_data(f'Top 5 by count with 5XX code:', out, result['top5xx'])
