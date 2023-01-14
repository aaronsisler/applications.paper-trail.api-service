# applications.paper-trail.api-service

## Local Development

### PyCharm Run Configuration

- Module Name

  ```commandline
  uvicorn
  ```

- Parameters

  ```commandline
  - main:app --reload
  ```

### Running the OpenApi Generator CLI

- Check version of OpenApi Generator

```bash
pipenv run openapi-generator version
```

- Validate the contract is formatted correctly

```bash
pipenv run openapi-generator validate -i ./contracts/paper-trail-api-service-v1.yaml
```

- Generate the files from contract

```bash
pipenv run openapi-generator generate -g python -i ./contracts/paper-trail-api-service-v1.yaml -o ./app
```
