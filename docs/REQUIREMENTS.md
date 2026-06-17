# REQUIREMENTS.md – med‑tech‑fusion  

**Document version:** 1.0 – 2026‑06‑17  
**Author:** Senior Product/Engineering Lead, Axentx  

---  

## 1. Overview  

med‑tech‑fusion is an Axentx product that provides a **software‑development platform** for creating **medical‑grade** applications that span **hardware, firmware, and cloud** components. The platform must enable developers, system integrators, and quality‑engineers to:

* Define device hardware profiles and generate corresponding firmware.  
* Deploy, test, and version firmware on physical or simulated devices.  
* Provision cloud services (data ingestion, analytics, AI inference) that are **HIPAA‑ and FDA‑compliant**.  
* Maintain a full audit trail, enforce role‑based access, and support continuous‑integration/continuous‑deployment (CI/CD) pipelines.  

The platform will be delivered as a set of containerised services with a web‑based UI and a REST/GraphQL API for automation.

---  

## 2. Scope  

| In‑Scope | Out‑Of‑Scope |
|----------|--------------|
| • Device onboarding & hardware abstraction layer. <br>• Firmware build, flash, and simulation. <br>• Cloud service provisioning (data lake, compute, AI inference). <br>• Regulatory compliance tooling (IEC 62304, 21 CFR Part 820). <br>• Audit logging, RBAC, and secure CI/CD integration. | • Manufacturing of medical devices. <br>• Direct patient‑care software (the platform only supports development, not deployment to patients). <br>• Custom hardware design (only integration of existing hardware). |

---  

## 3. Definitions  

| Term | Definition |
|------|------------|
| **Device Profile** | JSON/YAML description of a medical device’s hardware peripherals, communication interfaces, and safety requirements. |
| **Firmware Artifact** | Compiled binary (or ELF) that runs on the target microcontroller. |
| **Cloud Workspace** | Isolated set of cloud resources (storage, compute, AI endpoints) provisioned for a project. |
| **Regulatory Module** | Software component that validates design artefacts against IEC 62304 and FDA 21 CFR 820 rules. |
| **Audit Log** | Immutable, tamper‑evident record of all actions performed in the platform. |
| **vLLM** | Production‑grade LLM inference engine (used for AI‑assisted code generation). |
| **SGLang** | Structured‑generation language model (used for automated documentation). |

---  

## 4. Functional Requirements  

| ID | Requirement | Description |
|----|-------------|-------------|
| **FR‑1** | **Device Profile Management** | Users can create, edit, version, and delete device profiles via UI or API. Profiles must support at least: CPU architecture, peripheral map, safety class, and communication protocols (USB, BLE, CAN, etc.). |
| **FR‑2** | **Firmware Build Pipeline** | The platform must generate a reproducible build environment (Docker image) for each supported MCU family, compile source code, and produce signed firmware artifacts. |
| **FR‑3** | **Firmware Flash & Verification** | Provide a secure OTA and wired flashing service that can push firmware to physical devices or to a hardware‑in‑the‑loop (HIL) simulator, then verify checksum and runtime health. |
| **FR‑4** | **Hardware Simulation Environment** | Integrate an open‑source HIL simulator (e.g., Renode) to allow developers to run integration tests without physical hardware. |
| **FR‑5** | **Cloud Workspace Provisioning** | One‑click provisioning of a HIPAA‑compliant AWS GovCloud (or Azure Government) workspace that includes: S3 bucket, RDS instance, SageMaker endpoint, and IAM roles scoped to the project. |
| **FR‑6** | **Data Ingestion & Pipeline** | Secure ingestion of device telemetry (HL7/FHIR or custom JSON) into the cloud workspace, with schema validation and automatic storage in a time‑series database. |
| **FR‑7** | **AI‑Assisted Code Generation** | Expose vLLM‑backed LLM service to generate boiler‑plate firmware code, unit tests, and documentation, with output reviewed by the user before commit
