from core.form import Form

class Traveler:

    def __init__(self, form: Form, tileX: int, tileY: int):
        self.form: Form = form
        self.tileX: int = tileX
        self.tileY: int = tileY
        pass

