# TableService

## TableService - это web-приложение на Flask.

Приложение работает на Flask, PostgreSql, Celery.  

Данное приложение получает данные из таблицы при помощи Google API, сделанного в Google Sheets.  

Учитывается удаление, добавление и изменение строк в Google Sheets. 

Для перевода долларов в рубли берутся данные по курсу ЦБ РФ.  

Осуществляется проверка соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.  

Скрипты использующийся для работы приложения, работают автоматически используя планировщик задач Celery.  

![Главная страница](docs/1.jpg)
![Пример таблицы](docs/2.jpg)


# Сборка репозитория и локальный запуск

## Запуск приложения на ОС Linux:
Выполните в консоли:

git clone https://github.com/Straigan/webapp_kanal_service.git  
docker-compose up  

# Настройка

Для работы с Google Sheets, через Google API. Не обходимо создать в папке webapp credentials.json с помощью Apis & Services.
Не обходимо присвоить значения переменным в config файле через env в файле .env.

FLASK_APP='webapp'  
DATABASE_URL='postgresql://flaskuser:flaskpassword@postgres:5432/flaskdb'  
SECRET_KEY - секретный ключ для авторизации в Гугл Аутентификаторе  
SCOPES - область действия для API Google (https://www.googleapis.com/auth/spreadsheets.readonly)  
SAMPLE_SPREADSHEET_ID - ID таблицы  
SAMPLE_RANGE_NAME - область захвата данных таблицы  
CELERY_BROKER_URL='redis://redis:6379/0'  
CELERY_RESULT_BACKEND='redis://redis:6379/0' 
TOKEN_TELEGRAM - токен телеграм бота  
CHAT_ID_TELEGRAM - ID чата  

Данные для подключения к БД указаны в 'docker/.env-postgresql'.  
