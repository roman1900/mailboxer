import asyncio
import time
import redis
from datetime import datetime


class RateDB:
    def __init__(self):
        pass
    def insert_with_expiry(self,value,expiry):
        pass
    def select_record_count(self):
        pass

class RedisConnect(RateDB):
    def __init__(self):
        self.conn = redis.Redis()
    def insert_with_expiry(self,value,expiry):
        now = datetime.now()
        self.conn.set(now.timestamp(),value, ex=expiry)
    def select_record_count(self):
        return len(self.conn.keys())

class RateLogger(): 
    def __init__(self,rateDB):
        self.db = rateDB 

    def log(self,value,expiry):
        self.db.insert_with_expiry(value,expiry)

class RateMonitor:
    def __init__(self,rateDB,secs,limit):
        self.secs = secs
        self.limit = limit
        self.db = rateDB
    def rate_per(self):
        return self.db.select_record_count() 
    def within_rate_limit(self):
        return self.rate_per() < self.limit

async def main():
    start = datetime.now()
    rc = RedisConnect()
    rateMonitor = RateMonitor(rc,10,130)
    rateLogger = RateLogger(rc)
    sleep = 0.1
    start = datetime.now()
    while (True):
        if (rateMonitor.within_rate_limit()):
            print(f"sleeping {sleep} seconds")
            time.sleep(sleep)
            if sleep < 5: sleep += 0.1 
            rateLogger.log(1,rateMonitor.secs)

        print(f"Current rate per {rateMonitor.secs} secs :{rateMonitor.rate_per()} of {rateMonitor.limit} max")

    
if __name__ == "__main__":
    asyncio.run(main())

