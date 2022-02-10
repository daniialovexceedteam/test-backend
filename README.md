# data sandbox
sandbox for API requests
#### clone a repo
- git clone https://github.com/daniialovexceedteam/test-backend.git && cd test-backend
#### create .env file
- touch .env
#### add base settings to .env
- POSTGRES_DB=db_name
- POSTGRES_USER=user_name
- POSTGRES_PASSWORD=password
- POSTGRES_HOST=db
- SECRET_KEY=key
- ALLOWED_HOSTS=localhost
#### run docker-compose for the first time
- docker-compose --profile migrations up -d --build
- docker exec -it web python manage.py createsuperuser
#### regular run
- docker-compose up

### DOCS
- localhost/swagger/