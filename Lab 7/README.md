# Lab 7
1. Create an Azure Function App.
Dans le menu de gauche, recherche Function App et clique sur + Créer.
![alt text](<Capture d’écran 2024-10-02 à 16.49.00.png>)
![alt text](<Capture d’écran 2024-10-02 à 16.52.20.png>)
![alt text](<Capture d’écran 2024-10-02 à 16.57.11.png>)

2. Développer une fonction déclenchée par une requête HTTP
Accéder à la fonction dans le portail Azure :
Une fois l'application de fonction déployée, accède à celle-ci via le portail Azure.
Dans le tableau de bord de ton application, clique sur + Ajouter une fonction.
Créer une fonction déclenchée par HTTP 
Choisis Déclencheur HTTP comme modèle de fonction.
Nom de la fonction : Donne un nom à ta fonction (par exemple, HttpTriggerFunction).
Méthodes HTTP : Choisis les méthodes HTTP que la fonction doit accepter (par exemple, GET ou POST).
Autorisation : Choisis le type d'autorisation (par exemple, Anonymous pour permettre des appels sans clé API ou Function pour plus de sécurité).

![alt text](<Capture d’écran 2024-10-02 à 19.56.00.png>)
![alt text](<Capture d’écran 2024-10-02 à 20.01.30.png>)

![alt text](<Capture d’écran 2024-10-02 à 20.07.00.png>)
![alt text](<Capture d’écran 2024-10-02 à 20.07.49.png>)

3. Intégrer la fonction avec Azure Storage ou Azure Queue
 Créer un conteneur ou une file d'attente dans Azure Storage :
Accède à Comptes de stockage dans le portail Azure.
Sélectionne ton compte de stockage (celui associé à ton application de fonction) et crée un conteneur Blob ou une file d'attente.
![alt text](<Capture d’écran 2024-10-03 à 09.22.17.png>)
![alt text](<Capture d’écran 2024-10-03 à 10.15.05.png>)

Ajouter une liaison avec Azure Storage (Blob) :
Dans ta fonction, accède à Intégrations et clique sur + Ajouter une liaison.

Choisis Azure Blob Storage comme type de liaison :

Sélectionne Entrée si tu veux lire des données depuis un blob, ou Sortie si tu veux écrire des données dans un blob.
Configure le chemin du conteneur Blob et le nom du fichier cible (tu peux utiliser des paramètres comme {name}.txt).

4. Surveiller la performance et les journaux des fonctions
 Accéder à la surveillance dans le portail Azure :
 ![alt text](<Capture d’écran 2024-10-03 à 10.23.48.png>)

 . Vérifier les journaux en temps réel :
Pour consulter les journaux en temps réel, utilise Live Metrics Stream ou va dans l'onglet Console de Log Stream.![alt text](<Capture d’écran 2024-10-03 à 10.25.43.png>)
