"""
Rapport sur l’Analyse de l’Impact des Habitudes d’Étude sur la Performance Académique
Réalisé par : Younes KORBI, Ahmed ABBASSI

ISITCom, Sousse
"""


from tranformer import dictionnaire_de_transformation, dictionnaire_des_etiquettes
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_squared_error


def trouver_valeurs_aberrantes(dataset, dictionnaire_de_transformation):
    valeurs_aberrantes = []
    for index, ligne in dataset.iterrows():
        for colonne, valeur in ligne.items():
            if valeur not in dictionnaire_de_transformation[colonne]["choix"].keys() and not pd.isnull(valeur):
                valeurs_aberrantes.append({
                    "valeur": valeur,
                    "ligne": index,
                    "colonne": colonne 
                })
    return valeurs_aberrantes

def trouver_valeurs_manquantes(dataset, dictionnaire_de_transformation):
    valeurs_manquantes = []

    for index, ligne in dataset.iterrows():
        for colonne, valeur in ligne.items():
            if pd.isnull(valeur):
                valeurs_manquantes.append({
                    "ligne": index,
                    "colonne": colonne 
                })

    return valeurs_manquantes

def gestion_des_valeurs_aberrantes(dataset, dictionnaire_de_transformation):
    valeurs_aberrantes = trouver_valeurs_aberrantes(df, dictionnaire_de_transformation)
    for elem in valeurs_aberrantes:
        dataset.loc[elem["ligne"], elem["colonne"]] = None  

def gestion_des_valeurs_manquantes(dataset, dictionnaire_de_transformation):
    valeurs_manquantes =  trouver_valeurs_manquantes(dataset, dictionnaire_de_transformation)

    mean_moy = dataset["Moy"].mean()
    median_revision = dataset["Revision"].median()

    env = round(dataset["Env"].mean())
    doc = round(dataset["Documents"].mean())

    for ligne in valeurs_manquantes:
        if ligne["colonne"] == "Moy":
            dataset.loc[ligne["ligne"], ligne["colonne"]] = mean_moy
        elif ligne["colonne"] == "Revision":
            dataset.loc[ligne["ligne"], ligne["colonne"]] = median_revision
        elif ligne["colonne"] == "Env":
            dataset.loc[ligne["ligne"], ligne["colonne"]] = env
        elif ligne["colonne"] == "Documents":
            dataset.loc[ligne["ligne"], ligne["colonne"]] = doc

def afficher_infos_dataset(dataset, dictionnaire_de_transformation, TRANSFORMATION=False):
    nb_lignes, nb_colonnes = dataset.shape
    print(f"Nombre de lignes dans l'ensemble de données : {nb_lignes}")
    print(f"Nombre de colonnes dans l'ensemble de données : {nb_colonnes}")

    # Trouver les valeurs aberrantes et les valeurs manquantes
    valeurs_aberrantes = []
    if TRANSFORMATION == False:
        valeurs_aberrantes = trouver_valeurs_aberrantes(dataset, dictionnaire_de_transformation)
   
    valeurs_manquantes = trouver_valeurs_manquantes(dataset, dictionnaire_de_transformation)

    # Afficher le nombre de valeurs aberrantes
    nb_valeurs_aberrantes = len(valeurs_aberrantes)
    print(f"Nombre de valeurs aberrantes : {nb_valeurs_aberrantes}")

    # Afficher le nombre de valeurs manquantes
    nb_valeurs_manquantes = len(valeurs_manquantes)
    print(f"Nombre de valeurs manquantes : {nb_valeurs_manquantes}")

    # Affichage des valeurs aberrantes
    if valeurs_aberrantes:
        print("\nValeurs aberrantes :")
        for valeur_aberrante in valeurs_aberrantes:
            print(f"Valeur : {valeur_aberrante['valeur']}, Ligne : {valeur_aberrante['ligne']}, Colonne : {valeur_aberrante['colonne']}")
    
    # Affichage des valeurs manquantes
    if valeurs_manquantes:
        print("\nValeurs manquantes :")
        for valeur_manquante in valeurs_manquantes:
            print(f"Ligne : {valeur_manquante['ligne']}, Colonne : {valeur_manquante['colonne']}")

def nettoyage(dataset, dictionnaire_de_transformation):
    gestion_des_valeurs_aberrantes(dataset, dictionnaire_de_transformation)
    gestion_des_valeurs_manquantes(dataset, dictionnaire_de_transformation)

