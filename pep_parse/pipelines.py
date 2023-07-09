"""
Файлы со списком PEP должны быть именованы по маске pep_ДатаВремя.csv,
например — pep_2029-01-31T23-55-00.csv.
В файле должно быть три столбца:
«Номер», «Название» и «Статус».
Сохранение должно выполняться посредством Feeds, настройки в settings.py.
Файлы со сводкой по статусам должны быть именованы по маске
status_summary_ДатаВремя.csv, например — status_summary_2029-01-31_23-55-00.csv
Создавать этот файл нужно через Pipeline.
  В файле должно быть два столбца: «Статус» и «Количество».
  Дополнительно в pipeline посчитано общее количество документов PEP,
  в последней строке со сводкой в столбце «Статус» написан “Total”,
  а в столбце «Количество» выведено общее количество полученных документов PEP.
  Вывод данных через класс csv.DictWriter()
"""
import csv
import datetime
from collections import defaultdict

from pep_parse.settings import (
    BASE_DIR, COUNT, DT_FORMAT, RESULTS, STATUS, STATUS_CSV, STATUS_SUMMARY,
    SUMMARY
)


class PepParsePipeline:
    """
    Пропишем инициализатор пути.
    При открытии паук создаст defaultdict словарь
    В процессе будем заполнять словарик
    При закрытии сохраним в файлы csv.
    """

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """При запуске паука создается словарь со статусами PEP."""
        self.count_pep_status = defaultdict(int)

    def process_item(self, item, spider):
        """
        В процессе переборки item добавляем статусы pep в словарь,
        и считаем их количество.
        """
        self.count_pep_status[item.get(STATUS)] += 1
        return item

    def close_spider(self, spider):
        """
        При закрытии паука задаем формат вывод данных.
        Сохраняем результаты в CSV файл.
        """

        date_time = datetime.datetime.utcnow().strftime(DT_FORMAT)
        filename = f'{STATUS_SUMMARY}_{date_time}.csv'
        fieldnames = [STATUS_CSV, COUNT]

        with open(
                f'{self.results_dir}/{filename}', 'w', newline=''
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in self.count_pep_status.items():
                writer.writerow({STATUS_CSV: status, COUNT: count})
            total_count = sum(self.count_pep_status.values())
            writer.writerow({STATUS_CSV: SUMMARY, COUNT: total_count})
