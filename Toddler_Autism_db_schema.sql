-- Database: Toddler_Autism_2018

-- DROP DATABASE IF EXISTS "Toddler_Autism_2018";

CREATE DATABASE "Toddler_Autism_2018"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
	-- Table: public.Toddler_Autism_.2018.

-- DROP TABLE IF EXISTS public."Toddler_Autism_.2018.";

CREATE TABLE IF NOT EXISTS public."Toddler_Autism_.2018."
(
    "Case_No" bigint NOT NULL,
    "A1" integer,
    "A2" integer,
    "A3" integer,
    "A4" integer,
    "A5" integer,
    "A6" integer,
    "A7" integer,
    "A8" integer,
    "A9" integer,
    "A10" integer,
    "Age_Mons" integer,
    "Qchat-10-score" integer,
    "Sex" "char",
    "Ethnicity" text COLLATE pg_catalog."default",
    "Jaundice" "char",
    "Family_mem_with_ASD" "char",
    "Who completed the test" text COLLATE pg_catalog."default",
    "Class/ASD Traits" "char",
    CONSTRAINT "Toddler_Autism_.2018._pkey" PRIMARY KEY ("Case_No")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Toddler_Autism_.2018."
    OWNER to postgres;