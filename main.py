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
    print("durée de recherche :", translateSecondToHourMinuteSeconde(round(fin-debut,2)) ,"\nHash trouvé :", Rhash, "après", number ,"occurences")

def translateSecondToHourMinuteSeconde(s):
    day = s // (24 * 3600)
    time = s % (24 * 3600)
    hour = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    seconds = s
    duree = ""
    if (day > 0) :
        duree = day, "jours", hour, "heures", minutes, "minutes", seconds, "secondes"
    else :
        if (hour > 0) :
            duree = hour, "heures", minutes, "minutes", seconds, "secondes"
        else :
            if (minutes > 0):
                duree = minutes, "minutes", seconds, "secondes"
            else :
                duree = seconds, "secondes"
    return(duree)

def main():
  search(1,9)

if __name__ == "__main__":
    main()
