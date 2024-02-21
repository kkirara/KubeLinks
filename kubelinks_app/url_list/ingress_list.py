from kubernetes import client

from kubelinks_app.logger import logger
from kubelinks_app.url_list.url_class import Http_Ingress


def get_url_name(is_https: bool, host, path):
    http = 'https://' if is_https else 'http://'
    return f"{http}{host or '*'}{path}"


def get_url(is_https: bool, host, path):
    if not (host) or host.startswith('*'):
        return None
    else:
        return get_url_name(is_https, host, path)


def get_ingress_list():
    logger.debug('INGRESS: START')
    list_ingress = []
    try:
        v1 = client.NetworkingV1Api()
        ret = v1.list_ingress_for_all_namespaces()
        logger.debug(f'INGRESS: ingress items - {len(ret.items)}')
        for item in ret.items:
            if item.spec.tls:
                tls_hosts = [host for tls in item.spec.tls
                             for host in tls.hosts]
            else:
                tls_hosts = []
            for rule in item.spec.rules:
                for p in rule.http.paths:
                    is_https = rule.host in tls_hosts
                    list_ingress.append(Http_Ingress(
                        name=item.metadata.name,
                        url=get_url(is_https, rule.host, p.path),
                        url_name=get_url_name(is_https, rule.host, p.path),
                        namespace=item.metadata.namespace))
    except Exception as e:
        logger.error(f'INGRESS: {e}')
    logger.debug(f'INGRESS: FINISH - {len(list_ingress)}')
    return list_ingress
