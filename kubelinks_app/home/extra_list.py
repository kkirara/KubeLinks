import yaml
from dataclasses import dataclass

from kubelinks_app import app


@dataclass
class Extra_URL():
    name: str = None
    url: str = None
    url_name: str = None
    url_type: str = 'ExtraURL'


def get_eu_list():
    list_extraurls = []
    with open("./extraUrls/extraUrls.yaml", "r") as stream:
        try:
            app.logger.debug('ExtraUrls: START')
            data = yaml.load(stream, Loader=yaml.FullLoader)
            if not data:
                return []
            for item in data:
                list_extraurls.append(Extra_URL(
                    name=item['name'],
                    url=item['url'],
                    url_name=item.get('url_name') or item.get('url')))
        except Exception as e:
            app.logger.error(f'ExtraUrls: {e}')
    app.logger.debug('ExtraUrls: FINISH')
    return list_extraurls
