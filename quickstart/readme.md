# QuickStart

## Installation docker (Manjajo / ArchLinux)
``` sudo pacman -S docker ```

## Lancement du premier container Ubuntu

### Solution 1 : 

#### Importer ubuntu depuis un repo
``` docker pull ubuntu ```

#### Puis lancer un container
``` docker run -i -t ubuntu ```

### Solution 2 : Avec un Dockerfile

#### Créer un fichier **Dockerfile**

``` FROM ubuntu ```  

#### Puis construire l'image

``` sudo docker build -t first_docker_test:1.0 . ```

#### Et lancer un container avec l'image créée

``` docker run -i -t first_docker_test:1.0 ```

## Vérifier si le container est bien lancé

``` docker ps ```

### Réultat affiché
``` CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS               NAMES ```  
```746e4faaa019        first_docker_test:1.0   "/bin/bash"         9 seconds ago       Up 8 seconds                            priceless_kilby ```
