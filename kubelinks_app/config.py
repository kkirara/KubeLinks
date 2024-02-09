import os
from kubelinks_app.url_list import extra_list


class Config(object):
    DEBUG = True
    TESTING = True
    TITLE = os.getenv('KUBELINKS_TITLE', 'Ingress and Istio urls')
    ENABLED_NAMESPACE = bool(int(os.getenv('KUBELINKS_ENABLED_NAMESPACE', 0)))
    HEALTHZ = {
        "live": lambda: None,
        "ready": lambda: None,
    }
    URL_FILTERS = extra_list.get_url_filters()
    EXTRA_URLS = extra_list.get_extraurls_list()


class ProdactionConfig(Config):
    DEBUG = False
    TESTING = False
