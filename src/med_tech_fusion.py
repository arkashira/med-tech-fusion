import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Hardware:
    name: str
    firmware_version: str

@dataclass
class Simulation:
    hardware: Hardware
    firmware: str
    sync_status: bool

class MedTechFusion:
    def __init__(self):
        self.hardware_devices = []
        self.simulations = []

    def add_hardware(self, hardware: Hardware):
        self.hardware_devices.append(hardware)

    def simulate(self, hardware_name: str, firmware: str) -> Simulation:
        hardware = next((h for h in self.hardware_devices if h.name == hardware_name), None)
        if hardware is None:
            raise ValueError("Hardware device not found")
        sync_status = hardware.firmware_version == firmware
        simulation = Simulation(hardware, firmware, sync_status)
        self.simulations.append(simulation)
        return simulation

    def get_simulations(self) -> List[Simulation]:
        return self.simulations

    def reduce_development_time(self, simulation: Simulation) -> float:
        if simulation.sync_status:
            return 0.2  # 20% reduction
        else:
            return 0.0
