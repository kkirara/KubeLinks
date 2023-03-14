import yaml
from dataclasses import dataclass

from ..log import logger

@dataclass
class Extra_URL():
    name: str = None
    url: str = None

def get_eu_list():

    with open("/app/extraUrls/extraUrls.yaml", "r") as stream:
        list_extraurls = []
        try:
            logger.info('ExtraUrls: START')
            data = yaml.load(stream, Loader=yaml.FullLoader)

            for item in data:
                list_extraurls.append(Extra_URL(
                    name=item['name'],
                    url=item['url']))
        except Exception as e:
            logger.error(f'ExtraUrls: {e}')
        return list_extraurls
