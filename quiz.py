import time
import threading

class GameSettings:
    def __init__(self, timer_duration=15):
        self.timer_duration = timer_duration

def sleep_time():
    print("Chargement de votre questionnaire", end="")
    for _ in range(100):
        print(".", end="")
        time.sleep(0.05)
    print(" ")

def pose_question(question, options, reponse_correcte, timer_duration):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    reponse = None
    timer_expired = False

    def get_user_input():
        nonlocal reponse
        reponse = input(f"Votre réponse ({timer_duration}s max): ").lower()

    # Launch the timer in the background
    timer_thread = threading.Thread(target=get_user_input)
    timer_thread.start()

    start_time = time.time()
    timer_thread.join(timer_duration)

    # Check if the timer has expired
    if timer_thread.is_alive():
        timer_expired = True
        print("\nTime's up! La réponse correcte était :", reponse_correcte)

    elapsed_time = time.time() - start_time

    if not timer_expired:
        if reponse == reponse_correcte:
            print("Correct !")
            return 1
        else:
            print(f"Erreur. La réponse correcte était : {reponse_correcte}")
            return 0
    else:
        return 0

def jouer_quiz(settings):
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
        "paris",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de continents y a-t-il sur Terre?",
        ["5", "6", "7", "8"],
        "7",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la couleur du ciel par une journée claire?",
        ["Bleu", "Vert", "Rouge", "Jaune"],
        "bleu",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la plus grande planète de notre système solaire?",
        ["Mercure", "Vénus", "Terre", "Jupiter"],
        "jupiter",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand océan de la planète?",
        ["Atlantique", "Pacifique", "Indien", "Arctique"],
        "pacifique",
        settings.timer_duration
    )

    score += pose_question(
        "Qui a écrit 'Romeo et Juliette'?",
        ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "william shakespeare",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la capitale du Japon?",
        ["Pékin", "Tokyo", "Séoul", "Bangkok"],
        "tokyo",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de côtés a un hexagone?",
        ["4", "5", "6", "7"],
        "6",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la plus grande chaîne de montagnes du monde?",
        ["Himalaya", "Alpes", "Andes", "Rocheuses"],
        "himalaya",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand désert du monde?",
        ["Sahara", "Gobi", "Antarctique", "Karakoum"],
        "antarctique",
        settings.timer_duration
    )

    score += pose_question(
        "Qui a découvert la gravité en observant une pomme tomber?",
        ["Isaac Newton", "Galilée", "Einstein", "Tesla"],
        "isaac newton",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la plus grande île du monde?",
        ["Groenland", "Australie", "Borneo", "Sumatra"],
        "groenland",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de dents permanentes un adulte a-t-il normalement?",
        ["28", "30", "32", "34"],
        "32",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand animal terrestre?",
        ["Éléphant", "Girafe", "Rhinocéros", "Hippopotame"],
        "éléphant",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la première lettre de l'alphabet?",
        ["A", "B", "C", "D"],
        "a",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand lac d'eau douce du monde?",
        ["Lac Supérieur", "Lac Baïkal", "Lac Victoria", "Lac Tanganyika"],
        "lac supérieur",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de jours y a-t-il dans une année bissextile?",
        ["364", "365", "366", "367"],
        "366",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus haut sommet du monde?",
        ["Mont Everest", "Mont Kilimandjaro", "Mont McKinley", "Mont Fuji"],
        "mont everest",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand pays du monde en termes de superficie?",
        ["Russie", "Canada", "États-Unis", "Chine"],
        "russie",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus long fleuve du monde?",
        ["Nil", "Amazone", "Mississippi", "Yangtsé"],
        "nil",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la monnaie officielle du Japon?",
        ["Yen", "Won", "Dollar", "Euro"],
        "yen",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la plus grande ville du monde en population?",
        ["Tokyo", "Pékin", "Delhi", "Mumbai"],
        "tokyo",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de continents commencent par la lettre 'A'?",
        ["1", "2", "3", "4"],
        "2",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand organe du corps humain?",
        ["Cerveau", "Cœur", "Foie", "Peau"],
        "peau",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la devise de la France?",
        ["Liberté, égalité, fraternité", "In God We Trust", "E Pluribus Unum", "Veni, vidi, vici"],
        "liberté, égalité, fraternité",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de côtés a un triangle?",
        ["2", "3", "4", "5"],
        "3",
        settings.timer_duration
    )

    score += pose_question(
        "Qui a peint 'La Joconde'?",
        ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "leonardo da vinci",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le gaz le plus abondant dans l'atmosphère terrestre?",
        ["Azote", "Oxygène", "Argon", "Dioxyde de carbone"],
        "azote",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand mammifère marin?",
        ["Baleine bleue", "Orque", "Requin blanc", "Dauphin"],
        "baleine bleue",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la plus grande île d'Asie?",
        ["Japon", "Sumatra", "Java", "Bornéo"],
        "bornéo",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand lac salé du monde?",
        ["Mer Caspienne", "Lac de la Mer Morte", "Grand Lac Salé", "Lac Assal"],
        "mer caspienne",
        settings.timer_duration
    )

    score += pose_question(
        "Combien de joueurs composent une équipe de football?",
        ["8", "10", "11", "12"],
        "11",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le plus grand océan du monde?",
        ["Atlantique", "Pacifique", "Indien", "Arctique"],
        "pacifique",
        settings.timer_duration
    )

    score += pose_question(
        "Qui a écrit 'Hamlet'?",
        ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "william shakespeare",
        settings.timer_duration
    )

    score += pose_question(
        "Quel est le pays le plus peuplé du monde?",
        ["Inde", "Chine", "États-Unis", "Brésil"],
        "chine",
        settings.timer_duration
    )

    score += pose_question(
        "Quelle est la plus grande cascade du monde?",
        ["Chutes d'Iguaçu", "Chutes Victoria", "Chutes du Niagara", "Angel Falls"],
        "angel falls",
        settings.timer_duration
    )

    # Afficher le score final
    print(f"\nMerci d'avoir joué, {nom}!")
    print(f"Votre score final est de {score} sur 3.")

if __name__ == "__main__":
    game_settings = GameSettings(timer_duration=10)  # Customize timer duration if needed
    jouer_quiz(game_settings)
