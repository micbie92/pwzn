import requests
from multiprocessing.pool import ThreadPool
import multiprocessing as mp
import datetime

n = 10

pliczek = 'http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-b'

response = requests.head(pliczek)
resp_len = int(response.headers['Content-Length'])

result = [ None for x in range(n) ]

def kawalek(arg):
    ii, rrange = arg
    global result
    global pliczek
    response = requests.get(pliczek, headers = { "Range": "bytes={}-{}".format(*rrange) } )
    result[ii] = response.content
    return datetime.datetime.now()

p = ThreadPool(n)

args = []
step = int(resp_len / n)

for i in range(n):
    start = i*step
    if i == n-1:
        stop = resp_len
    else:
        stop = start+step
    stop-=1
    args.append( (i, (start, stop)) )

p.map(kawalek, args)

data = b"".join(result)

print(len(data_ok))

with open(pliczek.rsplit('/', 1)[1], 'wb') as f:
    f.write(data)


