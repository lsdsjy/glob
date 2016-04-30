from flask import Flask, render_template
import json
import markdown2
import os

app = Flask(__name__)

fp = open("config.json", "r")
data = json.loads("".join(map(lambda x: x.translate(None, "\n"), fp.readlines())))
fp.close()

title = data["title"]
author = data["author"]
email = data["email"]
theme = data["theme"]
# url = data["url"]
url = "http://127.0.0.1:5000"  # Local Server Mode

posts = {}
pages = {}


def fetch(dr):
    files = os.listdir("source/%s/" % dr)
    for src in files:
        fp = open("source/%s/%s" % (dr, src), "r")
        lines = [item.decode("utf-8") for item in fp.readlines()]
        fp.close()

        src = src.rpartition(".")[0]
        post_title = lines[0]
        post_date = lines[1]
        text = "".join(lines[3:])
        excerpt = text[:text.find("<!-- more -->")]
        text = markdown2.markdown(text)
        excerpt = markdown2.markdown(excerpt)
        excerpt += "<p><a href=\"posts/" + src + ".html\">READ MORE-></a></p>"

        if (dr == "posts"):
            posts[src] = (src, post_title, post_date,
                          text, excerpt)
        else:
            pages[src] = (src, post_title, post_date,
                          text, excerpt)


@app.route("/")
def index():
    return render_template(theme + "/index.html", url=url,
                           title=title, theme=theme, author=author,
                           posts=posts.values())


@app.route("/posts/<post_url>.html")
def post(post_url, is_post=True):
    p = posts[post_url] if is_post else pages[post_url]
    return render_template(theme + "/post.html", url=url,
                           title=title, theme=theme, author=author,
                           text=p[3], post_title=p[1],
                           post_date=p[2])


@app.route("/<post_url>.html")
def page(post_url):
    return post(post_url, False)


if __name__ == "__main__":
    fetch("posts")
    fetch("pages")
    print posts
    app.run(debug=True)
