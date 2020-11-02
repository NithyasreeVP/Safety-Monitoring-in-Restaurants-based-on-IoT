#!/usr/bin/env python
# coding: utf-8

# In[1]:
import requests
import sys


data = {'domain': open(sys.argv[1], 'r').read(),
        'problem': open(sys.argv[2], 'r').read()}

response = requests.post('http://solver.planning.domains/solve', json=data).json()


with open(sys.argv[3], 'w') as f:
    for act in response['result']['plan']:
        #f.write('\n')
        f.write(str(act['name']))
        f.write('\n')



# In[ ]:




