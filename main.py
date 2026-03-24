

# Glavni modul aplikacije
class App:
    def __init__(self):
        self.routes = {}    # mapa komandi i njihovih funkcija
        self.proizvodi = [] # lista proizvoda
        self.current_proizvod_id = 0
        
        # Definisanje ruta i njihovih funkcija
        self.routes["add"] = {
            "desc": "Dodaj novi zapis",
            "func": add_proizvod
        }

        self.routes["show"] = {
            "desc": "Prikaži sve zapise",
            "func": show_proizvodi
        }

        self.routes["details"] = {
            "desc": "Prikaži detalje jednog zapisa",
            "func": show_detalji
        }

        self.routes["delete"] = {
            "desc": "Obriši zapis",
            "func": delete_proizvod
        }

        self.routes["update"] = {
            "desc": "Ažuriraj zapis",
            "func": update_proizvod
        }

        self.routes["save"] = {
            "desc": "Sačuvaj podatke",
            "func": save_data
        }

        self.routes["load"] = {
            "desc": "Učitaj podatke",
            "func": load_data
        }

    # Glavna petlja aplikacije
    def run(self):
        # Učitavanje podataka iz fajla pri pokretanju aplikacije
        load_data()

        while True:

            # Prikaz dostupnih komandi
            print("Dostupne komande:")
            for cmd, info in self.routes.items():
                print(f"{cmd} - {info['desc']}", end="\t")

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
        "id": app.current_proizvod_id + 1,
        "naziv": naziv,
        "cena": cena,
        "proizvodjac": proizvodjac
    }
    app.proizvodi.append(proizvod)
    print("Proizvod je uspešno dodat.")
    app.current_proizvod_id = app.current_proizvod_id + 1

# Funkcija za prikaz svih proizvoda
def show_proizvodi():
    for proizvod in app.proizvodi:
        print(f"ID: {proizvod['id']}, Naziv: {proizvod['naziv']}, Cena: {proizvod['cena']}, Proizvođač: {proizvod['proizvodjac']}")
    print()

# Funkcija za prikaz detalja jednog proizvoda
def show_detalji():
    id_proizvoda = int(input("Unesite ID proizvoda> ").strip())
    for proizvod in app.proizvodi:
        if proizvod["id"] == id_proizvoda:
            print(f"ID: {proizvod['id']}")
            print(f"Naziv: {proizvod['naziv']}")
            print(f"Cena: {proizvod['cena']}")
            print(f"Proizvođač: {proizvod['proizvodjac']}")
            return
    print("Proizvod nije pronađen.")
    
# Funkcija za brisanje proizvoda
def delete_proizvod():
    id_proizvoda = int(input("Unesite ID proizvoda za brisanje> ").strip())
    for proizvod in app.proizvodi:
        if proizvod["id"] == id_proizvoda:
            app.proizvodi.remove(proizvod)
            print("Proizvod je uspešno obrisan.")
            return
    print("Proizvod nije pronađen.")

# Funkcija za ažuriranje proizvoda
def update_proizvod():
    id_proizvoda = int(input("Unesite ID proizvoda za ažuriranje> ").strip())

    # Pronađi proizvod i prikaži trenutne podatke
    # Da li postoji jednostavniji način da se pronađe proizvod? Možda koristiti dict umesto liste?
    for proizvod in app.proizvodi:
        if proizvod["id"] == id_proizvoda:
            print(f"Trenutni podaci za {proizvod['naziv']}:")
            print(f"Cena: {proizvod['cena']}")
            print(f"Proizvođač: {proizvod['proizvodjac']}")

            novi_naziv = input(f"Unesite novi naziv ({proizvod['naziv']})> ").strip()
            if novi_naziv:
                proizvod["naziv"] = novi_naziv

            nova_cena = input(f"Unesite novu cenu ({proizvod['cena']})> ").strip()
            if nova_cena:
                proizvod["cena"] = float(nova_cena)

            novi_proizvodjac = input(f"Unesite novog proizvođača ({proizvod['proizvodjac']})> ").strip()
            if novi_proizvodjac:
                proizvod["proizvodjac"] = novi_proizvodjac

            print("Proizvod je uspešno ažuriran.")
            return
    print("Proizvod nije pronađen.")

# Sačuvaj podatke u fajl
def save_data():
    with open("proizvodi.txt", "w", encoding='utf-8', ) as f:
        for proizvod in app.proizvodi:
            f.write(f"{proizvod['id']},{proizvod['naziv']},{proizvod['cena']},{proizvod['proizvodjac']}\n")

# Učitaj podatke iz fajla
# Pitati na konsultacijama da li je potrebno obraditi slučaj kada vrednost sadrži yarey
def load_data():
    app.proizvodi = []  # resetovanje liste proizvoda pre učitavanja
    try:
        with open("proizvodi.txt", "r", encoding='utf-8') as f:
            for line in f:
                id, naziv, cena, proizvodjac = line.strip().split(",")
                proizvod = {
                    "id": int(id),
                    "naziv": naziv,
                    "cena": float(cena),
                    "proizvodjac": proizvodjac
                }
                app.proizvodi.append(proizvod)
                app.current_proizvod_id = max(app.current_proizvod_id, int(id))
    except FileNotFoundError:
        print("Nije pronađen fajl sa podacima. Početak sa praznom listom proizvoda.")

if __name__ == "__main__":
    # Inicijalizacija i pokretanje aplikacije
    app = App()
    app.run()