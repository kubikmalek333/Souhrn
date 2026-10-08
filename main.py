import os
from datetime import datetime

with open(os.sep.join(["postavy.txt"]), encoding="utf-8") as soubor:
    postavy = []
    for radek in soubor:
        radek = radek.strip()
        if radek:
            cast = radek.split("#")
            postavy_dict = {
                "jmeno": cast[0],
                "vek": int(cast[1]),
                "pohlavi": cast[2],
                "zvire": cast[3].lower() == "ano",
                "datum_promitani": cast[4],
                "oblibenost": float(cast[5]),
            }
            if postavy_dict["oblibenost"] > 2.5:
                postavy.append(postavy_dict)

for postava in postavy:
    pohlavi_text = "muž" if postava["pohlavi"] == "m" else "žena"
    zvire_text = "ano" if postava["zvire"] else "ne"
    print(f"jméno postavy: {postava["jmeno"]}")
    print(f"věk: {postava["vek"]}let")
    print(f"pohlaví: {pohlavi_text}")
    print(f"je to zvířatko?: {zvire_text}")
    print(f"datum posledního promítání: {postava["datum_promitani"]}")
    print(f"oblíbenost u diváků: {postava["oblibenost"]}")
    print()

with open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup:
    for postava in postavy:
        radek = "\t".join([
            postava["jmeno"],
            str(postava["vek"]),
            postava["pohlavi"],
            "ano" if postava["zvire"] else "ne",
            postava["datum_promitani"],
            str(postava["oblibenost"]),
        ])
        vystup.write(radek + "\n")