
from math import sqrt

algorithm = 'old'
delay = 100
method = 'avg'

def variance (vals):
    if not len(vals):
        return 0
    avg = sum(vals)/max(len(vals),1)
    return sqrt(sum((val-avg)**2 for val in vals)/len(vals))

results = {}
with open('results_algorithm_%s_watdiv_100ms.txt' % algorithm, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if not line[0] == '!':
            query = line.strip()
            occs = query.count(' . ')
            if occs not in results:
                results[occs] = [[],[],[],[],[]]
        else:
            vals = line[1:].split(';')
            for idx, val in enumerate(vals):
                if val and val != 'TIMEOUT':
                    results[occs][idx].append(int(val))

with open('%s_algorithm%d_watdiv_%dms.csv' % (method, 1 if algorithm == 'old' else 2, delay), 'w') as f:
    f.write('query;time_first;http_first;time;http;results\n');
    for result in results:
        f.write('%d;' % result)
        if method == 'avg':
            f.write(';'.join(str(sum(vals)/max(len(vals),1)) for vals in results[result]))
        elif method == 'med':
            f.write(';'.join(str(sorted(vals)[len(vals)/2] if len(vals) else '') for vals in results[result]))
        elif method == 'var':
            f.write(';'.join(str(variance(vals)) for vals in results[result]))
        f.write('\n')

        