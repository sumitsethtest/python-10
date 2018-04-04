# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379)

"""1. Lpush 命令将一个或多个值插入到列表头部。 如果 key 不存在，一个空列表会被创建并执行 LPUSH 操作。 当 key 存在但不是列表类型时，返回一个错误。
执行 LPUSH 命令后，列表的长度。"""
# print(r.lpush("1",2,3,4))  #  输出的结果是3

"""2. Rpush 命令用于将一个或多个值插入到列表的尾部(最右边)。"""
# print(r.rpush('1', '张三', '1231awd', '1231'))

"""3.Blpop 命令移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。"""
# print(r.blpop('1', 10))

"""4.Brpop 命令移出并获取列表的最后一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。"""
# print(r.brpop('1'))

"""5. Brpoplpush 命令从列表中弹出一个值，将弹出的元素插入到另外一个列表中并返回它；
 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止"""
# print(r.brpoplpush(src='1', dst='张三', timeout=1))   # dst另一个列表的名字

""""""
