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