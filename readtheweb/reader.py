# coding: utf-8

from rdc.etl import H
from rdc.etl.extra.util import TransformBuilder
from rdc.etl.job import Job
from rdc.etl.status.console import ConsoleStatus
from rdc.etl.transform import Transform
from rdc.etl.transform.extract import Extract

from readtheweb.downloaders import RequestsDownloader
from readtheweb.transformers import SimpleHtmlTransformer


class Buffer(Transform):
    def __init__(self):
        super(Buffer, self).__init__()
        self.buffer = []

    def transform(self, row, ch):
        self.buffer.append(row)
        yield row


class Reader:
    extractors = []

    @property
    def downloaders(self):
        return [RequestsDownloader()]

    @property
    def transformers(self):
        return [SimpleHtmlTransformer()]

    cleaners = []

    def build_job(self, extractors=None, downloaders=None, transformers=None, cleaners=None):
        buffer = Buffer()
        job = Job()
        job.add_chain(
            *(
                list(extractors or self.extractors) + list(downloaders or self.downloaders) + list(
                    transformers or self.transformers) + list(cleaners or self.cleaners) + [buffer]
            )
        )
        return job, buffer

    def read(self, *urls):
        @TransformBuilder(Extract)
        def UrlExtractor():
            for url in urls:
                yield H(('url', url))

        job, buffer = self.build_job(extractors=[UrlExtractor()])
        job()

        return buffer.buffer
