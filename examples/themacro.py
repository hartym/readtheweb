from rdc.etl.transform import Transform

import readtheweb
from readtheweb.downloaders import RequestsDownloader
from readtheweb.transformers import SimpleHtmlTransformer


class SizeLogger(Transform):
    def transform(self, row, chan):
        total_size = 0
        for k in 'title', 'text',:
            print(k, len(row[k]), ' ')
            total_size += len(row[k])
        print('total size:', total_size, ' ')
        yield row


class Reader(readtheweb.Reader):
    @property
    def cleaners(self):
        return [SizeLogger()]


if __name__ == '__main__':
    reader = Reader()
    for k, v in reader.read('http://www.themacro.com/articles/2016/03/advice-for-startup-nonprofits/').buffer[0].items():
        print()
        print(k)
        print('=' * len(k))
        print(v)
