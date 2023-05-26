import yaml
from dataclasses import dataclass

from ..log import logger


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
            logger.info('ExtraUrls: START')
            data = yaml.load(stream, Loader=yaml.FullLoader)

            for item in data:
                list_extraurls.append(Extra_URL(
                    name=item['name'],
                    url=item['url'],
                    url_name=item.get('url_name') or item.get('url')))
        except Exception as e:
            logger.error(f'ExtraUrls: {e}')
    return list_extraurls
