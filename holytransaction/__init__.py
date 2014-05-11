"""
HolyTransaction Python Client Library

AUTHOR

Andrey Zamovskiy
Bitbucket: nixoid

LICENSE (The MIT License)

Copyright (c) 2014 Andrey Zamovskiy "andrey@noveltylab.com"

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

__author__ = 'nixoid'

import httplib2
import json
import os
import requests


from holytransaction.config import HT_ENDPOINT

class HtApiClient(object):
    """
    Api client instance

    Only token auth is implemented here.
    HMAC-SHA1 auth is also available but not implemented in this client
    """

    def __init__(self,
                 auth_token=None):
        """

        :param auth_token: HolyTransaction Auth Token
        """

        #Set up our requests session
        self.session = requests.session()

        #Set our Content-Type
        self.session.headers.update({'content-type': 'application/json'})

        self.endpoint = HT_ENDPOINT

        if auth_token:
            if type(auth_token) is str:

                #Set client auth token
                self.auth_token = auth_token

                #Set our global_request_params
                self.global_request_params = {'auth_token': auth_token}
            else:
                print "Your auth_token must be a string"
        else:
            print "You must pass an auth_token"


    def post(self, uri, params):
        """
        Execute POST request

        :return: Dictionary result
        """

        url = self.endpoint + uri
        response = self.session.post(url, data=json.dumps(params), params=self.global_request_params)
        print url
        print response
        return response.json()


    def get(self, uri):
        """
        Execute GET request

        :return: Dictionary result
        """

        url = self.endpoint + uri
        response = self.session.get(url, params=self.global_request_params)
        return response.json()
