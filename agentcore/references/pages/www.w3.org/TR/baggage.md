---
title: 'Propagation format for distributed context: Baggage'
description: '![W3C](https://www.w3.org/)'
product: Amazon Bedrock AgentCore
section: References / www.w3.org
source_url: https://www.w3.org/TR/baggage
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- www-w3-org
referenced_by:
- configuration-bundles-runtime.md
conversion: pandoc
---

[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

# Propagation format for distributed context: Baggage

[W3C Candidate Recommendation Snapshot](https://www.w3.org/standards/types#CR) 30 May 2024

More details about this document

This version:  
[https://www.w3.org/TR/2024/CR-baggage-20240530/](https://www.w3.org/TR/2024/CR-baggage-20240530/)

Latest published version:  
<https://www.w3.org/TR/baggage/>

Latest editor's draft:  
<https://w3c.github.io/baggage/>

History:  
<https://www.w3.org/standards/history/baggage/>

[Commit history](https://github.com/w3c/baggage/commits/master)

Implementation report:  
<https://w3c.github.io/baggage/reports/cr-2024-implementations>

Editors:  
Sergey Kanzhelev ([Google](https://google.com))

Yuri Shkuro (Meta)

Daniel Dyla ([Dynatrace](https://dynatrace.com))

J. Kalyana Sundaram (Microsoft)

Former editors:  
Alois Reitbauer

Morgan McLean

Daniel Khan

Feedback:  
[GitHub w3c/baggage](https://github.com/w3c/baggage/) ([pull requests](https://github.com/w3c/baggage/pulls/), [new issue](https://github.com/w3c/baggage/issues/new/choose), [open issues](https://github.com/w3c/baggage/issues/))

[public-trace-context@w3.org](mailto:public-trace-context@w3.org?subject=baggage) with subject line baggage ([archives](https://lists.w3.org/Archives/Public/public-trace-context))

Discussions  
[We are on Slack.](https://w3cdistributedtracing.slack.com/)

[Copyright](https://www.w3.org/policies/#copyright) © 2024 [World Wide Web Consortium](https://www.w3.org/). W3C^(®) [liability](https://www.w3.org/policies/#Legal_Disclaimer), [trademark](https://www.w3.org/policies/#W3C_Trademarks) and [permissive document license](https://www.w3.org/copyright/software-license-2023/ "W3C Software and Document Notice and License") rules apply.

------------------------------------------------------------------------

## Abstract

This specification defines a standard for representing and propagating a set of application-defined properties associated with a distributed request or workflow execution.

This is independent of the [Trace Context](https://www.w3.org/TR/trace-context/) specification. Baggage can be used regardless of whether Distributed Tracing is used. This specification standardizes representation and propagation of application-defined properties. In contrast, Trace Context specification standardizes representation and propagation of the metadata needed to enable Distributed Tracing scenarios.

The current version of the Baggage specification is targeted for implementations by applications and services, including web applications running within a browser. Web Browsers or User Agents are not currently in scope as a target implementation.

## Status of This Document

*This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at https://www.w3.org/TR/.*

During the Candidate Recommendation stage, the Working Group will audit:

- the [OpenTelemetry implementations of Baggage](https://opentelemetry.io/docs/specs/otel/baggage/api/) to make sure they are following the W3C Baggage spec.
- a sample of [OpenTelemetry's baggage test suites](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#baggage) to verify they are testing the standard.

This document was published by the [Distributed Tracing Working Group](https://www.w3.org/groups/wg/distributed-tracing) as a Candidate Recommendation Snapshot using the [Recommendation track](https://www.w3.org/2023/Process-20231103/#recs-and-notes).

Publication as a Candidate Recommendation does not imply endorsement by W3C and its Members. A Candidate Recommendation Snapshot has received [wide review](https://www.w3.org/2023/Process-20231103/#dfn-wide-review), is intended to gather [implementation experience](https://w3c.github.io/baggage/reports/cr-2024-implementations), and has commitments from Working Group members to [royalty-free licensing](https://www.w3.org/Consortium/Patent-Policy/#sec-Requirements) for implementations.

This Candidate Recommendation is not expected to advance to Proposed Recommendation any earlier than 30 August 2024.

This document was produced by a group operating under the [W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/groups/wg/distributed-tracing/ipr) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains [Essential Claim(s)](https://www.w3.org/Consortium/Patent-Policy/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy/#sec-Disclosure).

This document is governed by the [03 November 2023 W3C Process Document](https://www.w3.org/2023/Process-20231103/).

## 1. Conformance

[](#conformance)

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, and *SHOULD* in this document are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) \[[RFC2119](#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")\] \[[RFC8174](#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")\] when, and only when, they appear in all capitals, as shown here.

## 2. Overview

[](#overview)

The `baggage` header represents a set of user-defined properties associated with a distributed request. Libraries and platforms *SHOULD* propagate this header.

## 3. Baggage HTTP Header Format

[](#baggage-http-header-format)

The `baggage` header is used to propagate user-supplied key-value pairs through a distributed request. A received header *MAY* be altered to change or add information and it *SHOULD* be passed on to all downstream requests.

Multiple `baggage` headers are allowed. Values can be combined in a single header according to [RFC 7230](https://tools.ietf.org/html/rfc7230#page-24).

### 3.1 Header Name

[](#header-name)

Header name: `baggage`

In order to increase interoperability across multiple protocols and encourage successful integration, implementations *SHOULD* keep the header name lowercase.

### 3.2 Header Encoding

[](#header-encoding)

This header is a \[[UTF-8](#bib-utf-8 "UTF-8, a transformation format of ISO 10646")\] encoded \[[UNICODE](#bib-unicode "The Unicode Standard")\] string, however it uses only code points from the Basic Latin Unicode Block which are encoded identically in both Unicode and \[[ASCII](#bib-ascii "ISO/IEC 646:1991, Information technology -- ISO 7-bit coded character set for information interchange")\].

### 3.3 Header Content

[](#header-content)

This section uses the Augmented Backus-Naur Form (ABNF) notation of \[[RFC5234](#bib-rfc5234 "Augmented BNF for Syntax Specifications: ABNF")\].

#### 3.3.1 Definition

[](#definition)

``` ABNF
baggage-string         =  list-member 0*179( OWS "," OWS list-member )
list-member            =  key OWS "=" OWS value *( OWS ";" OWS property )
property               =  key OWS "=" OWS value
property               =/ key OWS
key                    =  token ; as defined in RFC 7230, Section 3.2.6
value                  =  *baggage-octet
baggage-octet          =  %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E
                          ; US-ASCII characters excluding CTLs,
                          ; whitespace, DQUOTE, comma, semicolon,
                          ; and backslash
OWS                    =  *( SP / HTAB ) ; optional white space, as defined in RFC 7230, Section 3.2.3
```

`token` is defined in \[[RFC7230](#bib-rfc7230 "Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing")\], Section 3.2.6: <https://tools.ietf.org/html/rfc7230#section-3.2.6>

The definition of `OWS` is taken from \[[RFC7230](#bib-rfc7230 "Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing")\], Section 3.2.3: <https://tools.ietf.org/html/rfc7230#section-3.2.3>

##### 3.3.1.1 baggage-string

[](#baggage-string)

List of `list-member`s with optional properties attached. Uniqueness of keys between multiple `list-member`s in a `baggage-string` is not guaranteed. The order of duplicate entries *SHOULD* be preserved when mutating the list. Producers *SHOULD* try to produce a `baggage-string` without any `list-member`s which duplicate the `key` of another list member.

##### 3.3.1.2 key

[](#key)

A `token` which identifies a `value` in the `baggage`. `token` is defined in [RFC7230, Section 3.2.6](https://tools.ietf.org/html/rfc7230#section-3.2.6). Leading and trailing whitespaces (`OWS`) are allowed and are not considered to be a part of the key.

Note

Though the baggage header is a \[[UTF-8](#bib-utf-8 "UTF-8, a transformation format of ISO 10646")\] encoded \[[UNICODE](#bib-unicode "The Unicode Standard")\] string, `key` is limited to the [ASCII code points](https://infra.spec.whatwg.org/#ascii-code-point) allowed by the definition of token in \[[RFC7230](#bib-rfc7230 "Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing")\]. This is due to the implementation details of stable implementations prior to the writing of this specification.

##### 3.3.1.3 value

[](#value)

A string which contains a value identified by the `key`. Any code points outside of the `baggage-octet` range *MUST* be percent-encoded. The percent code point (`U+0025`) *MUST* be percent-encoded. Code points which are not required to be percent-encoded *MAY* be percent-encoded. Percent-encoding is defined in \[[RFC3986](#bib-rfc3986 "Uniform Resource Identifier (URI): Generic Syntax")\], Section 2.1: <https://datatracker.ietf.org/doc/html/rfc3986#section-2.1>.

When decoding the value, percent-encoded octet sequences that do not match the UTF-8 encoding scheme *MUST* be replaced with the replacement code point (`U+FFFD`).

Leading and trailing whitespaces (`OWS`) are allowed and are not considered to be a part of the value.

Note, `value` *MAY* contain any number of the equal sign (`U+003D`) code points. Parsers *MUST NOT* assume that the equal sign is only used to separate `key` and `value`.

Note

Though the baggage header is a \[[UTF-8](#bib-utf-8 "UTF-8, a transformation format of ISO 10646")\] encoded \[[UNICODE](#bib-unicode "The Unicode Standard")\] string, `value` is limited to the [ASCII code points](https://infra.spec.whatwg.org/#ascii-code-point) of `baggage-octet`. This is due to the implementation details of stable implementations prior to the writing of this specification.

##### 3.3.1.4 property

[](#property)

Additional metadata *MAY* be appended to values in the form of property set, represented as semi-colon `;` delimited list of keys and/or key-value pairs, e.g. `;k1=v1;k2;k3=v3`. Property keys and values are given no specific meaning by this specification. Leading and trailing `OWS` is allowed and is not considered to be a part of the property key or value.

#### 3.3.2 Limits

[](#limits)

A platform *MUST* propagate all `list-member`s including any `list-member`s added by the platform whenever both of these conditions are met:

- **Condition 1:** The resulting `baggage-string` contains 64 `list-member`s or less.
- **Condition 2:** The resulting `baggage-string` is of size 8192 bytes or less.

If either of the above conditions is not met, a platform *MAY* drop `list-member`s until both conditions are met. The selection of which `list-member`s to drop and their order is unspecified and left to the implementer. Note that the above limits are *minimum* requirements to comply with the specification. An implementor or platform *MAY* define higher limits and *SHOULD* propagate as much baggage information as is reasonable within their requirements. If a platform cannot propagate all baggage, it *MUST NOT* propagate any partial `list-member`s. If there are multiple `baggage` headers, all limits apply to the combination of all `baggage` headers and not each header individually.

#### 3.3.3 Example

[](#example)

The following example header contains 3 `list-member`s. The `baggage-string` contained in the header contains 86 bytes. 82 bytes come from the `list-member`s and 4 bytes come from commas and optional whitespace.

``` hljs
baggage: key1=value1;property1;property2, key2 = value2, key3=value3; propertyKey=propertyValue
```

- `key1=value1;property1;property2`
  - 31 bytes
- `key2 = value2`
  - 13 bytes
- `key3=value3; propertyKey=propertyValue`
  - 38 bytes

### 3.4 Examples of HTTP headers

[](#examples-of-http-headers)

Assume we want to propagate these entries: `userId="alice"`, `serverNode="DF 28"`, `isProduction=false`,

Single header:

``` hljs
baggage: userId=alice,serverNode=DF%2028,isProduction=false
```

Here is one more example where values with characters outside of the `baggage-octet` range are percent-encoded. Consider the entry: `userId="Amélie"`, `serverNode="DF 28"`, `isProduction=false`:

``` hljs
baggage: userId=Am%C3%A9lie,serverNode=DF%2028,isProduction=false
```

Context might be split into multiple headers:

``` hljs
baggage: userId=alice
baggage: serverNode=DF%2028,isProduction=false
```

Values and names might begin and end with spaces:

``` hljs
baggage: userId =   alice
baggage: serverNode = DF%2028, isProduction = false
```

#### 3.4.1 Example use case

[](#example-use-case)

For example, if all of your data needs to be sent to a single node, you could propagate a property indicating that.

``` hljs
baggage: serverNode=DF%2028
```

For example, if you need to annotate logs with some request-specific information, you could propagate a property using the baggage header.

``` hljs
baggage: userId=alice
```

For example, if you have non-production requests that flow through the same services as production requests.

``` hljs
baggage: isProduction=false
```

### 3.5 Mutating baggage

[](#mutating-baggage)

A system receiving a `baggage` request header *SHOULD* send it to outgoing requests. A system *MAY* mutate the value of this header before passing it on.

Because baggage entry keys, values, and metadata are not specified here, producers and consumers *MAY* agree on any set of mutation rules that don't violate the specification. For example, keys may be deduplicated by keeping the first entry, keeping the last entry, or concatenating values together.

The following mutations are allowed:

- **Add a new key/value pair.** A key/value pair *MAY* be added.
- **Update an existing value.** The value for any given key *MAY* be updated.
- **Delete a key/value pair.** Any key/value pair *MAY* be deleted.
- **Deduplicating the list.** Duplicate keys *MAY* be removed.

If a system receiving or updating a `baggage` request header determines that the number of baggage entries exceeds the limit defined in the limits section above, it *MAY* drop or truncate certain baggage entries in any order chosen by the implementation.

If a system determines that the value of a baggage entry is not in the format defined in this specification, it *MAY* remove that entry before propagating the baggage header as part of outgoing requests.

## 4. Security Considerations

[](#security-considerations)

Systems relying on the `baggage` headers should also follow all best practices for parsing potentially malicious data, including checking for header length and content of header values. These practices help to avoid buffer overflow, HTML injection, and other types of attacks.

### 4.1 Information Exposure

[](#information-exposure)

As mentioned in the privacy section, `baggage` may carry sensitive information. Application owners should either ensure that no proprietary or confidential information is stored in `baggage`, or they should ensure that `baggage` isn't present in requests that cross trust-boundaries.

### 4.2 Other Risks

[](#other-risks)

Application owners need to make sure to test all code paths leading to the sending of the `baggage` header. For example, in web applications written in JavaScript, it is typical to make cross-origin requests. If one of these code paths leads to `baggage` headers being sent by cross-origin calls that are restricted using [`Access-Control-Allow-Headers`](https://fetch.spec.whatwg.org/#http-access-control-request-headers) \[[FETCH](#bib-fetch "Fetch Standard")\], it may fail.

## 5. Privacy Considerations

[](#privacy-considerations)

Requirements to propagate headers to downstream services, as well as storing values of these headers, open up potential privacy concerns. Using proprietary ways of context propagation, vendors and application developers could always encode information that contains user identifiable data. This standard makes it possible for systems to operate on a known, standardized header to restrict propagation of sensitive data in the baggage when crossing trust boundaries.

Systems *MUST* assess the risk of header abuse. This section provides some considerations and initial assessment of the risk associated with storing and propagating this header. Systems may choose to inspect and remove sensitive information from the fields before processing or propagating the received data. All mutations should, however, conform to the list of mutations defined in this specification.

### 5.1 Privacy of the baggage header

[](#privacy-of-the-baggage-header)

The main purpose of this header is to provide additional system-specific information to other systems within the same trust-boundary. The `baggage` header may contain any value in any of the keys. As such, the `baggage` header can contain user-identifiable data, however no key or its value or properties is given semantic meaning by this specification. Applications using baggage should be aware that the keys and values can be propagated to other systems. Hence, they should remove any private information that they don't want to be propagated to other systems.

## A. Acknowledgments

[](#acknowledgments)

Thanks to Armin Ruech, Jonathan Mace, Philippe Le Hegaret, Bastian Krol, and Reiley Yang for their contributions to this work.

## B. References

[](#references)

### B.1 Normative references

[](#normative-references)

\[ASCII\]  
[ISO/IEC 646:1991, Information technology -- ISO 7-bit coded character set for information interchange](https://www.ecma-international.org/publications-and-standards/standards/ecma-6/). Ecma International. URL: <https://www.ecma-international.org/publications-and-standards/standards/ecma-6/>

\[FETCH\]  
[Fetch Standard](https://fetch.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: <https://fetch.spec.whatwg.org/>

\[RFC2119\]  
[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

\[RFC3986\]  
[Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc3986>

\[RFC5234\]  
[Augmented BNF for Syntax Specifications: ABNF](https://www.rfc-editor.org/rfc/rfc5234). D. Crocker, Ed.; P. Overell. IETF. January 2008. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc5234>

\[RFC7230\]  
[Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing](https://httpwg.org/specs/rfc7230.html). R. Fielding, Ed.; J. Reschke, Ed.. IETF. June 2014. Proposed Standard. URL: <https://httpwg.org/specs/rfc7230.html>

\[RFC8174\]  
[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

\[UNICODE\]  
[The Unicode Standard](https://www.unicode.org/versions/latest/). Unicode Consortium. URL: <https://www.unicode.org/versions/latest/>

\[UTF-8\]  
[UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/rfc/rfc3629). F. Yergeau. IETF. November 2003. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc3629>

### B.2 Informative references

[](#informative-references)

\[infra\]  
[Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[↑](#title)
