# CompressPhBot

Имя
-----------

Васильев Максим Евгеньевич, 204

О боте
----------

Это достаточно базовый бот, который портит качество фото. Делается это при 
помощи API телеграма и библиотеки pillow. 

Название бота: **@CompressPh_bot**

Запуск бота на сервере.
-----

Мой бот работает на Amazon AWS. Автозапуск работает при помощи Watchtower, происходит подгрузка с приватного репозитория на DockerHub.
Скрипт **docker-compose.yml** лежит в репозитории. Переменные окружения, которые используются в нем, лежат на сервере в файле .env и подгружаются оттуда.
