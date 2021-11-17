
##
class Material():
    def __init__(self, n0, l0, a, nom):
        self.n0 = n0
        self.l0 = l0
        self.a = a
        self.nom = nom

    def indice(self, l):
        # l: longueur d'onde en nm
        return self.n0 + self.a*(l - self.l0)

AIR = Material(1, 1, 0, "AIR")
BK7 = Material(1.4281, 500, 10 ** (-4), "BK7")

if __name__ == "__main__":
    print(AIR.__instance__)
