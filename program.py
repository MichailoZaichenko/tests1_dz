class Numbers():
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.spisok = []
        self.spisok.append(self.a)
        self.spisok.append(self.b)
        self.spisok.append(self.c)
    def Sum(self):
        summa = sum(self.spisok)
        return summa

    def Average(self):
        average = sum(self.spisok)/len(self.spisok)
        return average

    def Min(self):
        minim = min(self.spisok)
        return minim

    def Max(self):
        maximum = max(self.spisok)
        return maximum

        