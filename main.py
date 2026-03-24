

# Glavni modul aplikacije
class App:
    def __init__(self):
        self.routes = {}    # mapa komandi i njihovih funkcija
        self.proizvodi = [] # lista proizvoda
        
        # Definisanje ruta

        self.routes["add"] = {
            "desc": "Dodaj novi zapis",
            "func": add_proizvod
        }

        self.routes["show"] = {
            "desc": "Prikaži sve zapise",
            "func": show_proizvodi
        }

    # Glavna petlja aplikacije
    def run(self):
        while True:

            # Prikaz dostupnih komandi
            print("Dostupne komande:")
            for cmd, info in self.routes.items():
                print(f"{cmd} - {info['desc']}")

            print("exit - Izlaz iz programa")
            print()

            # Čitanje korisničkog unosa
            cmd = input("> ").strip()

            # Obrada komande
            if cmd == "exit":
                break

            if cmd in self.routes:
                # Pozivanje funkcije povezane sa komandom
                self.routes[cmd]["func"]()
            else:
                print("Nepoznata komanda. Pokušajte ponovo.")

# Funkcija za dodavanje novog proizvoda
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

# Funkcija za prikaz svih proizvoda
def show_proizvodi():
    for proizvod in app.proizvodi:
        print(f"Naziv: {proizvod['naziv']}, Cena: {proizvod['cena']}, Proizvođač: {proizvod['proizvodjac']}")
    print()

if __name__ == "__main__":
    # Inicijalizacija i pokretanje aplikacije
    app = App()
    app.run()