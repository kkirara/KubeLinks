import yaml
from dataclasses import dataclass

from ..log import logger

@dataclass
class Extra_URL():
    name: str = None
    url: str = None
    url_name: str = None

def get_eu_list():

    with open("/app/extraUrls/extraUrls.yaml", "r") as stream:
        list_extraurls = []
        try:
            logger.info('ExtraUrls: START')
            data = yaml.load(stream, Loader=yaml.FullLoader)

            for item in data:
                if 'url_name' not in item or not item['url_name']:
                    url_name=item['url']
                else:
                    url_name=item['url_name']
                list_extraurls.append(Extra_URL(
                    name=item['name'],
                    url=item['url'],
                    url_name=url_name))
        except Exception as e:
            logger.error(f'ExtraUrls: {e}')
        return list_extraurls
