# Het programma begint met een basisset aan dieren
# De gebruikte datastructuur is een Python dictionary

import random

database_file_path = "vragen_database.txt"

dieren = {
    'vraag_start': "heeft",
    'vraag_onderwerp': "4 poten",
    'ja': 'olifant',
    'nee': {
        'vraag_start': "kruipt",
        'vraag_onderwerp': "op bladeren",
        'ja':'rups',
        'nee':'huismus'
    }
}

verbindwoorden = ["het dier", "jouw dier", "het"]

def formuleer_vraag(tak):
    # Formuleer een correcte vraag voor deze tak
    vraag_start = tak['vraag_start'].lower()
    vraag_onderwerp = tak['vraag_onderwerp'].lower()
    vraag_dier = random.choice(verbindwoorden)
    vraag = f"{vraag_start.capitalize()} {vraag_dier} {vraag_onderwerp}?"
    return vraag

def parse_nieuwe_vraag(nieuwe_vraag):
    # Functie om een nieuwe vraag te controleren en om te zetten in de juiste items
    nieuwe_vraag = nieuwe_vraag.lower().rstrip('? ').lstrip(' ').replace('  ', ' ')

    #TO-DO: parse empty input

    if " dier " in nieuwe_vraag:
        if " het " in nieuwe_vraag:
            split_str = " het dier "
        elif " je " in nieuwe_vraag:
            split_str = " je dier "
    elif " het " in nieuwe_vraag:
        split_str = " het "
    elif " hij " in nieuwe_vraag:
        split_str = " hij "
    else:
        split_str = None

    if split_str != None:
        vraag_items = nieuwe_vraag.split(split_str)
    else:
        vraag_items = []

    if len(vraag_items) != 2:
        herstelde_vraag = input("Ik kon je vraag niet goed verwerken. Probeer hem anders te stellen.")
        parse_nieuwe_vraag(herstelde_vraag)
    
    return vraag_items

def parse_branch_output(tak, depth=1):
    curr_depth = depth
    outlines = []
    for key, item in tak.items():
        print(' '*depth + f"{key}: {item},")
        if type(item) == type("test"):
            outlines.append(" "*depth + f"'{key}': '{item}',\n")
        elif type(item) == type({'key': 'value'}):
            outlines.append(" "*depth + f"'{key}'" + ": {\n")
            outlines.extend(parse_branch_output(item, curr_depth+1))
            outlines.append(" "*(depth-1) + "}\n")

    return outlines

def parse_branch_input(input_lines):
    output_dict = dict()
    i=0
    #print("New recursion started...")
    while i < len(input_lines):
        line = input_lines[i]
        #print(f"curr line: {i} - {line}", end="")
        line = line.strip().strip(",")
        if (line in {"{", "}"}): 
            i += 1
            continue
        line_items = line.split(": ")
        if line_items[1] == "{":
            nested_lines = input_lines[i+1:]
            nested_dict = parse_branch_input(nested_lines)
            key = line_items[0].strip("'")
            if key not in dieren.keys(): raise Exception(f"Key {key}in input file not found in dict keys {dieren.keys()}")
            value = nested_dict
            output_dict[key] = value
            i += len(value.keys())
        else:
            key = line_items[0].strip("'")
            if key not in dieren.keys(): raise Exception(f"Key {key}in input file not found in dict keys {dieren.keys()}")
            value = line_items[1].strip("'")
            output_dict[key] = value
            i += 1
    #print("Recursion ended")
    return output_dict

def store_dieren():
    #Sla de 'dieren' dictionary op in een text file
    outlines = parse_branch_output(dieren, 1)
    outlines.insert(0,"{\n")
    outlines.append("}")
    print("outlines lines:")
    for line in outlines:
        print(line)
    try:
        with open(database_file_path, "wt") as outfile:
            outfile.writelines(outlines)
    except:
        print("Een fout is opgetreden tijdens het opslaan van de file.")

def read_dieren():
    #Lees de databasefile en verschrijf 'dieren' met de inhoud
    out_dict = dict()
    inlines = []
    try:
        with open(database_file_path, "rt") as infile:
            inlines = infile.readlines()
    except:
        print("Een fout is opgetreden tijdens het lezen van de file.")
    
    out_dict = parse_branch_input(inlines)
    return out_dict

# Herhalen zolang de gebruiker dat wil
def raad_het_dier():
    print('Neem een dier in gedachten...')
    prompt = 'Ben je er klaar voor?'
    while vraag_ja_nee(prompt):
        doorloop_dieren_boomstructuur(dieren)
        prompt = 'Wil je nog een keer spelen?'

# Doorloop een tak
def doorloop_dieren_boomstructuur(tak):
    # We stellen eerst de vraag die op de tak beschikbaar is
    # De vraag heeft het formaat ['is'|'heeft'] het dier 'eigenschap'
    richting = vraag_ja_nee(formuleer_vraag(tak))
    nieuwe_tak = lagere_tak(tak, richting)

    if dier_gevonden(nieuwe_tak):
        eindig_spel(nieuwe_tak, tak, richting)
    else:
        doorloop_dieren_boomstructuur(nieuwe_tak)

# Een dier is gevonden als de tak waarop we zitten eindigt in een blad,
# in plaats van in een lagere tak. Een blad is een string, een
# lagere tak is een dict. We controleren op een blad met de functie
# isinstance
def dier_gevonden(tak):
    is_blad = not isinstance(tak, dict)
    return is_blad

def eindig_spel(blad, stam, richting):
    if vraag_ja_nee('Is je dier misschien een ' + blad + '?'):
        print('Yes! Ik het het geraden!')
    else:
        bewaar_nieuw_dier(stam, welke_kant(richting), blad)

def bewaar_nieuw_dier(hogere_tak, kant, oud_dier):
    nieuw_dier = input('Oh, wat jammer dat ik het niet heb geraden! Welk dier zat je aan te denken? ')

    if nieuw_dier.startswith('een '):
        nieuw_dier = nieuw_dier[4:len(nieuw_dier)]
    elif nieuw_dier.startswith('de '):
        nieuw_dier = nieuw_dier[3:len(nieuw_dier)]

    nieuwe_vraag = input('En welke vraag had ik moeten stellen om onderscheid te maken tussen een ' + oud_dier.lower() + ' en een ' + nieuw_dier.lower() + '? ')

    vraag_items = parse_nieuwe_vraag(nieuwe_vraag)

    hogere_tak[kant] = {
        'vraag_start': vraag_items[0],
        'vraag_onderwerp': vraag_items[1],
        'ja': nieuw_dier.lower(),
        'nee': oud_dier
    }

# Geef een deel van de boomstructuur terug die begint met
# ja of nee
def lagere_tak(tak, richting):
    if richting:
        return tak['ja']
    else:
        return tak['nee']

def welke_kant(ja):
    if ja:
        return 'ja'
    else:
        return 'nee'

def vraag_ja_nee(vraag):
    antwoord = input(vraag + ' ')
    return is_ja(antwoord)

def is_ja(tekst):
    tekst = tekst.lower()
    if tekst.startswith('j') or tekst.startswith('y'):
        return True
    else:
        return False

def dic_print(inp_dict: dict, depth=1):
    print(" "*(depth-1) + "{")
    curr_depth = depth
    for key, value in inp_dict.items():
        if type(value) == type({'key': 'value'}):
            print(" "*depth + f"{key}: ")
            dic_print(value, curr_depth+1)
        else:
            print(" "*depth + f"{key}: {value}")
    print(" "*(depth-1) + "}")
        


dieren = read_dieren()

dic_print(dieren)

raad_het_dier()
store_dieren()
