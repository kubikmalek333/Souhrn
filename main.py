from datetime import datetime

with open("postavy.txt", encoding="utf-8") as soubor:
    postavy = []
    for radek in soubor:
        radek = radek.strip()
        if radek:
            castky = radek.split("#")
            postavy_dict = {
                "jmeno": castky[0],
                "vek": int(castky[1]),
                "pohlavi": castky[2],
                "zvire": castky[3].lower() == "ano",
                "datum": datetime.strptime(castky[4], "%Y-%m-%d").date(),
                "oblibenost":float(castky[5])
			}
            if not postavy_dict["zvire"] and postavy_dict["oblibenost"] > 2.5:
                postavy.append(postavy_dict)

for postava in postavy:
    pohlavi_text = "muž" if postava["pohlavi"] == "muž" else "žena"
    zvire_text =  "ano" if postava["zvire"] == "ano" else "ne"
    print(f"Jméno: {postava["jmeno"]}")
    print(f"Věk: {postava["vek"]}let")
    print(f"Pohlaví: {pohlavi_text}")
    print(f"je to zvířatko?: {zvire_text}")
    print(f"Datum posledního vystoupení: {postava["datum"]}")
    print(f"Oblíbenost: {postava["oblibenost"]}")
    print()

with open("oblibene-postavy.txt", 'w', encoding="utf-8") as vystup:
    for postava in postavy:
        radek = "\t".join([
            postava["jmeno"],
            str(postava["vek"]),
            postava["pohlavi"],
            "ano" if postava["zvire"] else "ne",
            str(postava["datum"]),
            str(postava["oblibenost"])
        ])
        vystup.write(radek + "\n")