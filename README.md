# data sandbox
sandbox for API requests
#### clone a repo
- git clone
#### create .env file
- touch .env
#### add base settings to .env
- POSTGRES_DB=db_name
- POSTGRES_USER=user_name
- POSTGRES_PASSWORD=password
- POSTGRES_HOST=db
- SECRET_KEY=key
- ALLOWED_HOSTS=localhost
#### run docker-compose
- docker-compose up -d --build