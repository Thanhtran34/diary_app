CREATE DATABASE diary_app;
USE diary_app;

CREATE TABLE user (
  user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(20),
  password VARCHAR(20)
);

CREATE TABLE story (
  story_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200),
  content VARCHAR(10000)
);

CREATE TABLE diaries (
  diary_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  name VARCHAR(200),
  date DATETIME,
  CONSTRAINT user_fk
    FOREIGN KEY (user_id) REFERENCES user(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE diary_type (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  diary_id INT UNSIGNED NOT NULL,
  story_id INT UNSIGNED NOT NULL,
  working_day TINYINT UNSIGNED,
  process TINYINT UNSIGNED,
  CONSTRAINT diaries_fk
    FOREIGN KEY (diary_id) REFERENCES diaries(diary_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT story_fk
    FOREIGN KEY (story_id) REFERENCES story(story_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE VIEW diary_list
  AS SELECT
      MAX(story.name) AS story_name,
      MAX(user.user_id) AS user_id,
      MAX(username) AS username,
      MAX(diaries.date) AS diary_date
    FROM diary_type
    INNER JOIN diaries
      ON diary_type.diary_id = diaries.diary_id
    INNER JOIN story
      ON diary_type.story_id = story.story_id
    INNER JOIN user
      ON diaries.user_id = user.user_id
    GROUP BY story.name;
    
LOCK TABLES `story` WRITE;
/*!40000 ALTER TABLE `story` DISABLE KEYS */;
INSERT INTO `story` 
	   VALUES (1,'Academic Diary', 'An academic diary can take some the stress and hassle out of your life by making sure you manage your responsibilities for school better'),
			  (2,'Food Diary','Food diaries are an excellent way to track what you\'re eating'),
              (3,'Health Diary','A health diary is not just a list of medical readings and calorie counts. It is a way to record feelings, goals, activities, surrounding events, and results for any particular area of health'),
              (4,'School Diary','Unlike printed diaries, which we agree are pretty “bleh”, electronic school diaries are much more customizable and some have multiple categories pre-set for you'),
              (5,'Secret Diary', 'Everybody has certain things they don\'t wish to share with others. That\'s why a secret diary is so important to many people.'),
              (6,'Wedding Diary', 'There are so many moving parts involved in your big day that it\'s easy to lose sleep. The good news? There is a way to organize your wedding.'),
              (7,'Work Diary', 'Write about your work experiences to reflect on your professional life to track your day-to-day work, consider career opportunities, set milestones, and achieve your goals');
UNLOCK TABLES;

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` 
       VALUES (1,'user_1','user_1'),
              (2,'user_2','user_2'),
			  (3,'user_3','user_3');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `diaries` WRITE;
/*!40000 ALTER TABLE `diaries` DISABLE KEYS */;
INSERT INTO `diaries` 
       VALUES (1,1,'Summer','2022-03-01 18:05:15'),
              (2,1,'Spring','2022-03-01 18:07:47'),
              (3,2,'Autumn','2022-03-01 18:10:06'),
              (4,2,'Winter','2022-03-01 18:13:29'),
              (5,2,'Christmas','2022-03-11 18:17:49'),
              (6,3,'Birthday','2022-03-20 18:19:41'), 
              (7,3,'Wedding','2022-03-01 15:19:30');
/*!40000 ALTER TABLE `diaries` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `diary_type` WRITE;
/*!40000 ALTER TABLE `diary_type` DISABLE KEYS */;
INSERT INTO `diary_type` 
       VALUES (1,1,1, '10', '80'),
              (2,1,1, '8', '90'),
              (3,1,1, '6', '70'),
              (4,1,1, '4', '65'),
              (5,1,1, '10', '85'),
              (6,1,2,  '9', '90'),
              (7,1,2, '6', '45'),
              (8,1,2,'9', '55'),
              (9,1,2, '10', '80'),
              (10,1,2, '8', '90'),
              (11,2,2, '6', '70'),
              (12,2,2, '4', '65'),
              (13,2,3, '10', '85'),
              (14,2,3,  '9', '90'),
              (15,2,3, '6', '45'),
              (16,2,3,'9', '55'),
              (17,2,3, '10', '80'),
              (18,3,3, '8', '90'),
              (19,3,4, '6', '70'),
              (20,3,4, '4', '65'),
              (21,3,4, '10', '85'),
              (22,3,4,  '9', '90'),
              (23,3,4, '6', '45'),
              (24,4,4,'9', '55'),
              (25,4,4, '10', '80'),
              (26,4,4, '8', '90'),
              (27,4,4, '6', '70'),
              (28,4,5, '4', '65'),
              (29,5,5, '10', '85'),
              (30,5,5,  '9', '90'),
              (31,5,5, '6', '45'),
              (32,6,5,'9', '55'),
              (33,6,5, '10', '80'),
              (34,6,6, '8', '90'),
              (35,6,6, '6', '70'),
              (36,7,6, '4', '65'),
              (37,7,6, '10', '85'),
              (38,7,7,  '9', '90'),
              (39,7,7, '6', '45'),
              (40,7,7,'9', '55');
/*!40000 ALTER TABLE `diary_type` ENABLE KEYS */;
UNLOCK TABLES;