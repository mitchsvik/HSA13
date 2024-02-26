import json
from time import perf_counter, sleep

import redis
from pystalk import BeanstalkClient


ONE_MILION_ITERATIONS = 1000000


def benchmark_beanstalk():
    print('Benchmark Beanstalkd')
    client = BeanstalkClient('beanstalkd', 11300)

    print(f'Put {ONE_MILION_ITERATIONS} records in queue')
    time_start_put = perf_counter()
    for it in range(ONE_MILION_ITERATIONS):
        client.put_job(json.dumps({'job': it}))
    time_end_put = perf_counter()
    time_duration = time_end_put - time_start_put
    print(f'Took {time_duration} seconds to populate queue')

    time_start_reserve = perf_counter()
    for it in range(ONE_MILION_ITERATIONS):
        job = client.reserve_job(1)
        client.delete_job(job.job_id)
    time_end_reserve = perf_counter()
    time_duration = time_end_reserve - time_start_reserve
    print(f'Took {time_duration} seconds to process queue')


def redis_benchmark(client):
    print(f'Put {ONE_MILION_ITERATIONS} records in queue')
    time_start_put = perf_counter()
    for it in range(ONE_MILION_ITERATIONS):
        client.lpush('hsa10', json.dumps({'job': it}))
    time_end_put = perf_counter()
    time_duration = time_end_put - time_start_put
    print(f'Took {time_duration} seconds to populate queue')

    time_start_reserve = perf_counter()
    for it in range(ONE_MILION_ITERATIONS):
        client.rpop('hsa10', 1)
    time_end_reserve = perf_counter()
    time_duration = time_end_reserve - time_start_reserve
    print(f'Took {time_duration} seconds to process queue')


def redis_aof_benchmark():
    print('Benchmark Redis with AOF mode')
    client = redis.Redis(host='redis_aof', port=6379, decode_responses=True)

    redis_benchmark(client)


def redis_rdb_benchmark():
    print('Benchmark Redis with RDB mode')
    client = redis.Redis(host='redis_rdb', port=6380, decode_responses=True)

    redis_benchmark(client)


if __name__ == '__main__':
    print('Will start in 10 seconds')
    sleep(10)
    print('Start...')
    # Beanstalk benchmark
    benchmark_beanstalk()
    # Redis AOF benchmark
    redis_aof_benchmark()
    # Redis RDB benchmark
    redis_rdb_benchmark()
