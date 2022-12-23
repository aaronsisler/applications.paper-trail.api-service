# Local RDS instance

## Docker Commands

Start the MySQL Database container

```
docker-compose -f ./docker-rds/docker-compose.yml --env-file ./docker-rds/.env.local up -d
```

Stop the MySQL Database container

```
docker-compose -f ./docker-rds/docker-compose.yml --env-file ./docker-rds/.env.local down
```

--env-file ./config/.env.dev
