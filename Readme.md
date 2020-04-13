# Run local
```
bash deploy/stagin.sh
```

# Deploy Heroku
```
heroku container login
heroku create
heroku container:push web
heroku container:release web
heroku open
```

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/