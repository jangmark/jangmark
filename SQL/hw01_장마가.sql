create database sqlclass_db;
use sqlclass_db;

create table world
	(country VARCHAR(30),
	continent VARCHAR(30),
	area INT,
	population INT,
	capital VARCHAR(30),
	top_lever_domain VARCHAR(3)
	);
	
desc world;

insert into world
(country,continent,area,population,capital,top_lever_domain)
values ('Afghanistan','Asia',652230,25500100,'Kabul','.af');

insert into world
(country,continent,area,population,capital,top_lever_domain)
values('Algeria', 'Africa', 2381741, 38700000, 'Algiers', '.dz');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('New Zealand', 'Oceania' ,270467 ,4538520, 'Wellington', '.nz');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Australia', 'Oceania', 7692024, 23545500, 'Canberra', '.au');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Brazil', 'South America', 8515767, 202794000, 'Brasilia', '.br');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('China', 'Asia', 9596961, 1365370000, 'Beijing', '.cn');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('India', 'Asia', 3166414, 1246160000, 'New Delhi', '.in');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Russia', 'Eurasia', 17125242, 146000000, 'Moscow', '.ru');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('France', 'Europe', 640679, 65906000, 'Paris', '.fr');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Germany', 'Europe', 357114, 80716000, 'Berlin' ,'.de');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Denmark', 'Europe', 43094, 5634437, 'Copenhagen', '.dk');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Norway', 'Europe', 323802, 5124383, 'Oslo', '.no');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Sweden', 'Europe', 450295, 9675885, 'Stockholm', '.se');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('South Korea', 'Asia', 100210, 50423955, 'Seoul', '.kr');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Canada North', 'America', 9984670, 35427524, 'Ottawa', '.ca');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('United States', 'North America', 9826675, 318320000, 'Washington, D.C.', '.us');

insert into world 
(country,continent,area,population,capital,top_lever_domain)
values('Armenia', 'Eurasia', 29743, 3017400, 'Yerevan', '.am');

# 1) ?????? ????????? ?????? ??????
select country,continent,area,population,capital,top_lever_domain from world;

# 2) ?????? ????????? country, capital, top_lever_domain ????????? ?????? 
select country, capital, top_lever_domain
from world where continent = 'Europe';

# 3) ????????? ???????????? ????????? ?????? ???????????? country, population ????????? ??????
-- - order by ????????? DESC: ????????????
-- - order by ????????? ASC: ????????????
select country,population
from world where continent  = 'Asia' order by population DESC;

# 4) ?????? ????????? ?????????(country), ??????(continent), ??????(area) ????????? ??????????????? ?????????
-- ?????????????????? ???????????? ??????
select country, continent, area 
from world order by area desc;

# 5) ?????? ????????? ?????????, ?????????????????? ?????? (????????? ????????? ?????????????????? ???????????? ??????)

select country, top_lever_domain
from world order by top_lever_domain asc;                                                                                                                                                                                                                      


















































































                                                                                                                        