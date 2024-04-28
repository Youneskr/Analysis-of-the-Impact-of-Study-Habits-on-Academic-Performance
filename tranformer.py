import itertools

dictionnaire_de_transformation = {
    "Niveau scolaire": {
        "label" : "Niveau",
        "choix": {
            "Collège": 1,
            "Lycée": 2,
            "Enseignement supérieur": 3
        }
    },
    "Quelle est votre moyenne actuelle ?": {
        "label" : "Moy",
        "choix": {
            "Moins de 10": 5,
            "10 à 12": 11,
            "12 à 14": 13,
            "Plus de 14": 17
        }
    },
    "Combien de fois avez-vous redoublé ?": {
        "label": "Redoublement",
        "choix": {
            "Aucun": 0,
            "Une fois": 1,
            "Deux fois": 2,
            "Trois fois ou plus": 3
        }
    },
    "Combien d'heures consacrez-vous à la révision par jour ? " : {
        "label": "Revision",
        "choix": {
            "Moins d'une heure": 0.5,
            "1 à 2 heures": 1.5,
            "2 à 3 heures": 2.5,
            "Plus de 3 heures": 4
        }
    },
    "Préférez-vous étudier seul(e) ou en groupe ? ": {
        "label": "RevisionType",
        "choix": {
            "Seul(e)": 1,
            "En groupe": 2,
            "Les deux": 3
        }
    },
    "Quels types de documents ou de matériaux, révisez-vous le plus souvent ?": {
        "label": "Documents",
        "choix": {
            "Livres/textes académiques": 1,
            "Notes de cours": 2,
            "Articles de recherche": 3,
            "Tous": 4,
        }
    },
    "Quels sont vos environnements de révision préférés ?": {
        "label": "Env",
        "choix": {
            "Bibliothèque": 1,
            "Chambre": 2,
            "Café": 3,
            "Tous": 4
        }
    },
    "Quelle est votre méthode de prise de notes pendant la révision ?": {
        "label": "RevisionMethod",
        "choix": {
            "Prise de notes manuscrites": 1,
            "Prise de notes sur un ordinateur/tablette": 2,
            "Enregistrement vidéo/audio": 3,
            "Tous": 4
        }
    },
    "À quelle fréquence relisez-vous vos notes après les avoir prises ?": {
        "label": "RevisionFreq",
        "choix": {
            "Jamais": 1,
            "Rarement": 2,
            "De temps en temps": 3,
            "Souvent": 4
        }
    },
    "Comment gérez-vous les distractions pendant la révision ? ": {
        "label": "DistractionsAvoid",
        "choix": {
            "Élimination des distractions (éteindre téléphone, fermer les fenêtres, etc.)": 1,
            "utilisation de techniques de concentration (comme la méthode Pomodoro)": 2,
            "Acceptation des distractions et poursuite de la révision malgré celles-ci": 3
        }
    }, 
    "Combien de pauses prenez-vous pendant une session de révision d'une heure ?": {
        "label": "Pause",
        "choix": {
            "Aucune pause": 0,
            "1 pause": 1,
            "2 pauses": 2,
            "3 pauses ou plus": 3
        }
    },
    "Comment évaluez-vous votre niveau de concentration pendant la révision ?": {
        "label": "Concentration",
        "choix": {
            "Très concentré(e)": 1,
            "Moyennement concentré(e)": 2,
            "Peu concentré(e)": 3,
            "Pas du tout concentré(e)": 4
        }
    }
}


dictionnaire_des_etiquettes ={
    "Niveau scolaire": "Niveau",
    "Quelle est votre moyenne actuelle ?": "Moy",
    "Combien de fois avez-vous redoublé ?": "Redoublement",
    "Combien d'heures consacrez-vous à la révision par jour ? " : "Revision",
    "Préférez-vous étudier seul(e) ou en groupe ? ": "RevisionType",
    "Quels types de documents ou de matériaux, révisez-vous le plus souvent ?": "Documents",
    
    "Quels sont vos environnements de révision préférés ?": "Env",
    "Quelle est votre méthode de prise de notes pendant la révision ?": "RevisionMethod",
    
    "À quelle fréquence relisez-vous vos notes après les avoir prises ?": "RevisionFreq",
    "Comment gérez-vous les distractions pendant la révision ? ": "DistractionsAvoid", 
    "Combien de pauses prenez-vous pendant une session de révision d'une heure ?": "Pause",
    "Comment évaluez-vous votre niveau de concentration pendant la révision ?": "Concentration"
}


