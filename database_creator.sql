CREATE TABLE `ct` (
  `patient_id` int NOT NULL COMMENT '病人身份证号',
  `ct_video` mediumblob COMMENT '病人的ct视频',
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `ct_patient_id_uindex` (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `doctor` (
  `name` varchar(10) NOT NULL COMMENT '医生姓名',
  `department` varchar(10) NOT NULL COMMENT '所属科室\n',
  `title` varchar(10) DEFAULT NULL COMMENT '职称',
  `job_number` int NOT NULL COMMENT '医生工号',
  `photo` mediumblob COMMENT '医生照片',
  PRIMARY KEY (`job_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `medical_record` (
  `personal_medical_history` varchar(10) NOT NULL COMMENT '个人病史',
  `family_medical_history` varchar(10) NOT NULL COMMENT '家族病史',
  `job_number` varchar(10) NOT NULL COMMENT '主治医生的工号',
  `patient_id` varchar(20) NOT NULL COMMENT '病人身份证号\n',
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `medicine` (
  `medicine_name` varchar(20) NOT NULL COMMENT '药品名',
  `medicine_price` int NOT NULL COMMENT '药品价格',
  `medicine_id` int NOT NULL COMMENT '药品编号\n',
  `remaining_quantity` int NOT NULL COMMENT '剩余数量',
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `patient` (
  `name` varchar(10) NOT NULL COMMENT '病人姓名',
  `gender` varchar(10) NOT NULL,
  `disease` varchar(15) NOT NULL COMMENT '生的病',
  `weight(kg)` int NOT NULL COMMENT '体重',
  `height(cm)` int NOT NULL COMMENT '身高',
  `age` int NOT NULL COMMENT '年龄',
  `patient_id` int NOT NULL COMMENT '身份证号',
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `prescription` (
  `job_number` varchar(10) NOT NULL COMMENT '开药医生工号',
  `patient_id` varchar(20) NOT NULL COMMENT '病人身份证号',
  `medicine_id` varchar(20) DEFAULT NULL COMMENT '药品编号',
  `recipe_id` varchar(20) NOT NULL COMMENT '药方编号',
  PRIMARY KEY (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
