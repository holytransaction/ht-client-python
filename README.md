HolyTransaction python client
==================================

Python Library for the HolyTransaction.com API
This is initial release intended for use by several early adopters.
If you are interested in using HolyTransaction cryptocurrency platform in your project please register at
http://merchant.holytransaction.com/

## Version

0.1

## Requirements

- [HolyTransaction Merchant Account](http://merchant.holytransaction.com/)

## Installation

Automatic installation using [pip](http://pypi.python.org/pypi):

## Usage

```python
from holytransaction import HtApiClient
ht_api = HtApiClient(API_TOKEN)
balances = ht_api.get('balances')
print balances
```

## Examples / Quickstart

This repo includes an example.py file which demonstrates:

* OFAC check

## Methods

More documentation coming soon.

## Changelog

0.1.0

* Initial Release

## Contributing

Feel free to submit issues and pull requests at https://bitbucket.org/noveltylab/ht-client-python/

## Credits

- Andrey Zamovskiy &lt;andrey@noveltylab.com&gt;

## License

(The MIT License)

Copyright (c) 2013 George Sibble &lt;gsibble@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.