def transformation(dataset, dictionnaire_de_transformation):
    def convertir_niveau_scolaire(value):
        if value == "Collège":
            return 0
        elif value == "Lycée":
            return 1
        elif value == "Enseignement supérieur":
            return 2
        else:
            return np.nan

    def convertir_moyenne(value):
        if value == 'Moins de 10':
            return 5
        elif value == '10 à 12':
            return 11
        elif value == '12 à 14':
            return 13
        elif value == 'Plus de 14':
            return 15
        else:
            return np.nan

    def convertir_heure(value):
        if value == "Moins d'une heure":
            return 0.5
        elif value == "1 à 2 heures":
            return 1.5
        elif value == "2 à 3 heures":
            return 2.5
        elif value == "Plus de 3 heures":
            return 4
        else:
            return np.nan

    def convertir_redoublement(value):
        if value == "Aucun":
            return 0
        elif value == "Une fois":
            return 1
        elif value == "Deux fois":
            return 2
        elif value == "Trois fois ou plus":
            return 3
        else:
            return np.nan

    def convertir_preference(value):
        if value == "Seul(e)":
            return 1
        elif value == "En groupe":
            return 2
        elif value == "Les deux":
            return 3
        else:
            return np.nan

    def convertir_document(value):
        if value == "Livres/textes académiques":
            return 0
        elif value == "Notes de cours":
            return 1
        elif value == "Articles de recherche":
            return 2
        elif value == "Tous":
            return 3
        else:
            return np.nan

    def convertir_env(value):
        if value == "Bibliothèque":
            return 1
        elif value == "Chambre":
            return 2
        elif value == "Café":
            return 3
        elif value == "Tous":
            return 4
        else:
            return np.nan

    def convertir_revision_method(value):
        if value == "Prise de notes manuscrites":
            return 1
        elif value == "Prise de notes sur un ordinateur/tablette":
            return 2
        elif value == "Enregistrement vidéo/audio":
            return 3
        elif value == "Tous":
            return 4
        else:
            return np.nan

    def convertir_revision_freq(value):
        if value == "Jamais":
            return 1
        elif value == "Rarement":
            return 2
        elif value == "De temps en temps":
            return 3
        elif value == "Souvent":
            return 4
        else:
            return np.nan

    def convertir_distractions(value):
        if value == "Élimination des distractions (éteindre téléphone, fermer les fenêtres, etc.)":
            return 0
        elif value == "utilisation de techniques de concentration (comme la méthode Pomodoro)":
            return 1
        elif value == "Acceptation des distractions et poursuite de la révision malgré celles-ci":
            return 2
        else:
            return np.nan

    def convertir_pauses(value):
        if value == "Aucune pause":
            return 0
        elif value == "1 pause":
            return 1
        elif value == "2 pauses":
            return 2
        elif value == "3 pauses ou plus":
            return 3
        else:
            return np.nan

    def convertir_concentration(value):
        if value == "Très concentré(e)":
            return 0
        elif value == "Moyennement concentré(e)":
            return 1
        elif value == "Peu concentré(e)":
            return 2
        elif value == "Pas du tout concentré(e)":
            return 3
        else:
            return np.nan
        
    dataset['Niveau scolaire'] = dataset['Niveau scolaire'].apply(convertir_niveau_scolaire)
    dataset['Quelle est votre moyenne actuelle ?'] = dataset['Quelle est votre moyenne actuelle ?'].apply(convertir_moyenne)
    dataset["Combien d'heures consacrez-vous à la révision par jour ? "] = dataset["Combien d'heures consacrez-vous à la révision par jour ? "].apply(convertir_heure)
    dataset["Combien de fois avez-vous redoublé ?"] = dataset["Combien de fois avez-vous redoublé ?"].apply(convertir_redoublement)
    dataset["Préférez-vous étudier seul(e) ou en groupe ? "] = dataset["Préférez-vous étudier seul(e) ou en groupe ? "].apply(convertir_preference)
    dataset["Quels types de documents ou de matériaux, révisez-vous le plus souvent ?"] = dataset["Quels types de documents ou de matériaux, révisez-vous le plus souvent ?"].apply(convertir_document)
    dataset["Quels sont vos environnements de révision préférés ?"] = dataset["Quels sont vos environnements de révision préférés ?"].apply(convertir_env)
    dataset["Quelle est votre méthode de prise de notes pendant la révision ?"] = dataset["Quelle est votre méthode de prise de notes pendant la révision ?"].apply(convertir_revision_method)
    dataset["À quelle fréquence relisez-vous vos notes après les avoir prises ?"] = dataset["À quelle fréquence relisez-vous vos notes après les avoir prises ?"].apply(convertir_revision_freq)
    dataset["Comment gérez-vous les distractions pendant la révision ? "] = dataset["Comment gérez-vous les distractions pendant la révision ? "].apply(convertir_distractions)
    dataset["Combien de pauses prenez-vous pendant une session de révision d'une heure ?"] = dataset["Combien de pauses prenez-vous pendant une session de révision d'une heure ?"].apply(convertir_pauses)
    dataset["Comment évaluez-vous votre niveau de concentration pendant la révision ?"] = dataset["Comment évaluez-vous votre niveau de concentration pendant la révision ?"].apply(convertir_concentration)

    df.rename(columns=dictionnaire_des_etiquettes, inplace=True)

