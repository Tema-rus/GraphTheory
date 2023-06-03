import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from graph import Graph


class GraphIsomorphismGUI(QWidget):
    """
    Графический интерфейс для проверки изоморфизма двух графов.
    """

    def __init__(self) -> None:
        """
        Инициализация класса GraphIsomorphismGUI.
        """
        super().__init__()
        # Задание заголовка
        self.setWindowTitle('Изоморфизм')
        self.init_ui()

    def init_ui(self) -> None:
        """
        Инициализация пользовательского интерфейса
        """

        # Настройка размеров окна
        self.setFixedHeight(308)

        # Создание вертикального компоновщика
        layout = QVBoxLayout()

        # Создание меток и полей ввода для списков вершин
        label_vertices1 = QLabel('Список вершин графа 1 (В формате «Вершина1,Вершина2»):')
        self.input_vertices1 = QLineEdit()
        label_vertices2 = QLabel('Список вершин графа 2 (В формате «Вершина1,Вершина2»):')
        self.input_vertices2 = QLineEdit()

        # Создание меток и полей ввода для списков ребер
        label_edges1 = QLabel('Список ребер графа 1 (В формате «Вершина1-Вершина2,Вершина3-Вершина4»):')
        self.input_edges1 = QLineEdit()
        label_edges2 = QLabel('Список ребер графа 2 (В формате «Вершина1-Вершина2,Вершина3-Вершина4»):')
        self.input_edges2 = QLineEdit()

        # Создание кнопок для проверки изоморфизма и очистки
        self.button_check_isomorphism = QPushButton('Проверить изоморфизм')
        self.button_check_isomorphism.clicked.connect(self.check_isomorphism)
        self.button_clear = QPushButton('Очистить')
        self.button_clear.clicked.connect(self.clear_inputs)

        # Добавление виджетов на компоновщик
        layout.addWidget(label_vertices1)
        layout.addWidget(self.input_vertices1)
        layout.addWidget(label_edges1)
        layout.addWidget(self.input_edges1)
        layout.addWidget(label_vertices2)
        layout.addWidget(self.input_vertices2)
        layout.addWidget(label_edges2)
        layout.addWidget(self.input_edges2)
        layout.addWidget(self.button_check_isomorphism)
        layout.addWidget(self.button_clear)

        # Настройки стилей
        self.setStyleSheet('background-color: #f2f2f2; font-size: 12px')
        label_vertices1.setStyleSheet("font-weight: bold;")
        self.input_vertices1.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px;")
        label_vertices2.setStyleSheet("font-weight: bold;")
        self.input_vertices2.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px;")
        label_edges1.setStyleSheet("font-weight: bold;")
        self.input_edges1.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px;")
        label_edges2.setStyleSheet("font-weight: bold;")
        self.input_edges2.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px;")
        self.button_check_isomorphism.setStyleSheet(
            "background-color: #4caf50; color: white; padding: 8px 16px; font-weight: bold;"
        )
        self.button_clear.setStyleSheet(
            "background-color: #f44336; color: white; padding: 8px 16px; font-weight: bold;"
        )

        # Установка компоновщика для окна
        self.setLayout(layout)

    def check_isomorphism(self):
        try:
            # Получение введенных списков вершин и ребер
            vertices1 = self.input_vertices1.text().split(',')
            edges1 = [tuple(edge.split('-')) for edge in self.input_edges1.text().split(',')]
            vertices2 = self.input_vertices2.text().split(',')
            edges2 = [tuple(edge.split('-')) for edge in self.input_edges2.text().split(',')]

            # Создание графов на основе введенных данных
            graph1 = Graph(vertices1, edges1)
            graph2 = Graph(vertices2, edges2)

            # Проверка изоморфизма графов
            if graph1.is_isomorphic(graph2):
                QMessageBox.information(self, 'Результат', 'Графы изоморфны.')
            else:
                QMessageBox.information(self, 'Результат', 'Графы не изоморфны.')

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', str(e))

    def clear_inputs(self) -> None:
        """
        Обработчик события нажатия кнопки "Очистить".
        """
        # Очистка полей ввода
        self.input_vertices1.clear()
        self.input_edges1.clear()
        self.input_vertices2.clear()
        self.input_edges2.clear()
        print(self.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphIsomorphismGUI()
    window.show()
    sys.exit(app.exec_())
