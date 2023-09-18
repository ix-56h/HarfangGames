### How to run

Clone the repo and run `docker-compose up`

### TODO :
- [ ] Fix alembic autogenerate, declarative_base dependancy is not correctly imported.
- [ ] Process model validation within pydantic instead of validating data within crud/controllers
- [ ] Add fuzzy validator for game names
- [ ] Add a new Endpoint to filter games by years, best sellers, studios or platforms.
- [ ] Add One to Many foreign keys for platforms and studios
    - [ ] Create new models for platforms and studios
- [ ] Write basic tests

- [x] Implement Game model
- [x] Create dockerfile and docker compose
- [x] Alembic integration *(partially implemented)
    - [x] First migration (Not auto generated, need to fix issue with env.py)
- [x] Pydantic models
- [x] CRUD implementation for Game model
    - [x] Search by name (Like statement, no fuzzing)
    - [x] Create
    - [x] Get by name 
    - [x] Get by ID
    - [x] Get all
- [x] Basic Logging
- [x] Secure secret with .env within docker
- [x] Git ignore for fastapi Project


