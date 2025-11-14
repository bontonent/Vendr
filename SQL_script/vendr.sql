CREATE DATABASE vendr;
CREATE TABLE products(
	id SERIAL PRIMARY KEY,
    name_main_category TEXT,
    name_uncategory TEXT,
	name_product TEXT,
	min_salary DOUBLE PRECISION,
	mad_salary DOUBLE PRECISION,
	max_salary DOUBLE PRECISION,
	describe TEXT
);
