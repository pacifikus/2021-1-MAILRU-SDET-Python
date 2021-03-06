## Homework 5

Cкрипты на bash и python для анализа готового access.log

### Bash-скрипт

У скрипта 2 параметра:
- файл с логами
- тип запроса для подсчета количества запросов по конретному типу (POST, GET, etc) 

Пример запуска из терминала:

```
bash script.sh access.log
```

### Python-скрипт


Параметры:
- **path** - путь до файла с логами
- **total** - подсчет общего числа запросов
- **by-type** - подсчет числа запросов по типам (GET, POST, etc)
- **top10** - подсчет 10 самых частых запросов
- **top4xx** - подсчет 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой
- **top5xx** - подсчет 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
- **json** - сохранение в json

Пример запуска из терминала:

```
python script.py access.log --total --by-type --top10 --top4xx --top5xx
```