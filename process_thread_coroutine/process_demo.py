import traceback
import logging, time, sys
from random import random
from multiprocessing import Pool, Process

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)

def run(num=0):
    logging.info('Process %s start' % num)
    sleep_time = random() * 1000
    time.sleep(sleep_time)
    logging.info('Process %s end, and sleep %s s.' % (num, sleep_time))

def process_pool():
    num = int(sys.argv[1]) or 1  # 设置进程的数量,若没有这个参数则默认为1

    p = Pool()
    for i in range(num):
        print(i)
        p.apply_async(run, args=(i,))

    p.close()  # 不能再添加新的process了
    p.join()  # 等待子进程中全部结束
    logging.info('All subpresses done.')

def genprocess():
    pass


if __name__ == '__main__':
    p = Process(target=run, args=(2, ))
    p.start()
    p.join()
