# QA-API_Service

#### При запуске локального сервера в консоли выводится тякущее дерево сервиса. Отображающее все уровни вложенности 

##### На данный момент API предоставляет 2 способа взаимодействия:

 * GET-запрос к адресу */scheme*  
 Предоставляет список всех возможных схем вопросно-ответной сессии  
  
 * POST-запрос к корневому адресу */*  
 **Обязательный параметр:** номер выбранного ответа  
 Например: 127.0.0.1/1 - продвинет Вас дальше по сессии в пункт 1  
  
##### Методы в разработке:  
  
 * POST-запрос к адресу */back_n*  
 **Обязательный параметр:** *n* - кол-во шагов   
 Возвращает Вас назад по схеме на *n* шагов  
  
 * POST-запрос к адрему */scheme*  
 Сбрасывает Ваш прогресс и возвращает в точку выбора схемы  