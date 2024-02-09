from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from kubelinks_app.url_list.url_list import get_urls
from kubelinks_app.config import Config

URLS_TYPE = {'all': 0, 'ingress': 1, 'gateway': 2, 'extra': 3}


home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates')


@home_bp.route('/', defaults={'urls': 'all'}, methods=["GET"])
@home_bp.route('/home', defaults={'urls': 'all'}, methods=["GET"])
def home(urls):
    return get_page(urls)


@home_bp.route('/raw_data', defaults={'urls': 'all'}, methods=["GET"])
def raw_data(urls):
    return get_page(urls, use_filter=False)


def get_page(urls, use_filter: bool = True):
    try:
        return render_template("home.html",
                               title=Config.TITLE,
                               enabled_namespace=Config.ENABLED_NAMESPACE,
                               data=get_urls(URLS_TYPE.get(urls.lower(), 0), use_filter))
    except TemplateNotFound:
        abort(404)
