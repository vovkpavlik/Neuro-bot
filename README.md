# Чат-бот для Vk и telegram

Бот получает сообщение от пользователя и отвечает ему, исходя из заданных интрукций. Инструкции ответа берутся с сайта [DialogFlow](https://dialogflow.com). 
[_DialogFlow_](https://dialogflow.com) - это сервис от [google](https://google.com), цель которого заключается в быстром обучении бота с помощью Machine Learning. Самый простой пример - настройка привествия. Если боту приходит сообщение от пользователя `Привет` или `Бонжур`, бот отвечает одной из заранее подготовленных фраз. Все настройки происходят на платформе сервиса - сайте [_DialogFlow_](https://dialogflow.com). Отличие использования такого сервиса от простых списков, с набором ожидаемых сообщений и ответов, в том, что благодаря машинному обучения, бот может игнорировать некоторые грамматические ошибки или опечатки, допущенные пользователем. К примеру на сообщение `првет` бот не отправит ответ `повторите запрос`, а ответит `Здравствуй`.


## Запуск

Для запуска бота у вас уже должен быть установлен __Python 3__ и __telegram__.

###### **Создание канала в telegram**

- В поисковой строке диалогов _telegram_ найдите `BotFather`. Следуйте его инструкциям и получите персональный token а также ваш новый канал.
- В поисковой строке найдите `userinfobot` и, следуя инструкциям, получите id вашего бота.

###### **Создание сообщества в VK**
- Создайте новое сообщество _VK_. 
- В настройках сообщества разрешите отправку сообщений, а также получите ключ, перейдя во вкладку _API разработчикам_.

###### **Создание проекта на DialogFlow**
- Зарегистрийтесь на сайте [_google_](https://google.com).
- Создайте проект на [_DialogFlow_](https://cloud.google.com/dialogflow/docs/quick/setup).
- Создайте агента по [_ссылке_](https://cloud.google.com/dialogflow/docs/quick/build-agent).
- Во вкладке _Intents_ добавьте вопросы и ответы для вашего бота.

###### **Настройка проекта**
- Скачайте код из репозитория github в отдельную папку. Сюда же можно загрузить `.json` файл с инструкциями для бота.
- Установите зависимости командой `pip install -r requirements.txt`.
- Запустите ВК-бота командой `python3 vk_bot.py`, а телеграм-бота - командой `python3 tg_bot.py`. 

###### **Обучение бота**
При необходимости, боту можно добавить новые темы для разговора, не прибегая к платформе сервиса. Для этого:, 
- отредактируйте файл intents.json, соблюдая его структуру. Введите в нем фразы пользователя и ответы от бота.
- отредактированный файл intents.json используется в коде скрипта `create_intents.py`, который создает новые инструкции для бота. Это может быть использовано, если в вашем проекте преобладает большое количество разговоров с пользователем. С помощью такого метода вам не придется вручную добавлять каждую инструкцию для бота.

## Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге проекта и запишите туда данные в таком формате: 
```
VK_TOKEN=Ваш токен с Девмана
TG_TOKEN=Ваш токен полученный от BotFather
TG_CHAT_ID=Chat-id полученный от userinfobot
GOOGLE_PROJECT_ID=id вашего проекта на [_DialogFlow_](https://cloud.google.com/dialogflow/docs/quick/setup)
GOOGLE_APPLICATION_CREDENTIALS=путь к вашему файлу с ключами от DialogFlow
```
