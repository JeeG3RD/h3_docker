CREATE DATABASE nasa;

CREATE DATABASE astroids (
    `Neo Reference ID` PRIMARY KEY NOT NULL,
    `Est Dia in Miles(min)` FLOAT,
    `Est Dia in Miles(max)` FLOAT,
    `Jupiter Tisserand Invariant` FLOAT,
    `Eccentricity` FLOAT,
    `Semi Major Axis` FLOAT,
    `Hazardous` BOOL
)