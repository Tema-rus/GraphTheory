from typing import List, Tuple, Dict


class Graph:
    """
    Класс, представляющий неориентированный граф.
    """

    def __init__(self, vertices: List[str] = None, edges: List[Tuple[str, str]] = None):
        """
        Инициализация класса.

        :param vertices: Список вершин графа.
        :type vertices: List[str]
        :param edges: Список ребер графа.
        :type edges: List[Tuple[str, str]]
        """
        self.vertices = vertices or []
        self.edges = edges or []

    def add_vertex(self, vertex: str) -> None:
        """
        Метод, добавляющий вершину в граф, если её ещё нет.

        :param vertex: Вершина, которую нужно добавить.
        :type vertex: str
        """
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    def add_edge(self, edge: Tuple[str, str]) -> None:
        """
        Метод, для добавления ребра в граф, если его вершины существуют.

        :param edge: Ребро, которое нужно добавить.
        :type edge: Tuple[str, str]
        """
        vertex1, vertex2 = edge
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.edges.append(edge)

    def degree(self, vertex: str) -> int:
        """
        Метод, вычисляющий степень вершины графа.

        :param vertex: Вершина, для которой нужно найти степень.
        :return: Степень вершины.
        :rtype: int
        """
        return len([edge for edge in self.edges if vertex in edge])

    def is_isomorphic(self, other: 'Graph') -> bool:
        """
        Метод для проверки изоморфизма двух графов.

        :param other: Другой граф для сравнения.
        :type other: Graph
        :return: True, если графы изоморфны, а иначе False.
        :rtype: bool
        """
        # Сравниваем количество вершин и ребер, графы не могут быть изоморфными
        if len(self.vertices) != len(other.vertices) or len(self.edges) != len(other.edges):
            return False

        return self._check_isomorphism(other)

    def _check_isomorphism(self, other: 'Graph', mapping: Dict[str, str] = None) -> bool:
        """
        Рекурсивная функция для проверки изоморфизма графов.

        :param other: Другой граф для сравнения.
        :type other: Graph
        :param mapping: Текущее отображение вершин между графами.
        :type mapping: Dict[str, str]
        :return: True, если графы изоморфны, False в противном случае.
        :rtype: bool
        """
        if mapping is None:
            mapping = {}

        if len(mapping) == len(self.vertices):
            # Проверяем, если каждая вершина первого графа имеет соответствующую вершину во втором графе
            for edge1 in self.edges:
                found_matching_edge = False
                for edge2 in other.edges:
                    if self._are_edges_isomorphic(edge1, edge2, mapping):
                        # Проверяем изоморфность каждого ребра
                        found_matching_edge = True
                        break
                if not found_matching_edge:
                    # Если не найдено соответствующего ребра, графы не изоморфны
                    return False
            return True

        for vertex1 in self.vertices:
            # Выбираем вершину первого графа, для которой нет соответствия во втором графе
            if vertex1 not in mapping:
                for vertex2 in other.vertices:
                    # Выбираем вершину второго графа, которая еще не соответствует другой вершине первого графа
                    if vertex2 not in mapping.values():
                        mapping[vertex1] = vertex2  # Добавляем соответствующую пару вершин
                        if self._check_isomorphism(other, mapping):
                            # Рекурсивно продолжаем проверку изоморфизма
                            return True
                        del mapping[vertex1]  # Если не изоморфны, удаляем соответствие
        return False  # Иначе графы не изоморфны

    def _are_edges_isomorphic(self, edge1, edge2, mapping):
        """
            Проверка изоморфизма двух ребер с учетом заданного соответствия вершин.
            :param edge1: Ребро первого графа в формате (вершина1, вершина2).
            :param edge2: Ребро второго графа в формате (вершина1, вершина2).
            :param mapping: Соответствие вершин между графами.
            :return: True, если ребра изоморфны, False в противном случае.
            """

        # Разбиваем первое и второе ребро на вершины
        vertex1_1, vertex1_2 = edge1
        vertex2_1, vertex2_2 = edge2

        # Проверка, что обе вершины первого ребра находятся в соответствии
        if vertex1_1 in mapping and vertex1_2 in mapping:
            mapped_vertex1_1 = mapping[vertex1_1]
            mapped_vertex1_2 = mapping[vertex1_2]

            # Проверка совпадения соответствующих вершин в обоих ребрах
            if (mapped_vertex1_1 == vertex2_1 and mapped_vertex1_2 == vertex2_2) or \
                    (mapped_vertex1_1 == vertex2_2 and mapped_vertex1_2 == vertex2_1):
                return True

        # Иначе ребра не изоморфны
        return False


if __name__ == '__main__':
    Graph1 = Graph(['A', 'B', 'C'], [('A', 'B'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'A'), ('A', 'B'), ('B', 'B')])
    Graph2 = Graph(['X', 'Y', 'Z'], [('X', 'Y'), ('Y', 'Y'), ('Y', 'Z'), ('Z', 'X'), ('X', 'X'), ('X', 'Y'), ('Y', 'Y')])

    if Graph1.is_isomorphic(Graph2):
        print("Графы graph1 и graph2 изоморфны.")
    else:
        print("Графы graph1 и graph2 не изоморфны.")
