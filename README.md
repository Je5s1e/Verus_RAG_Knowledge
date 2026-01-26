# Verus_RAG_Knowledge

Verus_RAG_Knowledge is a specialized knowledge base designed to facilitate the automated generation of formal specifications for Verus projects. It aggregates high-value external knowledge—including official tutorial documentation and verified codebases from open-source GitHub repositories—to provide LLMs with the necessary context for complex formal reasoning.

## Core Tooling & Standard Library

These repositories provide the fundamental logic rules and the mathematical definitions used by the Verus verifier.

| Source | Description | Link |
| --- | --- | --- |
| **Verus Core** | The primary repository for the Verus verifier and the `vstd` source code. | [verus-lang/verus](https://github.com/verus-lang/verus) |
| **VSTD API** | The official API reference for the Verus Standard Library (Essential for indexing `requires`/`ensures` contracts). | [vstd Documentation](https://verus-lang.github.io/verus/verusdoc/vstd/) |


## Documentation & Theoretical Guides

Critical for training or prompting the model on Verus-specific concepts like triggers, invariants, and state machine transitions.

| Source | Knowledge Type | Link |
| --- | --- | --- |
| **Verus Guide** | Comprehensive tutorial covering syntax, proof techniques, and the `verus!` macro. | [Verus Guide & Reference](https://verus-lang.github.io/verus/guide/) |
| **Transition Systems** | Specialized documentation for verifying state machines and asynchronous logic. | [State Machines Guide](https://verus-lang.github.io/verus/state_machines/) |


## Verified System Projects (Case Studies)

These production-grade projects serve as "Golden Examples" for the RAG system, offering complex, real-world proof patterns.

| Project | Domain | Link |
| --- | --- | --- |
| **VeriSMo** | A verified security module for confidential virtual machines. | [microsoft/verismo](https://github.com/microsoft/verismo) |
| **Anvil** | A framework for verifying Kubernetes controllers. | [anvil-verifier/anvil](https://github.com/anvil-verifier/anvil) |
| **Vest** | A high-performance verified binary parser and serializer framework. | [secure-foundations/vest](https://github.com/secure-foundations/vest) |
| **IronKV** | A formally verified, sharded key-value store. | [verus-lang/verified-ironkv](https://github.com/verus-lang/verified-ironkv) |
