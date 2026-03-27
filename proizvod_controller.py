import proizvod_repository as pr
import proizvodcli as cli

class ProizvodController:

    def __init__(self, app):
        self.app = app
        self.proizvodRepository = pr.ProizvodRepository()

    # Funkcija za dodavanje novog proizvoda
    def add_proizvod(self):
        naziv, cena, proizvodjac = cli.Proizvodcli.input_proizvod()
        id = self.proizvodRepository.add_proizvod(naziv, cena, proizvodjac)
        cli.Proizvodcli.log(f"Proizvod ID: {id} je uspešno dodat.")

    # Funkcija za prikaz svih proizvoda
    def show_proizvodi(self):
        proizvodi = self.proizvodRepository.all_proizvodi()
        if not proizvodi:
            cli.Proizvodcli.log("Nema proizvoda za prikaz.")
            return
        
        for proizvod in proizvodi:
            cli.Proizvodcli.log(f"ID: {proizvod['id']}, Naziv: {proizvod['naziv']}, Cena: {proizvod['cena']}, Proizvođač: {proizvod['proizvodjac']}")
        

    # Funkcija za prikaz detalja jednog proizvoda
    def show_detalji(self):
        try:
            id_proizvoda = cli.Proizvodcli.input_id()
            proizvod = self.proizvodRepository.get_proizvod_by_id(id_proizvoda)
            if proizvod:
                cli.Proizvodcli.output_proizvod(proizvod)
        except ValueError as e:
            cli.Proizvodcli.log(str(e))
    
    # Funkcija za brisanje proizvoda
    def delete_proizvod(self):
        try:
            id_proizvoda = cli.Proizvodcli.input_id()
            self.proizvodRepository.delete_proizvod(id_proizvoda)
            cli.Proizvodcli.log("Proizvod je uspešno obrisan.")
        except ValueError as e:
            cli.Proizvodcli.log(str(e))
            return

    # Funkcija za ažuriranje proizvoda
    def update_proizvod(self):
        try:
            id_proizvoda = cli.Proizvodcli.input_id()
            proizvod = self.proizvodRepository.get_proizvod_by_id(id_proizvoda)
            naziv, cena, proizvodjac = cli.Proizvodcli.edit_val_proizvod(proizvod)
            self.proizvodRepository.update_proizvod(id_proizvoda, naziv, cena, proizvodjac)
            cli.Proizvodcli.log("Proizvod je uspešno ažuriran.")
        except ValueError as e:
            cli.Proizvodcli.log(str(e))
            return

    # Sačuvaj podatke u fajl
    def save_data(self, file="proizvodi.txt"):
        self.proizvodRepository.save_proizvodi(file)

    # Učitaj podatke iz fajla
    def load_data(self, file="proizvodi.txt"):
        self.proizvodRepository.load_data(file)