import requests
import bs4
from multiprocessing import Queue, Process, Pool

n = 4

q_in, q_out = Queue(), Queue()

adres = 'http://194.29.175.134:4444'

session = requests.session()

r = session.post(adres+'/login', {'uname': 'foo', 'password': 'bar'})
r = session.get(adres+'/245259245303')


def process(q_out, q_in):
    session = requests.session()
    r = session.post(adres+'/login', {'uname': 'foo', 'password': 'bar'})
    while True:
        i, adr = q_in.get()
#        print(adres+adr, i, '1')
        r = session.get(adres+adr)
#        print(adres+adr, i, '2')
        adrs = [ link['href'] for link in bs4.BeautifulSoup(r.text).findAll('a') ]
        q_out.put((i+1, adrs))


bs = bs4.BeautifulSoup(r.text)
links = [ link['href'] for link in bs.findAll('a') ] 

results = [ [] for x in range(n+1) ]
results[0] = links

np = 4

processes = []
for i in range(np):
    p = Process(target=process, args=(q_in, q_out))
    p.start()
    processes.append(p)


for link in links:
    q_out.put((0, link))


while True:#not q_out.empty() or not q_in.empty():
    try:
        level, links = q_in.get(timeout=1)
    except Exception:
        break
#    print(level)
    results[level]+=links
    if level < n:
        for link in links:
            q_out.put((level, link))
#    else:
 #       print('koniec')


for pr in processes:
    pr.terminate()

print(results)
print( [ len(x) for x in results ] )

