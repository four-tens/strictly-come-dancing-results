# strictly-come-dancing-results

[![Build Status](https://travis-ci.org/mrwilson/strictly-come-dancing-results.svg?branch=master)](https://travis-ci.org/mrwilson/strictly-come-dancing-results)

The [Strictly Come Dancing](http://www.bbc.co.uk/strictlycomedancing/) Results Open Dataset

## Contents

 * Celebrities
 * Professionals
 * Results

## Reading into a database

Using PostgreSQL

```sql
CREATE DATABASE strictly_results;

\connect strictly_results;

CREATE TABLE IF NOT EXISTS results (
    celebrity_id INTEGER,
    professional_id INTEGER,
    celebrity TEXT,
    professional TEXT,
    dance TEXT,
    song TEXT,
    series INTEGER,
    week INTEGER,
    running_order INTEGER,
    score_craig INTEGER,
    score_arlene INTEGER,
    score_len INTEGER,
    score_bruno INTEGER,
    score_alesha INTEGER,
    score_darcey INTEGER,
    score_jennifer INTEGER,
    score_donny INTEGER,
    score_shirley INTEGER,
    total INTEGER
);

COPY results FROM '/<absolute-path-to>/results.csv' WITH CSV HEADER;
```

## Data

This data was initially sourced and collated from [Ultimate Strictly](http://www.ultimatestrictly.com/) (link to their [excellent source page](http://www.ultimatestrictly.com/acknowledgements/)), manually sanitised and normalised, with additional data sourced from Wikipedia.
