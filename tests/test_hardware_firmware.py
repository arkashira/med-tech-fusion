import pytest
from src.hardware_firmware import HardwareFirmwarePipeline, FirmwareStatus, Hardware, Firmware

def test_sync_happy_path():
    pipeline = HardwareFirmwarePipeline()
    hardware = Hardware(1, "Hardware 1")
    firmware = Firmware(1, "Firmware 1", FirmwareStatus.PENDING)
    pipeline.add_hardware(hardware)
    pipeline.add_firmware(firmware)
    result = pipeline.sync()
    assert result[0].status == FirmwareStatus.SUCCESS

def test_sync_edge_case():
    pipeline = HardwareFirmwarePipeline()
    hardware = Hardware(2, "Hardware 2")
    firmware = Firmware(1, "Firmware 1", FirmwareStatus.PENDING)
    pipeline.add_hardware(hardware)
    pipeline.add_firmware(firmware)
    result = pipeline.sync()
    assert result[0].status == FirmwareStatus.PENDING
