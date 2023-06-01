import sys
from collections import defaultdict
from typing import Dict, List, Tuple, Set

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class GraphIsomorphismChecker(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Задание заголовка
        self.setWindowTitle("Изоморфизм")

        # Настройка размеров окна
        self.setMinimumWidth(315)
        self.setFixedHeight(175)

        # Настройка шрифтов
        font = self.font()
        font.setFamily('Times New Roman')
        font.setPixelSize(17)
        self.setFont(font)

        layout = QVBoxLayout()

        self.entry1 = QLineEdit()
        self.entry1.setPlaceholderText("Введите список ребер графа 1")
        layout.addWidget(self.entry1)

        self.entry2 = QLineEdit()
        self.entry2.setPlaceholderText("Введите список ребер графа 2")
        layout.addWidget(self.entry2)

        self.calculate_button = QPushButton("Проверить изоморфизм")
        self.calculate_button.clicked.connect(self.check_isomorphism)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)

    def get_dict_links(self, list_links: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
        dict_links = defaultdict(set)
        for link in list_links:
            vertex1, vertex2 = link
            dict_links[vertex1].add(vertex2)
            dict_links[vertex2].add(vertex1)
        return dict(dict_links)

    def is_isomorphic(self, graph1: Dict[str, Set[str]], graph2: Dict[str, Set[str]]) -> bool:
        def is_match(vertex1: str, vertex2: str) -> bool:
            if vertex1 in matched:
                return matched[vertex1] == vertex2

            matched[vertex1] = vertex2
            if len(graph1[vertex1]) != len(graph2[vertex2]):
                return False

            for neigh1, neigh2 in zip(graph1[vertex1], graph2[vertex2]):
                if not is_match(neigh1, neigh2):
                    return False

            return True

        if len(graph1) != len(graph2):
            return False

        matched = {}
        for v1 in graph1:
            for v2 in graph2:
                if is_match(v1, v2):
                    return True

        return False

    def parse_links(self, links_str: str) -> List[Tuple[str, str]]:
        links_list = []
        try:
            links_str = links_str.strip()
            if links_str.startswith("(") and links_str.endswith(")"):
                links_str = links_str[1:-1]
            links = links_str.split("),")
            for link in links:
                link = link.strip()
                if link.startswith("(") and link.endswith(")"):
                    link = link[1:-1]
                vertex1, vertex2 = link.split(",")
                vertex1 = vertex1.strip()
                vertex2 = vertex2.strip()
                links_list.append((vertex1, vertex2))
        except Exception:
            raise ValueError("Некорректный формат ввода списка ребер")

        return links_list

    def check_isomorphism(self) -> None:
        graph1_input = self.entry1.text()
        graph2_input = self.entry2.text()

        try:
            graph1_links = self.parse_links(graph1_input)
            graph2_links = self.parse_links(graph2_input)
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            return

        try:
            graph1 = self.get_dict_links(graph1_links)
            graph2 = self.get_dict_links(graph2_links)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            return

        is_isomorphic = self.is_isomorphic(graph1, graph2)
        if is_isomorphic:
            self.result_label.setText("Графы изоморфны")
        else:
            self.result_label.setText("Графы не изоморфны")

    def clear_fields(self) -> None:
        self.entry1.clear()
        self.entry2.clear()
        self.result_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphIsomorphismChecker()
    window.show()
    sys.exit(app.exec_())
