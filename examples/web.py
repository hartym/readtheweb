from flask import Flask, request, render_template
from markdown import markdown

from examples.themacro import Reader
from readtheweb import urlnorm

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    url, title, article = '', '', ''

    if request.method == 'POST':
        url = urlnorm.norms(request.form['url'])
        result = Reader().read(url)
        title = result.buffer[0]['title']
        article = markdown(result.buffer[0]['text'])

    return render_template('read.html.j2', url=url, title=title, article=article, )


if __name__ == "__main__":
    app.run(debug=True)
