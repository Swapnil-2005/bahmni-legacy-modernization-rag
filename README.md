An AI-powered RAG system that extracts and explains hidden business logic from legacy healthcare codebases to enable safe modernization.
🔹 Project Summary 

Built an AI-powered system to understand and modernize legacy healthcare software

Uses Retrieval-Augmented Generation (RAG) to explain real business logic from code

Designed specifically for large, risky-to-change enterprise systems

Prevents loss of hidden business & medical rules during modernization

Works on actual source code, not assumptions or documentation

🔹 What This Tool Helps With

Understand complex legacy Java codebases like Bahmni-Core

Discover embedded healthcare workflows and validation rules

Reduce risk before refactoring or migrating legacy systems

Help new developers onboard faster to large enterprise systems

Provide human-readable explanations grounded in real code

🔹 Business Value

Safer legacy modernization

Faster understanding of critical systems

Lower maintenance and refactoring risk

Preserves years of embedded domain knowledge

Especially valuable for healthcare IT systems


┌──────────────────────┐
│  Bahmni-Core         │
│  Java Source Code    │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│  Code Ingestion      │
│  (.java file scan)   │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│  Code Chunking       │
│  (file-level docs)  │
└─────────┬────────────┘
          │
          ▼
┌────────────────────────────┐
│  Vector Embeddings          │
│  (semantic meaning)         │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│  Vector Store (FAISS)       │
│  Fast similarity search     │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│  Retriever                 │
│  (top-k relevant code)     │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│  LLM Reasoning (Sarvam AI)  │
│  Uses ONLY retrieved code  │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│  Human-Readable Explanation│
│  (rules, workflows, logic) │
└────────────────────────────┘



Python Codebase
│
├── ingest.py     → Scans Java files
├── chunk.py      → Creates semantic documents
├── embed.py      → Builds vector store (FAISS)
├── retrieve.py   → Finds relevant code chunks
├── generate.py   → LLM explanation layer
└── app.py        → Streamlit UI

query : What is Bahmni-Core and what problem does it solve?
Ans: 
1. Bahmni-Core is the foundational module of the Bahmni platform, designed to address critical challenges in healthcare IT systems, particularly in resource-constrained environments like India. It solves the following key problems:
2.Complex Observation Handling: Manages structured and unstructured patient data (e.g., vitals, diagnoses) efficiently, supporting complex observations like location data through specialized handlers (e.g., LocationObsHandler).
3.Data Retrieval Limitations: Provides services to fetch the latest patient observations (e.g., getLatest), observations by visit/encounter, and patient-program-specific data, overcoming OpenMRS's rigid querying constraints.
4.Legacy System Integration: Acts as a middleware layer to simplify integration with legacy systems (e.g., OpenMRS) while adding Bahmni-specific functionality like visit-aware data filtering and multi-concept grouping.
5.Error Handling: Standardizes error reporting through custom exceptions (e.g., BahmniCoreException, CannotModifyEncounterException) for consistent debugging and system reliability.
By abstracting low-level complexities, Bahmni-Core enables scalable, maintainable healthcare applications tailored to Indian public health needs.

