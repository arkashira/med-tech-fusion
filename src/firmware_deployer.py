import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class Firmware:
    name: str
    version: str
    cloud_service: str

class FirmwareDeployer:
    def __init__(self):
        self.deployed_firmwares = []

    def deploy_firmware(self, firmware: Firmware):
        self.deployed_firmwares.append(firmware)
        return f"Firmware {firmware.name} version {firmware.version} deployed to {firmware.cloud_service}"

    def get_deployment_status(self):
        return self.deployed_firmwares

def main():
    parser = ArgumentParser(description="Firmware Deployer")
    parser.add_argument("--name", help="Firmware name")
    parser.add_argument("--version", help="Firmware version")
    parser.add_argument("--cloud-service", help="Cloud service to deploy to")
    args = parser.parse_args()

    deployer = FirmwareDeployer()
    firmware = Firmware(args.name, args.version, args.cloud_service)
    print(deployer.deploy_firmware(firmware))

if __name__ == "__main__":
    main()
