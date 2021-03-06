from amqpez import AMQPEzConfigBuilder, AMQPEz

def deserialize(x):
    return int(x)

def serialize(x):
    return str(x)

conf = AMQPEzConfigBuilder() \
        .add_connection_params("localhost") \
        .add_basic_credentials("guest", "guest") \
        .add_exchange("test_exchange") \
        .add_queue('test_queue') \
        .add_serializers(serialize, deserialize) \
        .add_task(lambda x: x+5) \
        .add_qos(1) \
        .build() 

amqpez = AMQPEz(conf)
try:
    amqpez.start()
except KeyboardInterrupt:
    amqpez.stop()