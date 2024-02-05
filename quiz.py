import time

def sleep_time():
    print("Chargement de votre questionnaire", end="")
    for _ in range(100):
        print(".", end="")
        time.sleep(0.05)
    print(" ")

def pose_question(question, options, reponse_correcte):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    reponse = input("Your answer: ").lower().strip()

    if reponse == reponse_correcte:
        print("Correct !")
        return 1
    else:
        print(f"Erreur. La réponse correcte était : {reponse_correcte}")
        return 0

def jouer_quiz():
    score = 0

    print("Bienvenue au Quiz!")

    nom = input("Entrez votre nom : ")
    print(f"\nBonjour {nom}!\n")

    sleep_time()

    print("D'accord, commençons le quiz!\n")

    # Pose de questions
    score += pose_question(
        "Quel est la capitale de la France?",
        ["Paris", "Londres", "Berlin", "Madrid"],
        "paris"
    )

    score += pose_question(
        "Combien de continents y a-t-il sur Terre?",
        ["5", "6", "7", "8"],
        "7"
    )

    score += pose_question(
        "Quelle est la couleur du ciel par une journée claire?",
        ["Bleu", "Vert", "Rouge", "Jaune"],
        "bleu"
    )
    score += pose_question(
    "Quelle est la plus grande planète de notre système solaire?",
    ["Mercure", "Vénus", "Terre", "Jupiter"],
    "jupiter"
    )

    score += pose_question(
    "Quel est le plus grand océan de la planète?",
    ["Atlantique", "Pacifique", "Indien", "Arctique"],
    "pacifique"
    )      

    score += pose_question(
    "Qui a écrit 'Romeo et Juliette'?",
    ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    "william shakespeare"
    )

    score += pose_question(
    "Quelle est la capitale du Japon?",
    ["Pékin", "Tokyo", "Séoul", "Bangkok"],
    "tokyo"
    )
    score += pose_question(
    "Combien de côtés a un hexagone?",
    ["4", "5", "6", "7"],
    "6"
    )

    score += pose_question(
    "Quelle est la plus grande chaîne de montagnes du monde?",
    ["Himalaya", "Alpes", "Andes", "Rocheuses"],
    "himalaya"
    )

    score += pose_question(
    "Quel est le plus grand désert du monde?",
    ["Sahara", "Gobi", "Antarctique", "Karakoum"],
    "antarctique"
    )  

    score += pose_question(
    "Qui a découvert la gravité en observant une pomme tomber?",
    ["Isaac Newton", "Galilée", "Einstein", "Tesla"],
    "isaac newton"
    )

    score += pose_question(
    "Quelle est la plus grande île du monde?",
    ["Groenland", "Australie", "Borneo", "Sumatra"],
    "groenland"
    )

    score += pose_question(
    "Combien de dents permanentes un adulte a-t-il normalement?",
    ["28", "30", "32", "34"],
    "32"
    )

    score += pose_question(
    "Quel est le plus grand animal terrestre?",
    ["Éléphant", "Girafe", "Rhinocéros", "Hippopotame"],
    "éléphant"
    )

    score += pose_question(
    "Quelle est la première lettre de l'alphabet?",
    ["A", "B", "C", "D"],
    "a"
    )

    score += pose_question(
    "Quel est le plus grand lac d'eau douce du monde?",
    ["Lac Supérieur", "Lac Baïkal", "Lac Victoria", "Lac Tanganyika"],
    "lac supérieur"
    )

    score += pose_question(
    "Combien de jours y a-t-il dans une année bissextile?",
    ["364", "365", "366", "367"],
    "366"
    )

    score += pose_question(
    "Quel est le plus haut sommet du monde?",
    ["Mont Everest", "Mont Kilimandjaro", "Mont McKinley", "Mont Fuji"],
    "mont everest"
    )

    score += pose_question(
    "Quel est le plus grand pays du monde en termes de superficie?",
    ["Russie", "Canada", "États-Unis", "Chine"],
    "russie"
    )

    score += pose_question(
    "Quel est le plus long fleuve du monde?",
    ["Nil", "Amazone", "Mississippi", "Yangtsé"],
    "nil"
    )

    score += pose_question(
    "Quelle est la monnaie officielle du Japon?",
    ["Yen", "Won", "Dollar", "Euro"],
    "yen"
    )  

    score += pose_question(
    "Quelle est la plus grande ville du monde en population?",
    ["Tokyo", "Pékin", "Delhi", "Mumbai"],
    "tokyo"
    )

    score += pose_question(
    "Combien de continents commencent par la lettre 'A'?",
    ["1", "2", "3", "4"],
    "2"
    )

    score += pose_question(
    "Quel est le plus grand organe du corps humain?",
    ["Cerveau", "Cœur", "Foie", "Peau"],
    "peau"
    )

    score += pose_question(
    "Quelle est la devise de la France?",
    ["Liberté, égalité, fraternité", "In God We Trust", "E Pluribus Unum", "Veni, vidi, vici"],
    "liberté, égalité, fraternité"
    )

    score += pose_question(
    "Combien de côtés a un triangle?",
    ["2", "3", "4", "5"],
    "3"
    )

    score += pose_question(
    "Qui a peint 'La Joconde'?",
    ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
    "leonardo da vinci"
    )

    score += pose_question(
    "Quel est le gaz le plus abondant dans l'atmosphère terrestre?",
    ["Azote", "Oxygène", "Argon", "Dioxyde de carbone"],
    "azote"
    )

    score += pose_question(
    "Quel est le plus grand mammifère marin?",
    ["Baleine bleue", "Orque", "Requin blanc", "Dauphin"],
    "baleine bleue"
    )

    score += pose_question(
    "Quelle est la plus grande île d'Asie?",
    ["Japon", "Sumatra", "Java", "Bornéo"],
    "bornéo"
    )

    score += pose_question(
    "Quel est le plus grand lac salé du monde?",
    ["Mer Caspienne", "Lac de la Mer Morte", "Grand Lac Salé", "Lac Assal"],
    "mer caspienne"
    )

    score += pose_question(
    "Combien de joueurs composent une équipe de football?",
    ["8", "10", "11", "12"],
    "11"
    )

    score += pose_question(
    "Quel est le plus grand océan du monde?",
    ["Atlantique", "Pacifique", "Indien", "Arctique"],
    "pacifique"
    )

    score += pose_question(
    "Qui a écrit 'Hamlet'?",
    ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    "william shakespeare"
    )

    score += pose_question(
    "Quel est le pays le plus peuplé du monde?",
    ["Inde", "Chine", "États-Unis", "Brésil"],
    "chine"
    )

    score += pose_question(
    "Quelle est la plus grande cascade du monde?",
    ["Chutes d'Iguaçu", "Chutes Victoria", "Chutes du Niagara", "Angel Falls"],
    "angel falls"
    )
    # Afficher le score final
    print(f"\nMerci d'avoir joué, {nom}!")
    print(f"Votre score final est de {score} sur 3.")

if __name__ == "__main__":
    jouer_quiz()
