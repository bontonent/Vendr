CREATE DABASE vendr;
CREATE TABLE products(
	id SERIAL PRIMARY KEY,
	name_company TEXT,
	min_salary DOUBLE PRECISION,
	mad_salary DOUBLE PRECISION,
	max_salary DOUBLE PRECISION,
	describe TEXT
);
