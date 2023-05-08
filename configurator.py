# -*- coding: utf-8 -*-
# Include for processing the YAML file using classes
#
"""
After converting the config file to YAML instead of just a python include,
I needed to check for missing items and set a default.  This seems unwieldy
and I'm sure it can be improved, but it's working for now
"""


class YamlDict:
    def __load__(self, raw, name, default=None):
        try:
            var = raw[name]
        except KeyError:
            var = default
        return var

    def __default__(self, dict, name, default=None):
        try:
            var = dict[name]
        except TypeError:
            var = default
        return var


class Speedtest(YamlDict):
    def __init__(self, raw):
        self.servers = self.__load__(raw, "servers", [])
        self.threads = self.__load__(raw, "threads",None)
        self.interval = self.__load__(raw, "interval",7200)


class Mqtt(YamlDict):
    def __init__(self, raw):
        self.username = self.__load__(raw, "username", "speedtest-mqtt")
        self.password = self.__load__(raw, "password", "speedtest-mqtt")
        self.server = self.__load__(raw, "server", "127.0.0.1")
        self.serverPort = self.__load__(raw, "server_port", 1883)
        self.topic = self.__load__(raw, "topic", "speedtest")
        self.qos = self.__load__(raw, "qos", 0)


class Config:
    def __init__(self, raw):
        try:
            self.speedtest = Speedtest(raw["speedtest"])
        except KeyError:
            self.speedtest = Speedtest({})
        try:
            self.mqtt = Mqtt(raw["mqtt"])
        except KeyError:
            self.mqtt = Mqtt({})
        try:
            self.debug = raw["debug"]
        except KeyError:
            self.debug = False
