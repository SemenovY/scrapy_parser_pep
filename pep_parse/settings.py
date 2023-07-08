"""
Пропишем константы.
Укажем формат сохранения в FEEDS
Укажем параметры для ITEM_PIPELINES.
"""
from pathlib import Path


BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ALLOWED_DOMAINS = [
    'peps.python.org',
]

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
NUMBER = 'number'
NAME = 'name'
STATUS = 'status'
STATUS_CSV = 'Статус'
COUNT = 'Количество'
SUMMARY = 'Всего'
STATUS_SUMMARY = 'status_summary'
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
