import re


class PoewikiPipeline(object):
    def process_item(self, item, spider):
        item['affixmods'] = re.sub(r'\[\[(((?!\|).)+?)\]\]', r'\1', item['affixmods'])
        item['affixmods'] = re.sub(r'\[\[(.+?)\|.+?\]\]', r'\1', item['affixmods'])
        item['affixmods'] = item['affixmods'].split('<br>')
        if item['hasBasemods']:
            item['basemod'] = re.sub(r'\[\[(((?!\|).)+?)\]\]', r'\1', item['basemod'])
            item['basemod'] = re.sub(r'\[\[(.+?)\|.+?\]\]', r'\1', item['basemod'])
            item['basemod'] = item['basemod'].split('<br>')
        return item
