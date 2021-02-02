import redis


def connect():
    r = redis.StrictRedis(host='47.97.184.36', port=3310, db=0, decode_responses=True)
    return r


def clear(r: redis):
    r.flushdb()


def clear_all(r: redis):
    r.flushall()

