# Sait-Katalog

## Информация о разработчиках

1. Старкова Дарья - DashaStark
2. Фролов Александр - afteraf
3. Печинкин Александр - Alexander  Pechinkin04
4. Уланов Алексей - Pilot2281

## Технологии

- Python 3.9.6
- Django 4.2.19
- PostgreSQL 17

## Установка и запуск локально

### 1. Клонируй репозиторий

### 2. Создай и активируй виртуальное окружение

#### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Windows
```powershell
python3 -m venv venv
venv/Scripts/activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Создание БД

#### Подкючение к серверу
```
psql -U postgres
```

#### Создание
```sql
CREATE DATABASE your_db_name;
\q
```

### 5. Настройка конфига

#### В restaurant/restaurant/settings.py добавляем пользователя БД

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_password",
        "HOST": "localhost",   # или IP, если база на другом сервере
        "PORT": "5432",        # стандартный порт PostgreSQL
    }
}
```

### 6. Выполни миграции

```python
python manage.py makemigrations
python manage.py migrate
```

### 7. Запусти сервер

```python
python manage.py runserver
```






