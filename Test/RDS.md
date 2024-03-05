데이터베이스 database-1에 대한 연결 세부 정보

이 암호는 지금만 확인할 수 있습니다. 참조할 수 있도록 암호를 복사하여 저장하세요. 암호를 잊어버린 경우 데이터베이스를 수정하여 변경해야 합니다. SQL 클라이언트 애플리케이션 또는 유틸리티를 사용하여 데이터베이스에 연결할 수 있습니다.
데이터베이스 연결에 대해 자세히 알아보기 

마스터 사용자 이름  
admin

마스터 암호  
4sIUsIhXS7DlrP9GRFWn

엔드포인트  
database-1.cbmqymaw6rm0.ap-northeast-2.rds.amazonaws.com

포트  
3306

강의에 사용된 실습용 스키마  
https://github.com/soaple/first-met-aws-practice/blob/master/chapter_07/backup.sql

위 SQL문의 마지막에 아래와 같은 insert문이 있는데 
사용자를 추가한 것   
유저명은 user  
비밀번호는 1234  

LOCK TABLES `wp_users` WRITE;
/*!40000 ALTER TABLE `wp_users` DISABLE KEYS */;
INSERT INTO `wp_users` VALUES
(1,'user','81dc9bdb52d04dc20036dbd8313ed055','user','user@example.com','http://127.0.0.1','2023-07-08 07:29:10','',0,'user');
/*!40000 ALTER TABLE `wp_users` ENABLE KEYS */;


S3 실습을 위한  
IAM의 액세스키  
액세스 키  
분실하거나 잊어버린 비밀 액세스 키는 검색할 수 없습니다. 대신 새 액세스 키를 생성하고 이전 키를 비활성화합니다.

액세스 키  
AKIAQ3EGTZRVNPIQ4TG2  

비밀 액세스 키  
btqVCjuZgZL2kpYpDLPaXQAAQ+dVSGTFBnbPjxfv



콘솔 로그인 URL
https://058264374378.signin.aws.amazon.com/console  

사용자 이름  
IAMtest  

콘솔 암호  
o'jFz3#&



15강 실습 순서
15.4
15.5
15.6

콘솔 로그인 URL

https://058264374378.signin.aws.amazon.com/console
사용자 이름

testAdmin
콘솔 암호

VomW3I'C
숨기기