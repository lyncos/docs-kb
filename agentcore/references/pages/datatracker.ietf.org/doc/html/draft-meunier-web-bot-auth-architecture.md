---
title: HTTP Message Signatures for automated traffic Architecture
description: 'Workgroup: Web Bot Auth'
product: Amazon Bedrock AgentCore
section: References / datatracker.ietf.org
source_url: https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture
fetched: '2026-09-26'
tags:
- agentcore
- datatracker-ietf-org
- reference
- related
referenced_by:
- browser-web-bot-auth.md
conversion: pandoc
---

-  Light
-  Dark
-  Auto

  

| Internet-Draft  | HTTP Message Signatures for Bots | March 2026 |
|-----------------|----------------------------------|------------|
| Meunier & Major | Expires 3 September 2026         | \[Page\]   |

Workgroup:  
Web Bot Auth

Internet-Draft:  
draft-meunier-web-bot-auth-architecture-05

Published:  
2 March 2026

Intended Status:  
Informational

Expires:  
3 September 2026

Authors:  
T. Meunier

Cloudflare

S. Major

Google

# HTTP Message Signatures for automated traffic Architecture

## [Abstract](#abstract)

This document describes an architecture for identifying automated traffic using \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. The goal is to allow automated HTTP clients to cryptographically sign outbound requests, allowing HTTP servers to verify their identity with confidence.[¶](#section-abstract-1)

## [About This Document](#name-about-this-document)

This note is to be removed before publishing as an RFC.[¶](#section-note.1-1)

The latest revision of this draft can be found at <https://thibmeu.github.io/http-message-signatures-directory/draft-meunier-web-bot-auth-architecture.html>. Status information for this document may be found at <https://datatracker.ietf.org/doc/draft-meunier-web-bot-auth-architecture/>.[¶](#section-note.1-2)

Discussion of this document takes place on the Web Bot Auth Working Group mailing list ([mailto:web-bot-auth@ietf.org](mailto:web-bot-auth@ietf.org)), which is archived at <https://mailarchive.ietf.org/arch/browse/web-bot-auth/>. Subscribe at <https://www.ietf.org/mailman/listinfo/web-bot-auth/>.[¶](#section-note.1-3)

Source for this draft and an issue tracker can be found at <https://github.com/thibmeu/http-message-signatures-directory>.[¶](#section-note.1-4)

## [Status of This Memo](#name-status-of-this-memo)

This Internet-Draft is submitted in full conformance with the provisions of BCP 78 and BCP 79.[¶](#section-boilerplate.1-1)

Internet-Drafts are working documents of the Internet Engineering Task Force (IETF). Note that other groups may also distribute working documents as Internet-Drafts. The list of current Internet-Drafts is at <https://datatracker.ietf.org/drafts/current/>.[¶](#section-boilerplate.1-2)

Internet-Drafts are draft documents valid for a maximum of six months and may be updated, replaced, or obsoleted by other documents at any time. It is inappropriate to use Internet-Drafts as reference material or to cite them other than as "work in progress."[¶](#section-boilerplate.1-3)

This Internet-Draft will expire on 3 September 2026.[¶](#section-boilerplate.1-4)

## [Copyright Notice](#name-copyright-notice)

Copyright (c) 2026 IETF Trust and the persons identified as the document authors. All rights reserved.[¶](#section-boilerplate.2-1)

This document is subject to BCP 78 and the IETF Trust's Legal Provisions Relating to IETF Documents (<https://trustee.ietf.org/license-info>) in effect on the date of publication of this document. Please review these documents carefully, as they describe your rights and restrictions with respect to this document. Code Components extracted from this document must include Revised BSD License text as described in Section 4.e of the Trust Legal Provisions and are provided without warranty as described in the Revised BSD License.[¶](#section-boilerplate.2-2)

[▲](#)

## [Table of Contents](#name-table-of-contents)

## [1.](#section-1) [Introduction](#name-introduction)

Agents are increasingly used in business and user workflows, including AI assistants, search indexing, content aggregation, and automated testing. These agents need to reliably identify themselves to origins for several reasons:[¶](#section-1-1)

1.  Regulatory compliance requiring transparency of automated systems[¶](#section-1-2.1.1)

2.  Origin resource management and access control[¶](#section-1-2.2.1)

3.  Protection against impersonation and reputation management[¶](#section-1-2.3.1)

4.  Service level differentiation between human and automated traffic[¶](#section-1-2.4.1)

Current identification methods such as IP allowlisting, User-Agent strings, or shared API keys have significant limitations in security, scalability, and manageability. This document defines an architecture enabling agents to cryptographically identify themselves using \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. It proposes that every request from bots to be signed by a private key owned by its provider. This way, every origin can validate the service identity.[¶](#section-1-3)

## [2.](#section-2) [Motivation](#name-motivation)

There is an increase in agent traffic on the Internet. Many agents choose to identify their traffic today via IP Address lists and/or unique User-Agents. This is often done to demonstrate trust and safety claims, support allowlisting/denylisting the traffic in a granular manor, and enable sites to monitor and rate limit per agent operator. However, these mechanisms have drawbacks:[¶](#section-2-1)

1.  User-Agent, when used alone, can be spoofed meaning anyone may attempt to act as that agent. It is also overloaded - an agent may be using Chromium and wish to present itself as such to ensure rendering works, yet it still wants to differentiate its traffic to the site.[¶](#section-2-2.1.1)

2.  IP blocks alone can present a confusing story. IPs on cloud plaforms have layers of ownership - the platform owns the IP and registers it in their published IP blocks, only to be re-published by the agent with little to bind the publication to the actual service provider that may be renting infra. Purchasing dedicated IP blocks is expensive, time consuming, and requires significant specialist knowledge to set up. These IP blocks may have prior reputation history that needs to be carefully inspected and managed before purchase and use.[¶](#section-2-2.2.1)

3.  An agent may go to every website on the Internet and share a secret with them like a Bearer from \[[OAUTH-BEARER](#OAUTH-BEARER)\]. This is impractical to scale for any agent beyond select partnerships, and insecure, as key rotation is challenging and becomes less secure as the consumers scale.[¶](#section-2-2.3.1)

Using well-established cryptography, we can instead define a simple and secure mechanism that empowers small and large agents to share their identity.[¶](#section-2-3)

### [2.1.](#section-2.1) [HTTP layer choice](#name-http-layer-choice)

This architecture operates solely at the HTTP layer. It allows signatures to be generated and verified without modifying the transport layer or TLS stack. It enables flexible deployment across proxies, gateways, and origin servers, and aligns with existing tooling and infrastructure that already inspect and manipulate HTTP headers.[¶](#section-2.1-1)

Because the signature is embedded in the request itself, it travels with the message through intermediaries, preserving end-to-end verifiability even when requests are forwarded or transformed within the HTTP layer.[¶](#section-2.1-2)

## [3.](#section-3) [Conventions and Definitions](#name-conventions-and-definitions)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)\] \[[RFC8174](#RFC8174)\] when, and only when, they appear in all capitals, as shown here.[¶](#section-3-1)

The following terms are used throughout this document:[¶](#section-3-2)

**User**  
An entity initiating requests through an agent. May be a human operator or another system.[¶](#section-3-3.2.1)

**Agent**  
An orchestrated user agent (e.g. Chromium, CURL). It implements the HTTP protocol and constructs valid HTTP requests with \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\] signatures.[¶](#section-3-3.4.1)

**Origin**  
An HTTP server receiving signed requests that implements the HTTP protocol and verifies \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\] signatures. It acts as a verifier of the signature as defined by \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\].[¶](#section-3-3.6.1)

## [4.](#section-4) [Architecture](#name-architecture)

[¶](#section-4-1.1)

A User initiates an action requiring the Agent to perform an HTTP request. The Agent constructs the request, generates a signature using its signing key, and includes it in the request as defined in [Section 3.1](https://rfc-editor.org/rfc/rfc9421#section-3.1) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\] along with the `Signature-Agent` header for discovery for its verification key. Upon receiving the request, the Origin ensures it has the verification key for the Agent, validates the signature, and processes the request if the signature is valid.[¶](#section-4-2)

### [4.1.](#section-4.1) [Deployment Models](#name-deployment-models)

Signature verification can be performed either directly by origins or delegated to a fronting proxy. Direct verification by origins provides simplicity and control. Proxy verification offloads processing and enables shared caching across multiple origins. The choice depends on traffic volume and operational requirements.[¶](#section-4.1-1)

### [4.2.](#section-4.2) [Generating HTTP Message Signature](#name-generating-http-message-sig)

\[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\] defines components to be signed.[¶](#section-4.2-1)

Agents MUST include at least one of the following components:[¶](#section-4.2-2)

`@authority`  
as defined in [Section 2.2.3](https://rfc-editor.org/rfc/rfc9421#section-2.2.3) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\][¶](#section-4.2-3.2.1)

`@target-uri`  
as defined in [Section 2.2.2](https://rfc-editor.org/rfc/rfc9421#section-2.2.2) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\][¶](#section-4.2-3.4.1)

Agents MUST include the following `@signature-params` as defined in [Section 2.3](https://rfc-editor.org/rfc/rfc9421#section-2.3) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\][¶](#section-4.2-4)

`created`  
as defined in [Section 2.3](https://rfc-editor.org/rfc/rfc9421#section-2.3) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\][¶](#section-4.2-5.2.1)

`expires`  
as defined in [Section 2.3](https://rfc-editor.org/rfc/rfc9421#section-2.3) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\][¶](#section-4.2-5.4.1)

`keyid`  
MUST be a base64url JWK SHA-256 Thumbprint as defined in [Section 3.2](https://rfc-editor.org/rfc/rfc7638#section-3.2) of \[[JWK-THUMBPRINT](#JWK-THUMBPRINT)\] for RSA and EC, and in [Appendix A.3](https://rfc-editor.org/rfc/rfc8037#appendix-A.3) of \[[JWK-OKP](#JWK-OKP)\] for ed25519.[¶](#section-4.2-5.6.1)

`tag`  
MUST be `web-bot-auth`[¶](#section-4.2-5.8.1)

The signing key is available to the agent at request time. Algorithms should be registered with IANA as part of HTTP Message Signatures Algorithm registry.[¶](#section-4.2-6)

The creation of the signature is defined in [Section 3.1](https://rfc-editor.org/rfc/rfc9421#section-3.1) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\].[¶](#section-4.2-7)

It is RECOMMENDED the expiry to be no more than 24 hours.[¶](#section-4.2-8)

#### [4.2.1.](#section-4.2.1) [Signature-Agent](#name-signature-agent)

`Signature-Agent` is an HTTP Method context header defined in Section 4.1 of \[[DIRECTORY](#DIRECTORY)\]. It is RECOMMENDED that the Agent sends requests with `Signature-Agent` header, as described in [Section 4.2.4](#sending-request). If the header is to be sent, one of its members MUST be signed as a component as defined in [Section 2.1](https://rfc-editor.org/rfc/rfc9421#section-2.1) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\].[¶](#section-4.2.1-1)

This results in the following components to be signed[¶](#section-4.2.1-2)

    ("@authority" "signature-agent";key="sig1")

[¶](#section-4.2.1-3)

It is RECOMMENDED that the `key` matches the signature label.[¶](#section-4.2.1-4)

#### [4.2.2.](#section-4.2.2) [Anti-replay](#name-anti-replay)

Origins MAY want to prevent signatures from being spoofed or used multiple times by bad actors and thus require a `nonce` to be added to the `@signature-params`. This is described in [Section 7.2.2](https://rfc-editor.org/rfc/rfc9421#section-7.2.2) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\].[¶](#section-4.2.2-1)

Agents SHOULD extend `@signature-parameters` defined in [Section 4.2](#generating-http-message-signature) as follows:[¶](#section-4.2.2-2)

`nonce`  
base64url encoded random byte array. It is RECOMMENDED to use a 64-byte array.[¶](#section-4.2.2-3.2.1)

Client MUST ensure that this `nonce` is unique for the validity window of the signature, as defined by created and expires attributes.[¶](#section-4.2.2-4)

#### [4.2.3.](#section-4.2.3) [Additional headers](#name-additional-headers)

Agents MAY include additional components, such as specific HTTP headers, in the signature. This can be prompted by the origin requesting additional headers, as described in [Section 4.3](#requesting-message-signature), or initiated by the agent to provide more information within the signature scope. For example, an agent might include an HTTP header expressing its intent and sign it.[¶](#section-4.2.3-1)

Origins MAY ignore certain headers at their own discretion, and request a new signature, as described in [Section 4.3](#requesting-message-signature).[¶](#section-4.2.3-2)

#### [4.2.4.](#section-4.2.4) [Sending a request](#name-sending-a-request)

An Agent SHOULD send a request with the signature generated above. Updating the architecture diagram, the flow looks as follow.[¶](#section-4.2.4-1)

[¶](#section-4.2.4-2.1)

The Agent SHOULD send requests with two headers[¶](#section-4.2.4-3)

1.  `Signature` defined in [Section 4.2](#generating-http-message-signature)[¶](#section-4.2.4-4.1.1)

2.  `Signature-Input` defined in [Section 4.2](#generating-http-message-signature)[¶](#section-4.2.4-4.2.1)

Mentioned in [Section 4.2.1](#signature-agent), the Agent MAY send requests with `Signature-Agent` header.[¶](#section-4.2.4-5)

### [4.3.](#section-4.3) [Requesting a Message signature](#name-requesting-a-message-signat)

[Section 5](https://rfc-editor.org/rfc/rfc9421#section-5) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\] defines the `Accept-Signature` field which can be used to request a Message Signature from a client by an origin. An Origin MAY choose to request signatures from clients that did not initially provide them. If requesting, Origins MUST use the same parameters as those defined by the [Section 4.2](#generating-http-message-signature). The status code SHOULD be 403 Forbidden as defined in [Section 15.5.4](https://rfc-editor.org/rfc/rfc9110#section-15.5.4) of \[[HTTP](#HTTP)\].[¶](#section-4.3-1)

Origin MAY request a new signature with tag "web-bot-auth" even if a nonce is provided, for example if it believes the nonce is a replay, or if it doesn't store nonces and thus requests new signatures every time. The status code SHOULD be 429 Too Many Requests as defined in [Section 4](https://rfc-editor.org/rfc/rfc6585#section-4) of \[[HTTP-MORE-STATUS-CODE](#HTTP-MORE-STATUS-CODE)\].[¶](#section-4.3-2)

### [4.4.](#section-4.4) [Validating Message signature](#name-validating-message-signatur)

Upon receiving an HTTP request, the origin has to verify the signature. The algorithm is provided in [Section 3.2](https://rfc-editor.org/rfc/rfc9421#section-3.2) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. Similar to a regular User-Agent check, this happens at the HTTP layer, once headers are received.[¶](#section-4.4-1)

Additional requirements are placed on this validation:[¶](#section-4.4-2)

- During step 1 to 3 included, if the Origin fails to parse the provided `Signature`, `Signature-Input`, or `Signature-Agent` headers, it MAY respond with status code 400 Bad Request as defined in [Section 15.5.1](https://rfc-editor.org/rfc/rfc9110#section-15.5.1) of \[[HTTP](#HTTP)\].[¶](#section-4.4-3.1.1)

- During step 4, the Origin MAY discard signatures for which the `tag` is not set to `web-bot-auth`.[¶](#section-4.4-3.2.1)

- During step 5, the Origin MAY discard signatures for which they do not know the `keyid`.[¶](#section-4.4-3.3.1)

- During step 5, if the keyid is unknown to the origin, they MAY fetch the provider directory as indicated by `Signature-Agent` header defined in Section 4 of \[[DIRECTORY](#DIRECTORY)\].[¶](#section-4.4-3.4.1)

Origin MAY require the `nonce` to satisfy certain constraint: be globally unique using a global nonce store, be unique to a specific location or time window using a local cache, or not constraint at all.[¶](#section-4.4-4)

### [4.5.](#section-4.5) [Key Distribution and Discovery](#name-key-distribution-and-discov)

This section describes the discovery mechanism for the agent directory.[¶](#section-4.5-1)

The reference for discovery is a FQDN. It SHOULD provide a directory hosted on the well known registered in Section 4 of \[[DIRECTORY](#DIRECTORY)\].[¶](#section-4.5-2)

Example:[¶](#section-4.5-3)

    {
      "keys": {
        "kty": "OKP",
        "crv": "Ed25519",
        "kid": "NFcWBst6DXG-N35nHdzMrioWntdzNZghQSkjHNMMSjw",
        "x": "JrQLj5P_89iXES9-vFgrIy29clF9CC_oPPsw3c5D0bs",
        "use": "sig",
        "nbf": 1712793600,
        "exp": 1715385600
      }
    }

[¶](#section-4.5-4)

#### [4.5.1.](#section-4.5.1) [Out-of-band communication between client and origin](#name-out-of-band-communication-b)

A service submitting their key to an origin, or the origin manually adding a service to their trusted list.[¶](#section-4.5.1-1)

#### [4.5.2.](#section-4.5.2) [Public list](#name-public-list)

Could be a GitHub repository like the public suffix list. The issue is the gating of such repositories, and therefore its governance.[¶](#section-4.5.2-1)

#### [4.5.3.](#section-4.5.3) [Signature-Agent header](#name-signature-agent-header)

This allows for backward compatibility with existing header agent filtering, and an upgrade to a cryptographically secured protocol. See [Section 4.2.1](#signature-agent) for more details.[¶](#section-4.5.3-1)

### [4.6.](#section-4.6) [Session Protocol Considerations](#name-session-protocol-considerat)

Per-request signature generation and verification may incur computational overhead from cryptographic operations and key discovery. For high-frequency interactions, origins might establish sessions to reduce repeated verification.[¶](#section-4.6-1)

One approach: after successful signature verification, an origin issues a session credential (e.g., an HTTP cookie) that subsequent requests present in lieu of a full signature. This trades cryptographic verification costs for the security properties of bearer tokens, including susceptibility to credential theft and replay within the session lifetime.[¶](#section-4.6-2)

The design of session protocols, including appropriate session lifetimes and binding mechanisms, is out of scope for this document.[¶](#section-4.6-3)

## [5.](#section-5) [Security Considerations](#name-security-considerations)

### [5.1.](#section-5.1) [Use of TLS](#name-use-of-tls)

We reassess [Section 7.1.2](https://rfc-editor.org/rfc/rfc9421#section-7.1.2) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. Clients SHOULD use TLS \[[RFC8446](#RFC8446)\] (https) or equivalent transport security when making requests with Message signatures. Failing to do so exposes the Message signature to numerous attacks that could give attackers unintended access.[¶](#section-5.1-1)

This include reverse proxy and their consideration presented in [Section 5.7](#reverse-proxy).[¶](#section-5.1-2)

An origin SHOULD refuse Signature headers when communicated over an unsecured channel.[¶](#section-5.1-3)

### [5.2.](#section-5.2) [Performance Impact](#name-performance-impact)

Origins should account for the overhead of signature verification in their operations. A local cache of public keys reduces network requests and verification latency. The choice of signing algorithm impacts CPU requirements. Origins should monitor verification latency and set appropriate timeouts to maintain service levels under load.[¶](#section-5.2-1)

### [5.3.](#section-5.3) [Nonce validation](#name-nonce-validation)

Clients are the one controlling the nonce. While [Section 4.2.2](#anti-replay) mandates that clients MUST provide a globally unique nonce, it is the origin's responsibility to enforce it.[¶](#section-5.3-1)

Different validation policies have different performance and operational considerations. Global uniqueness requires a global nonce store. Some origins may find that their use case can tolerate sharding on location, timing, or other properties.[¶](#section-5.3-2)

### [5.4.](#section-5.4) [Key Compromise Response](#name-key-compromise-response)

An agent signing key might get compromised.[¶](#section-5.4-1)

If that happens, the agent SHOULD cease using the compromised key as soon as possible, notify affected origins if possible, and generate a new key pair.[¶](#section-5.4-2)

To minimise the impact of a key compromise, the origin should support rapid key rotation and monitor for suspicious signature patterns.[¶](#section-5.4-3)

### [5.5.](#section-5.5) [Shared Secrets Considered Harmful](#name-shared-secrets-considered-h)

Implementations MUST NOT use shared HMAC defined in [Section 3.3.3](https://rfc-editor.org/rfc/rfc9421#section-3.3.3) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. Shared secrets break non-repudiation and make auditing difficult. Each automated client SHOULD use a unique asymmetric keypair to ensure attribution, support key rotation, and enable effective revocation if needed.[¶](#section-5.5-1)

### [5.6.](#section-5.6) [Key Reuse Considered Harmful](#name-key-reuse-considered-harmfu)

Implementations SHOULD NOT reuse a signing key for different purposes. For example, if an agent implementor has two agents they want to differentiate, these should use distinct signing keys and signing key directories.[¶](#section-5.6-1)

### [5.7.](#section-5.7) [Reverse proxy consideration](#name-reverse-proxy-consideration)

An origin may be placed behind a reverse proxy, which means the proxy will see the `Signature` and `Signature-Agent` headers before the origin does. A proxy SHOULD NOT strip the `Signature` or `Signature-Agent` headers from requests.[¶](#section-5.7-1)

A proxy SHOULD NOT replay signatures against other reverse proxies used by the origin, as this allows impersonation of the principal signature agent.[¶](#section-5.7-2)

Origins MAY require a specific nonce policy to prevent such malicious behaviour and decide to validate the signature themselves. This has to be done in accordance with [Section 5.3](#nonce-validation). For example, an origin could require a nonce derived from public information (such as the current date), mandate nonce chaining (where each nonce is the hash of the previous one), or provide its own nonce in an `Accept-Signature` response to challenge the agent.[¶](#section-5.7-3)

Such policies MAY incur additional round-trip between the client and the origin to convey `accept-signature` header, or deployment specific exchanges.[¶](#section-5.7-4)

#### [5.7.1.](#section-5.7.1) [Signature-Agent labeling](#name-signature-agent-labeling)

An intermediary is allowed to relabel an existing signature when processing the message, per [Section 7.2.5](https://rfc-editor.org/rfc/rfc9421#section-7.2.5) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\].[¶](#section-5.7.1-1)

This MAY apply to `Signature-Agent`, when included in the request as defined in [Section 4.2.1](#signature-agent), An intermediary updating the member key MUST update the components of the associated signatures accordingly.[¶](#section-5.7.1-2)

For instance, an intermediary updating the `Signature-Agent` from `sig2` to `sig3` on the example provided in [Appendix A.1.2](#example-signature-agent-included) would result in the following `Signature`, `Signature-Input`, and `Signature-Agent` header.[¶](#section-5.7.1-3)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Agent: sig3="https://signature-agent.test"
    Signature-Input: sig2=("@authority" "signature-agent";key="sig3")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=1735693200\
     ;nonce="XSHtZVCThSIAksXsH9WBs6AtxtXC0eQGiIcUGSoJstFs8lAWakjhrfwzLhyjtme5iXMZvmFWqDEs6cT3Jf+BbQ=="\
     ;tag="web-bot-auth"
    Signature: sig2=:I1QWNzGXdP1a4dSvOHLCVOOanEYHDk+ZsVxM9MLX/p4ko69ghKwR5EOtAD96g7g4GWP7lmpM/jFAf9q8EFRDTPLjUXySwMv4YPgabv2LQihTJG2y8a2m6IGltyruwQNiqSJVUuRaG9+b17CGmAMFZh30X6GXLdQJrCARpeTqPwp2DC+a8haDE/VE5EruqzjA5/2mKwvrkzkSqeW5tOVtFwWRRHIOidquf/8Je6kM9mhgkg4arudLA5SL4wyyYE1jURIgcOl8agrfdJ5Def23DIRtiOLRa8jT9cpTLFAuFHN+mrZA/LH9h0gSIg1cPb+0cMASee5uku1KjWcFer7jWA==:

[¶](#section-5.7.1-4)

`Signature` is unchanged as the base is similar. Both `Signature-Agent` and `Signature-Input` reflect the update from `sig2` to `sig3`. . \# Privacy Considerations[¶](#section-5.7.1-5)

### [5.8.](#section-5.8) [Public Identity](#name-public-identity)

This architecture assumes that automated clients identify themselves explicitly using digital signatures. The identity associated with a signing key is expected to be publicly discoverable for verification purposes. This reduces anonymity and allows receivers to associate requests with specific agents. If an agent wishes not to identify itself, this is not the right choice of protocol for it.[¶](#section-5.8-1)

### [5.9.](#section-5.9) [No Human Correlation](#name-no-human-correlation)

The key used for signing MUST NOT be tied to a specific human individual. Keys SHOULD represent a role, company, or automation identity (e.g., "news-aggregator- bot", "example-crawler-v1"). This avoids accidental exposure of personally identifiable information and prevents the misuse of keys for user tracking or profiling.[¶](#section-5.9-1)

### [5.10.](#section-5.10) [Minimizing Tracking Risks](#name-minimizing-tracking-risks)

To limit tracking risks, implementations SHOULD avoid long-lived, globally unique key identifiers unless strictly necessary. Key rotation SHOULD be supported, and clients SHOULD take care to avoid signing information that could be used to correlate activity across contexts, especially where sensitive user data is involved.[¶](#section-5.10-1)

## [6.](#section-6) [IANA Considerations](#name-iana-considerations)

This document has no IANA actions.[¶](#section-6-1)

## [7.](#section-7) [References](#name-references)

### [7.1.](#section-7.1) [Normative References](#name-normative-references)

\[DIRECTORY\]  
Meunier, T. and S. Major, "HTTP Message Signatures Directory", Work in Progress, Internet-Draft, draft-meunier-http-message-signatures-directory-05, 2 March 2026, \<<https://datatracker.ietf.org/doc/html/draft-meunier-http-message-signatures-directory-05>\>.

\[HTTP\]  
Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "HTTP Semantics", STD 97, RFC 9110, DOI 10.17487/RFC9110, June 2022, \<<https://www.rfc-editor.org/rfc/rfc9110>\>.

\[HTTP-CACHE\]  
Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "HTTP Caching", STD 98, RFC 9111, DOI 10.17487/RFC9111, June 2022, \<<https://www.rfc-editor.org/rfc/rfc9111>\>.

\[HTTP-MESSAGE-SIGNATURES\]  
Backman, A., Ed., Richer, J., Ed., and M. Sporny, "HTTP Message Signatures", RFC 9421, DOI 10.17487/RFC9421, February 2024, \<<https://www.rfc-editor.org/rfc/rfc9421>\>.

\[HTTP-MORE-STATUS-CODE\]  
Nottingham, M. and R. Fielding, "Additional HTTP Status Codes", RFC 6585, DOI 10.17487/RFC6585, April 2012, \<<https://www.rfc-editor.org/rfc/rfc6585>\>.

\[JWK-OKP\]  
Liusvaara, I., "CFRG Elliptic Curve Diffie-Hellman (ECDH) and Signatures in JSON Object Signing and Encryption (JOSE)", RFC 8037, DOI 10.17487/RFC8037, January 2017, \<<https://www.rfc-editor.org/rfc/rfc8037>\>.

\[JWK-THUMBPRINT\]  
Jones, M. and N. Sakimura, "JSON Web Key (JWK) Thumbprint", RFC 7638, DOI 10.17487/RFC7638, September 2015, \<<https://www.rfc-editor.org/rfc/rfc7638>\>.

\[RFC2119\]  
Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, \<<https://www.rfc-editor.org/rfc/rfc2119>\>.

\[RFC8174\]  
Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, \<<https://www.rfc-editor.org/rfc/rfc8174>\>.

### [7.2.](#section-7.2) [Informative References](#name-informative-references)

\[OAUTH-BEARER\]  
Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage", RFC 6750, DOI 10.17487/RFC6750, October 2012, \<<https://www.rfc-editor.org/rfc/rfc6750>\>.

\[RFC8446\]  
Rescorla, E., "The Transport Layer Security (TLS) Protocol Version 1.3", RFC 8446, DOI 10.17487/RFC8446, August 2018, \<<https://www.rfc-editor.org/rfc/rfc8446>\>.

## [Appendix A.](#appendix-A) [Test Vectors](#name-test-vectors)

### [A.1.](#appendix-A.1) [RSASSA-PSS Using SHA-512](#name-rsassa-pss-using-sha-512)

The test vectors in this section use the RSA-PSS key defined in [Appendix B.1.2](https://rfc-editor.org/rfc/rfc9421#appendix-B.1.2) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. This section includes non-normative test vectors that may be used as test cases to validate implementation correctness.[¶](#appendix-A.1-1)

#### [A.1.1.](#appendix-A.1.1) [Signature-Agent absent from the request](#name-signature-agent-absent-from)

This example presents a minimal signature using the rsa-pss-sha512 algorithm over test-request. The request does not contain a `Signature-Agent` header.[¶](#appendix-A.1.1-1)

The corresponding signature base is:[¶](#appendix-A.1.1-2)

    NOTE: '\' line wrapping per RFC 8792

    "@authority": example.com
    "@signature-params": ("@authority")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=4889289600\
     ;nonce="EfK54mBzFxPqwpmZ430GZRqVGrLT/DplPWuFIM1jLJDjrAIX3yFGidftF1h1+zLHfjoNKhx74yU1psH1XD7BeA=="\
     ;tag="web-bot-auth"

[¶](#appendix-A.1.1-3)

This results in the following Signature-Input and Signature header fields being added to the message under the label `sig1`:[¶](#appendix-A.1.1-4)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Input: sig1=("@authority")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=4889289600\
     ;nonce="EfK54mBzFxPqwpmZ430GZRqVGrLT/DplPWuFIM1jLJDjrAIX3yFGidftF1h1+zLHfjoNKhx74yU1psH1XD7BeA=="\
     ;tag="web-bot-auth"
    Signature: sig1=:Bqj+UQfJNSRx0Dz/K/4/+Bo1l8UUH5Ps1zYzX6H6nKCyZJ88Hry/KZF2JishxI1h9+LJTmRmDmw2HxbUeZkoUUgmLbg168GWiYFBK0IQRKQvvbnzrONutKNmanvIXNvrN2ZB2h+w9ekSol3XJRncErrwcU2PWltBR+An4H2kIiRBfnBRi85eCVF+s6SYRxoAJvRo6avTCvCZe9Gvw8Ezbj8QnHU37uvTN72+MBDEsFN94ozfAT8MTB4wAwqXYLMf9mnl0mpK2UbnXrzgffRxOhEHVvHNIN8aB7ThM1p4JzaTN1HuXQFPYOWgCojOCv2IovGOygai/j3p4PzMJUp4Lw==:

[¶](#appendix-A.1.1-5)

#### [A.1.2.](#appendix-A.1.2) [Signature-Agent included present on the request](#name-signature-agent-included-pr)

This example presents a minimal signature using the rsa-pss-sha512 algorithm over test-request. The request contains a `Signature-Agent` header.[¶](#appendix-A.1.2-1)

The corresponding signature base is:[¶](#appendix-A.1.2-2)

    NOTE: '\' line wrapping per RFC 8792

    "@authority": example.com
    "signature-agent";key="agent2": "https://signature-agent.test"
    "@signature-params": ("@authority" "signature-agent";key="agent2")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=4889289600\
     ;nonce="zJwYV5pG8TA9NnaOu9RBShBXtiWuyoWthZXQBT2J77XTpW3ADk49DlbOvpqjJqy3SH3lyNVS/Zo0DmKQX8HYuQ=="\
     ;tag="web-bot-auth"

[¶](#appendix-A.1.2-3)

This results in the following Signature-Input and Signature header fields being added to the message under the label `sig2`:[¶](#appendix-A.1.2-4)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Agent: agent2="https://signature-agent.test"
    Signature-Input: sig2=("@authority" "signature-agent";key="agent2")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=4889289600\
     ;nonce="zJwYV5pG8TA9NnaOu9RBShBXtiWuyoWthZXQBT2J77XTpW3ADk49DlbOvpqjJqy3SH3lyNVS/Zo0DmKQX8HYuQ=="\
     ;tag="web-bot-auth"
    Signature: sig2=:ngb8Yuk2zY/O5nyApob/uwIRWNE1md5xrzYSpPfVCWMHMjdQhj8HTPY8lrE8jHDHRtpqUy7jvYM8LzaHb1NGyxPemVMEOoZpBWXxboqSbp1LTAb2o5qbETmSuDM7UZE4WuSDQoIG5GF5AZ8b8lFEWDP1pw0XV1zsZMn8EPU/DbTkFtGgVPdGehjywJRqnXCXEX0wRCGg4+nTJwWs736JqgbBCuafQPCdwITQucMyGA12QOmMc8eQUdjcS/uqzkDxj1+iI3PDCYnscUTHcGuNv6rWxIx0D+rqWhOoLeYwzDPUm3qs2utVCATIgK0ktLWSfGcPK6p3IwJIUj7cSkbVRg==:

[¶](#appendix-A.1.2-5)

#### [A.1.3.](#appendix-A.1.3) [Legacy Signature-Agent (sf-string instead of sf-dictionary) included present on the request](#name-legacy-signature-agent-sf-s)

THIS IS A LEGACY EXAMPLE. IF YOU ARE AN IMPLEMENTER, PLEASE UPDATE TO THE ABOVE.[¶](#appendix-A.1.3-1)

This example presents a minimal signature using the rsa-pss-sha512 algorithm over test-request. The request contains a `Signature-Agent` header.[¶](#appendix-A.1.3-2)

The corresponding signature base is:[¶](#appendix-A.1.3-3)

    NOTE: '\' line wrapping per RFC 8792

    "@authority": example.com
    "signature-agent": "https://signature-agent.test"
    "@signature-params": ("@authority" "signature-agent")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=1735693200\
     ;nonce="XSHtZVCThSIAksXsH9WBs6AtxtXC0eQGiIcUGSoJstFs8lAWakjhrfwzLhyjtme5iXMZvmFWqDEs6cT3Jf+BbQ=="\
     ;tag="web-bot-auth"

[¶](#appendix-A.1.3-4)

This results in the following Signature-Input and Signature header fields being added to the message under the label `sig2`:[¶](#appendix-A.1.3-5)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Agent: "https://signature-agent.test"
    Signature-Input: sig2=("@authority" "signature-agent")\
     ;created=1735689600\
     ;keyid="oD0HwocPBSfpNy5W3bpJeyFGY_IQ_YpqxSjQ3Yd-CLA"\
     ;alg="rsa-pss-sha512"\
     ;expires=1735693200\
     ;nonce="XSHtZVCThSIAksXsH9WBs6AtxtXC0eQGiIcUGSoJstFs8lAWakjhrfwzLhyjtme5iXMZvmFWqDEs6cT3Jf+BbQ=="\
     ;tag="web-bot-auth"
    Signature: sig2=:I1QWNzGXdP1a4dSvOHLCVOOanEYHDk+ZsVxM9MLX/p4ko69ghKwR5EOtAD96g7g4GWP7lmpM/jFAf9q8EFRDTPLjUXySwMv4YPgabv2LQihTJG2y8a2m6IGltyruwQNiqSJVUuRaG9+b17CGmAMFZh30X6GXLdQJrCARpeTqPwp2DC+a8haDE/VE5EruqzjA5/2mKwvrkzkSqeW5tOVtFwWRRHIOidquf/8Je6kM9mhgkg4arudLA5SL4wyyYE1jURIgcOl8agrfdJ5Def23DIRtiOLRa8jT9cpTLFAuFHN+mrZA/LH9h0gSIg1cPb+0cMASee5uku1KjWcFer7jWA==:

[¶](#appendix-A.1.3-6)

### [A.2.](#appendix-A.2) [EdDSA Using Curve edwards25519](#name-eddsa-using-curve-edwards25)

The test vectors in this section use the Ed25519 key defined in [Appendix B.1.4](https://rfc-editor.org/rfc/rfc9421#appendix-B.1.4) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\]. This section include non-normative test vectors that may be used as test cases to validate implementation correctness.[¶](#appendix-A.2-1)

#### [A.2.1.](#appendix-A.2.1) [Signature-Agent absent from the request](#name-signature-agent-absent-from-)

This example presents a minimal signature using the ed25519 algorithm over test-request. The request does not contain a `Signature-Agent` header.[¶](#appendix-A.2.1-1)

The corresponding signature base is:[¶](#appendix-A.2.1-2)

    NOTE: '\' line wrapping per RFC 8792

    "@authority": example.com
    "@signature-params": ("@authority")\
     ;created=1735689600\
     ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"\
     ;alg="ed25519"\
     ;expires=4889289600\
     ;nonce="g0iqFa9e1ffijlyOScDkXpfSmTbYpRNSGPJrQ1It20ahwgzB3jOUcdgLgFxUg7RMtW4V8IILaKKtA+YuSyIgJQ=="\
     ;tag="web-bot-auth"

[¶](#appendix-A.2.1-3)

This results in the following Signature-Input and Signature header fields being added to the message under the label `sig1`:[¶](#appendix-A.2.1-4)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Input: sig1=("@authority")\
     ;created=1735689600\
     ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"\
     ;alg="ed25519"\
     ;expires=4889289600\
     ;nonce="g0iqFa9e1ffijlyOScDkXpfSmTbYpRNSGPJrQ1It20ahwgzB3jOUcdgLgFxUg7RMtW4V8IILaKKtA+YuSyIgJQ=="\
     ;tag="web-bot-auth"
    Signature: sig1=:FFASViSdcgsyaqqYiCnkHreeZzbNKcTzDvZC5uVlP/dn9IbWj8j0o4wKFTH3rBnUiSUBduwm1Gp5VlIPCp01Ag==:

[¶](#appendix-A.2.1-5)

#### [A.2.2.](#appendix-A.2.2) [Signature-Agent included present on the request](#name-signature-agent-included-pre)

This example presents a minimal signature using the ed25519 algorithm over test-request. The request contains a `Signature-Agent` header.[¶](#appendix-A.2.2-1)

The corresponding signature base is:[¶](#appendix-A.2.2-2)

    NOTE: '\' line wrapping per RFC 8792

    "@authority": example.com
    "signature-agent";key="agent2": "https://signature-agent.test"
    "@signature-params": ("@authority" "signature-agent";key="agent2")\
     ;created=1735689600\
     ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"\
     ;alg="ed25519"\
     ;expires=4889289600\
     ;nonce="XeP72svPKNiGEg3aDE7WJuTpN69H08oMFqC8NLFy1MptpENAT3WZTYwK+MYdsFMlaqHCJGo9ZAhqer1NWY9Epg=="\
     ;tag="web-bot-auth"

[¶](#appendix-A.2.2-3)

This results in the following Signature-Input and Signature header fields being added to the message under the label `sig2`:[¶](#appendix-A.2.2-4)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Agent: agent2="https://signature-agent.test"
    Signature-Input: sig2=("@authority" "signature-agent";key="agent2")\
     ;created=1735689600\
     ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"\
     ;alg="ed25519"\
     ;expires=4889289600\
     ;nonce="XeP72svPKNiGEg3aDE7WJuTpN69H08oMFqC8NLFy1MptpENAT3WZTYwK+MYdsFMlaqHCJGo9ZAhqer1NWY9Epg=="\
     ;tag="web-bot-auth"
    Signature: sig2=:DGiW2ErlQh0hc8wY2FQdbnFd6CEmonyY8nlvECIJFaUSYYNvNvSsGyP99BUGtq51gA4ouXlkUwjnta084bpjCg==:

[¶](#appendix-A.2.2-5)

#### [A.2.3.](#appendix-A.2.3) [Legacy Signature-Agent (sf-string instead of sf-dictionary) included present on the request](#name-legacy-signature-agent-sf-st)

THIS IS A LEGACY EXAMPLE. IF YOU ARE AN IMPLEMENTER, PLEASE UPDATE TO THE ABOVE.[¶](#appendix-A.2.3-1)

This example presents a minimal signature using the ed25519 algorithm over test-request. The request contains a `Signature-Agent` header.[¶](#appendix-A.2.3-2)

The corresponding signature base is:[¶](#appendix-A.2.3-3)

    NOTE: '\' line wrapping per RFC 8792

    "@authority": example.com
    "signature-agent": "https://signature-agent.test"
    "@signature-params": ("@authority" "signature-agent")\
     ;created=1735689600\
     ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"\
     ;alg="ed25519"\
     ;expires=1735693200\
     ;nonce="e8N7S2MFd/qrd6T2R3tdfAuuANngKI7LFtKYI/vowzk4lAZYadIX6wW25MwG7DCT9RUKAJ0qVkU0mEeLElW1qg=="\
     ;tag="web-bot-auth"

[¶](#appendix-A.2.3-4)

This results in the following Signature-Input and Signature header fields being added to the message under the label `sig2`:[¶](#appendix-A.2.3-5)

    NOTE: '\' line wrapping per RFC 8792

    Signature-Agent: "https://signature-agent.test"
    Signature-Input: sig2=("@authority" "signature-agent")\
     ;created=1735689600\
     ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"\
     ;alg="ed25519"\
     ;expires=1735693200\
     ;nonce="e8N7S2MFd/qrd6T2R3tdfAuuANngKI7LFtKYI/vowzk4lAZYadIX6wW25MwG7DCT9RUKAJ0qVkU0mEeLElW1qg=="\
     ;tag="web-bot-auth"
    Signature: sig2=:jdq0SqOwHdyHr9+r5jw3iYZH6aNGKijYp/EstF4RQTQdi5N5YYKrD+mCT1HA1nZDsi6nJKuHxUi/5Syp3rLWBA==:

[¶](#appendix-A.2.3-6)

## [Appendix B.](#appendix-B) [Implementations](#name-implementations)

This draft has a couple of public implementations. A demonstration server has been deployed to <https://http-message-signatures-example.research.cloudflare.com/>.[¶](#appendix-B-1)

It uses ed25519 example signing and verifying keys defined in [Appendix B.1.4](https://rfc-editor.org/rfc/rfc9421#appendix-B.1.4) of \[[HTTP-MESSAGE-SIGNATURES](#HTTP-MESSAGE-SIGNATURES)\].[¶](#appendix-B-2)

### [B.1.](#appendix-B.1) [Clients](#name-clients)

- [Chrome MV3](https://github.com/cloudflare/web-bot-auth) (TypeScript)[¶](#appendix-B.1-1.1.1)

- [Cloudflare Workers](https://github.com/cloudflare/web-bot-auth) (TypeScript)[¶](#appendix-B.1-1.2.1)

- [Puppeteer script](https://github.com/stytchauth/web-bot-auth-example) (JavaScript)[¶](#appendix-B.1-1.3.1)

- [Guzzle middleware](https://github.com/olipayne/guzzle-web-bot-auth-middleware) (PHP)[¶](#appendix-B.1-1.4.1)

- [Python script](https://zenn.dev/oymk/articles/944069e5eddc27) (Python)[¶](#appendix-B.1-1.5.1)

- [Bot-Authentication](https://github.com/cyberstormdotmu/bot-authentication) (Python)[¶](#appendix-B.1-1.6.1)

- [HTPie plugin](https://github.com/cloudflare/web-bot-auth) (Python)[¶](#appendix-B.1-1.7.1)

- [Web scrapers (scrapy/crawl4ai)](https://github.com/cyberstormdotmu/bot-authentication) (Python)[¶](#appendix-B.1-1.8.1)

- [HUMAN Verified AI Agents](https://github.com/HumanSecurity/human-verified-ai-agent) (Python)[¶](#appendix-B.1-1.9.1)

- [Linzer](https://github.com/nomadium/linzer/blob/master/spec/integration/cloudflare_example_research_spec.rb) (Ruby)[¶](#appendix-B.1-1.10.1)

- [Rust binaries](https://github.com/cloudflare/web-bot-auth) (Rust)[¶](#appendix-B.1-1.11.1)

### [B.2.](#appendix-B.2) [Servers](#name-servers)

- [Caddy plugin](https://github.com/cloudflare/web-bot-auth) (Go)[¶](#appendix-B.2-1.1.1)

- [Cloudflare Workers](https://github.com/cloudflare/web-bot-auth) (TypeScript)[¶](#appendix-B.2-1.2.1)

- [Apache module](https://github.com/garyillyes/web-bot-auth-apache) (C)[¶](#appendix-B.2-1.3.1)

### [B.3.](#appendix-B.3) [Test vectors](#name-test-vectors-2)

- In [JSON format](https://github.com/cloudflare/web-bot-auth/blob/main/packages/web-bot-auth/test/test_data/web_bot_auth_architecture_v2.json)[¶](#appendix-B.3-1.1.1)

## [Acknowledgments](#name-acknowledgments)

The editor would also like to thank the following individuals (listed in alphabetical order) for feedback, insight, and implementation of this document - Marwan Fayed, Maxime Guerreiro, Scott Hendrickson, Jonathan Hoyland, Mark Nottingham, Eugenio Panero, Lucas Pardue, Malte Ubl, Loganaden Velvindron, Tanya Verma.[¶](#appendix-C-1)

## [Changelog](#name-changelog)

v04[¶](#appendix-D-1)

- Change Signature-Agent to a sf-dictionary[¶](#appendix-D-2.1.1)

- Add security consideration around intermediary re-keying Signature-Agent[¶](#appendix-D-2.2.1)

- Add `target-uri` as a valid replacement for `@authority`[¶](#appendix-D-2.3.1)

- Add more contributors[¶](#appendix-D-2.4.1)

- Add new implementations of architecture drafts[¶](#appendix-D-2.5.1)

- Remove "purpose" field from web-bot-auth architecture example[¶](#appendix-D-2.6.1)

v03[¶](#appendix-D-3)

- Update linzer example url[¶](#appendix-D-4.1.1)

- Fix section and name of status code 429[¶](#appendix-D-4.2.1)

- Fix typos[¶](#appendix-D-4.3.1)

v02[¶](#appendix-D-5)

- Add response status code[¶](#appendix-D-6.1.1)

- Add a few reference to improve readability[¶](#appendix-D-6.2.1)

- Add consideration to sign additional headers[¶](#appendix-D-6.3.1)

- Add use of TLS in security considerations[¶](#appendix-D-6.4.1)

- Add RSASSA-PSS example[¶](#appendix-D-6.5.1)

- Update acknowledgement section[¶](#appendix-D-6.6.1)

- Reference new implementations: PHP, Python, Ruby, Rust[¶](#appendix-D-6.7.1)

- Fix signature-agent in the arch diagram to use structured fields[¶](#appendix-D-6.8.1)

- Fix test vectors to use signature-agent with structured fields[¶](#appendix-D-6.9.1)

- Fix some typos[¶](#appendix-D-6.10.1)

v01[¶](#appendix-D-7)

- Add mandatory signing of Signature-Agent by clients if present[¶](#appendix-D-8.1.1)

- Add test vectors for request with and without Signature-Agent[¶](#appendix-D-8.2.1)

- Update example diagram to be correct[¶](#appendix-D-8.3.1)

- Add security consideration about reverse proxy[¶](#appendix-D-8.4.1)

- Update why origin may request a new signature[¶](#appendix-D-8.5.1)

- Update nonce validation wording and global uniqueness[¶](#appendix-D-8.6.1)

- Acknowledgements[¶](#appendix-D-8.7.1)

v00[¶](#appendix-D-9)

- Initial draft[¶](#appendix-D-10.1.1)

- How to leverage HTTP Message Signature to sign request[¶](#appendix-D-10.2.1)

- How to verify these Signature[¶](#appendix-D-10.3.1)

- Define web-bot-auth tag to scope this signature[¶](#appendix-D-10.4.1)

- Derive keyid using JWK Thumbprint[¶](#appendix-D-10.5.1)

- High level Security and Privacy considerations[¶](#appendix-D-10.6.1)

## [Authors' Addresses](#name-authors-addresses)

Thibault Meunier

Cloudflare

Email: <ot-ietf@thibault.uk>

Sandor Major

Google

Email: <ietf@sandormajor.com>

[Datatracker](/doc/draft-meunier-web-bot-auth-architecture/)

draft-meunier-web-bot-auth-architecture-05  
Replaced Internet-Draft (individual)

- Info
- Contents
- Prefs

[TABLE]

[Report a datatracker bug ](https://github.com/ietf-tools/datatracker/issues/new/choose)

Show sidebar by default

Yes No

Tab to show by default

Info Contents

HTMLization configuration

HTMLize the plaintext Plaintextify the HTML

Maximum font size Page dependencies

Inline Reference

Citation links

Go to reference section Go to linked document

![](//analytics.ietf.org/matomo.php?idsite=7)
