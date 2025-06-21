class Resturant:
    def __init__(self, name: str, menu: dict):
        self.name = name
        self.menu = menu

    def show_menu(self):
        return f"Resturant: {self.name}. Menu: {self.menu}"
    