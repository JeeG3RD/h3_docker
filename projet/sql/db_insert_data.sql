CREATE TABLE IF NOT EXISTS asteroids (
    `Id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `NeoReferenceID` INT,
    `Name` INT,
    `AbsoluteMagnitude` FLOAT,
    `EstDiainMiles(min)` FLOAT,
    `EstDiainMiles(max)` FLOAT,
    `CloseApproachDate` DATE, 
    `EpochDateCloseApproach` BIGINT,  
    `RelativeVelocitykmperhr` FLOAT,
    `Milesperhour` FLOAT,
    `MissDist.(miles)` FLOAT,
    `OrbitID` INT,  
    `OrbitDeterminationDate` DATETIME, 
    `OrbitUncertainity` INT,  
    `MinimumOrbitIntersection` FLOAT,
    `JupiterTisserandInvariant` FLOAT,
    `EpochOsculation` FLOAT,
    `Eccentricity` FLOAT,
    `SemiMajorAxis` FLOAT,
    `Inclination` FLOAT,
    `AscNodeLongitude` FLOAT,
    `OrbitalPeriod` FLOAT,
    `PerihelionDistance` FLOAT,
    `PerihelionArg` FLOAT,
    `AphelionDist` FLOAT,
    `PerihelionTime` FLOAT,
    `MeanAnomaly` FLOAT,
    `MeanMotion` FLOAT,
    `Hazardous` BOOL
)