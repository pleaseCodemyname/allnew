create table buyTBL 
(   idNum Number(8) not null primary key,
    userID char(8) not null,
    prodName Nchar(6) not null,
    groupName nchar(4),
    price number(8) not null,
    amount number(3) not null,
    FOREIGN KEY (userid) REFERENCES userTBL(userID));


create SEQUENCE idSEQ;
insert into buyTBL values(idSEQ.NEXTVAL, 'KBS','�ȭ', NULL , 30, 2);
insert into buyTBL values(idSEQ.NEXTVAL, 'KBS','��Ʈ��', '����' , 1000, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'JYP','�����', '����' , 200, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','�����', '����', 200, 5);
insert into buyTBL values(idSEQ.NEXTVAL, 'KBS','û����', '�Ƿ�' , 50, 3);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','�޸�', '����' , 80, 10);
insert into buyTBL values(idSEQ.NEXTVAL, 'SSK','å', '����' , 15, 5);
insert into buyTBL values(idSEQ.NEXTVAL, 'EJW','å', '����' , 15, 2);
insert into buyTBL values(idSEQ.NEXTVAL, 'EJW','û����', '�Ƿ�' , 50, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','�ȭ', NULL , 30, 2);
insert into buyTBL values(idSEQ.NEXTVAL, 'EJW','å', '����' , 15, 1);
insert into buyTBL values(idSEQ.NEXTVAL, 'BBK','�ȭ', NULL , 30, 2);

select * from buyTBL