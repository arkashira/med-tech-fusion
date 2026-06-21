import pytest
import json
from src.data_bridge import DataBridge, Config

def test_mqtt_transport():
    config = Config('MQTT', 'AWS', 'tls_cert', 'tls_key')
    bridge = DataBridge(config)
    assert bridge.send_message('Hello, world!') == 'MQTT: Hello, world!'

def test_https_transport():
    config = Config('HTTPS', 'Azure', 'tls_cert', 'tls_key')
    bridge = DataBridge(config)
    assert bridge.send_message('Hello, world!') == 'HTTPS: Hello, world!'

def test_grpc_transport():
    config = Config('gRPC', 'GCP', 'tls_cert', 'tls_key')
    bridge = DataBridge(config)
    assert bridge.send_message('Hello, world!') == 'gRPC: Hello, world!'

def test_invalid_transport():
    config = Config('Invalid', 'AWS', 'tls_cert', 'tls_key')
    bridge = DataBridge(config)
    with pytest.raises(ValueError):
        bridge.send_message('Hello, world!')

def test_load_config():
    config_file = 'config.json'
    with open(config_file, 'w') as f:
        json.dump({
            'transport': 'MQTT',
            'cloud_provider': 'AWS',
            'tls_cert': 'tls_cert',
            'tls_key': 'tls_key'
        }, f)
    bridge = DataBridge.from_config_file(config_file)
    assert bridge.config.transport == 'MQTT'
    assert bridge.config.cloud_provider == 'AWS'
    assert bridge.config.tls_cert == 'tls_cert'
    assert bridge.config.tls_key == 'tls_key'
