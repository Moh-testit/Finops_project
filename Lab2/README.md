# Lab 2
 1. Créer un réseau virtuel (VNet) avec plusieurs sous-réseaux
b. Créer un Virtual Network (VNet) :
Dans le menu de gauche, clique sur Réseaux virtuels.
Clique sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 11.27.19.png>)
Dans l'onglet Adresses IP, configure la plage d'adresses du VNet (par exemple, 10.0.0.0/16).
Répète l'opération pour créer plusieurs sous-réseaux.
Clique sur Vérifier + créer puis sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 11.28.18.png>)

2. Configurer les groupes de sécurité réseau (NSG)

a. Créer un NSG :
Dans le portail Azure, recherche Groupes de sécurité réseau.
Clique sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 11.34.03.png>)
![alt text](<Capture d’écran 2024-10-02 à 11.34.44.png>)
b. Configurer les règles du NSG :
Une fois le NSG créé, clique dessus.
Sous Paramètres, va dans Règles de sécurité entrante.
Ajoute des règles comme :
Autoriser le RDP (port 3389) pour la VM Windows.
Autoriser le SSH (port 22) pour la VM Linux.
![alt text](<Capture d’écran 2024-10-02 à 11.37.54.png>)
![alt text](<Capture d’écran 2024-10-02 à 11.41.19.png>)
![alt text](<Capture d’écran 2024-10-02 à 11.42.33.png>)

3. Déployer des VMs dans des sous-réseaux spécifiques
![alt text](<Capture d’écran 2024-10-02 à 11.46.02.png>)
![alt text](<Capture d’écran 2024-10-02 à 11.53.08.png>)

4. Configurer le VNet Peering entre deux VNets

a. Créer un deuxième VNet :
Reprends le même processus pour créer un autre VNet (ex : Lab2VNet2) avec une plage d'adresses différente (par exemple, 10.1.0.0/16).
Crée également des sous-réseaux dans ce VNet (par exemple, 10.1.1.0/24).
![alt text](<Capture d’écran 2024-10-02 à 12.06.31.png>)
![alt text](<Capture d’écran 2024-10-02 à 12.16.59.png>)