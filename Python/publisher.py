import paho.mqtt.publish as publish

msgs = [{'topic':"topology/test/multiple", 'payload':"multiple 1"},
    ("topology", "multiple 2", 0, False)]
publish.multiple(msgs, hostname="localhost")
