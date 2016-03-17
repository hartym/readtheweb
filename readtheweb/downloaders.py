# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache
from cachecontrol.heuristics import OneDayCache

from rdc.etl import H
from rdc.etl.transform import Transform


class RequestsDownloader(Transform):
    def transform(self, row, chan):
        yield H(('response', session.get(row['url'], headers=headers)))


session = CacheControl(
    requests.Session(),
    cache=FileCache('.http_cache'),
    heuristic=OneDayCache(),
)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}