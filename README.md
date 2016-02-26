# lblog

A simple blog framework powered by Flask.

## Features

- Markdown support

- Local server to preview

- Deploy to Github Pages (coming soon)

## Sample
http://lsdsjy.github.io/lblog

## Usage

- Edit your configuration in `config.json`

- Put your markdown source files of posts in `posts/` and your customized pages in `pages/`

A markdown source file example:
  
```
The First Passage
2016-02-26
---
Hello World!
```

The first line is the title of the *passage* and the second is *date*. There should be a *seperating line* followed by the *text*.

- Run local server at `http://localhost:5000/` or `http://127.0.0.1:5000/`

```
python sever.py
```

- Generating static HTML files

```
python generate.py
```

- Upload static files to your site

## Customize

lblog uses Jinja2 for HTML templates.

Put your own HTML templates in `templates/theme_name/` and static files (`.css/.js`) in `static/theme_name/`

## Dependencies
- Python 2.7
- Flask
- Frozen-Flask
- Jinja2
- Werkzeug

## License

WTFPL
