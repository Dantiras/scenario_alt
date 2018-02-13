﻿#План-схема рута Ульянки.
#Рут разделяется на две ветки: ветку Огоньков и ветку Неудачника.

label alt_day6_us_7dl_start:
    call alt_day6_us_7dl_begin
    
label alt_day6_us_px_start:
    call alt_day6_us_px_begin
####################################
#СОБСТВЕННО, РУТ!!! Отдельный файл и т.п.
####################################

####################################
#ВН - ПОД СОМНЕНИЕМ - надо ли отдельный шестой день, концерт, и т.д.?
####################################
#Подъём#TODON1
#Зарядка#TODON2
#Завтрак#TODON3
#Помощь с подготовкой концерта (выбор - Мику, Лена, сбежать)#TODON4
#Мику - репетиция, предложения дружбы (флаг-эпилог)#TODON5
#Лена - признания, рисунки, параллели, газета (флаг-эпилог)#TODON6
#Сбежать - планируется страшная мстя жуликамTODON7
#Обед#TODON8
#Мику - саунд-чек#TODON9
#Лена - Уходим гулять в одиночестве, пытаясь найти Лес Памяти (см. н16)#TODON10
#Ульяна - солёная змеюка с чердака, бумажка с аммиак-селитрой в душевые#TODON11
#Концерт#TODON12
#Ужин#TODON13
#Дискотека#TODON14-15-16 (Танец со Славей, Ульянкой, ОД)
#Беседа на крылечке (повторение сцены чаепития из д.2) - проверка по флагам, иначе ОД утаскивает Семёна купаться на мыс.TODON17
#Отбой#TODON18
#День7 - подъём! #TODON19 (Ульянка - с мордой в пасте)#TODON20
#Завтрак#TODON21
#Сборы#TODON22
#Отъезд#TODON23
#Пробуждение дома#TODON24
#Эпилог#TODON25
#Выбор: согласиться на встречу или нет?#TODON26
#Согласие:поездка#TODON27 - встреча, ЭПИЛОГ-ГУД ВН#TODON28
#Отказ:дома, новости#TODON29 - репортаж про подлёдную рыбалку ЭПИЛОГ-БЭД ВН#TODON30
####################################

####################################
#ВО - основная история
####################################
#Подъём#TODO011
#Зарядка#TODO012
#Завтрак#TODO013
#Карьер#TODO014
#Локи - замирает и уходит#TODO015, Ссора с Ульяной#TODO016
#Дрищ - отступает к карьеру#TODO017, устраивает истерику#TODO018
#Обед#TODO019
#Сцена с Данечкой#TODO020
#Локи - помощь с репетицией #TODO021
#Дрищ - поиск партии #TODO022 - Мику#TODO023, Ольга#TODO024, Лена#TODO025, Алиса#TODO026, Славя#TODO027(повторное прохождение)
#Лена, Алиса, Славя - дальние ворота#TODO028
#Славя - забирает Семёна на концерт#TODO029, иначе - Саныч забирает#TODO030
#Концерт#TODO031
#Ужин#TODO032
#Дисотека#TODO033
#Локи - медляк со Славей (если звали), объяснение#TODO034
#Дрищ - сцена на пристани(если звали), возвращение Ульяны #TODO035
#Если не звали Славю - просто танцуем, беспокоимся за девочек, пытаемся сбежать, но Саныч водворяет обратно на танцпол.#TODO036
#Отбой#TODO037
#День седьмой - подъём#TODO038
#Завтрак#TODO039
#нет Славя-флага - Ульянка, Лена и Алиса вернулись ночью, мы видим их уже в столовой, ругающимися с ОД - ПОДВЕТКА ПУСТОШЕЙ #TODO040
#Славя-флаг - здороваемся с девочками, уточняем, всё ли в силе - ПОДВЕТКА ПОБЕГА#TODO041

####################################
#ПОДВЕТКА ПУСТОШЕЙ
####################################
#Сбор вещей#TODO042
#Отъезд#TODO043
#Эпилог#TODO044
#Мику-флаг - друзья навечно#TODO045
#Иначе - проверка пт:
#Больше 7 - Путь над пустошами, ЭПИЛОГ-ГУД1 ВО#TODO046
#Меньше 7 - Тай-тай, ЭПИЛОГ-БЭД1 ВО#TODO047

####################################
#ПОДВЕТКА ПОБЕГА
####################################
#Уборка остановки#TODO048
#Автобус? И правда!#TODO049
#Славя-флаг - выбор, сесть или не сесть#TODO050
#Иначе - выбора нет, мы возвращаемся обратно в лагерь#TODO051
#ЭПИЛОГ ДЕЖАВЮ#TODO052
#Дрищ - настоящее дежавю (побег)#TODO053
#Локи - дежавю!(побег)#TODO054
#Садимся в автобус, тру-концовка (История Пустошей и нестареющей юности)#TODO055

#Итого:
#30 сцен для ветки неудачника
#54 сцены для ветки огоньков (включая подветки пустошей и побега)
#############################################