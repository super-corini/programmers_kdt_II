
## Day 5 - Mission 1. My New Assistant

#### 사전 작업
- MYSQL에 `bicsubi` database CREATE
- MySQL 에 `weapon` table CREATE
- `weapon` database에 무기들 INSERT
- 편의를 위해 id를 자동생성 되도록 설정하였고, 기본키로 설정하였습니다.
<br>

```sql
CREATE TABLE weapon(
	id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(200),
	stock INT,
	PRIMARY KEY(id)
);

INSERT INTO weapon (name, stock) VALUES('AK-47', 2);
INSERT INTO weapon (name, stock) VALUES('TRG', 5);
INSERT INTO weapon (name, stock) VALUES('FAMAS', 1);
```

