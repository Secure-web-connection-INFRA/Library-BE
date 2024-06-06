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
    role         TEXT    DEFAULT USER 
);

-- -- Create the update_timestamp_auth trigger if it does not exist
-- DROP TRIGGER IF EXISTS update_timestamp_auth;

-- CREATE TRIGGER update_timestamp_auth
-- AFTER UPDATE ON auth
-- BEGIN
--     UPDATE auth
--     SET updatedAt = CURRENT_TIMESTAMP
--     WHERE id = OLD.id;
-- END;

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

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b123', '2 states', 'Coming from two very different cultural backgrounds, Krish and Ananya try to convince their parents to bless their relationship before they get married.','Chetan Bhagat', '2014', '2-states.pdf', '2-states.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b001', 'To Kill a Mockingbird', 'A novel about the serious issues of rape and racial inequality.', 'Harper Lee', '1960', 'to_kill_a_mockingbird.pdf', 'to_kill_a_mockingbird.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b002', '1984', 'A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.', 'George Orwell', '1949', '1984.pdf', '1984.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b003', 'Pride and Prejudice', 'A romantic novel that charts the emotional development of the protagonist Elizabeth Bennet.', 'Jane Austen', '1813', 'pride_and_prejudice.pdf', 'pride_and_prejudice.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b004', 'The Great Gatsby', 'A story about the young and mysterious millionaire Jay Gatsby and his quixotic passion for the beautiful Daisy Buchanan.', 'F. Scott Fitzgerald', '1925', 'the_great_gatsby.pdf', 'the_great_gatsby.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b005', 'Moby Dick', 'The narrative of Captain Ahab''s obsessive quest to kill Moby Dick, a giant white sperm whale.', 'Herman Melville', '1851', 'moby_dick.pdf', 'moby_dick.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b006', 'War and Peace', 'A novel that chronicles the French invasion of Russia and the impact of the Napoleonic era on Tsarist society.', 'Leo Tolstoy', '1869', 'war_and_peace.pdf', 'war_and_peace.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b007', 'The Catcher in the Rye', 'A story about adolescent alienation and loss of innocence in the protagonist Holden Caulfield.', 'J.D. Salinger', '1951', 'the_catcher_in_the_rye.pdf', 'the_catcher_in_the_rye.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b008', 'Crime and Punishment', 'A psychological drama that portrays the moral dilemmas and mental anguish of the protagonist Raskolnikov.', 'Fyodor Dostoevsky', '1866', 'crime_and_punishment.pdf', 'crime_and_punishment.jpeg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b009', 'The Hobbit', 'A fantasy novel about the quest of home-loving hobbit Bilbo Baggins to win a share of the treasure guarded by Smaug the dragon.', 'J.R.R. Tolkien', '1937', 'the_hobbit.pdf', 'the_hobbit.jpg');

INSERT INTO bookList (bID, bTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover)
VALUES ('b010', 'The Odyssey', 'An epic poem that tells the story of Odysseus'' journey home after the fall of Troy.', 'Homer', '8th Century BC', 'the_odyssey.pdf', 'the_odyssey.jpg');
