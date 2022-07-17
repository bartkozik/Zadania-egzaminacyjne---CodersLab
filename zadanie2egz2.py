query_1 = """ create table Users(
id serial primary key,
name varchar(60),
email varchar(60),
password varchar(60));"""

query_2 = """create table Messages(
id serial primary key,
user_id int references Users(id),
message text);
"""

query_3 = """create table Items( 
id serial primary key,
name varchar(40),
description text,
price decimal(7,2));
"""

query_4 = """create table Orders( 
id serial primary key,
description text);
"""

query_5 = """create table ItemsOrders(
id serial primary key,
item_id int references Items(id) on delete cascade,
order_id int references Orders(id) on delete cascade);
"""

guery_6 = "select * from Items where price>13;"
query_7 = "insert into Orders(description) values('randomowy opis dodanej transakcji');"
query_8 = "delete from Users where id=7;"
query_9 = """select Users.name as user_name, Users.id as user_id, Messeges.message as u_message from Users
           join Messages on Users.id=Messages.user_id;"""

query_10 = "alter table Messages add date_of_created timestamp default current_timestamp;"