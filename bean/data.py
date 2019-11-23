# coding:utf8


class GoodSubmitRequest:

    def __init__(self, good):
        self.good = good

    def __str__(self):
        return "(good = %s" % self.good + ")"


class Good:
    '''
        +------------------+------------------+------+-----+---------+----------------+
        | Field            | Type             | Null | Key | Default | Extra          |
        +------------------+------------------+------+-----+---------+----------------+
        | id               | int(11)          | NO   | PRI | NULL    | auto_increment |
        | name             | varchar(10)      | NO   |     | NULL    |                |
        | image1           | varchar(200)     | YES  |     | NULL    |                |
        | image2           | varchar(200)     | YES  |     | NULL    |                |
        | image3           | varchar(200)     | YES  |     | NULL    |                |
        | status           | int(11)          | NO   |     | NULL    |                |
        | price            | int(10) unsigned | NO   |     | NULL    |                |
        | short_desc       | varchar(20)      | YES  |     | NULL    |                |
        | descs            | longtext         | YES  |     | NULL    |                |
        | address          | varchar(20)      | YES  |     | NULL    |                |
        | phone            | int(10) unsigned | NO   |     | NULL    |                |
        | view_times       | int(10) unsigned | NO   |     | NULL    |                |
        | create_time      | datetime(6)      | YES  |     | NULL    |                |
        | last_modify_time | datetime(6)      | YES  |     | NULL    |                |
        | city_id          | varchar(20)      | NO   | MUL | NULL    |                |
        | user_id          | varchar(50)      | NO   | MUL | NULL    |                |
        +------------------+------------------+------+-----+---------+----------------+
    '''

    def __init__(self, name, image1, image2, image3, status, price, short_desc, descs, address, phone,
                 create_time, city_id, user_id, user_nickname):
        self.name = name
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.status = status
        self.price = price
        self.short_desc = short_desc
        self.descs = descs
        self.address = address
        self.phone = phone
        self.view_times = 0
        self.create_time = create_time
        self.city_id = city_id
        self.user_id = user_id
        self.user_nickname = user_nickname

    def __str__(self):
        return "(good = %s" % self.name + " , user = %s" % self.user_nickname + ")"


class Need:
    '''
        +------------------+------------------+------+-----+---------+----------------+
        | Field            | Type             | Null | Key | Default | Extra          |
        +------------------+------------------+------+-----+---------+----------------+
        | id               | int(11)          | NO   | PRI | NULL    | auto_increment |
        | name             | varchar(10)      | NO   |     | NULL    |                |
        | image1           | varchar(200)     | YES  |     | NULL    |                |
        | status           | int(11)          | NO   |     | NULL    |                |
        | price_min        | int(10) unsigned | NO   |     | NULL    |                |
        | price_max        | int(10) unsigned | NO   |     | NULL    |                |
        | short_desc       | varchar(20)      | YES  |     | NULL    |                |
        | descs            | longtext         | YES  |     | NULL    |                |
        | address          | varchar(20)      | YES  |     | NULL    |                |
        | phone            | int(11)          | NO   |     | NULL    |                |
        | view_times       | int(10) unsigned | NO   |     | NULL    |                |
        | create_time      | datetime(6)      | YES  |     | NULL    |                |
        | last_modify_time | datetime(6)      | YES  |     | NULL    |                |
        | city_id          | varchar(20)      | NO   | MUL | NULL    |                |
        | user_id          | varchar(50)      | NO   | MUL | NULL    |                |
        +------------------+------------------+------+-----+---------+----------------+
    '''
    def __init__(self, name, price, descs, address, phone,
                 create_time, city_id, user_id, user_nickname):
        self.name = name
        self.price = price
        self.descs = descs
        self.address = address
        self.phone = phone
        self.create_time = create_time
        self.city_id = city_id
        self.user_id = user_id
        self.user_nickname = user_nickname

    def __str__(self):
        return "(need = %s" % self.name + " , user = %s" % self.user_nickname + ")"


class City:

    '''
        +---------+-------------+------+-----+---------+-------+
        | Field   | Type        | Null | Key | Default | Extra |
        +---------+-------------+------+-----+---------+-------+
        | id      | varchar(20) | NO   | PRI | NULL    |       |
        | name    | varchar(10) | NO   |     | NULL    |       |
        | enabled | tinyint(1)  | NO   |     | NULL    |       |
        +---------+-------------+------+-----+---------+-------+
    '''

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "(city_id = %s" % self.id + ")"

