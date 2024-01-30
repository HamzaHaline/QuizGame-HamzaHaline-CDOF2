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

    reponse = input("Votre réponse : ").lower()

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

    # Afficher le score final
    print(f"\nMerci d'avoir joué, {nom}!")
    print(f"Votre score final est de {score} sur 3.")

if __name__ == "__main__":
    jouer_quiz()
