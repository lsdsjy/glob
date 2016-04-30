import server
from server import app, posts, pages
from flask_frozen import Freezer

server.url = 'http://lsdsjy.github.io'

freezer = Freezer(app)


@freezer.register_generator
def post():
    for p in posts:
        yield {'url': p}


@freezer.register_generator
def page():
    for p in pages:
        yield {'url': p}

freezer.freeze()
