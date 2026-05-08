CREATE TABLE IF NOT EXISTS games (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    platform TEXT NOT NULL,
    finished BOOLEAN DEFAULT 0,
    rating REAL,
    playtime REAL
);