import redis 



def hello_redis():

    redisClient = redis.Redis()

    datas = {"name"  : "johncena" , "age" : 22, "country" : "china"}

    redisClient.hmset("stu:101" , datas)

    print(redisClient.hgetall("stu:101"))



hello_redis()

