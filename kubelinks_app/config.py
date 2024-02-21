import os
from kubelinks_app.url_list import extra_list
SET_SORT_FIELD = ('name', 'url', 'url_name', 'url_type',
                  'namespace', 'pretty_name')


class Config(object):
    DEBUG = True
    TESTING = True
    TITLE = os.getenv('KUBELINKS_TITLE', 'Ingress and Istio urls')
    ENABLED_NAMESPACE = bool(int(os.getenv('KUBELINKS_ENABLED_NAMESPACE', 0)))
    BASE_PATH = os.getenv('KUBELINKS_BASE_PATH', '')
    DEFAULT_SORT = [item.strip() for item in os.getenv(
        'KUBELINKS_DEFAULT_SORT', '').lower().split(',') if item.strip() in SET_SORT_FIELD]
    HEALTHZ = {
        "live": lambda: None,
        "ready": lambda: None,
    }
    URL_FILTERS = extra_list.get_url_filters()
    EXTRA_URLS = extra_list.get_extraurls_list()


class ProdactionConfig(Config):
    DEBUG = False
    TESTING = False
