import scrapy
from wiki_scrapper.items import PoewikiItem
from scrapy import Selector


class UniqueItems(scrapy.Spider):
    name = 'uniqueitems'
    start_urls = [
         'https://pathofexile.gamepedia.com/List_of_unique_claws',
         'https://pathofexile.gamepedia.com/List_of_unique_axes',
         'https://pathofexile.gamepedia.com/List_of_unique_bows',
         'https://pathofexile.gamepedia.com/List_of_unique_rings'
         'https://pathofexile.gamepedia.com/List_of_unique_accessories',
         'https://pathofexile.gamepedia.com/List_of_unique_flasks',
         'https://pathofexile.gamepedia.com/List_of_unique_jewels',
         'https://pathofexile.gamepedia.com/List_of_unique_maps',
         'https://pathofexile.gamepedia.com/List_of_unique_body_armours',
         'https://pathofexile.gamepedia.com/List_of_unique_boots',
         'https://pathofexile.gamepedia.com/List_of_unique_gloves',
         'https://pathofexile.gamepedia.com/List_of_unique_helmets',
         'https://pathofexile.gamepedia.com/List_of_unique_shields',
         'https://pathofexile.gamepedia.com/List_of_unique_daggers',
         'https://pathofexile.gamepedia.com/List_of_unique_maces',
         'https://pathofexile.gamepedia.com/List_of_unique_staves',
         'https://pathofexile.gamepedia.com/List_of_unique_swords',
         'https://pathofexile.gamepedia.com/List_of_unique_wands',
    ]

    def parse(self, response):
        sel = Selector(response)
        items = sel.xpath('//table[@class="wikitable sortable item-table"]//tr')
        itemlist = []
        for item in items:
            mods = item.xpath('./td[last()]/@data-sort-value').extract_first()
            unique_item = PoewikiItem()
            if mods:
                mods = mods.split("<span class=\"item-stat-separator -unique\"></span>")
                modslength = len(mods)
                unique_item['name'] = item.xpath('.//span[@class="c-item-hoverbox__activator"]/a[1]/text()').extract_first()
                unique_item['hasBasemods'] = False
                unique_item['itemimage'] = item.xpath('.//span[@class="c-item-hoverbox__display"]/img/@src').extract_first()
                if modslength >= 2:
                    unique_item['basemod'] = mods[0]
                    unique_item['hasBasemods'] = True
                unique_item['affixmods'] = mods[modslength - 1]
                itemlist.append(unique_item)
        return itemlist
