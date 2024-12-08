
CREATE TABLE "students" (
	"id" serial NOT NULL UNIQUE,
	"name" text(65535),
	"email" varchar(255),
	"number" varchar(255),
	"dob" date,
	PRIMARY KEY("id")
);


CREATE TABLE "courses" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255),
	"instructor_id" int,
	PRIMARY KEY("id")
);


CREATE TABLE "enrollment" (
	"id" serial NOT NULL UNIQUE,
	"course_id" int,
	"student_id" int,
	"grade" varchar(255),
	"enroll_date" date,
	PRIMARY KEY("id")
);


CREATE TABLE "instructors" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255),
	"email" varchar(255),
	"department" varchar(255),
	PRIMARY KEY("id")
);


ALTER TABLE "enrollment"
ADD FOREIGN KEY("student_id") REFERENCES "students"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "enrollment"
ADD FOREIGN KEY("course_id") REFERENCES "courses"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "instructors"
ADD FOREIGN KEY("id") REFERENCES "courses"("instructor_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;