def drop(dataset, tableaucolonnes):
    for item in tableaucolonnes:
        dataset = dataset.drop(item, axis=1)

def pretraitement(dataset, dictionnaire_de_transformation):
    nettoyage(dataset, dictionnaire_de_transformation)
    transformation(dataset, dictionnaire_de_transformation)



if __name__ == '__main__':
    df= pd.read_csv("dataset.CSV")
    df = df.drop('Horodateur', axis=1)
    
    print("Affichage avant gestion des valeurs aberrantes :")
    afficher_infos_dataset(df, dictionnaire_de_transformation)
    print("\n-------------------------------------------\n")

    print("Affichage après gestion des valeurs aberrantes :")
    gestion_des_valeurs_aberrantes(df, dictionnaire_de_transformation)
    afficher_infos_dataset(df, dictionnaire_de_transformation)
    print("\n-------------------------------------------\n")

    print("Transformation :")
    transformation(df, dictionnaire_de_transformation)
    # print("\n-------------------------------------------\n")

    gestion_des_valeurs_manquantes(df, dictionnaire_de_transformation)
    print("\n-------------------------------------------\n")

    print("Affichage aprés gestion des valeurs manquantes :")
    afficher_infos_dataset(df, dictionnaire_de_transformation, True)
    print("\n-------------------------------------------\n")

    print("Réduction de dimentionnal :")

    y = df['Moy']
    X = df.drop(["Moy","Niveau", "Redoublement"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    model = LinearRegression()
    model.fit(X_train, y_train)
    # score = model.score(X, y)
    predictions = model.predict(X_test)

    # Calcul de l'erreur absolue moyenne (MAE)
    mae = mean_absolute_error(y_test, predictions)
    # Calcul de l'erreur quadratique moyenne (MSE)
    mse = mean_squared_error(y_test, predictions)
    # Calcul du score R2
    r2 = r2_score(y_test, predictions)

    # Affichage des résultats
    print(predictions)
    print(f"MAE: {mae}")
    print(f"MSE: {mse}")
    print(f"R2 score: {r2}")
    print(f"score: {model.score(X_test, y_test)}")

    def predire_la_moyenne(model,Revision=1.5, RevisionType=3, Documents=2, Env=2, RevisionMethod=2, RevisionFreq=2, DistractionsAvoid=1, Pause=2, Concentration=0): 
        x = np.array([Revision,RevisionType, Documents, Env, RevisionMethod, RevisionFreq, DistractionsAvoid, Pause, Concentration]).reshape(1, -1)
        print(f"Predicted average: {model.predict(x)[0]}") 

    predire_la_moyenne(model)

    # GENERER DES FIGURES

    # transposed_df = df.groupby("Documents")["Moy"].mean().transpose()

    # # Créer une figure et un axe
    # fig, ax = plt.subplots(figsize=(10, 6))

    # # Trier les données
    # sorted_df = df.groupby("Documents")["Moy"].mean().sort_values(ascending=False)

    # # Définir les couleurs
    # colors = plt.cm.tab10(np.arange(len(sorted_df)))

    # # Tracer le graphique à barres avec les données transposées et les couleurs définies
    # bars = ax.bar(range(len(sorted_df)), sorted_df, color=colors)

    # # Ajouter les étiquettes de moyenne au-dessus de chaque barre
    # for bar in bars:
    #     height = bar.get_height()
    #     ax.annotate(f"{height:.1f}", xy=(bar.get_x() + bar.get_width() / 2, height),
    #                 xytext=(0, 3), textcoords="offset points",
    #                 ha='center', va='bottom', fontsize=18)

    # # Définir les labels et le titre du graphique
    # ax.set_xlabel("Documents utilisées pour la revision", weight='bold', fontsize=17)
    # ax.set_ylabel("Moyenne", weight='bold', fontsize=17)

    # # Supprimer les étiquettes de l'axe des x
    # ax.set_xticks([])

    # # Créer une légende pour identifier chaque couleur

    # # legend_labels = ['utilisation de techniques de concentration','Élimination des distractions','Acceptation des distractions','Notes sur un ordinateur']
    # legend_labels = sorted_df.index

    # plt.legend(bars, legend_labels, loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=18)
    
    # plt.margins(0.1, 0.1)

    # # Afficher le graphique
    # plt.savefig("exemple.png", format="svg", bbox_inches='tight', pad_inches=0.1)
    # plt.show()