from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from . import gateway_list, ingress_list, extra_list

URLS_TYPE = {'all': 0, 'ingress': 1, 'gateway': 2, 'extra': 3}

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates')


@home_bp.route('/', defaults={'urls': 'all'}, methods=["GET"])
def home(urls):
    try:
        return render_template("home.html",
                               data=get_urls(URLS_TYPE.get(urls.lower(), 0)))
    except TemplateNotFound:
        abort(404)


def get_urls(urls_type: int = 0):
    ingress = ingress_list.get_ingress_list()
    gateway = gateway_list.get_gw_list()
    extraurls = extra_list.get_eu_list()
    match urls_type:
        case 1: urls = ingress
        case 2: urls = gateway
        case 3: urls = extraurls
        case _: urls = extraurls + ingress + gateway
    return {'urls': urls,
            'ingress': len(ingress),
            'gateway': len(gateway),
            'extra': len(extraurls),
            }
