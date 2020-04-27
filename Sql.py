
create_database = 'CREATE DATABASE IF NOT EXISTS test DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
drop_table_if_exist_sql = "drop table if exists test_case;"

create_table = """

    create table test_case(
        id int not null auto_increment comment '主键',
        bookname varchar(40) unique not null comment '书名',
        author varchar(30) not null comment '作者',
        test_result varchar(30) default null,
        primary key(id)
    )engine=innodb character set utf8 comment '测试数据表';
"""