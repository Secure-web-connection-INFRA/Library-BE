CREATE TABLE auth (
    id           TEXT PRIMARY KEY
                      UNIQUE
                      NOT NULL,
    emailAddress TEXT UNIQUE
                      NOT NULL,
    password     TEXT NOT NULL,
    createdAt         DEFAULT (CURRENT_TIMESTAMP),
    updatedAt         DEFAULT (CURRENT_TIMESTAMP) 
);

CREATE TRIGGER update_timestamp_auth
AFTER UPDATE ON auth
BEGIN
    UPDATE auth
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;