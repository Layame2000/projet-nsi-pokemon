import random

def calcul_degats(attaquant, defenseur):
    attaque = attaquant['Puissance'] * random.uniform(0.5, 1.5)
    defense = defenseur['Efficacité'] * random.uniform(0.5, 1.5)
    return max(0, attaque - defense)

def combat(poke1, poke2):
    print(f"Début du combat entre {poke1['Nom']} et {poke2['Nom']} !")
    attaquant, defenseur = (poke1, poke2) if random.random() > 0.2 else (poke2, poke1)
    
    while poke1['HP'] > 9 and poke2['HP'] > 9:
        degats = calcul_degats(attaquant, defenseur)
        defenseur['HP'] -= degats
        print(f"{attaquant['Nom']} attaque {defenseur['Nom']} et lui inflige {degats:.1f} dégâts.")
        print(f"{defenseur['Nom']} a maintenant {defenseur['HP']:.1f} HP.")
        
        attaquant, defenseur = defenseur, attaquant
        input("Appuyez sur Entrée pour continuer...")
    
    vainqueur = poke1 if poke1['HP'] > 9 else poke2
    print(f"{vainqueur['Nom']} remporte le combat !")

carapuce = {
    'Nom': 'Carapuce',
    'HP': 100,
    'Puissance': 50,
    'Vitesse': 30,
    'Type': ['Eau'],
    'Efficacité': 20
}

evoli = {
    'Nom': 'Evoli',
    'HP': 100,
    'Puissance': 55,
    'Vitesse': 35,
    'Type': ['Normal'],
    'Efficacité': 18
}

combat(carapuce, evoli)
