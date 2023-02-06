DROP USER IF EXISTS 'test_qa';
DROP DATABASE IF EXISTS vkeducation;
CREATE DATABASE vkeducation;
CREATE USER 'test_qa'@'%' IDENTIFIED BY 'qa_test';
GRANT ALL ON vkeducation.* TO 'test_qa'@'%';
FLUSH PRIVILEGES;
USE vkeducation;

CREATE TABLE `test_users` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `surname` varchar(255) NOT NULL,
    `middle_name` varchar(255) DEFAULT NULL,
    `username` varchar(16) DEFAULT NULL,
    `password` varchar(255) NOT NULL,
    `email` varchar(64) NOT NULL,
    `access` smallint DEFAULT NULL,
    `active` smallint DEFAULT NULL,
    `start_active_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `email` (`email`),
    UNIQUE KEY `ix_test_users_username` (`username`)
);

INSERT INTO `test_users` VALUES(1, "TestName", "TestSurname", NULL, "TestUsername", "TestPassword",
"TestEmail@example.net",1, NULL, NULL);


INSERT INTO `test_users` VALUES(2, "TestNddame", "На русском", NULL, "TestUserdfsname", "TestPassword",
"TestEmail@exampdssle.net",1, NULL, NULL);