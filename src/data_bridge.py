import json
import ssl
import argparse
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    transport: str
    cloud_provider: str
    tls_cert: str
    tls_key: str

class DataBridge:
    def __init__(self, config: Config):
        self.config = config
        self.transports = {
            'MQTT': self.mqtt_transport,
            'HTTPS': self.https_transport,
            'gRPC': self.grpc_transport
        }

    def mqtt_transport(self, message: str):
        # Simulate MQTT transport
        return f'MQTT: {message}'

    def https_transport(self, message: str):
        # Simulate HTTPS transport
        return f'HTTPS: {message}'

    def grpc_transport(self, message: str):
        # Simulate gRPC transport
        return f'gRPC: {message}'

    def send_message(self, message: str):
        if self.config.transport in self.transports:
            return self.transports[self.config.transport](message)
        else:
            raise ValueError('Invalid transport')

    @staticmethod
    def load_config(config_file: str):
        with open(config_file, 'r') as f:
            config_data = json.load(f)
        return Config(
            transport=config_data['transport'],
            cloud_provider=config_data['cloud_provider'],
            tls_cert=config_data['tls_cert'],
            tls_key=config_data['tls_key']
        )

    @classmethod
    def from_config_file(cls, config_file: str):
        config = cls.load_config(config_file)
        return cls(config)

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--config', help='Path to config file')
        parser.add_argument('--message', help='Message to send')
        args = parser.parse_args()
        bridge = DataBridge.from_config_file(args.config)
        print(bridge.send_message(args.message))

if __name__ == '__main__':
    DataBridge().main()
