CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(20)
);

INSERT INTO books (name, status) VALUES
('DevOps Handbook', 'available'),
('Docker Deep Dive', 'taken'),
('Kubernetes Basics', 'available');