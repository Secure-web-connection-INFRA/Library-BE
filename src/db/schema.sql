-- Create the auth table if it does not exist
CREATE TABLE IF NOT EXISTS auth (
    id           NUMERIC PRIMARY KEY
                         UNIQUE,
    name         TEXT,
    emailAddress TEXT    UNIQUE
                         NOT NULL,
    password     TEXT    NOT NULL,
    updatedAt    TEXT    NOT NULL
                         DEFAULT (CURRENT_TIMESTAMP) 
);

-- Create the update_timestamp_auth trigger if it does not exist
DROP TRIGGER IF EXISTS update_timestamp_auth;

CREATE TRIGGER update_timestamp_auth
AFTER UPDATE ON auth
BEGIN
    UPDATE auth
    SET updatedAt = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;

-- Create the authReset table if it does not exist
CREATE TABLE IF NOT EXISTS authReset (
    token     TEXT PRIMARY KEY ON CONFLICT ROLLBACK,
    id          REFERENCES auth (id) 
                   NOT NULL,
    createdAt REAL DEFAULT (CURRENT_TIMESTAMP) 
);

-- Create the reset_token_trigger if it does not exist
DROP TRIGGER IF EXISTS reset_token_trigger;

CREATE TRIGGER reset_token_trigger
BEFORE INSERT ON authReset 
WHEN new.id IN (SELECT id from authReset)
BEGIN
    DELETE FROM authReset WHERE id = new.id;
END;

-- Create the bookList table if it does not exist
CREATE TABLE IF NOT EXISTS bookList (
    bID          TEXT PRIMARY KEY
                      UNIQUE
                      NOT NULL,
    BTitle       TEXT NOT NULL,
    bDesc        TEXT NOT NULL,
    bAuthor      TEXT NOT NULL,
    bPublishedOn TEXT NOT NULL,
    bUrl         TEXT,
    bCover       TEXT
);



CREATE TABLE IF NOT EXISTS otp (
    emailAddress TEXT    PRIMARY KEY
                         REFERENCES auth (emailAddress) 
                         NOT NULL,
    otp          NUMERIC,
    attempt      NUMERIC DEFAULT (0),
    createdAt    TEXT    DEFAULT (CURRENT_TIMESTAMP) 
);
