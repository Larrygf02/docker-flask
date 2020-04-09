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