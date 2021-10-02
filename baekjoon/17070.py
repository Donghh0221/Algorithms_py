head = (0, 1)
N = 3


class solution:
    def __init__(self, house):
        self.search_for = []
        self.house = house

    def check_possible_next_move_horizontal_state(self, head):
        x, y = head
        if self.house[y][x + 1] == 0:
            self.search.append([x + 1, y, 'h'])

    def check_possible_next_move_vertical_state(self, head):
        pass

    def check_possible_next_move_diagonal_state(self, head):
        pass

    def find_count(self):
        while self.search_for:
            head, state = self.search_for.pop(0)
            if state == 'h':
                pass
            elif state == 'v':
                pass
            elif  state == 'd':
                pass