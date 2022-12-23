USE PAPER_TRAIL_RECORD_DATA_LOCAL;

/*
  Main tables
*/

DROP TABLE IF EXISTS USER;


CREATE TABLE USER (
    user_id INT NOT NULL AUTO_INCREMENT,
    principal_id VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);