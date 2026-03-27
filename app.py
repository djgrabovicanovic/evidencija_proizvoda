
import proizvod_controller as pc

# Glavni modul aplikacije
class App:
    def __init__(self):
        self.routes = {}    # mapa komandi i njihovih funkcija
        self.proizvodController = pc.ProizvodController(self)

        self.register_route("add", "Dodaj novi zapis", self.proizvodController.add_proizvod)
        self.register_route("show", "Prikaži sve zapise", self.proizvodController.show_proizvodi)
        self.register_route("details", "Prikaži detalje jednog zapisa", self.proizvodController.show_detalji)
        self.register_route("delete", "Obriši zapis", self.proizvodController.delete_proizvod)
        self.register_route("update", "Ažuriraj zapis", self.proizvodController.update_proizvod)
        self.register_route("save", "Sačuvaj podatke", self.proizvodController.save_data)
        self.register_route("load", "Učitaj podatke", self.proizvodController.load_data)
        
    # Definisanje ruta i njihovih funkcija
    def register_route(self, name, desc, func):
        self.routes[name] = {
            "desc": desc,
            "func": func
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
