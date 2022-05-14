
import sqlite3

db_connect = sqlite3.connect('Department.db')

cursor = db_connect.cursor()


query = """ CREATE TABLE `Department` (
  dept_id INT(100) NOT NULL,
  dept_name varchar(255) NOT NULL CHECK (dept_name LIKE 'Department%'),
  chair_name varchar(255) NOT NULL,
  facultyMember_number varchar(255) NOT NULL,
  PRIMARY KEY(dept_id)
);
    """
cursor.execute(query)

query = """ CREATE TABLE `Student` (
  `student_id` INT(100) NOT NULL,
  `student_fname` varchar(255) NOT NULL,
  `student_lname` varchar(255) NOT NULL ,
  `initials` varchar(255) NOT NULL CHECK (length(initials) >1),
   PRIMARY KEY (student_id)
);
    """
cursor.execute(query)



query = """ CREATE TABLE `Major` (
  `major_id` INT(100) NOT NULL,
  `major_name` varchar(255) NOT NULL,
  `dept_id` INT(100) NOT NULL,
  `code` varchar(3) NOT NULL CHECK (length(code) = 3),
  PRIMARY KEY (major_id),
  FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
) ;
    """

cursor.execute(query)


query = """ CREATE TABLE `Event` (
  `event_id` INT(100) NOT NULL,
  `event_name` varchar(255) NOT NULL,
  `start_date` varchar(255) NOT NULL,
  `end_date` varchar(255) NOT NULL  CHECK (end_date >= start_date),
   PRIMARY KEY (event_id)
);
    """
cursor.execute(query)



query = """ CREATE TABLE `Enrollment` (
  `student_id` INT(100) NOT NULL,
  `major_id` INT(100) NOT NULL,
   PRIMARY KEY (student_id, major_id),
   FOREIGN KEY (major_id) REFERENCES Major(major_id),
   FOREIGN KEY (student_id) REFERENCES Student(student_id)
);
    """
cursor.execute(query)


query = """ CREATE TABLE `Participation` (
  `student_id` INT(200) NOT NULL,
  `event_id` INT(200) NOT NULL,
   PRIMARY KEY (student_id, event_id),
   FOREIGN KEY (student_id) REFERENCES Student(student_id),
   FOREIGN KEY (event_id) REFERENCES Event(event_id)
);
    """
cursor.execute(query)


query = """ CREATE TABLE `Activity` (
  `dept_id` INT(200) NOT NULL,
  `event_id` INT(200) NOT NULL,
   PRIMARY KEY (dept_id, event_id),
   FOREIGN KEY (dept_id) REFERENCES Student(dept_id),
   FOREIGN KEY (event_id) REFERENCES Event(event_id)
);
    """
cursor.execute(query)




#
#
#
# ###############Insert row into table####################
query = """
    INSERT INTO `Department` (`dept_name`,`chair_name`,`facultyMember_number`,`dept_id` )
    VALUES ('Department of Math', 'Addison', '10', '1'),
    ('Department of Chinese', 'Adelaide', '32', '2'),
    ('Department of Computer ', 'Andrew', '11', '3'),
    ('Department of Art', 'Haley', '33', '4'),
    ('Department of law', 'Hunter', '23', '5');
    """
cursor.execute(query)


query = """
    INSERT INTO `Student` (`student_lname`, `student_fname`, `initials`, `student_id`)
    VALUES ('Peter', 'Ma', 'PM', '1'),
    ('Jack ', 'Zhang', 'JZ', '2'),
    ('Tom', 'Li', 'TL', '3'),
    ('Mark', 'Liu', 'ML', '4'),
    ('Zhihui', 'Wen', 'ZW', '5');
    """
cursor.execute(query)



query = """
    INSERT INTO `Major` (`major_name`, `major_id`, `code`, `dept_id`)
    VALUES ('computer math', '1', 'CPM', '1'),
    ('chinese art', '2', 'CNA', '2'),
    ('database', '3', 'DBS', '3'),
    ('art history', '4', 'AHT', '4'),
    ('Legal Fundamentals', '5', 'LFM', '5');
    """
cursor.execute(query)


query = """
    INSERT INTO `Event` (`event_name`, `event_id`, `start_date`, `end_date`)
    VALUES ('math competition on line', '1', '2022-10-11', '2022-10-20'),
    ('math competition', '2', '2022-10-21', '2022-10-24'),
    ('music concert', '3', '2022-10-10', '2022-10-19'),
    ('english competition', '4', '2022-10-11', '2022-10-22'),
    ('speaking competition', '5', '2022-11-26', '2022-11-28');
    """
cursor.execute(query)

query = """
    INSERT INTO `Enrollment` (`student_id`, `major_id`)
    VALUES ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '4');
    """
cursor.execute(query)



query = """
    INSERT INTO `Participation` (`student_id`, `event_id`)
    VALUES ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5');
    """
cursor.execute(query)



query = """
    INSERT INTO `Activity` (`dept_id`, `event_id`)
    VALUES ('1', '1'),
    ('2', '2'),
    ('2', '3'),
    ('2', '4'),
    ('1', '5');
    """
cursor.execute(query)


db_connect.commit()
cursor.close()

db_connect.close()

