import pytest
from src.med_tech_fusion import MedicalSoftware, create_medical_software

def test_medical_software_compilation():
    medical_software = create_medical_software("MedTechFusion", "1.0", ["Hardware1", "Hardware2"], ["Firmware1", "Firmware2"], ["Cloud1", "Cloud2"])
    assert medical_software.compile() == "MedTechFusion compiled successfully"

def test_medical_software_integration():
    medical_software = create_medical_software("MedTechFusion", "1.0", ["Hardware1", "Hardware2"], ["Firmware1", "Firmware2"], ["Cloud1", "Cloud2"])
    assert medical_software.integrate() == "MedTechFusion integrated with hardware, firmware, and cloud components"

def test_medical_software_creation():
    medical_software = create_medical_software("MedTechFusion", "1.0", ["Hardware1", "Hardware2"], ["Firmware1", "Firmware2"], ["Cloud1", "Cloud2"])
    assert medical_software.name == "MedTechFusion"
    assert medical_software.version == "1.0"
    assert medical_software.hardware_dependencies == ["Hardware1", "Hardware2"]
    assert medical_software.firmware_dependencies == ["Firmware1", "Firmware2"]
    assert medical_software.cloud_dependencies == ["Cloud1", "Cloud2"]

def test_medical_software_empty_dependencies():
    medical_software = create_medical_software("MedTechFusion", "1.0", [], [], [])
    assert medical_software.compile() == "MedTechFusion compiled successfully"
    assert medical_software.integrate() == "MedTechFusion integrated with hardware, firmware, and cloud components"
