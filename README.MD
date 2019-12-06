# Simple python app with redis

## To build the app please type following commands after going inside the root directory

```docker
docker build -t <yourappname> .
```

## After the above code , we can run the redis server using the docker network host 

```docker
docker run --network=host redis
```

## After running redis server in docker,we can run our app

```docker
docker run -it --network=host <yourappname>
```
