# tap-bynder
Singer tap for extracting from Bynder API (https://bynder.docs.apiary.io/#introduction/definitions)

## Setup

`python3 setup.py install`

## Running the tap

#### Discover mode:

`tap-bydner --config config.json --discover > catalog.json`

#### Sync mode:

`tap-bydner --config config.json -p catalog.json -s state.json`
