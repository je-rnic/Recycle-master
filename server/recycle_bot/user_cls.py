
class user:
    def __init__(self):
        self.points = 0

    def add(self):
        self.points += 100
        return "have recycled and gained 100 points"

    def get_points(self):
        return self.points
