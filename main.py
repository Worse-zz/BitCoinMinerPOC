from hashlib import sha512
from datetime import datetime

def search(number, NbZero):
    debut = datetime.timestamp(datetime.now())
    Rhash = ""
    attendu = "0" * NbZero
    while (str(Rhash[:NbZero]) != str(attendu)):
        Rhash = (sha512(str(number).encode()).hexdigest())
        number += 1
    fin = datetime.timestamp(datetime.now())
    print("durée de recherche :", round(fin-debut,2) ,"seconde(s) \nHash trouvé :", Rhash, "après", number ,"occurences")

def main():
  search(1,6)

if __name__ == "__main__":
    main()
