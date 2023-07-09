"""
Парсер должен выводить собранную информацию в два файла .csv.

В первый файл нужно вывести список всех PEP: номер, название и статус.
Второй файл должен содержать сводку по статусам PEP — сколько найдено
документов в каждом статусе (статус, количество). В последней строке этого
файла в колонке «Статус» должно стоять слово Total,
а в колонке «Количество» — общее количество всех документов.
"""
import re
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
        content = response.xpath('//*[@id="pep-content"]')
        pep_content = content.css('h1::text').get()
        pattern_content = r'PEP (?P<number>\d+) – (?P<name>.*)'
        h1_text_match = re.search(pattern_content, pep_content)

        data = {
            NUMBER: int(h1_text_match.group('number')),
            NAME: h1_text_match.group('name'),
            STATUS: content.css('dl dd abbr::text').get(),
        }
        yield PepParseItem(data)


# kaonashi
# =^..^=______/
