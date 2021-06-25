# SequelPro에서 Failed Error 해결하는 법
### 📍시스템 환경설정 > MySQL > ACTIVE를 반드시 해주고 시작할 것.

방법1. MySQL 설치 후 터미널에서 비밀번호를 변경해준다.

            > cd /usr/local/mysql/bin

            > ./mysql -u root -p

            
            > ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY '변경할 패스워드';
            > Query OK, 0 rows affected 명령이 나오면 완료!

방법2. 시스템 환경설정에서 비밀번호를 변경해준다.

            시스템 환경설정 > MySQL > Initialize Database > 비밀번호 변경


# Connection in MySQL
### Host, Username은 자동으로 설정되므로 아래와 같이 적어줄 것.
            > Name: (입력없음)
            > Host: 127.0.0.1
            > Username: root
            > Password: 비밀번호 입력
            