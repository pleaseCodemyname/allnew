create table usertbl (
    userid  char(8) not null primary key,
    username    nvarchar2(10) not null,
    birthyear   number(4) not null,
    addr    nchar(2) not null,
    mobile1 char(3),
    mobile2 char(8),
    height  number(3),
    mdate   date
);

insert into usertbl values('LSG', '�̽±�', 1987, '����', '011', '11111111', 182, '2008-8-8');
insert into usertbl values('kbs', '�����', 1979, '�泲', '011', '22222222', 173, '2012-4-4');
insert into usertbl values('kkh', '���ȣ', 1971, '����', '019', '33333333', 177, '2007-7-7');
insert into usertbl values('jyp', '������', 1950, '���', '011', '44444444', 166, '2008-4-4');
insert into usertbl values('ssk', '���ð�', 1979, '����', NULL , NULL , 186, '2013-12-12');
insert into usertbl values('ljb', '�����', 1963, '�泲', '016', 66666666, 182, '2009-9-9');
insert into usertbl values('yjs', '������', 1969, '���', NULL , NULL , 170, '2005-5-5');
insert into usertbl values('ejw', '������', 1972, '���', '011', '88888888', 174, '2014-3-3');
insert into usertbl values('jkw', '������', 1965, '���', '018', '99999999', 172, '2010-10-10');
insert into usertbl values('bbk', '�ٺ�Ŵ', 1973, '����', '010', '00000000', 176, '2013-5-5');

select * from usertbl
