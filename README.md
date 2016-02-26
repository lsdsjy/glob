# lblog

A simple blog framework powered by Flask.

## Features
- Markdown support
- Local server to preview

## Sample
http://lsdsjy.github.io/lblog

## Usage

- Run local server

```
python sever.py
```

- Generating static HTML files

```
python generate.py
```

- Edit your configuration in `config.json`

- Put your markdown source files of posts in `posts/` and your customized pages in `pages/`

## Customize

lblog uses Jinja2 for HTML templates.

Put your own HTML templates in `templates/theme_name/` and static files (*.css/*.js) in `static/theme_name/`


## Dependencies
- Python 2.7
- Flask
- Frozen-Flask
- Jinja2
- Werkzeug

## License

WTFPL
