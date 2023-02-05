USE PAPER_TRAIL_RECORD_DATA_LOCAL;

/*
  Main tables
*/

DROP TABLE IF EXISTS RAW_ACCOUNT_TRANSACTION;

DROP TABLE IF EXISTS USER;


CREATE TABLE USER (
    user_id INT NOT NULL AUTO_INCREMENT,
    principal_id VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);

CREATE TABLE RAW_ACCOUNT_TRANSACTION (
    raw_account_transaction_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    account_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    account_transaction_date VARCHAR(255) NOT NULL,
    account_transaction_year INT NOT NULL,
    account_transaction_month INT NOT NULL,
    account_transaction_day INT NOT NULL,
    is_pending BOOLEAN NOT NULL DEFAULT FALSE,
    merchant_name VARCHAR(255) NOT NULL,
    merchant_name_detailed VARCHAR(255),
    categories VARCHAR(150),
    create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (raw_account_transaction_id)
);