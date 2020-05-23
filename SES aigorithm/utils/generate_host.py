import sys
import os
import json


absPath = os.path.abspath(os.path.dirname(sys.argv[0]))
numProc = 15
if len(sys.argv) > 1:
    numProc = int(sys.argv[1])

data = {}
data['host_info'] = []

for i in range(numProc):
    portNumber = 55500+i
    data['host_info'].append({
        'host': '127.0.0.1',
        'port': portNumber
    })

with open('{}/../config/socket-host.json'.format(absPath), "w") as fw:
    json.dump(data, fw, indent=2)
