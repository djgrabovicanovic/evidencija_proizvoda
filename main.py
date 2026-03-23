
class App:
    def __init__(self):
        self.routes = {}
        self.proizvodi = []
        
        self.routes["add"] = {
            "desc": "Dodaj novi zapis",
            "func": add_proizvod
        }

        self.routes["show"] = {
            "desc": "Prikaži sve zapise",
            "func": show_proizvodi
        }

    def run(self):
        while True:

            print("Dostupne komande:")
            for cmd, info in self.routes.items():
                print(f"{cmd} - {info['desc']}")

            print("exit - Izlaz iz programa")
            print()

            cmd = input("> ").strip()
            if cmd == "exit":
                break

            if cmd in self.routes:
                self.routes[cmd]["func"]()
            else:
                print("Nepoznata komanda. Pokušajte ponovo.")


def add_proizvod():
    naziv =input("Naziv proizvoda> ").strip()
    cena = float(input("Cena proizvoda> ").strip())
    proizvodjac = input("Proizvođač> ").strip()
    proizvod = {
        "naziv": naziv,
        "cena": cena,
        "proizvodjac": proizvodjac
    }
    app.proizvodi.append(proizvod)

def show_proizvodi():
    for proizvod in app.proizvodi:
        print(f"Naziv: {proizvod['naziv']}, Cena: {proizvod['cena']}, Proizvođač: {proizvod['proizvodjac']}")
    print()

if __name__ == "__main__":
    app = App()
    app.run()