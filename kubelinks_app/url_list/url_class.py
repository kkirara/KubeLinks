from dataclasses import dataclass


@dataclass
class Url():
    name: str = None
    url: str = None
    url_name: str = None
    url_type: str = None
    namespace: str = None

    @property
    def pretty_name(self):
        return (1 if self.url_name.startswith('http') else 0, self.url_name)


@dataclass
class Extra_URL(Url):
    url_type: str = 'ExtraURL'


@dataclass
class Http_Ingress(Url):
    url_type: str = 'ingress'


@dataclass
class Http_Gateway(Url):
    url_type: str = 'gateway'
    is_https: bool = False
    host: str = None
