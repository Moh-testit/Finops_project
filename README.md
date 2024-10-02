# Finops_project
Differents labs projects on Azure cloud
1. Déployer une machine virtuelle Linux dans Azure
Dans le menu de gauche, clique sur Machines virtuelles.
Clique sur Créer puis sur Machine virtuelle.
Dans l'onglet Informations de base :
Sélectionne ton groupe de ressources ou crée-en un.
Choisis un nom pour la VM (ex. : WindowsVM).
Sélectionne Windows Server 2019 Datacenter comme image.
Choisis la taille de la VM (par exemple, une VM de type Standard B1s)
![alt text](<Capture d’écran 2024-10-02 à 10.16.59.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.14.22.png>)

Clique sur Vérifier et créer puis sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 10.15.46.png>)

![alt text](<Capture d’écran 2024-10-02 à 10.17.09.png>)


2. Déployer une machine virtuelle Linux dans Azure
Reprends le même processus pour la VM Linux, en choisissant une distribution comme Ubuntu Server 20.04 LTS.
Configure les paramètres de base (groupe de ressources, nom de la VM, taille, etc.).
Pour la connexion, tu peux générer une clé SSH ou utiliser un mot de passe.

Lors de la création de la VM, Azure te proposera des tailles. Pour un test simple, des tailles comme Standard B1s ou Standard B2s suffisent.

Assure-toi que les ports suivants sont ouverts :
RDP (3389) pour la VM Windows.
SSH (22) pour la VM Linux.
![alt text](<Capture d’écran 2024-10-02 à 10.27.34.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.27.52.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.29.00.png>)


3. Se connecter aux VMs à l’aide de RDP et SSH
____Connexion à la VM Windows via RDP :
Sur le portail Azure, accède à ta VM Windows et note son adresse IP publique.
Sur ton PC local (Windows), lance Remote Desktop Connection (RDP).
Saisis l’adresse IP publique de la VM et connecte-toi avec les informations d'identification que tu as définies (nom d'utilisateur et mot de passe).
____Connexion à la VM Linux via SSH :
Ouvre un terminal (ou un client SSH comme PuTTY sur Windows).
![alt text](<Capture d’écran 2024-10-02 à 10.37.14.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.37.27.png>)

4. Installer des logiciels sur les VMs et prendre des snapshots
a. Installation de logiciels :
Pour la VM Windows :
Une fois connecté via RDP, utilise PowerShell ou l'interface graphique pour installer des logiciels.
Par exemple, pour installer IIS (serveur web), lance PowerShell en tant qu’administrateur et exécute :
Install-WindowsFeature -name Web-Server -IncludeManagementTools
--- Pour la VM Linux :
Une fois connecté via SSH, utilise la commande apt ou yum pour installer des logiciels.
Par exemple, pour installer Apache2 (serveur web), exécute :
sudo apt update
sudo apt install apache2 -y
![alt text](<Capture d’écran 2024-10-02 à 10.40.42.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.41.34.png>)


Prendre un snapshot d’une VM :
Sur le portail Azure, accède à la page de la VM.
Dans le menu de gauche, sélectionne Disques puis choisis le disque que tu veux sauvegarder.
Clique sur Créer un snapshot.
Nomme le snapshot et sélectionne les options de stockage, puis clique sur Créer.
![alt text](<Capture d’écran 2024-10-02 à 10.47.40.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.50.27.png>)
![alt text](<Capture d’écran 2024-10-02 à 10.51.10.png>)