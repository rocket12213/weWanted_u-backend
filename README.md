**Ovierview**
웹 개발자 채용 관리 플랫폼 (wanted clone)

**Features**
+ Scrum 개발 방식을 적용하여 Sprint로 개발 및 검토를 하며 효율적으로 협업  
+ Python requests module을 활용한 web data scraping  
+ Django 웹 프레임워크를 활용한 다양한 backend API 구현  
  - 인증: bcrypt, PyJWT module을 활용한 회원가입, 로그인 기능 구현
  - 인가: decorator를 이용하여 인증 절차를 다른 엔드포인트에 적용
  - 채용 공고 data 전송, review 작성, 이력서 등록, 팔로우 기능 구현
+ Integration Test (httpie 라이브러리 활용)
+ git과 github를 사용하여 코드의 버전 관리 및 협업
+ AWS RDS 서비스의 MySQL을 데이터베이스로 사용하여 EC2 서버에 API 배포

**Requirements**
bcrypt==3.1.7   
beautifulsoup4==4.8.1   
bs4==0.0.1   
certifi==2019.9.11   
cffi==1.13.1   
chardet==3.0.4   
Django==2.2.6   
django-cors-headers==3.1.1   
idna==2.8   
mysql-connector-python==8.0.18   
protobuf==3.10.0  
pycparser==2.19  
PyJWT==1.7.1  
pytz==2019.3  
requests==2.22.0  
selenium==3.141.0  
six==1.12.0  
soupsieve==1.9.4  
sqlparse==0.3.0  
urllib3==1.25.6  

**Endpoint**
회원가입 & 로그인 (user app)  
[POST] 회원가입  
[POST] 로그인  

채용공고(job app)  
[GET] 상세 채용 정보   
[GET] 채용 공고 리스트   
[GET] 팔로우한 채용 공고 리스트   

팔로우(follow app)  
[POST] 채용 공고 팔로우  

이력서(resume app)  
[GET] 이력서 저장 타입  
[POST] 이력서  
[GET] 이력서  

