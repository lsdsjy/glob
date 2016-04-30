from flask import Flask, render_template, url_for
import json
import markdown2
import os

app = Flask(__name__)

with open("config.json", "r") as fp:
    site = json.loads("".join(map(lambda x: x.translate(None, "\n"), fp.readlines())))

site["url"] = "http://127.0.0.1:5000"  # Local Server Mode

posts = {}
pages = {}


def fetch(dr):
    files = os.listdir("source/%s/" % dr)
    result = {}
    for src in files:
        with open("source/%s/%s" % (dr, src), "r") as fp:
            lines = [item.decode("utf-8") for item in fp.readlines()]

        src = src.rpartition(".")[0]
        title = lines[0]
        date = lines[1]
        text = "".join(lines[3:])
        excerpt = text[:text.find("<!-- more -->")]
        text = markdown2.markdown(text)
        excerpt = markdown2.markdown(excerpt)
        excerpt += "<p><a href=\"posts/" + src + ".html\">READ MORE-></a></p>"

        result[src] = ({"src": src, "title": title, "date": date,
                       "text": text, "excerpt": excerpt})

    return result


@app.route("/")
def index():
    return render_template(site["theme"] + "/index.html", site=site, posts=posts)


@app.route("/posts/<url>.html")
def post(url):
    return render_template(site["theme"] + "/post.html", site=site, post=posts[url.encode("ascii", "ignore")])


@app.route("/<url>.html")
def page(url):
    return post(url)


if __name__ == "__main__":
    posts = fetch("posts")
    pages = fetch("pages")
    #with app.test_request_context():
    #    print url_for('static', filename="index.html")
    app.run(debug=True)
