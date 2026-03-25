

# Glavni modul aplikacije
class App:
    def __init__(self):
        self.routes = {}    # mapa komandi i njihovih funkcija
        self.proizvodController = ProizvodController(self)
        
        # Definisanje ruta i njihovih funkcija
        self.routes["add"] = {
            "desc": "Dodaj novi zapis",
            "func": self.proizvodController.add_proizvod
        }

        self.routes["show"] = {
            "desc": "Prikaži sve zapise",
            "func": self.proizvodController.show_proizvodi
        }

        self.routes["details"] = {
            "desc": "Prikaži detalje jednog zapisa",
            "func": self.proizvodController.show_detalji
        }

        self.routes["delete"] = {
            "desc": "Obriši zapis",
            "func": self.proizvodController.delete_proizvod
        }

        self.routes["update"] = {
            "desc": "Ažuriraj zapis",
            "func": self.proizvodController.update_proizvod
        }

        self.routes["save"] = {
            "desc": "Sačuvaj podatke",
            "func": self.proizvodController.save_data
        }

        self.routes["load"] = {
            "desc": "Učitaj podatke",
            "func": self.proizvodController.load_data
        }

    # Glavna petlja aplikacije
    def run(self):
        # Učitavanje podataka iz fajla pri pokretanju aplikacije
        self.proizvodController.load_data()

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


class ProizvodController:

    def __init__(self, app):
        self.app = app
        self.proizvodi = [] # lista proizvoda
        self.current_proizvod_id = 0  ## TODO move to model class

    # Funkcija za dodavanje novog proizvoda
    def add_proizvod(self):
        naziv =input("Naziv proizvoda> ").strip()
        while True:
            try:
                cena = float(input("Cena proizvoda> ").strip())
                break
            except ValueError:
                print("Greška: Unesite validan broj za cenu.")
        proizvodjac = input("Proizvođač> ").strip()
        proizvod = {
            "id": self.current_proizvod_id + 1,
            "naziv": naziv,
            "cena": cena,
            "proizvodjac": proizvodjac
        }
        self.proizvodi.append(proizvod)
        print("Proizvod je uspešno dodat.")
        self.current_proizvod_id = self.current_proizvod_id + 1

    # Funkcija za prikaz svih proizvoda
    def show_proizvodi(self):
        if not self.proizvodi:
            print("Nema proizvoda za prikaz.")
            return
        
        for proizvod in self.proizvodi:
            print(f"ID: {proizvod['id']}, Naziv: {proizvod['naziv']}, Cena: {proizvod['cena']}, Proizvođač: {proizvod['proizvodjac']}")
        print()

    # Funkcija za prikaz detalja jednog proizvoda
    def show_detalji(self):
        try:
            id_proizvoda = int(input("Unesite ID proizvoda> ").strip())
        except ValueError:
            print("Greška: Unesite validan broj za ID.")
            return
        for proizvod in self.proizvodi:
            if proizvod["id"] == id_proizvoda:
                print(f"ID: {proizvod['id']}")
                print(f"Naziv: {proizvod['naziv']}")
                print(f"Cena: {proizvod['cena']}")
                print(f"Proizvođač: {proizvod['proizvodjac']}")
                return
        print(f"Proizvod - ID {id_proizvoda} nije pronađen.")
        
    # Funkcija za brisanje proizvoda
    def delete_proizvod(self):
        try:
            id_proizvoda = int(input("Unesite ID proizvoda za brisanje> ").strip())
        except ValueError:
            print("Greška: Unesite validan broj za ID.")
            return
        
        for proizvod in self.proizvodi:
            if proizvod["id"] == id_proizvoda:
                self.proizvodi.remove(proizvod)
                print("Proizvod je uspešno obrisan.")
                return
        print("Proizvod nije pronađen.")

    # Funkcija za ažuriranje proizvoda
    def update_proizvod(self):
        try:
            id_proizvoda = int(input("Unesite ID proizvoda za ažuriranje> ").strip())
        except ValueError:
            print("Greška: Unesite validan broj za ID.")
            return

        # Pronađi proizvod i prikaži trenutne podatke
        # Da li postoji jednostavniji način da se pronađe proizvod? Možda koristiti dict umesto liste?
        for proizvod in self.proizvodi:
            if proizvod["id"] == id_proizvoda:
                print(f"Trenutni podaci za {proizvod['naziv']}:")
                print(f"Cena: {proizvod['cena']}")
                print(f"Proizvođač: {proizvod['proizvodjac']}")

                novi_naziv = input(f"Unesite novi naziv ({proizvod['naziv']})> ").strip()
                if novi_naziv:
                    proizvod["naziv"] = novi_naziv

                nova_cena = input(f"Unesite novu cenu ({proizvod['cena']})> ").strip()
                if nova_cena:
                    try:
                        proizvod["cena"] = float(nova_cena)
                    except ValueError:
                        print("Greška: Cena nije ažurirana jer uneta vrednost nije validan broj.")

                novi_proizvodjac = input(f"Unesite novog proizvođača ({proizvod['proizvodjac']})> ").strip()
                if novi_proizvodjac:
                    proizvod["proizvodjac"] = novi_proizvodjac

                print("Proizvod je uspešno ažuriran.")
                return
        print("Proizvod nije pronađen.")

    # TODO move to model
    # TODO Preći na csv - standardna biblioteka biblioteka. Pitati na konsultacijama da li se može koristiti JSON
    # Sačuvaj podatke u fajl
    def save_data(self, file="proizvodi.txt"):
        with open(file, "w", encoding='utf-8', ) as f:
            for proizvod in self.proizvodi:
                f.write(f"{proizvod['id']},{proizvod['naziv']},{proizvod['cena']},{proizvod['proizvodjac']}\n")

    # TODO move to model
    # Učitaj podatke iz fajla
    # Pitati na konsultacijama da li je potrebno obraditi slučaj kada vrednost sadrži yarey
    def load_data(self, file="proizvodi.txt"):
        self.proizvodi = []  # resetovanje liste proizvoda pre učitavanja
        try:
            with open(file, "r", encoding='utf-8') as f:
                for line in f:
                    id, naziv, cena, proizvodjac = line.strip().split(",")
                    proizvod = {
                        "id": int(id),
                        "naziv": naziv,
                        "cena": float(cena),
                        "proizvodjac": proizvodjac
                    }
                    self.proizvodi.append(proizvod)
                    self.current_proizvod_id = max(self.current_proizvod_id, int(id))
        except ValueError:
            print("Pogrešan format falja!")
            exit(-1)
        except FileNotFoundError:
            print("Nije pronađen fajl sa podacima. Početak sa praznom listom proizvoda.")




if __name__ == "__main__":
    # Inicijalizacija i pokretanje aplikacije
    app = App()
    app.run()