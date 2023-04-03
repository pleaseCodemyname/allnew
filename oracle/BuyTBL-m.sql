create table buyTBL 
(   idNum Number(8) not null primary key,
    userID char(8) not null,
    prodName Nchar(6) not null,
    groupName nchar(4),
    price number(8) not null,
    amount number(3) not null,
    FOREIGN KEY (userid) REFERENCES userTBL(userID));


create SEQUENCE idSEQ;
insert into buyTBL values(idSEQ.NEXTVAL, 'KBS','운동화', NULL , 30, 2);
insert into buyTBL values(idSEQ.NEXTVAL, 'KBS','노트북', '전자' , 1000, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'JYP','모니터', '전자' , 200, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','모니터', '전자', 200, 5);
insert into buyTBL values(idSEQ.NEXTVAL, 'KBS','청바지', '의류' , 50, 3);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','메모리', '전자' , 80, 10);
insert into buyTBL values(idSEQ.NEXTVAL, 'SSK','책', '서적' , 15, 5);
insert into buyTBL values(idSEQ.NEXTVAL, 'EJW','책', '서적' , 15, 2);
insert into buyTBL values(idSEQ.NEXTVAL, 'EJW','청바지', '의류' , 50, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','운동화', NULL , 30, 2);
insert into buyTBL values(idSEQ.NEXTVAL, 'EJW','책', '서적' , 15, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','운동화', NULL , 30, 2);

select * from buyTBL