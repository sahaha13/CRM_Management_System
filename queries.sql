--TRIGGERS--

/* Create trigger to increment no_of_courses by 1 in teacher_info table if teacher_ID in teacher_info table is same as teacher_ID in course_details table*/
CREATE TRIGGER increment_no_of_courses
AFTER INSERT ON course_details
FOR EACH ROW
BEGIN
UPDATE teacher_info SET no_of_courses = no_of_courses + 1 WHERE teacher_ID = NEW.teacher_ID;
END;

/* Create trigger to increment Courses_assisted by 1 in volunteer_info if volunteer_ID in volunteer_info table is same as Volunteer_ID in course_details table*/
CREATE TRIGGER increment Courses_assisted
AFTER INSERT ON course_details
FOR EACH ROW
BEGIN
UPDATE volunteer_info SET Courses_assisted = Courses_assisted + 1 WHERE volunteer_ID = NEW.Volunteer_ID;
END;

--Aggregate functions--

/*Aggregate function to Show total number of participants in participant_info table*/
SELECT COUNT(*) FROM participant_info;

/*Aggregate function to select teacher with max no_of-courses*/
SELECT * FROM teacher_info WHERE no_of_courses = (SELECT MAX(no_of_courses) FROM teacher_info);

/*Aggregate function to select volunteer with max Courses_assisted*/
SELECT * FROM volunteer_info WHERE Courses_assisted = (SELECT MAX(Courses_assisted) FROM volunteer_info);

/*Aggregate function to Show total number of courses in course_details table*/
SELECT COUNT(*) FROM course_details;

/*Aggregate function to show total number of participants in advance_program_details table*/
SELECT COUNT(*) FROM advance_program_details;

--JOIN functions--


/* JOIN course_details and teacher_info with teacher_ID*/
SELECT * FROM course_details LEFT OUTER JOIN teacher_info ON course_details.teacher_ID = teacher_info.teacher_ID;

/* JOIN course_details and volunteer_info with volunteer_ID*/
SELECT * FROM course_details  INNER JOIN volunteer_info ON course_details.Volunteer_ID = volunteer_info.volunteer_ID;

/* JOIN participant_info and advance_program_details with Registration_ID*/
SELECT * FROM participant_info RIGHT OUTER JOIN advance_program_details ON participant_info.Registration_ID = advance_program_details.Registration_ID;

/* Join participant_info and course_details with Course_ID*/
SELECT * FROM participant_info INNER JOIN course_details ON participant_info.Course_ID = course_details.Course_ID;


--SET operations--
/* Set operation to get list of course_details with Course_Start_Date as 2022-09-08 intersection Course_End_Date as 2022-09-11 and No_of_pax is above 40*/
SELECT * FROM course_details WHERE Course_Start_Date = '2022-09-08' AND Course_End_Date = '2022-09-11' AND No_of_pax > 40;

/*Set operation to get list of participants where Amount is 1200 and Registration_type is 'Online'*/
SELECT * FROM participant_info WHERE Amount = 1200 AND Registration_type = 'Online';

/*Set operation to get list of participants whose District is Indore or Bhopal or Damoh*/
SELECT * FROM participant_info WHERE District = 'Indore' OR District = 'Bhopal' OR District = 'Damoh';

/* Set operation to get list of participants whose Course_ID is HP173 and Registration_type is 'Online'*/
SELECT * FROM participant_info WHERE Course_ID = 'HP173' AND Registration_type = 'Online';



--Cursors--
/*procedure with cursor to insert all the Registration ID from participant_info table into temp table*/
delimiter $$
CREATE OR REPLACE PROCEDURE insert_reg_id()
BEGIN
DECLARE reg_id VARCHAR(20);
DECLARE participant_name VARCHAR(20);
DECLARE done INT DEFAULT FALSE;
DECLARE cur CURSOR FOR SELECT Registration_ID,name FROM participant_info;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
OPEN cur;
read_loop: LOOP
FETCH cur INTO reg_id,participant_name;
IF done THEN
LEAVE read_loop;
END IF;
INSERT INTO temp_table VALUES (reg_id,participant_name);
END LOOP;
CLOSE cur;
END;

delimiter $$
CREATE OR REPLACE PROCEDURE print_registration_id()
BEGIN
DECLARE done INT DEFAULT FALSE;
DECLARE reg_id VARCHAR(10);
DECLARE cur CURSOR FOR SELECT Registration_ID FROM participant_info;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
OPEN cur;
read_loop: LOOP
FETCH cur INTO reg_id;
return reg_id;
IF done THEN
LEAVE read_loop;
END IF;
END LOOP;
CLOSE cur;
END;



drop procedure get_registration_id

--Procedure--
/* Create procedure to display rows where Number_of_courses>4 in advance_program_details*/
DELIMITER &&
CREATE PROCEDURE display_advance_program_details
BEGIN
SELECT * FROM advance_program_details WHERE Number_of_courses>4;
END &&;
DELIMITER;

drop procedure display_advance_program_details



/* Call procedure display_advance_program_details*/
CALL display_advance_program_details;

--Function--
/* Function to display teacher_name from teacher_info whose no_of_courses is >10 and count them */

DELIMITER $$
create function course_count(id varchar(50))
returns int
begin
declare count int;
select no_of_courses into count from teacher_info where teacher_ID=id;
if count>10 then
return count;
else
return 0;
end if;
end
$$

select teacher_ID,teacher_name,course_count(teacher_ID) from teacher_info where course_count(teacher_ID)>10;

drop function course_count;