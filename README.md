# RA
Тут написано, как я выполняла работу.

### Произвести запуск продукта

1)Чтобы произвести запуск продукта нам потребуется командная трока или терминал, где мы сможет запустить файл run-nifi.bat

2)Изнаально требуется установить компилятор jdk для запуска в командной строке в windows, так как в MACе зачастую уже имеется js и ldk.

3)Запускаем файл и ищем http host 127.0.0.1 и https port 8443

4)Вводим домен, затем в получившейся сьранице пароль и заходим в NIFI APACHE.

### Подробно изучить интерфейс продукта. (Понять назначение основных элементов)

Интерфейс состоит из панели инструментов(Processor для операций с данными, порты, Process Group - объединение процессоров и других групповых процессоров).Status Bar, где находится вся краткая статистика о работе,

### Изучить функционал.

Создаем группу с помощью Process Group, заходим в группу, где у нас есть поле для работы.
Чтобы работать с проектом добавим определенный процессор для рабооты или из предложеных слева на панели или в типах. Создаем нужный нам тип, опять проваливаемся в проект и с помощью настроек изменяем имя проекта и насраиваем характеристики.


<img width="758" alt="Снимок экрана 2024-02-21 в 00 51 46" src="https://github.com/arlinrus/RA/assets/111064731/5384802f-73fe-485c-9ac7-2b6f099c9b81">


Далее можно создать 2 процессор и соединить с первым :


<img width="442" alt="Снимок экрана 2024-02-21 в 00 57 12" src="https://github.com/arlinrus/RA/assets/111064731/f4ae0046-dcd5-4ccc-9e4a-2e5d61bcc63f">

У нас появилась очередь, которая показывает колво сгенерированных значений, чтобы очистить и запустить след необходимо очистить её.

<img width="979" alt="Снимок экрана 2024-02-21 в 01 08 16" src="https://github.com/arlinrus/RA/assets/111064731/e4ff6117-b4f7-4282-a288-691bee515b5e">



### Что происзодит а каждом этапе выполнения потока?

В комментариях описала процесс

![Снимок экрана (41)](https://github.com/arlinrus/RA/assets/111064731/35c4e843-080f-4113-9696-9618b76b8cfc)










