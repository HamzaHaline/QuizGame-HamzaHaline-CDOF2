                         # QuizGame-HamzaHaline-CDOF2


## Description
Welcome to the Quiz Game! This is a simple console-based quiz game coded in pygtho  here players can answer a series of questions to test their knowledge in various subjects.The Quiz Game has a user-friendly interface, which makes it easy to play. The game consists of a series of questions, and the player has to choose the correct answer from the given options. The player's score is displayed at the end of the game.

## How to Run the Project
1) Clone the repository to your local machine:
    bash
    git clone https://github.com/your-username/quiz-game.git
    ```

2) Navigate to the project directory:
    ```bash
    cd quiz-game
    ```

3. Run the quiz game:
    ```bash
    python quiz_game.py
    ```

## How to Contribute
We welcome contributions to improve the quiz game! If you'd like to contribute, follow these steps:

1. Fork the repository.

2. Clone your fork to your local machine:
    ```bash
    git clone https://github.com/HamzaHaline/QuizGame-HamzaHaline-CDOF2
    ```

3. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```

4. Make your changes and commit them:
    ```bash
    git add .
    git commit -m "Description of your changes"
    ```

5. Push the changes to your fork:
    ```bash
    git push origin feature-name
    ```

6. Create a pull request on GitHub.


Feel free to download, use, and modify the code to suit your needs. Happy coding!


To make this project you need to follow this step:
## Installation
Install package with pip
```bash
  pip install time
```

## Deployment
To deploy this project run this code or the code in quiz.py
```bash
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

```