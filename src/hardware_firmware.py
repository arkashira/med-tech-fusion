from dataclasses import dataclass
from enum import Enum
from typing import List

class FirmwareStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILURE = 3

@dataclass
class Hardware:
    id: int
    name: str

@dataclass
class Firmware:
    id: int
    name: str
    status: FirmwareStatus

class HardwareFirmwarePipeline:
    def __init__(self):
        self.hardware = []
        self.firmware = []

    def add_hardware(self, hardware: 'Hardware'):
        self.hardware.append(hardware)

    def add_firmware(self, firmware: 'Firmware'):
        self.firmware.append(firmware)

    def sync(self):
        for hardware in self.hardware:
            for firmware in self.firmware:
                if hardware.id == firmware.id:
                    firmware.status = FirmwareStatus.SUCCESS
        return self.firmware
