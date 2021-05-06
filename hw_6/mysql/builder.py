from mysql.models import TotalCount, CountByType, TopMostFrequent,\
    TopBiggestClientError, TopFrequentServerError


class MySQLBuilder:

    def __init__(self, client, path):
        self.client = client
        self.path = path
        self.requests = self.read_data()

    def read_data(self):
        with open(self.path) as file:
            requests = file.readlines()
            requests = [request.split() for request in requests]
            return requests

    def count_total(self):
        row = TotalCount(
            count=len(self.requests)
        )
        self.client.session.add(row)
        self.client.session.commit()
        return row

    def count_by_type(self):
        temp_dict = {}
        for request in self.requests:
            request_type = request[5][1:]
            if request_type in temp_dict:
                temp_dict[request_type] += 1
            elif len(request_type) < 7:
                temp_dict[request_type] = 1

        rows = []
        for request_type, count in temp_dict.items():
            row = CountByType(
                count=int(count),
                type_name=request_type
            )
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def top_10(self):
        temp_dict = {}
        for request in self.requests:
            url = request[6]
            if url in temp_dict:
                temp_dict[url] += 1
            else:
                temp_dict[url] = 1

        rows = []
        for url, count in sorted(temp_dict.items(),
                                 key=lambda x: x[1],
                                 reverse=True)[:10]:
            row = TopMostFrequent(
                count=int(count),
                url=url
            )
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def top_5_4xx_requests(self):
        temp_data = []
        for request in self.requests:
            url = request[6]
            status = request[8]
            size = request[9]
            ip = request[0]
            if status[0] == '4':
                item = (url, status, int(size), ip)
                temp_data.append(item)

        rows = []
        for item in sorted(temp_data,
                           key=lambda x: x[2],
                           reverse=True)[:5]:
            row = TopBiggestClientError(
                url=item[0],
                code=int(item[1]),
                size=int(item[2]),
                ip=item[3]

            )
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def top_5_5xx_users(self):
        temp_dict = {}
        for request in self.requests:
            ip = request[0]
            status = request[8]
            if status[0] == '5':
                if ip in temp_dict:
                    temp_dict[ip] += 1
                else:
                    temp_dict[ip] = 1

        rows = []
        for ip, count in sorted(temp_dict.items(),
                                key=lambda x: x[1],
                                reverse=True)[:5]:
            row = TopFrequentServerError(
                ip=ip,
                count=int(count)
            )
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def run_all(self):
        self.count_total()
        self.count_by_type()
        self.top_10()
        self.top_5_4xx_requests()
        self.top_5_5xx_users()
