
# Проверка изоморфизма

Репозиторий содержит 2 python файла:

+ [graph.py](#graphpy) - Содержит класс `Graph` - неориентированный граф, предоставляющий функционал для нахождения степени
  вершины графа и проверки изоморфизма между двумя графами.
+ [main.py](#mainpy) - Содержит класс `GraphIsomorphismGUI`, предоставляющий графический интерфейс пользователя (GUI) для ввода
  графов и их проверки на изоморфизм.

А также 2 папки:
+ `build` - нужна для запуска `dist/main.exe`
+ `dist` - папка, в которой хранится `main.exe`

## Содержание
- [Установка и запуск](#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-%D0%B8-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
- [graph.py](#graphpy)
  - [Использование](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
  - [API](#api)
  - [Методы](#%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B)
  - [Примеры](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B)
    - [Пример №1](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%E2%84%961)
    - [Пример №2](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%E2%84%962)
- [main.py](#mainpy)
  - [Использование](#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-1)
  - [Пример ввода данных](#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%B2%D0%B2%D0%BE%D0%B4%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
  - [Зависимости](#%D0%97%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8)

## Установка и запуск

1. Скачайте или склонируйте репозиторий на ваш компьютер.
2. Перейдите в папку `dist`, которая содержит исполняемый файл.
3. Запустите `main.exe`, дважды кликнув по нему.

Примечание: Возможно, в некоторых операционных системах открытие исполняемого файла может вызвать предупреждение
безопасности. Если это происходит, выполните следующие действия:

- Для Windows: щелкните правой кнопкой мыши на `main.exe`, выберите "Свойства" и установите флажок "Разблокировать".
- Для macOS: откройте "Настройки системы", перейдите в "Безопасность и конфиденциальность" и разрешите
  запуск `main.app`.

## [graph.py](graph.py)

Класс `Graph` - неориентированный граф, предоставляющий функционал для нахождения степени вершины графа и проверки
изоморфизма между двумя графами.

### Использование

```python
# Создание графа
graph1 = Graph(['0', '1', '2'], [('0', '1'), ('1', '2'), ('2', '0')])

# Добавление вершины
graph1.add_vertex('3')

# Добавление ребра
graph1.add_edge(('1', '3'))

# Проверка степени вершины
degree = graph1.degree('1')

# Создание второго графа
graph2 = Graph(['1', '2', '3'], [('1', '2'), ('2', '3'), ('3', '1')])

# Проверка изоморфности графов
if graph1.is_isomorphic(graph2):
    print("Графы graph1 и graph2 изоморфны.")
else:
    print("Графы graph1 и graph2 не изоморфны.")
```

### API

```python
Graph(vertices: List[str] = None, edges: List[Tuple[str, str]] = None)
```

Создаёт объект класса `Graph` с указанными вершинами и ребрами. По умолчанию пустой граф.

### Методы

+ `add_vertex(vertex: str) -> None`: Добавляет вершину в граф, если ее еще нет.
+ `add_edge(edge: Tuple[str, str]) -> None`: Добавляет ребро в граф, если его вершины существуют.
+ `degree(vertex: str) -> int`: Возвращает степень вершины в графе.
+ `is_isomorphic(other: Graph) -> bool`: Проверяет, является ли данный граф изоморфным другому графу.

### Примеры

#### Пример №1

```python
graph1 = Graph(['A', 'B', 'C'], [('A', 'B'), ('C', 'A')])
graph2 = Graph(['X', 'Y', 'Z'], [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')])

if graph1.is_isomorphic(graph2):
    print("Графы graph1 и graph2 изоморфны.")
else:
    print("Графы graph1 и graph2 не изоморфны.")
```

Вывод:

```
Графы graph1 и graph2 не изоморфны.
```

#### Пример №2

```python
graph1 = Graph(['0', '1', '2'], [('0', '1'), ('1', '2'), ('2', '0')])
graph2 = Graph(['1', '2', '3'], [('1', '2'), ('2', '3'), ('3', '1')])

if graph1.is_isomorphic(graph2):
    print("Графы graph1 и graph2 изоморфны.")
else:
    print("Графы graph1 и graph2 не изоморфны.")
```

Вывод:

```
Графы graph1 и graph2 изоморфны.
```

## [main.py](main.py)

### Использование

1. Запускаем программу
2. В поле `Список графа 1` вводим вершины графа 1, разделенные запятыми **без пробелов**.
3. В поле `Список ребер графа 1` вводим ребра графа 1, разделенные запятыми **без пробелов** в формате *
   *Вершина1-Вершина2,Вершина3-Вершина-4**.
4. В поле `Список вершин графа 2` вводим вершины графа 2, разделенные запятыми **без пробелов**
5. В поле `Список ребер графа 2` вводим ребра графа 2, разделенные запятыми **без пробелов** в формате *
   *вершина1-вершина2**
6. Нажимаем кнопку `Проверить изоморфизм`.
7. Программа проверит изоморфизм введенных графов и выведет соответствующий результат в диалоговом окне.
8. Если хотим очистить поля ввода, нажимаем кнопку `Очистить`.

### Пример ввода данных

* Граф 1:
    * Список вершин графа 1:

       ```
       A,B,C
       ```

    * Список ребер графа 1:

      ```
      A-B,A-C
      ```

* Граф 2:
    * Список вершин графа 2:

      ```
      X,Y,Z
      ```

    * Список ребер графа 2:

      ```
      X-Y,X-Z
      ```

### Зависимости

Для запуска приложения `main.py` необходимо установить PyQt5

```bash
pip install pyqt5
```
