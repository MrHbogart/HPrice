import pandas as pd

class HPrice:
    def __init__(self, data, n):
        self.data = data
        self.n = n

    def HPrice(self):
        date = []
        price = []
        volume = []
        return result