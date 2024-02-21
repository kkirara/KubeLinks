import yaml

from kubelinks_app.logger import logger
from kubelinks_app.url_list.url_class import Extra_URL


def get_extraurls_list():
    list_extraurls = []
    with open("./extraConfigs/extraUrls.yaml", "r") as stream:
        try:
            logger.debug('ExtraUrls: START')
            data = yaml.load(stream, Loader=yaml.FullLoader)
            if not data:
                return []
            for item in data:
                list_extraurls.append(Extra_URL(
                    name=item['name'],
                    url=item['url'],
                    url_name=item.get('url_name') or item.get('url')
                ))
        except Exception as e:
            logger.error(f'ExtraUrls: {e}')
    logger.debug('ExtraUrls: FINISH')
    return list_extraurls


def get_url_filters():
    list_url_filters = []
    with open("./extraConfigs/urlFilters.yaml", "r") as data:
        try:
            logger.debug('get_url_filters: START')
            list_url_filters = yaml.load(data, Loader=yaml.FullLoader)
            if not list_url_filters:
                return []
        except Exception as e:
            logger.error(f'get_url_filters: {e}')
    logger.debug('get_url_filters: FINISH')
    return list_url_filters
