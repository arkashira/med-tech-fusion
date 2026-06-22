import pytest
from med_tech_fusion import MedTechFusion, Hardware, Simulation

def test_add_hardware():
    med_tech_fusion = MedTechFusion()
    hardware = Hardware("Device1", "1.0")
    med_tech_fusion.add_hardware(hardware)
    assert len(med_tech_fusion.hardware_devices) == 1

def test_simulate():
    med_tech_fusion = MedTechFusion()
    hardware = Hardware("Device1", "1.0")
    med_tech_fusion.add_hardware(hardware)
    simulation = med_tech_fusion.simulate("Device1", "1.0")
    assert simulation.sync_status

def test_simulate_hardware_not_found():
    med_tech_fusion = MedTechFusion()
    with pytest.raises(ValueError):
        med_tech_fusion.simulate("Device1", "1.0")

def test_get_simulations():
    med_tech_fusion = MedTechFusion()
    hardware = Hardware("Device1", "1.0")
    med_tech_fusion.add_hardware(hardware)
    med_tech_fusion.simulate("Device1", "1.0")
    simulations = med_tech_fusion.get_simulations()
    assert len(simulations) == 1

def test_reduce_development_time():
    med_tech_fusion = MedTechFusion()
    hardware = Hardware("Device1", "1.0")
    med_tech_fusion.add_hardware(hardware)
    simulation = med_tech_fusion.simulate("Device1", "1.0")
    reduction = med_tech_fusion.reduce_development_time(simulation)
    assert reduction == 0.2

def test_reduce_development_time_no_sync():
    med_tech_fusion = MedTechFusion()
    hardware = Hardware("Device1", "1.0")
    med_tech_fusion.add_hardware(hardware)
    simulation = med_tech_fusion.simulate("Device1", "2.0")
    reduction = med_tech_fusion.reduce_development_time(simulation)
    assert reduction == 0.0
