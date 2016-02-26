import server
from server import fetch, app, posts, pages
from flask_frozen import Freezer

fetch('posts')
fetch('pages')

server.url = 'http://lsdsjy.github.io'

freezer = Freezer(app)


@freezer.register_generator
def post():
    for p in posts:
        yield {'post_url': p}


@freezer.register_generator
def page():
    for p in pages:
        yield {'post_url': p}

freezer.freeze()
