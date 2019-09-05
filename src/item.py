class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You have picked up: {self.name}")

    def on_drop(self):
        if self.name == 'lamp':
            print("It's not wise to drop your source of light!")
        print(f"You have dropped: {self.name}")