import random

class Options:

    f1constructors = {
        "Mercedes" : 37.6
        "Red Bull" : 26.1
        "McLaren" : 18.9
        "Ferrari" : 18.8
        "Aston Martin" : 16.6
        "Alpine" : 15.2
        "Alpha Tauri" : 12.9
        "Alpha Romeo" : 8.9
        "Williams" : 6.3
        "Haas" : 6.1
    }

    f1driver = {
        "L. Hamilton" : 33.3
        "M. Verstappen" : 25.3
        "V. Bottas" : 23.3
        "S. Perez" : 18.3
        "C. Leclerc" : 17.9
        "D. Ricciardo" : 16.3
        "S. Vettel" : 15.0
        "F. Alonso" : 15.0
        "C. Sainz" : 14.4
        "L. Norris" : 13.8
        "L. Stroll" : 13.6
        "P. Gasly" : 11.7
        "E. Occon" : 10.2
        "K. Raikkonen" : 9.3
        "Y. Tsunoda" : 9.0
        "A. Giovinazzi" : 7.8
        "N. Latifi" : 6.4
        "G. Russell" : 6.3
        "M. Schumacher" : 5.7
        "N. Mazepin" : 5.3
    }

    def chooseF1constructor(self):
        f1constructor, price = random.choice(list(f1constructors.items()))
