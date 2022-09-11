CREATE DATABASE MNG
GO
USE MNG
GO
CREATE TABLE nganh(
    maNganh VARCHAR(10) PRIMARY KEY,
    tenNganh NVARCHAR(50) NOT NULL

)
CREATE TABLE student(
    id VARCHAR(10) PRIMARY KEY,
    Hoten NVARCHAR(50) NOT NULL,
    Birthday DATE CHECK (Birthday < getdate()),
    Gender VARCHAR(3) NOT NULL,
    Ethnic VARCHAR(10) NOT NULL,
    Email VARCHAR(30) NOT NULL,
    Cccd VARCHAR(40) NOT NULL,
    Addres VARCHAR(50) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    tenNganh NVARCHAR(50) FOREIGN KEY REFERENCES nganh
)

CREATE TABLE monhoc(
    MaMH varchar(10) primary key,
    tenNganh NVARCHAR(50) FOREIGN KEY REFERENCES nganh,
    TenMH Nvarchar (20) unique,
    DVHT int CHECK (DVHT between 2 and 9)
)
CREATE TABLE loginn(
    id VARCHAR(10) FOREIGN KEY REFERENCES student,
    passworld VARCHAR(20) NOT NULL,
    
)
CREATE TABLE ppoint(
    id VARCHAR(10) FOREIGN KEY REFERENCES student,
    class VARCHAR(10) NOT NULL,
    TenMH NVARCHAR(30) FOREIGN KEY REFERENCES monhoc,
    HocKy int check(HocKy>0) not null,
    diemCC FLOAT DEFAULT 0,
    diemGK FLOAT DEFAULT 0,
    diemKTHP FLOAT DEFAULT 0,
    CONSTRAINT PK_point PRIMARY KEY (id,class)
)


SELECT * FROM student
SELECT @@SERVERNAME