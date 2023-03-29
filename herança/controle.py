class ControleBonifica():
    _total2 = 0
    def __init__(self):
        self._total = 0
    def register(self, f):
        self._total += f.get_bonificca()
    @property
    def total(self):
        return self._total