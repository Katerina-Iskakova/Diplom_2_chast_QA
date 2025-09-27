# DIPLOM_2_chast_QA_Katerina_Iskakova_34_kogorta - Яндекс Самокат

Проект для тестирования API Яндекс Самокат с помощью автоматизированного теста.

## Описание

Этот проект содержит тест для проверки функциональности API Яндекс Самокаь, включая:
- Создание заказа
- Получение заказа по треку
- Проверку документации API

## Структура проекта

```
Diplom_2_chast_QA/
├── configuration.py      # Конфигурация URL и путей API
├── data.py              # Тестовые данные для заказов
├── sender_stand_request.py  # Функции для работы с API
├── create_order_test.py # Основной тест создания и получения заказа
└── README.md           # Документация проекта
```

## Файлы проекта

### configuration.py
Содержит конфигурационные данные:
- `URL_SERVICE` - базовый URL сервиса
- `DOC_PATH` - путь к документации API
- `CREATE_ORDER_PATH` - путь для создания заказа
- `GET_ORDER_PATH` - путь для получения заказа по треку

### data.py
Содержит тестовые данные для создания заказа:
- Имя и фамилия клиента
- Адрес доставки
- Станция метро
- Телефон
- Время аренды
- Дата доставки
- Комментарий
- Цвет самоката

### sender_stand_request.py
Содержит функции для работы с API:
- `get_docs()` - получение документации API
- `create_order(order_body)` - создание заказа
- `get_order_by_track(track)` - получение заказа по треку

### create_order_test.py
Основной тест, который:
1. Создает заказ через API
2. Проверяет успешность создания (статус код 201)
3. Получает номер трека заказа
4. Запрашивает данные заказа по треку
5. Проверяет успешность получения (статус код 200)

## Установка зависимостей

Для работы проекта необходимо установить следующие пакеты:

```bash
pip install requests
pip install pytest
```

## Запуск тестов

### Запуск основного теста
```bash
python create_order_test.py
```

### Запуск всех тестов с pytest
```bash
pytest
```

## Пример использования

```python
import sender_stand_request
import data

# Создание заказа
response = sender_stand_request.create_order(data.order_body)
print(f"Статус код: {response.status_code}")

# Получение трека
track = response.json()["track"]

# Получение заказа по треку
order_response = sender_stand_request.get_order_by_track(track)
print(f"Данные заказа: {order_response.json()}")
```

## API Endpoints

- **GET** `/docs/` - Документация API
- **POST** `/api/v1/orders` - Создание заказа
- **GET** `/api/v1/orders/track?t={track}` - Получение заказа по треку

## Требования

- Python 3.6+
- requests
- pytest (для запуска тестов)

## Статус коды

- `200` - Успешное получение данных
- `201` - Успешное создание заказа
- `404` - Ресурс не найден
- `400` - Некорректный запрос