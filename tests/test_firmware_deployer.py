from firmware_deployer import Firmware, FirmwareDeployer

def test_deploy_firmware():
    deployer = FirmwareDeployer()
    firmware = Firmware("test-firmware", "1.0", "aws")
    result = deployer.deploy_firmware(firmware)
    assert result == "Firmware test-firmware version 1.0 deployed to aws"

def test_get_deployment_status():
    deployer = FirmwareDeployer()
    firmware1 = Firmware("test-firmware1", "1.0", "aws")
    firmware2 = Firmware("test-firmware2", "2.0", "gcp")
    deployer.deploy_firmware(firmware1)
    deployer.deploy_firmware(firmware2)
    status = deployer.get_deployment_status()
    assert len(status) == 2
    assert status[0].name == "test-firmware1"
    assert status[1].name == "test-firmware2"

def test_deploy_firmware_edge_case():
    deployer = FirmwareDeployer()
    firmware = Firmware("", "", "")
    result = deployer.deploy_firmware(firmware)
    assert result == "Firmware  version  deployed to "
