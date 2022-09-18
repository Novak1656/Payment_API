# Payment_API - https://payment-system-api-v1.herokuapp.com/item/1

## Запуск проекта
1. Установите virtualenv для создания виртуальной среды
```
pip install virtualenv
```

2. Создайте virtualenv и активируйте его
```
> virtualenv env
> env/source/activate
(env)>
```

3. Выполните следующие команды
```
pip install django django-rest-framework python-decouple stripe
```

4. В корневой папке проекта создайте файл .env и укажите в нём следующие параметры
```
SECRET_KEY='YOUR_DJANGO_SECRET_KEY'
STRIPE_PUBLIC_KEY='YOUR_STRIPE_API_PUBLIC_KEY'
STRIPE_SECRET_KEY='YOUR_STRIPE_API_SECRET_KEY'
```

5. Создайте и выполните миграции
```
cd payment_system
python manage.py makemigrations
python manage.py migrate
```

6. Создайте суперпользователя
```
python manage.py createsuperuser
```

7. Запустите локальный сервер
```
python manage.py runserver
```

## Руководство пользователя
Так как данный проект был разработан в рамках тестового задания все действия с моделями базы данных производятся в админке (http://127.0.0.1:8000/admin/)
Перед использованием проекта создайте пару записей в каждой из 3 моделей БД приложения.

### APP URLS
1. http://127.0.0.1:8000/item/{id} - Возвращает шаблон с информацией о предмете и кнопку для совершения покупки
2. http://127.0.0.1:8000/buy/item/{id} - Возвращает Stripe Session Id
3. http://127.0.0.1:8000/order/{order_id} - Возвращает шаблон с информацией о каждом предмете в заказе и кнопку для совершения покупки
4. http://127.0.0.1:8000/buy/order/{order_id} - Возвращает Stripe Session Id
