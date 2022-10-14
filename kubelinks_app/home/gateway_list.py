import json
from dataclasses import dataclass

from ..log import logger
from kubernetes import client


@dataclass
class Http_Gateway():
    metadata_name: str = None
    host: str = None
    port: str = None
    is_https: bool = False
    link: str = None
    host_name: str = None


class obj(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)


def dict2obj(d):
    return json.loads(json.dumps(d), object_hook=obj)


def get_port(port, preffix=':'):
    if port.protocol == "HTTP" and port.number == 80:
        return ''
    elif port.protocol == "HTTPS" and port.number == 443:
        return ''
    else:
        return f'{preffix}{port.number}'


def get_link(host, port):
    if '*' in host:
        return None
    else:
        return get_name(host, port)


def get_name(host, port):
    protocol = port.protocol.lower()
    host_name = host[host.find("*"):] if '*' in host else host
    return f'{protocol}://{host_name}{get_port(port)}'


def removed(list_gw):
    https_host = set()
    http_host = set()
    for x in list_gw:
        if not x.is_https:
            http_host.add(x.host)
        else:
            https_host.add(x.host)
    http_host &= https_host
    return filter(lambda x: x.is_https
                  or not x.is_https and x.host not in http_host, list_gw)


def get_gw_list(remove_duplicate: bool = True):
    logger.info('GATEWAY: START')
    list_gw = []
    try:
        gateways = dict2obj(client.CustomObjectsApi()
                            .list_cluster_custom_object(
                                group="networking.istio.io",
                                version="v1beta1",
                                plural="gateways"))
        for item in gateways.items:
            for server in item.spec.servers:
                port = server.port
                if port.protocol in ('HTTP', 'HTTPS'):
                    for host in server.hosts:
                        link = get_link(host, port)
                        host_name = get_name(host, port)
                        list_gw.append(Http_Gateway(
                            item.metadata.name,
                            host, port.number,
                            port.protocol == 'HTTPS',
                            link, host_name))
    except Exception as e:
        logger.error(f'GATEWAY: {e}')
    logger.info('GATEWAY: FINISH')
    return removed(list_gw) if remove_duplicate else list_gw
