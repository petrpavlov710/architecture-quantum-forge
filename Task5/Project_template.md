# Запуск и демонстрация работы бота

#### Запуск проекта

Все команды необходимо выполнять из корневой директории проекта.

Запуск LLM Mistral локально

```bash
docker compose -f app/docker-compose.yml up -d
```

Добавление в индекс приватных данных

```bash
python -m app.scripts.add_secret_document
```

Запуск FastAPI приложения

```bash
python -m app.main
```

Запуск скрипта, который отправляет 5 хороших и 5 плохих запросов с включенной защитой

```bash
python -m app.queries_cycle
```

#### Индексирование knowledge_base

Проиндексированная база должна была быть создана в предыдущих заданиях. Если ее нет, файлы будут созданы при запуске приложения.

## Работа бота без защиты данных

![screenshot](screenshots/без-защиты.png)

## Работа бота с защитой данных

![Скриншот 1](screenshots/1.png)
![Скриншот 2](screenshots/2.png)
![Скриншот 3](screenshots/3.png)
![Скриншот 4](screenshots/4.png)
![Скриншот 5](screenshots/5.png)
![Скриншот 6](screenshots/6.png)
![Скриншот 7](screenshots/7.png)
![Скриншот 8](screenshots/8.png)
![Скриншот 9](screenshots/9.png)
![Скриншот 10](screenshots/10.png)
