#  READ ME

```bash
# sqlite3 시작
sqlite3 pjt.sqlite3
```

```sqlite
# 01_create_table.sql 파일을 읽어 오겠다
.read 01_create_table.sql
```

```sqlite
--01_create_table.sql

CREATE TABLE movies (
    '영화코드'  INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);

-- import boxoffice csv
.mode csv
.import boxoffice.csv movies

.headers on
.mode column

SELECT * FROM movies;



[TABlE 생성]
CREATE TABLE 테이블명

[출력하기]
SELECT * FROM movies;
```



```sqlite
-- 02_crud.sql



--1. 최근 영화 극한직업이 누락되어 있습니다. 영진위 API에서 얻은 정보에 따르면, 위와 같습니다. 해당 레코드를 테이블에 추가 해주세요.
INSERT INTO movies (영화코드, 영화이름, 관람등급, 감독, 개봉연도, 누적관객수, 상영시간, 제작국가, 장르)
   ...> VALUES(20182530, '극한직업', '15세이상관람가', '이병헌', 20190123, 3138467, 111, '한국', '코미디');
SELECT * FROM movies;

[data 추가(INSERT)]
INSERT INTO 테이블명 (변수1, 변수2)
   ...> VALUES(값1,값2);
 


-- 2. 데이터 수집과정에서 실수로 과거의 데이터가 포함되었습니다. 영화코드가 20040521인 데이터를 출력하세요. 그리고, 해당 데이터를 삭제하세요.
SELECT * FROM movies WHERE 영화코드=20040521;
--20040521      클레멘타인  15세관람가  김두영   20040521      67000            100           한 국        액션 
DELETE FROM movies WHERE 영화코드=20040521;

[특정 조건을 출력하기]
SELECT 출력하고 싶은 값 FROM 테이블명 WHERE 조건;
[data 삭제(DELETE)]
DELETE FROM 테이블명 WHERE 삭제하고싶은 조건(ex:id=3);



-- 3. 영화코드 20185124인 데이터를 출력하세요. 공란으로 되어 있는 컬럼에 값을 '없음'으로 수정하세요. 그리고 해당 데이터의 감독이 변경되었는지 확인하세요.
SELECT * FROM movies WHERE 영화코드=20185124;
--20185124      러브 유어셀프 인 서울  전체관람가              20190126      180966           111           한국        공연
UPDATE movies SET 감독='없음' WHERE 영화코드=20185124;

[data 수정(UPDATE)]
UPDATE 테이블명 SET 수정 내용 WHERE 조건;
```



```sqlite
-- 03_select.sql
--1. 상영시간이 150분 이상인 영화이름만 출력하세요.
SELECT 영화이름 FROM movies WHERE 상영시간>=150;
                  
-- 2. 장르가 애니메이션인 영화코드와 영화이름를 출력하세요.
SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션';

--3. 제작국가가 덴마크이고 장르가 애니메이션인 영화이름을 출력하세요.
SELECT 영화이름 FROM movies WHERE 장르='애니메이션' and 제작국가='덴마크';

--4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수를 출력하세요.
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>=1000000 and 관람등급='청소년관람불가';

-- 5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화를 출력하세요.
SELECT * FROM movies WHERE 20000101<=개봉연도 and 개봉연도 <=20091231; 

--6. 장르를 중복 없이 출력하세요.
SELECT DISTINCT 장르 FROM movies;


and를 통해 두가지 조건을 줄수도 있다.
>= 같은 조건도 사용 가능
중복을 없애기 위해서는 DISTINCT를 사용해 중복을 제거
```



```sqlite
-- 04_expression.sql
--1. 모든 영화의 총 누적관객수를 출력하세요.
SELECT SUM(누적관객수) FROM movies;

--2. 가장 많은 누적관객수인 영화이름과 누적관객수를 출력하세요.
SELECT 영화이름, MAX(누적관객수) FROM movies;

--3. 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력하세요.
SELECT 장르, MIN(상영시간) FROM movies;

--4. 제작국가가 한국인 영화의 평균 누적관객수를 출력하세요.
SELECT AVG(누적관객수) FROM movies WHERE 제작국가="한국";

--5. 관람등급이 청소년관람불가인 영화의 개수를 출력하세요.
SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';

--6. 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력하세요.
SELECT COUNT(*) FROM movies WHERE 상영시간 >=100 and 장르 = '애니메이션';

SUM(): 을 통해 합을 구할 수 있다.
MAX(): 를 이용해 최대값
MIN(): 을 이용해 최소값
AVG(): 를 이용해 평균값
COUNT(): 를 이용해 카운트를 구할수 있다.

```



```sqlite
-- 05_order.sql
--1. 누적관객수 상위 5개 영화의 모든 데이터를 출력하세요.
SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
--2. 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개만 출력하세요.
SELECT * FROM movies WHERE 장르 ="애니메이션" ORDER BY 누적관객수 DESC , 제작국가 ASC LIMIT 10;
--3. 상영시간이 긴 영화를 만든 감독의 이름을 10개만 출력하세요.
SELECT DISTINCT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;

내림차순 : ORDER BY 누적관객수 DESC LIMIT 5;
오름차순 : ORDER BY 누적관객수 ASC LIMIT 5;
2가지를 쓰려면 RDER BY 누적관객수 DESC , 제작국가 ASC LIMIT 10;
콤마를 통해 사용

```

