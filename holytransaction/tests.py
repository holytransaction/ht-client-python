__author__ = 'nixoid'

import unittest
from sure import this
from httpretty import HTTPretty, httprettified
from holytransaction import HtApiClient



class ClientTests(unittest.TestCase):

    def setUp(self):
        self.client = HtApiClient(auth_token='9vi73Q0g7dVnOneiPT47Bf7bdmfG2rvBqyW40yx56NaSrBaqjPzyxgzP0dV47BwUNCf6UAf2UGIMcOjo4Y9R')

    @httprettified
    def test_post(self):
        HTTPretty.register_uri(HTTPretty.POST, "https://api.holytransaction.com/api/v1/ofac",
                               body='''{"k":"v"}''',
                               content_type='text/json')
        this(self.client.post("ofac", {'c': "d"})).should.equal({'k': "v"})


    @httprettified
    def test_get(self):
        HTTPretty.register_uri(HTTPretty.GET, "https://api.holytransaction.com/api/v1/balances",
                               body='''{"k":"v"}''',
                               content_type='text/json')

        this(self.client.get("balances")).should.equal({'k': "v"})


