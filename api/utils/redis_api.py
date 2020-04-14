# coding:utf8

import redis

"""
@ Author Jue
@ Date 2020-04-13 19:46:46

"""


def publish_good(good, is_publish):

    print("publish_good", "is_publish = ", str(is_publish))
    # 出售信息 key: g_12 => good info map
    publish_good_map(good)

    # 城市出售列表 是否publish，是: 写入 key: cgl_hebeixianghe => good id list
    publish_good_cgl(good, is_publish)

    if not is_publish:
        # 个人出售 key: a_12 => good id list
        publish_good_agl(good)


def publish_good_map(good):
    # key    : g_12
    # value  : good info map

    r = redis.Redis(host='localhost', port=6379, db=0)

    key = "g_" + str(good.id)

    # 商品信息
    r.hset(key, "id", str(good.id))
    r.hset(key, "user_nickname", good.user_nickname)
    r.hset(key, "city_id", str(good.city_id))
    r.hset(key, "name", good.name)
    r.hset(key, "image1", str(good.image1))
    r.hset(key, "image2", str(good.image2))
    r.hset(key, "status", str(good.status))
    r.hset(key, "price", str(good.price))
    r.hset(key, "descs", str(good.descs))
    r.hset(key, "address", str(good.address))
    r.hset(key, "phone", str(good.phone))
    r.hset(key, "create_time", str(good.create_time))
    # r.hset(key, "time_stamp", str(good.time_stamp))

    print("publish_good_map", "key =", key)
    pass


# city good list
def publish_good_cgl(good, is_publish):

    r = redis.Redis(host='localhost', port=6379, db=0)

    key = "cgl_" + good.city_id

    if good.status == 1:
        r.lrem(key, str(good.id))
        print("publish_good_cgl", "is_publish =", str(is_publish), "remove", str(good.id))
    else:
        r.lpush(key, str(good.id))
        print("publish_good_cgl", "is_publish =", str(is_publish), "add", str(good.id))


# author good list
def publish_good_agl(good):
    # key   : agl_12
    # value : good id list

    r = redis.Redis(host='localhost', port=6379, db=0)

    key = "agl_" + str(good.author_id)

    r.lpush(key, str(good.id))

    print("publish_good_agl", "key =", key, "value =", str(good.id))


def publish_author(author):
    r = redis.Redis(host='localhost', port=6379, db=0)
    key = "a_" + str(author.id)

    # 作者信息
    r.hset(key, "id", str(author.id))
    r.hset(key, "openid", str(author.openid))
    r.hset(key, "nickname", str(author.nickname))
    r.hset(key, "town", str(author.town))
    r.hset(key, "address", str(author.address))
    r.hset(key, "point", str(author.point))
    r.hset(key, "phone", str(author.phone))
    r.hset(key, "town", str(author.town))
    r.hset(key, "status", str(author.status))

    print("publish_author", "key =", key, "value =", r.hgetall(key))

    return key


def publish_city(city):
    r = redis.Redis(host='localhost', port=6379, db=0)
    key = "c_" + str(city.id)

    # 城市分信息
    r.hset(key, "id", str(city.id))
    r.hset(key, "name", str(city.name))
    r.hset(key, "enabled", str(city.enabled))

    print("publish_city", "key =", key, "value =", r.hgetall(key))

    return key