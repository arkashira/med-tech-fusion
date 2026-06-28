# dataflow.md

## System Dataflow Architecture

```
+---------------------------+          +---------------------------+
|  External Data Sources    |          |  Egress to User           |
|  (Hardware, Firmware,     |          |  (Dashboards, APIs,       |
|   Cloud Services, IoT)    |          |   Reports)                |
+------------+--------------+          +------------+--------------+
             |                                     |
             v                                     v
+------------+--------------+          +------------+--------------+
|  Ingestion Layer          |          |  Query/Serving Layer      |
|  (Edge Gateways,          |          |  (GraphQL, REST,          |
|   MQTT, HTTP, SDKs)       |          |   Streaming)              |
+------------+--------------+          +------------+--------------+
             |                                     |
             v                                     v
+------------+--------------+          +------------+--------------+
|  Processing/Transform     |          |  Storage Tier             |
|  Layer (ETL, Validation,  |          |  (Data Lake, DB, Cache)   |
|   Anomaly Detection)      |          |  (Encrypted, Tiered)      |
+------------+--------------+          +------------+--------------+
```

---

### 1. External Data Sources
- **Medical Device Firmware**  
  - OTA update payloads (binary blobs)  
  - Device logs (structured JSON, binary telemetry)
- **Hardware Sensors**  
  - Real‑time vitals (ECG, SpO₂, BP) via BLE/USB  
  - Environmental sensors (temperature, humidity)
- **Cloud Services**  
  - Vendor APIs (e.g., FDA e‑Registry, HL7/FHIR endpoints)  
  - Third‑party analytics (e.g., Medidata, Redox)
- **User‑Generated Content**  
  - Clinical notes, imaging metadata, patient questionnaires

> **Auth Boundary:**  
> All external sources must authenticate via mutual TLS or OAuth2.0 with device certificates. Firmware updates are signed and verified before ingestion.

---

### 2. Ingestion Layer
| Component | Role | Auth/Compliance |
|-----------|------|-----------------|
| **Edge Gateway** | Aggregates sensor streams, buffers, forwards to cloud | TLS 1.3, device certs |
| **MQTT Broker** | Lightweight pub/sub for telemetry | ACLs, TLS |
| **HTTP/HTTPS API Gateway** | REST endpoints for firmware uploads, status queries | OAuth2.0, rate limiting |
| **SDK (iOS/Android/Embedded)** | Native client libraries for device integration | API keys, JWT |
| **Event Collector** | Centralized ingestion point (Kafka/Kinesis) | IAM roles, encryption at rest |

> **Auth Boundary:**  
> Edge gateways and SDKs must present device certificates or signed JWTs. API Gateway enforces OAuth scopes per operation.

---

### 3. Processing / Transform Layer
| Component | Function | Tech Stack | Auth/Compliance |
|-----------|----------|------------|-----------------|
| **Stream Processor** | Real‑time validation, anomaly detection, enrichment | Apache Flink / Spark Structured Streaming | TLS, Kerberos |
| **Batch ETL Jobs** | Periodic aggregation, feature engineering | Airflow + dbt | IAM, VPC |
| **Data Quality Engine** | Schema validation, missing‑value handling | Great Expectations | Role‑based access |
| **FHIR Mapper** | Convert raw telemetry to FHIR resources | HAPI FHIR | HIPAA‑compliant encryption |
| **Audit Logger** | Immutable audit trail of all transformations | WORM storage | GDPR, HIPAA |

> **Auth Boundary:**  
> Only authorized services with signed JWTs can trigger ETL jobs. All data passes through encrypted channels; audit logs are write‑once.

---

### 4. Storage Tier
| Layer | Storage | Encryption | Access Control |
|-------|---------|------------|----------------|
| **Raw Data Lake** | S3/MinIO (object store) | SSE‑S3 / SSE‑KMS | Bucket policies, IAM |
| **Processed Data Warehouse** | Redshift / Snowflake | Transparent Data Encryption | RBAC, column‑level |
| **Cache** | Redis / Memcached | TLS, in‑memory encryption | Service‑to‑service auth |
| **Metadata Catalog** | AWS Glue / DataHub | Encrypted at rest | Data stewards |
| **Immutable Ledger** | WORM / Immutable S3 | KMS | Audit‑only access |

> **Auth Boundary:**  
> All storage buckets enforce bucket policies; only services with specific IAM roles can read/write. Data at rest is encrypted with customer‑managed keys.

---

### 5. Query / Serving Layer
| Service | API | Auth | Rate Limits |
|---------|-----|------|-------------|
| **GraphQL API** | Unified schema for devices, telemetry, FHIR | OAuth2.0 scopes | 10k req/min |
| **REST API** | Legacy endpoints, firmware status | API keys | 5k req/min |
| **Streaming API** | WebSocket for live vitals | JWT | 1k concurrent |
| **Batch Export** | CSV/Parquet downloads | S3 pre‑signed URLs | 100 per day |
| **Analytics Dashboard** | Embedded UI (React) | SSO (OIDC) | N/A |

> **Auth Boundary:**  
> All serving endpoints require OAuth2.0 or JWT with scopes. SSO enforces MFA for admin dashboards.

---

### 6. Egress to User
- **Web Dashboard** (React + Material‑UI) – real‑time device health, alerts, compliance reports.  
- **Mobile App** (React Native) – patient‑centric vitals, medication reminders.  
- **API Clients** – SDKs for third‑party integration (FHIR, HL7).  
- **Export Services** – CSV/Excel/JSON for regulatory submissions.  

> **Auth Boundary:**  
> End‑user access is protected by OAuth2.0 with MFA. All data transmitted over TLS 1.3. Data residency controls per jurisdiction.

---

## Security & Compliance Highlights
- **HIPAA / GDPR**: All PHI encrypted in transit and at rest; audit logs immutable.  
- **Device Authentication**: Mutual TLS with X.509 certificates.  
- **Data Residency**: Geo‑partitioned data lakes per region.  
- **Audit Trail**: Immutable ledger of all data lineage events.  

---

*End of dataflow.md*