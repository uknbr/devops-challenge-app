![Docker Image](https://img.shields.io/badge/image%20name-uknbr%2Fdevops--challenge-blue)
![Image Version](https://img.shields.io/docker/v/uknbr/devops-challenge?sort=date)
![Docker Pulls](https://img.shields.io/docker/pulls/uknbr/devops-challenge)
![Docker Stars](https://img.shields.io/docker/stars/uknbr/devops-challenge)
![Docker Image Size](https://img.shields.io/docker/image-size/uknbr/devops-challenge?sort=date)

## Challenge Instructions - Phase 1
```sh
docker run -dti --name challenge uknbr/devops-challenge:2
docker exec -ti challenge bash
```

# Challenge App - Phase 2

## Install Dependencies

```sh
$ pip install -r requirements.txt
```

## Run

```sh
$ python myapp.py
```

### /stat
- Return service status: **SUCCESS** or **ERROR**

### /code
- Return from variable **CODE**

### /info
- Return from variable **NAME**
- Return current hostname
- Return a joke for programmers
