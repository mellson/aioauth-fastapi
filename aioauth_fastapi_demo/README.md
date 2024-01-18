# Demo server

Demo server was deployed to heroku: [https://aioauth-fastapi.herokuapp.com/api/openapi/](https://aioauth-fastapi.herokuapp.com/api/openapi/)

It can be tested on [https://openidconnect.net/](https://openidconnect.net/) and [https://oidcdebugger.com/](https://oidcdebugger.com/) playgrounds.

### Client credentials of demo server

```
Authorization Endpoint: https://aioauth-fastapi.herokuapp.com/oauth2/authorize
Token endpoint: https://aioauth-fastapi.herokuapp.com/oauth2/token
Client id: be861a8a-7817-4a9e-93d3-9976bf099893
Client secret: 71569cc8-89ea-48c1-adb3-10f831020840
Scopes: read write
```

To start working with the playground, you need to create a new user and log in. `access_token` will be saved in cookies. `access_token` lifetime is 15 minutes.

# Local installation

Use Python 3.8

```
brew install python@3.8
```

Install requirements:

```
pip3.8 install -e ."[dev]"
```

Fix the weird type error in `pydantic`:

```
pip3.8 install --force-reinstall typing-extensions==4.5.0
```

Run database server

```
docker compose up
```

Create .env file (and adjust to your local setup):

```
cp .env.dist .env
```

Create RSA keys for JWT:

```
openssl genrsa -out jwtRSA256-private.pem 2048
openssl rsa -in jwtRSA256-private.pem -pubout -outform PEM -out jwtRSA256-public.pem
```

Apply migrations

```
alembic upgrade head
```

Run local server

```
python3.8 -m aioauth_fastapi_demo
```
