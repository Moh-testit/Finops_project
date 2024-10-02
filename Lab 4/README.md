# Lab 4
1. Créer un compte de stockage avec différentes options de réplication
Créer un compte de stockage :
Dans le menu de gauche, recherche Comptes de stockage et clique dessus.
Clique sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 14.28.56.png>)


Réplication : Sélectionne l'option de réplication la plus adaptée :
Locally Redundant Storage (LRS) : Réplication à 3 copies dans un seul datacenter.
Geo-Redundant Storage (GRS) : Réplication dans une autre région pour assurer la résilience.
Zone-Redundant Storage (ZRS) : Réplication dans plusieurs zones d'une même région pour résister aux défaillances de zone.
Clique sur Vérifier + Créer puis sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 14.32.02.png>)
![alt text](<Capture d’écran 2024-10-02 à 14.46.34.png>)

2. Télécharger et gérer des blobs via le portail Azure et l'Azure CLI

Créer un conteneur Blob via le portail Azure :
Une fois le compte de stockage créé, accède à ce dernier.
Dans le menu de gauche, sélectionne Conteneurs sous la section Services de données.
Clique sur + Conteneur et donne un nom (ex : mycontainer).
Définis le niveau d'accès (privé, public) en fonction de tes besoins, puis clique sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 14.51.53.png>)
![alt text](<Capture d’écran 2024-10-02 à 14.52.24.png>)

Créer un conteneur Blob via le portail Azure :
Une fois le compte de stockage créé, accède à ce dernier.
Dans le menu de gauche, sélectionne Conteneurs sous la section Services de données.
Clique sur + Conteneur et donne un nom (ex : mycontainer).
Définis le niveau d'accès (privé, public) en fonction de tes besoins, puis clique sur Créer.
--Télécharger des fichiers dans le conteneur via le portail :
Ouvre le conteneur créé (mycontainer).
Clique sur Télécharger et sélectionne les fichiers que tu veux télécharger depuis ton ordinateur.
Les fichiers seront maintenant stockés en tant que blobs dans ce conteneur.
![alt text](<Capture d’écran 2024-10-02 à 14.52.54.png>)
![alt text](<Capture d’écran 2024-10-02 à 14.53.26.png>)
![alt text](<Capture d’écran 2024-10-02 à 14.53.59.png>)
![alt text](<Capture d’écran 2024-10-02 à 14.54.50.png>)

Gérer les blobs via Azure CLI :
Ouvre ton terminal ou PowerShell et connecte-toi à Azure si ce n'est pas déjà fait :
az login

![alt text](<Capture d’écran 2024-10-02 à 14.56.17.png>)
![alt text](<Capture d’écran 2024-10-02 à 14.58.05.png>)

![alt text](<Capture d’écran 2024-10-02 à 15.00.24.png>)

Créer un conteneur via CLI :
Exécute cette commande pour créer un conteneur :
az storage container create --name mycontainer --account-name lab4storageaccount --public-access off
![alt text](<Capture d’écran 2024-10-02 à 15.12.04.png>)

Télécharger un fichier dans un blob via CLI :

Utilise cette commande pour télécharger un fichier dans le conteneur 
az storage blob upload --container-name mycontainer --file /path/to/local/file --name blobname --account-name lab4storageaccount

Lister les blobs dans un conteneur :

Liste tous les blobs du conteneur avec cette commande
az storage blob list --container-name mycontainer --account-name lab4storageaccount --output table

3. Configurer des signatures d'accès partagé (SAS) pour un accès sécurisé
Créer une SAS via le portail Azure :
Accède à ton compte de stockage et clique sur Signatures d'accès partagé dans le menu de gauche.

![alt text](<Capture d’écran 2024-10-02 à 15.32.53.png>)

Clique sur Générer la signature d'accès partagé et les URL.
Copie l'URL SAS générée ou la chaîne de signature et partage-la pour donner accès aux blobs de manière sécurisée.
![alt text](<Capture d’écran 2024-10-02 à 15.33.33.png>)

Créer une SAS via Azure CLI :
Pour générer une SAS avec Azure CLI, utilise la commande suivante :

az storage blob generate-sas --account-name lab4storageaccount --container-name mycontainer --name blobname --permissions r --expiry 2024-10-05 --output tsv

Cette commande génère une SAS pour un blob spécifique avec des permissions de lecture qui expire le 5 octobre 2024.

Utilise l'URL du blob avec la SAS pour accéder au fichier :
https://lab4storageaccount.blob.core.windows.net/mycontainer/blobname?sas_token


4. Implémenter des politiques de gestion du cycle de vie

Configurer la gestion du cycle de vie dans le portail Azure :
Accède à ton compte de stockage.
Dans le menu de gauche, sous Services de données, clique sur Gestion du cycle de vie.
Clique sur + Ajouter une règle pour créer une nouvelle règle.

Active la règle et clique sur Enregistrer.
![alt text](<Capture d’écran 2024-10-02 à 15.51.45.png>)