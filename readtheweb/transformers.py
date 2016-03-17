# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

from html2text import html2text
from rdc.etl.transform import Transform
from readability import Document

from readtheweb.utils import resolve_future


class SimpleHtmlTransformer(Transform):
    def transform(self, row, chan):
        row['response'] = resolve_future(row['response'])

        doc = Document(row['response'].content)

        row['title'] = doc.title()
        summary = doc.summary()
        row['text'] = html2text(summary, bodywidth=160).replace('****', '').strip()

        yield row