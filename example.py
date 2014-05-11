__author__ = 'nixoid'

from holytransaction import HtApiClient


ht_api = HtApiClient(auth_token='9vi73Q0g7dVnOneiPT47Bf7bdmfG2rvBqyW40yx56NaSrBaqjPzyxgzP0dV47BwUNCf6UAf2UGIMcOjo4Y9R')
# ht_api.endpoint = 'http://localhost:3000/api/v1/'
ofac_result = ht_api.post("ofac", {'name': "Delgado, Jorge Armando"})

print ofac_result