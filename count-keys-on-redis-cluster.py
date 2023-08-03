#!/usr/bin/env python

import os

import redis


REDIS_CFG_HOST = os.environ.get('REDIS_CFG_HOST')
MATCH_GLOB = os.environ.get('REDIS_MATCH_GLOB')

key_count = 0

def main():
    global key_count
    conn = redis.cluster.RedisCluster(host=REDIS_CFG_HOST)

    for data in conn.scan_iter(MATCH_GLOB, 100000):
        key_count = key_count + 1

    print(f"All keys counted, there are {key_count} matching {MATCH_GLOB}")

try:
    if __name__ == '__main__':
        main()
except KeyboardInterrupt:
    print(f"Processed {key_count} keys")
    exit(1)
