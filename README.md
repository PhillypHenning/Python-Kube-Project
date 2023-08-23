# Counter app
Extremely simple counter app that counts to 2 minutes and logs every second.
## Local testing
```
cd counter_app
python app.py
```

## Docker
```
cd counter_app
docker build . counter:latest
docker run counter:latest
```

## Docker Compose
```
cd counter_app
docker-compose up
```

# Flask app testing
Example flask web app with a redis sidecar
## Local testing
```
cd flask_app
python -m pip install -r requirements.txt
flask run
```

## Docker
```
cd counter_app
docker build . counter:latest
docker run web:latest
```

## Docker Compose
```
cd counter_app
docker-compose up
```