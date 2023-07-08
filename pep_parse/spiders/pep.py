"""
Парсер должен выводить собранную информацию в два файла .csv.

В первый файл нужно вывести список всех PEP: номер, название и статус.
Второй файл должен содержать сводку по статусам PEP — сколько найдено
документов в каждом статусе (статус, количество). В последней строке этого
файла в колонке «Статус» должно стоять слово Total,
а в колонке «Количество» — общее количество всех документов.
"""
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, NAME, NUMBER, STATUS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Находим все ссылки на документы PEP."""
        section = response.xpath('//section[@id="numerical-index"]')
        pep_list = section.xpath('.//a[@class="pep reference internal"]/@href')
        for pep_link in pep_list:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает информацию со страницы PEP."""
        h1 = response.css('#pep-content > h1::text').get().split()
        number = h1[1]
        name = ' '.join(h1[3:])
        status = response.css('abbr::text').get()
        data = {
            NUMBER: number,
            NAME: name,
            STATUS: status,
        }
        yield PepParseItem(data)


# kaonashi
# =^..^=______/
