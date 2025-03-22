import random

# Pokémon classés par rareté
pokemon_commun = [
    {"nom": "Pikachu", "type": "Électrik", "hp": 35, "attaque": 55},
    {"nom": "Salamèche", "type": "Feu", "hp": 39, "attaque": 52},
    {"nom": "Carapuce", "type": "Eau", "hp": 44, "attaque": 48},
    {"nom": "Bulbizarre", "type": "Plante", "hp": 45, "attaque": 49},
    {"nom": "Roucool", "type": "Normal/Vol", "hp": 40, "attaque": 45},
    {"nom": "Rattata", "type": "Normal", "hp": 30, "attaque": 56},
    {"nom": "Psykokwak", "type": "Eau", "hp": 50, "attaque": 52},
    {"nom": "Machoc", "type": "Combat", "hp": 70, "attaque": 80},
    {"nom": "Fantominus", "type": "Spectre/Poison", "hp": 30, "attaque": 35},
    {"nom": "Evoli", "type": "Normal", "hp": 55, "attaque": 55},
]

pokemon_rare = [
    {"nom": "Dracaufeu", "type": "Feu/Vol", "hp": 78, "attaque": 84},
    {"nom": "Tortank", "type": "Eau", "hp": 79, "attaque": 83},
    {"nom": "Florizarre", "type": "Plante/Poison", "hp": 80, "attaque": 82},
    {"nom": "Ronflex", "type": "Normal", "hp": 160, "attaque": 110},
    {"nom": "Carchacrok", "type": "Dragon/Sol", "hp": 108, "attaque": 130},
    {"nom": "Luxray", "type": "Électrik", "hp": 80, "attaque": 120},
    {"nom": "Gardevoir", "type": "Psy/Fée", "hp": 68, "attaque": 65},
    {"nom": "Lucario", "type": "Combat/Acier", "hp": 70, "attaque": 110},
    {"nom": "Simiabraz", "type": "Feu/Combat", "hp": 76, "attaque": 104},
    {"nom": "Torterra", "type": "Plante/Sol", "hp": 95, "attaque": 109},
]

pokemon_legendaire = [
    {"nom": "Mewtwo", "type": "Psy", "hp": 106, "attaque": 110},
    {"nom": "Rayquaza", "type": "Dragon/Vol", "hp": 105, "attaque": 150},
    {"nom": "Kyogre", "type": "Eau", "hp": 100, "attaque": 150},
    {"nom": "Groudon", "type": "Sol", "hp": 100, "attaque": 150},
    {"nom": "Lugia", "type": "Psy/Vol", "hp": 106, "attaque": 90},
    {"nom": "Ho-Oh", "type": "Feu/Vol", "hp": 106, "attaque": 130},
    {"nom": "Arceus", "type": "Normal", "hp": 120, "attaque": 150},
    {"nom": "Giratina", "type": "Spectre/Dragon", "hp": 150, "attaque": 120},
    {"nom": "Dialga", "type": "Acier/Dragon", "hp": 100, "attaque": 120},
    {"nom": "Palkia", "type": "Eau/Dragon", "hp": 90, "attaque": 120},
]

pokemon_obtenus = []

def ouvrirbooster():
    input("🎁 Appuyez sur Entrée pour ouvrir le booster...")  
    booster = []  

    for _ in range(5):  # Tirer 3 cartes
        chance = random.randint(1, 100)  # Tirage de la rareté
        if chance <= 60:
            pokemon = random.choice(pokemon_commun)  # 60% Commun
            rarete = "🟢 Commun"
        elif chance <= 90:
            pokemon = random.choice(pokemon_rare)  # 30% Rare
            rarete = "🔵 Rare"
        else:
            pokemon = random.choice(pokemon_legendaire)  # 10% Légendaire
            rarete = "🟠 Légendaire"
        
        booster.append((pokemon, rarete))

    # Trier du moins rare au plus rare
    booster.sort(key=lambda x: ["🟢 Commun", "🔵 Rare", "🟠 Légendaire"].index(x[1]))

    print("\n✨ Vous avez obtenu :")
    for pokemon, rarete in booster:
        print(f"{rarete} - {pokemon['nom']} ({pokemon['type']}) | HP: {pokemon['hp']} | Attaque: {pokemon['attaque']}")
        pokemon_obtenus.append(pokemon)

# Exécuter la fonction
ouvrirbooster()
