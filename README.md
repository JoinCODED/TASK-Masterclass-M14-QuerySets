# QuerySets

Searching... Aggregating... Indexing...

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M14-QuerySets).
2. Make sure to have `python 3.9.13` installed (use `pyenv install 3.9.13` to ensure it is installed).
3. Install the project dependencies using `poetry install`.
4. Run the migrations using `poetry run manage migrate`.

## Mocking Data

1. Create a database using `psql`:
   - `psql -d postgres`
   - `CREATE DATABASE music_task;`
2. Create a `.env` file inside the project.
   - Add `DEBUG=False`
   - Add `DATABASE_URL=postgres://username:password@localhost:5432/music_task`
3. Open the database using `poetry run manage dbshell`.
4. Load the mock data using `\i ./fixtures/main.sql`.
   - Note: you might some errors, ignore them.

## QuerySet Task I

Use the following [reference](https://docs.djangoproject.com/en/4.0/ref/models/querysets/) to your advantage.

### Album QuerySets

1. Go to `albums.models.py`.
2. Go to `Album.singles`, this is a computed property.
   - Add the correct queryset to return the songs belonging to this album.
   - HINT 1: use `self` to refer to the current instance of album.
   - HINT 2: songs are related to an instance of albums through the name `songs`.
3. Go to the next computed property `features`.
   - Add the correct queryset to return the songs belonging to this album that contain the word `feat` (case-insensitive) in their name.
   - HINT: you will need to use the `contain` lookup.
4. Go to the next computed property `top_single`.
   - Get the top single sold in this album based on `Song.purchase_count` (i.e., the highest `purchase_count` is the top single).
   - If there are two songs that have the same purchase count then take any one by random.
   - HINT: you will need to filter the related `songs` by `is_single`, order the query set by `purchase_count` and take the highest one.
   - NOTE: we are only looking at singles (i.e., `Song.is_single == True`).

### Band QuerySets

1. Go to `bands.models.py`.
2. Go to `Band.singles`.
   - Add the correct queryset to return the singles belonging to this album.
   - A single is not directly related to the band, you need to filter by the intermediate model Album.
   - NOTE: remember that we need `is_single=True`.
3. Go to `Band.features`.
   - Get all the songs that have `feat` in their `name`.
   - HINT: you will need to use the `contain` lookup.
4. Go to `Band.top_single`.
   - Get all the singles related to this band.
   - Filter them by `is_single=True`.
   - Sort them by `purchase_count`.
   - Select the highest purchase count single.
   - If there are two songs that have the same purchase count then take any one by random.
   - If there are no `feature` songs at all, return `None`

#### Band QuerySets Bonus

1. Go to `Band.top_single`.
2. Get all the songs related to this band that have `feat` in their name.
3. Sort them by `purchase_count`.
4. Select the highest purchase count single.
5. If there are two songs that have the same purchase count then take any one by random.
6. If there are no singles at all, return `None`
