## Установка
Используемая версия python - 3.10.5.
1. Создать виртуальное окружение `python -m venv venv`.
2. Выполнить `pip install -r requirements.txt`.
3. Скачать [архив](https://drive.google.com/file/d/1TWnthKO1Ui1j0PmstlJl7B3UMHSe27p0/view?usp=sharing) с нашей моделью и распаковать его в директорию `model/`.
4. Файл `.env.example` переименовать в `.env`.
5. Установить [PostgreSQL 16.6](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads), если не установлен, и запустить.
6. Открыть `.env` и заполнить поля связанные с базой данных.
7. Запустить `db_handler.py` для создания необходимых таблиц.
8. Запустить `app.py` 