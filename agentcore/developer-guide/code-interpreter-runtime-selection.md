---
title: Runtime selection
description: For a language, you can optionally specify a particular runtime. The following table shows the supported languages and their available runtimes.
product: Amazon Bedrock AgentCore
section: Developer Guide / code
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-runtime-selection.html
fetched: '2026-09-26'
tags:
- agentcore
- code
---

# Runtime selection
<a name="code-interpreter-runtime-selection"></a>

For a language, you can optionally specify a particular runtime. The following table shows the supported languages and their available runtimes.


| Language | Available runtimes | 
| --- | --- | 
| Python |  `python`  | 
| JavaScript |  `nodejs` , `deno`  | 
| TypeScript |  `nodejs` , `deno`  | 

**Note**  
For the `nodejs` runtime, we support CommonJS (CJS) modules for JavaScript and ECMAScript (ESM) modules for TypeScript.