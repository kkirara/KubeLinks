import json
from kubernetes import client
from types import SimpleNamespace

from kubelinks_app.logger import logger
from kubelinks_app.url_list.url_class import Http_Gateway


HTTPS = ['HTTPS']
HTTP = ["HTTP", "HTTP2"]


def dict2obj(data):
    return json.loads(json.dumps(data),
                      object_hook=lambda d: SimpleNamespace(**d))


def get_port(port, preffix=':'):
    if port.protocol in HTTP and port.number == 80:
        return ''
    elif port.protocol in HTTPS and port.number == 443:
        return ''
    else:
        return f'{preffix}{port.number}'


def get_url(host, port):
    return None if '*' in host else get_url_name(host, port)


def get_url_name(host, port):
    protocol = 'https://' if port.protocol in HTTPS else 'http://'
    host_name = host[host.find("*"):] if '*' in host else host
    return f'{protocol}{host_name}{get_port(port)}'


def removed(list_gw: list[Http_Gateway]):
    https_host = set(x.host for x in list_gw if x.is_https)
    return list(filter(lambda x: x.is_https
                       or not x.is_https
                       and x.host not in https_host, list_gw))


def get_gateway_list(remove_duplicate: bool = True):
    logger.debug('GATEWAY: START')
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
                if port.protocol in HTTP or port.protocol in HTTPS:
                    for host in server.hosts:
                        list_gw.append(Http_Gateway(
                            name=item.metadata.name,
                            url=get_url(host, port),
                            url_name=get_url_name(host, port),
                            is_https=port.protocol in HTTPS,
                            host=host,
                            namespace=item.metadata.namespace))
    except Exception as e:
        logger.error(f'GATEWAY: {e}')
    logger.debug('GATEWAY: FINISH')
    return removed(list_gw) if remove_duplicate else list_gw
