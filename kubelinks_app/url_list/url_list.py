import re
import copy

from kubelinks_app.logger import logger
from kubelinks_app.config import Config
from kubelinks_app.url_list import gateway_list, ingress_list


def get_urls(urls_type: int = 0, use_filter: bool = False):
    ingress = ingress_list.get_ingress_list()
    gateway = gateway_list.get_gateway_list()
    extraurls = Config.EXTRA_URLS
    if use_filter:
        ingress = filter_urls(ingress, use_filter)
        gateway = filter_urls(gateway, use_filter)

    match urls_type:
        case 1: urls = ingress
        case 2: urls = gateway
        case 3: urls = extraurls
        case _: urls = extraurls + ingress + gateway

    if len(Config.DEFAULT_SORT) > 0:
        logger.debug(f'get_urls: SORT = {Config.DEFAULT_SORT}')
        urls.sort(key=lambda x: [getattr(x, fileld_name)
                  for fileld_name in Config.DEFAULT_SORT])

    return {'urls': urls,
            'ingress': len(ingress),
            'gateway': len(gateway),
            'extra': len(extraurls),
            }


def filter_urls(list_urls, use_filter):
    logger.debug('get_url_filters: START')
    logger.debug(f'get_url_filters: len list_urls = {len(list_urls)}')

    if (not use_filter
        or list_urls == []
            or Config.URL_FILTERS == []):
        return list_urls

    filtered_url = []
    for item in list_urls:
        if item.url is None:
            # filtered_url.append(item)
            continue
        new_item = apply_filter(find_filter(item), item)
        if new_item:
            filtered_url.append(new_item)

    logger.debug(f'get_url_filters: len filtered_url = {len(filtered_url)}')
    logger.debug('get_url_filters: FINISH')
    return filtered_url


def apply_filter(matched_filter, item):

    logger.debug(f'matched_filter = {matched_filter}')
    if matched_filter is None:
        return item

    if matched_filter.get('hide', False):
        # Skip this url
        return None

    new_item = copy.copy(item)
    same_names = new_item.url == new_item.url_name
    if 'replace' in matched_filter.keys():
        new_item.url = re.sub(
            matched_filter["match"], matched_filter["replace"], new_item.url)

    if matched_filter.get('pretty_name', ''):
        new_item.url_name = matched_filter.get('pretty_name', '')
    elif same_names:
        new_item.url_name = new_item.url
    return new_item


def find_filter(item):
    for filter in Config.URL_FILTERS:
        logger.debug(
            f'filter["match"]= {filter["match"]} item.url= {item.url}')
        if re.search(filter["match"], item.url):
            logger.debug(f'filter= {filter}')
            return filter
    return None
