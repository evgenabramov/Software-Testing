# Тестирование проекта "Шифратор"
Задание по курсу "Технологии программирования" ФИВТ МФТИ, 1 курс, 2019 год

##  Описание проекта

"Шифратор" - программа, которая шифрует/дешифрует тексты на латинице шифром Цезаря и шифром Виженера. Кроме того, по предложенному для обработки тексту Шифратор можно обучить частотам встречаемости отдельных символов в тексте и по построенной модели взломать шифр Цезаря.

**Требования:**

1. Шифрование оставляет нетронутыми знаки препинания, пробелы и переносы строк. 
2. Заглавные буквы шифрование переводит в заглавные и наоборот.

## Тестирование

Для проверки корректности работы алгоритмов используется ***юнит-тестирование***.

Чтобы можно было провести нагрузочное и стресс-тестирование, сформулируем *нагрузочные требования* к программе:

1. Время работы каждой операции не превосходит **3 секунд**
2. Размер текстов, с которыми работает программа, не превышает **5*10^9 символов**.

В части проекта, отвечающей за ***нагрузочное тестирование***, проверяется соответствие заявленным требованиям при нагрузке ниже предельного значения.

В части проекта, отвечающей за ***стресс-тестирование***, исследуется поведение программы при нагрузках, превышающих предельное значение. Тем самым, проверяется потенциальная возможность увеличить требования к нагрузке на систему.

### Описание и результаты юзабилити-тестирования:

В случае данного проекта успешный результат юзабилити-тестирования означает удобство пользовательского интерфейса.

По результатам опроса тестировщиков-пользователей:

*Плюсы программы:*

1. При неправильном вводе параметров пользователь видит, что конкретно сделано не так.
2. Для ничего не знающего о программе пользователя есть возможность вывести подсказку по работе с программой с помощью параметра —help, где отражены описания каждого параметра и метода.
3. При неправильном вводе работа программы сразу прекращается, поэтому нельзя получить некорректный результат.

*Минусы программы:*

1. Запуск программы происходит из терминала, что является своего рода преградой для обычных пользователей - мало кто пользуется терминалом, поэтому имело бы смысл сделать визуальный интерфейс