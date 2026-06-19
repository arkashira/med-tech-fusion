import json
from dataclasses import dataclass
from typing import List

@dataclass
class MedicalSoftware:
    name: str
    version: str
    hardware_dependencies: List[str]
    firmware_dependencies: List[str]
    cloud_dependencies: List[str]

    def compile(self):
        # Simulate compilation process
        return f"{self.name} compiled successfully"

    def integrate(self):
        # Simulate integration process
        return f"{self.name} integrated with hardware, firmware, and cloud components"

def create_medical_software(name: str, version: str, hardware_dependencies: List[str], firmware_dependencies: List[str], cloud_dependencies: List[str]) -> MedicalSoftware:
    return MedicalSoftware(name, version, hardware_dependencies, firmware_dependencies, cloud_dependencies)

def main():
    medical_software = create_medical_software("MedTechFusion", "1.0", ["Hardware1", "Hardware2"], ["Firmware1", "Firmware2"], ["Cloud1", "Cloud2"])
    print(medical_software.compile())
    print(medical_software.integrate())

if __name__ == "__main__":
    main()
