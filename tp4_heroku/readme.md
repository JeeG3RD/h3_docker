# Installation de Heroku (Avec snap sous Manjaro)
``` sudo snap install --classic heroku ```

## Connecion à Heroku

``` heroku login ```

## Connexion au Container Registry
``` heroku container:login ```

## Push de l'application

```heroku container:push web --app nom-de-l-app```

## Publication de l'app

```heroku container:release web --app nom-de-l-app```

## Afficher les logs d'une application

``` heroku logs --app nom-de-l-app ```

## (Fix) Important : 

Ajouter ``` --server.port ``` lors du run de streamlit


### Adresse de l'application
https://h3-docker-tp4-jg3rd.herokuapp.com/