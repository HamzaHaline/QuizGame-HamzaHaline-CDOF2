                         # QuizGame-HamzaHaline-CDOF2


## Description
Welcome to the Quiz Game! This is a simple console-based quiz game coded in python. Here players can answer a series of questions to test their knowledge in various subjects.The game consists of a series of questions, and the player has to choose the correct answer from the given options. The player's score is displayed at the end of the game.

                     ## How to Run the Project
1) Clone the repository to your local machine:
   ```bash
    git clone https://github.com/your-username/quiz-game.git
    ```

2) Navigate to the project directory:
    ```bash
    cd QuizGame-HamzaHaline-CDOF2
    ```

To make this project you need to follow this step:
3) Installation
Install package with pip
```bash
  pip install time
```

4) Deployment
To deploy this project run this code or the code in quiz.py
```bash
    import time

def sleep_time():
    # Display a loading message while simulating a delay
    print("Chargement de votre questionnaire", end="")
    for _ in range(100):
        print(".", end="")
        time.sleep(0.05)
    print(" ")

def pose_question(question, options, reponse_correcte):
    # Display the question and its options
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    # Get the user's response and convert it to lowercase
    reponse = input("Votre réponse : ").lower()

    if reponse == reponse_correcte:
        # Inform the user if the answer is correct
        print("Correct !")
        return 1
    else:
        # Inform the user if the answer is incorrect and display the correct answer
        print(f"Erreur. La réponse correcte était : {reponse_correcte}")
        return 0

def jouer_quiz():
    score = 0

    # Welcome the player
    print("Bienvenue au Quiz!")

    # Get the player's name
    nom = input("Entrez votre nom : ")
    print(f"\nBonjour {nom}!\n")

    # Simulate a loading time
    sleep_time()

    # Start the quiz
    print("D'accord, commençons le quiz!\n")

    # Pose questions and update the score
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

    # Display the final score
    print(f"\nMerci d'avoir joué, {nom}!")
    print(f"Votre score final est de {score} sur 3.")

if __name__ == "__main__":
    # Run the quiz when the script is executed
    jouer_quiz()


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


## Authors
Hamza HALINE - Initial work and maintenance

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Special thanks to Mr.Gwénolé MARTIN for his help building this project
