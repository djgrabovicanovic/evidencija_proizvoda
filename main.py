

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
        self.proizvodRepository = ProizvodRepository()
        

    # Funkcija za dodavanje novog proizvoda
    def add_proizvod(self):
        naziv, cena, proizvodjac = Proizvodcli.input_proizvod()
        id = self.proizvodRepository.add_proizvod(naziv, cena, proizvodjac)
        Proizvodcli.log(f"Proizvod ID: {id} je uspešno dodat.")

    # Funkcija za prikaz svih proizvoda
    def show_proizvodi(self):
        proizvodi = self.proizvodRepository.all_proizvodi()
        if not proizvodi:
            Proizvodcli.log("Nema proizvoda za prikaz.")
            return
        
        for proizvod in proizvodi:
            Proizvodcli.log(f"ID: {proizvod['id']}, Naziv: {proizvod['naziv']}, Cena: {proizvod['cena']}, Proizvođač: {proizvod['proizvodjac']}")
        

    # Funkcija za prikaz detalja jednog proizvoda
    def show_detalji(self):
        try:
            id_proizvoda = Proizvodcli.input_id()
            proizvod = self.proizvodRepository.get_proizvod_by_id(id_proizvoda)
            if proizvod:
                Proizvodcli.output_proizvod(proizvod)
        except ValueError as e:
            Proizvodcli.log(str(e))
    
    # Funkcija za brisanje proizvoda
    def delete_proizvod(self):
        try:
            id_proizvoda = Proizvodcli.input_id()
            self.proizvodRepository.delete_proizvod(id_proizvoda)
            Proizvodcli.log("Proizvod je uspešno obrisan.")
        except ValueError as e:
            Proizvodcli.log(str(e))
            return

    # Funkcija za ažuriranje proizvoda
    def update_proizvod(self):
        try:
            id_proizvoda = Proizvodcli.input_id()
            proizvod = self.proizvodRepository.get_proizvod_by_id(id_proizvoda)
            naziv, cena, proizvodjac = Proizvodcli.edit_val_proizvod(proizvod)
            self.proizvodRepository.update_proizvod(id_proizvoda, naziv, cena, proizvodjac)
            Proizvodcli.log("Proizvod je uspešno ažuriran.")
        except ValueError as e:
            Proizvodcli.log(str(e))
            return

    # Sačuvaj podatke u fajl
    def save_data(self, file="proizvodi.txt"):
        self.proizvodRepository.save_proizvodi(file)

    # Učitaj podatke iz fajla
    def load_data(self, file="proizvodi.txt"):
        self.proizvodRepository.load_data(file)

class Proizvodcli:
    
    # Ispisivanje stringa na konzoli i možda u fajl
    @staticmethod
    def log(logstring):
        print(logstring)

    @staticmethod
    def input_proizvod():
        naziv = input("Naziv proizvoda> ").strip()
        while True:
            try:
                cena = float(input("Cena proizvoda> ").strip())
                break
            except ValueError:
                print("Greška: Unesite validan broj za cenu.")
        proizvodjac = input("Proizvođač> ").strip()
        return naziv, cena, proizvodjac

    @staticmethod
    def input_id():
        while True:
            try:
                return int(input("Unesite ID proizvoda> ").strip())
            except ValueError:
                print("Greška: Unesite validan broj za ID.")

    @staticmethod
    def output_proizvod(proizvod):
        print(f"ID: {proizvod['id']}")
        print(f"Naziv: {proizvod['naziv']}")
        print(f"Cena: {proizvod['cena']}")
        print(f"Proizvođač: {proizvod['proizvodjac']}")
    
    @staticmethod
    def edit_val_proizvod(proizvod):
        if not proizvod:
            raise ValueError("Proizvod nije prosleđen")
        
        novi_naziv = input(f"Unesite novi naziv ({proizvod['naziv']})> ").strip()
        if not novi_naziv:
            novi_naziv = proizvod['naziv']
        
        nova_cena = proizvod['cena']
        while True:
            cena = input(f"Unesite novu cenu ({proizvod['cena']})> ").strip()
            if not cena:
                break
            else:
                try:
                    nova_cena = float(cena)
                    break
                except ValueError:
                    Proizvodcli.log("Greška: Cena nije ažurirana jer uneta vrednost nije validan broj.")

        novi_proizvodjac = input(f"Unesite novog proizvođača ({proizvod['proizvodjac']})> ").strip()
        if not novi_proizvodjac:
            novi_proizvodjac = proizvod['proizvodjac']
        return novi_naziv, nova_cena, novi_proizvodjac
        

class ProizvodRepository:
    def __init__(self):
        self.proizvodi = [] # lista proizvoda
        self.current_proizvod_id = 0
    
    def add_proizvod(self, naziv, cena, proizvodjac):
        
        proizvod = {
            "id": self.current_proizvod_id + 1,
            "naziv": naziv,
            "cena": cena,
            "proizvodjac": proizvodjac
        }
        self.proizvodi.append(proizvod)
        self.current_proizvod_id = self.current_proizvod_id + 1
        return proizvod['id']

    def all_proizvodi(self):
        return list(self.proizvodi)

    def get_proizvod_by_id(self, id):
        for proizvod in self.proizvodi:
            if proizvod["id"] == id:
                return proizvod
        raise ValueError(f"Proizvod - ID {id} nije pronađen.")
    
    def delete_proizvod(self, id):
        for proizvod in self.proizvodi:
            if proizvod["id"] == id:
                self.proizvodi.remove(proizvod)
                return
        raise ValueError(f"Proizvod - ID {id} nije pronađen.")
    
    def update_proizvod(self, id, naziv, cena, proizvodjac):
        proizvod = self.get_proizvod_by_id(id)
        proizvod['naziv'] = naziv
        proizvod['cena'] = cena
        proizvod['proizvodjac'] = proizvodjac
    
    # TODO Preći na csv - standardna biblioteka biblioteka. Pitati na konsultacijama da li se može koristiti JSON
    # Pitati na konsultacijama da li je potrebno obraditi slučaj kada vrednost sadrži yarey
    def save_proizvodi(self, file='proizvodi.txt'):
        with open(file, "w", encoding='utf-8', ) as f:
            for proizvod in self.proizvodi:
                f.write(f"{proizvod['id']},{proizvod['naziv']},{proizvod['cena']},{proizvod['proizvodjac']}\n")
    
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