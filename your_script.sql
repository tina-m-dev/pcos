-- your_script.sql
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

INSERT INTO test_table (name) VALUES ('Hello, GitHub Actions!');
