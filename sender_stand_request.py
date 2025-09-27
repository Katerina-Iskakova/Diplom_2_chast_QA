import configuration

import requests

import data 

# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Функция для создания заказа
def create_order(order_body):
    # Выполняем POST-запрос к URL для создания заказа
    # Передаем данные заказа в теле запроса в формате JSON
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)

# Функция для получения заказа по треку
def get_order_by_track(track):
    # Выполняем GET-запрос к URL для получения заказа по треку
    # Трек передается как параметр запроса
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))

# Вызываем функцию get_docs и сохраняем результат в переменную response
response = get_docs()

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
print(response.status_code)