#! /usr/bin/python
# -*- coding:utf-8 -*

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.structs import TopicPartition

import time

#   ----------------------------模拟kafka产生消息和消费消息--------------------


bootstrap_servers = []
class OperateKafka:
    def __init__(self,bootstrap_servers,topic):
     self.bootstrap_servers = bootstrap_servers
     self.topic = topic
     print('ip=',self.bootstrap_servers)
     print('topic=', self.topic)
#生产者
    def produce(self):
       producer = KafkaProducer(bootstrap_servers = self.bootstrap_servers)
       for i in range(4):
          msg = "msg%d" %i
    # producer.send(self.topic,key=str(i).uo,value=msg)#报错，需增加编码格式转成2进制发送，改成如下
      # producer.send(self.topic, key=str(i).encode('utf-8'), value=msg.encode('utf-8'))
          producer.send(self.topic, key=str(i).encode('utf-8'), value=msg.encode('utf-8'))
    # producer.send(self.topic, key=b'foo', value=b'bar')
    # response = producer.send(self.topic, msg, partition=0)
    # print('response=',response)
       producer.close()

#消费者
    def consume(self):
        consumer = KafkaConsumer(self.topic,bootstrap_servers = self.bootstrap_servers)
        print(consumer.partitions_for_topic(self.topic))
        print(consumer.topics())
        print(consumer.subscription())
        print(consumer.assignment())
        print(consumer.beginning_offsets(consumer.assignment()))

        consumer.seek(TopicPartition(topic=self.topic,partition=0),1)
        for message in consumer:
            print("%s:%d:%d: key=%s value=%s"
            % (message.topic,message.partition,message.offset, message.key,message.value))

#一个消费者订阅多个topic
    def consums(self):
        consumer = KafkaConsumer(bootstrap_servers=['192.168.1.179:9092'])
        consumer.subscribe(topics=['test','test1','test2','test3'])
        print(consumer.topics())
        print(consumer.position(TopicPartition(topic='test3',partition=0)))
        for message in consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            message.offset, message.key,
            message.value))

    def consumepoll(self):
        consumer = KafkaConsumer(group_id="mygroup",max_poll_interval_ms=3,bootstrap_servers=['192.168.1.179:9092'])
        consumer.subscribe(topics=('test2','test3'))
        while True:
            message = consumer.poll(timeout_ms=5)
            if message:
                print(message)
                time.sleep(1)



def main():
    bootstrap_servers = ['192.168.13.210:31090']
    topic = 'ifaas-imageStructure'

    operateKfk = OperateKafka(bootstrap_servers,topic)
    #operateKfk.produce()
    operateKfk.consume()

if __name__ == '__main__':
    main()
