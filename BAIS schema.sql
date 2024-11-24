CREATE TABLE "users" (
  id SERIAL PRIMARY KEY,
  email varchar(50) UNIQUE NOT NULL,
  password text NOT NULL,
  createdAt int NOT NULL
);
