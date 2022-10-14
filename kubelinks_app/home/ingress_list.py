from dataclasses import dataclass, field

from ..log import logger
from kubernetes import client


@dataclass
class Http_Ingress():
    metadata_name: str = None
    host: str = None
    path: str = None
    https: bool = False
    link: str = field(init=False)
    host_name: str = field(init=False)

    def __post_init__(self):
        http = 'https://' if self.https else 'http://'
        host = self.host if self.host else '*'
        self.host_name = f"{http}{host}{self.path}"
        if not (self.host) or self.host.startswith('*'):
            self.link = None
        else:
            self.link = self.host_name


def get_ingress_list():
    logger.info('INGRESS: START')
    list_ingress = []
    try:
        v1 = client.NetworkingV1Api()
        ret = v1.list_ingress_for_all_namespaces()
        logger.info(f'INGRESS: ingress items - {len(ret.items)}')
        for item in ret.items:
            if item.spec.tls is not None:
                tls_hosts = [
                    host for tls in item.spec.tls for host in tls.hosts]
            else:
                tls_hosts = []
            for rule in item.spec.rules:
                for p in rule.http.paths:
                    list_ingress.append(Http_Ingress(
                        metadata_name=item.metadata.name,
                        host=rule.host,
                        path=p.path,
                        https=rule.host in tls_hosts))
    except Exception as e:
        logger.error(f'INGRESS: {e}')
    logger.info(f'INGRESS: FINISH - {len(list_ingress)}')
    return list_ingress
