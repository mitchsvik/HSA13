# HSA13
Redis vs Beanstalkd 

The examples use 3 instances: `beanstalkd`, `redis` with AOF mode, `redis` with RDB mode.
For each instance evaluating performace of write and read 1M jobs

#### Redis storage configuration

Check for 100000 changes in 10 seconds

### Beanstalkd

```
hsa13_test        | Benchmark Beanstalkd
hsa13_test        | Put 1000000 records in queue
hsa13_test        | Took 48.12317181399999 seconds to populate queue
hsa13_test        | Took 91.14896537599998 seconds to process queue (reserve + delete)
```

### Redis + AOF

```
hsa13_test        | Benchmark Redis with AOF mode
hsa13_test        | Put 1000000 records in queue
hsa13_test        | Took 59.853800070000034 seconds to populate queue
hsa13_test        | Took 58.562333652000234 seconds to process queue
```

### Redis + RDB

```
hsa13_test        | Benchmark Redis with RDB mode
hsa13_test        | Put 1000000 records in queue
hsa13_test        | Took 57.503122234999864 seconds to populate queue
hsa13_test        | Took 56.91890110899931 seconds to process queue
```
