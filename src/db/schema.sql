CREATE TABLE auth (
    id           NUMERIC PRIMARY KEY
                         UNIQUE,
    name         TEXT,
    emailAddress TEXT    UNIQUE
                         NOT NULL,
    password     TEXT    NOT NULL,
    updatedAt    TEXT    NOT NULL
                         DEFAULT (CURRENT_TIMESTAMP) 
);

CREATE TRIGGER update_timestamp_auth
AFTER UPDATE ON auth
BEGIN
    UPDATE auth
    SET updatedAt = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;

CREATE TABLE authReset (
    token     TEXT PRIMARY KEY ON CONFLICT ROLLBACK,
    email          REFERENCES auth (emailAddress) 
                   NOT NULL,
    createdAt REAL DEFAULT (CURRENT_TIMESTAMP) 
);

CREATE TRIGGER reset_token_trigger
BEFORE INSERT ON authReset WHEN new.id IN (SELECT id from authReset)
BEGIN
    DELETE FROM authReset WHERE id = new.id;
END;

CREATE TABLE bookList (
    bID          TEXT PRIMARY KEY
                      UNIQUE
                      NOT NULL,
    BTitle       TEXT NOT NULL,
    bDesc        TEXT NOT NULL,
    bAuthor           NOT NULL,
    bPublishedOn      NOT NULL,
    bUrl         TEXT
);