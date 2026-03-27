import proizvodcli

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