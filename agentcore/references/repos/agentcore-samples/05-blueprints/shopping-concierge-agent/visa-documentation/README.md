---
title: Visa Payment Integration Documentation
description: This directory contains comprehensive documentation for integrating Visa's tokenization and passkey authentication into your AI agent application.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/05-blueprints/shopping-concierge-agent/visa-documentation/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Visa Payment Integration Documentation

This directory contains comprehensive documentation for integrating Visa's tokenization and passkey authentication into your AI agent application.

## Documentation Overview

### 📖 [Visa Payment Integration Guide](visa-payment-integration-guide.md)
**Start here** - A complete walkthrough of the Visa payment integration process, covering:
- Architecture overview (VTS, VIC, Auth iFrame)
- Prerequisites and credentials
- Phase-by-phase implementation steps
- Data storage considerations
- Security best practices

### 🔄 [Travel Booking Flow Diagram](travel-booking-sequence-diagram.md)
Visual sequence diagram showing the complete payment flow in a **travel booking context**:
- User books a flight
- Card tokenization (one-time setup)
- Passkey creation (one-time setup)
- Payment authentication and completion

### 🛍️ [Shopping Flow Diagram](shopping-sequence-diagram.md)
Visual sequence diagram showing the complete payment flow in a **shopping context**:
- User purchases products
- Card tokenization (one-time setup)
- Passkey creation (one-time setup)
- Payment authentication and completion

## Quick Navigation

### For First-Time Implementation
1. Read the [Visa Payment Integration Guide](visa-payment-integration-guide.md) to understand the overall flow
2. Review the [Travel Booking Diagram](travel-booking-sequence-diagram.md) or [Shopping Diagram](shopping-sequence-diagram.md) to visualize the sequence
3. Refer back to the Visa Payment Integration Guide for detailed step-by-step instructions

### For Understanding Specific Flows
- **Travel/Booking Use Case** → [Travel Booking Diagram](travel-booking-sequence-diagram.md)
- **E-commerce/Shopping Use Case** → [Shopping Diagram](shopping-sequence-diagram.md)

### For Technical Details
- **API Endpoints and Payloads** → [Visa Payment Integration Guide](visa-payment-integration-guide.md)
- **Data Storage** → [Visa Payment Integration Guide - Data Storage Considerations](visa-payment-integration-guide.md#data-storage-considerations)
- **Security** → [Visa Payment Integration Guide - Security Best Practices](visa-payment-integration-guide.md#security-best-practices)

## Key Concepts

### The Three Visa Services
- **VTS (Visa Token Service)** - Converts card numbers to secure tokens and manages device binding
- **VIC (Visa Intelligent Commerce)** - Orchestrates payment transactions and generates cryptograms
- **Auth iFrame** - Provides secure passkey creation and authentication interface

### The Two Phases
1. **One-Time Setup** (Phases 2-3)
   - Card tokenization
   - Passkey creation and device binding
   
2. **Per-Transaction** (Phases 4-5)
   - Passkey authentication
   - Payment credential generation
   - Transaction completion

## Contributing

When updating this documentation:
- Verify all information against the source API documentation
- Avoid adding speculative security explanations
- Keep implementation suggestions (not prescriptive requirements)
- Update both diagrams if the flow changes
- Maintain consistency across all three documents
