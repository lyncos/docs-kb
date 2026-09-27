---
title: Search Context7 documentation
description: Search Context7 with a natural language query. Context7 finds the most relevant libraries, searches their documentation, and returns the best matching code and documentation snippets. Optionally provide libraries, a version, or a programming language to narrow the results.
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/search/search-context7-documentation
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Search Context7 documentation

> Search Context7 with a natural language query. Context7 finds the most relevant libraries, searches their documentation, and returns the best matching code and documentation snippets. Optionally provide libraries, a version, or a programming language to narrow the results.

`GET /v3/search`

## OpenAPI

````yaml openapi.json get /v3/search
openapi: 3.0.0
info:
  title: Context7 Public API
  description: The Context7 Public API provides programmatic access to library
    documentation and search functionality. Get up-to-date documentation and
    code examples for any library.
  version: 2.0.0
  contact:
    name: Context7 Support
    url: https://context7.com
    email: support@context7.com
servers:
  - url: https://context7.com/api
    description: Production server
tags:
  - name: Search
    description: Search for libraries in the Context7 database
  - name: Context
    description: Retrieve documentation context for queries
  - name: Refresh
    description: Refresh existing libraries to fetch latest documentation
  - name: Policies
    description: Manage teamspace access policies and filters
  - name: Add Library
    description: Submit new libraries for documentation processing
  - name: Metrics
    description: Retrieve usage metrics for libraries
paths:
  /v3/search:
    get:
      summary: Search Context7 documentation
      description: Search Context7 with a natural language query. Context7 finds the
        most relevant libraries, searches their documentation, and returns the
        best matching code and documentation snippets. Optionally provide
        libraries, a version, or a programming language to narrow the results.
      operationId: searchDocumentation
      tags:
        - Search
      parameters:
        - $ref: "#/components/parameters/QueryParam"
        - $ref: "#/components/parameters/TypeParam"
        - name: library
          in: query
          description: Optional library hints. Repeat for up to four values; each may be a
            fuzzy product name such as `next.js` or an exact Context7 ID such as
            `/vercel/next.js`.
          required: false
          style: form
          explode: true
          schema:
            type: array
            maxItems: 4
            items:
              type: string
              minLength: 1
              maxLength: 120
          example:
            - next.js
            - react
        - name: version
          in: query
          description: Optional version constraint. Requires at least one library value.
            It is strict when one library is provided and contextual when
            multiple libraries are provided.
          required: false
          schema:
            type: string
            pattern: ^v?[0-9]+([._][0-9]+){0,2}([-+][a-zA-Z0-9.-]+)?$
          example: "15.2"
        - name: language
          in: query
          description: Optional programming-language preference used for library
            selection, retrieval, and reranking. This is a soft preference and
            does not exclude language-neutral documentation.
          required: false
          schema:
            type: string
            minLength: 1
            maxLength: 40
          example: TypeScript
      responses:
        "200":
          description: Bounded documentation evidence from the selected libraries
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                $ref: "#/components/schemas/SearchContextResponse"
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "402":
          $ref: "#/components/responses/SpendingLimitError"
        "404":
          description: No documentation matched the question or library hints
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: no_documentation_found
                message: No documentation library matched the request. Check the library hint or
                  name.
        "429":
          $ref: "#/components/responses/RateLimitError"
        "503":
          description: Documentation search could not be completed
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: search_failed
                message: The documentation search could not be completed.
      security:
        - {}
        - bearerAuth: []
components:
  parameters:
    QueryParam:
      name: query
      in: query
      description: User's original question or task - used for intelligent relevance ranking
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 500
      example: How to manage state with hooks
    TypeParam:
      name: type
      in: query
      description: Response format type
      required: false
      schema:
        type: string
        enum:
          - json
          - txt
        default: txt
      example: json
  schemas:
    CodeSnippet:
      type: object
      description: A code snippet from library documentation
      properties:
        codeTitle:
          type: string
          description: Title of the code snippet
        codeDescription:
          type: string
          description: Description of what the code does
        codeLanguage:
          type: string
          description: Primary programming language
        codeTokens:
          type: integer
          description: Token count for the snippet
        codeId:
          type: string
          description: URL to source location
        pageTitle:
          type: string
          description: Title of the documentation page
        codeList:
          type: array
          description: Code examples in different languages
          items:
            $ref: "#/components/schemas/CodeExample"
        isDynamic:
          type: boolean
          description: Whether this snippet was recovered from the dynamic source-code
            index instead of the primary docs index
        sourceFile:
          type: string
          description: Repo-relative source file path for dynamic snippets
      required:
        - codeTitle
        - codeDescription
        - codeLanguage
        - codeTokens
        - codeId
        - pageTitle
        - codeList
    CodeExample:
      type: object
      description: A single code example
      properties:
        language:
          type: string
          description: Programming language
        code:
          type: string
          description: The actual code content
      required:
        - language
        - code
    InfoSnippet:
      type: object
      description: A documentation snippet
      properties:
        pageId:
          type: string
          description: URL to source page
        breadcrumb:
          type: string
          description: Navigation breadcrumb path
        content:
          type: string
          description: The documentation content
        contentTokens:
          type: integer
          description: Token count for the content
      required:
        - content
        - contentTokens
    ContextResponse:
      type: object
      description: Documentation context response
      properties:
        codeSnippets:
          type: array
          description: Relevant code snippets
          items:
            $ref: "#/components/schemas/CodeSnippet"
        infoSnippets:
          type: array
          description: Relevant documentation snippets
          items:
            $ref: "#/components/schemas/InfoSnippet"
        rules:
          type: object
          description: Optional library-specific rules and guidelines
          properties:
            global:
              type: array
              description: Global team rules
              items:
                type: string
            libraryOwn:
              type: array
              description: Rules defined by the library owner
              items:
                type: string
            libraryTeam:
              type: array
              description: Library-specific rules from the team
              items:
                type: string
      required:
        - codeSnippets
        - infoSnippets
    SearchCodeSnippet:
      allOf:
        - $ref: "#/components/schemas/CodeSnippet"
        - type: object
          properties:
            libraryId:
              type: string
              description: Context7 library ID that produced this snippet
          required:
            - libraryId
    SearchInfoSnippet:
      allOf:
        - $ref: "#/components/schemas/InfoSnippet"
        - type: object
          properties:
            libraryId:
              type: string
              description: Context7 library ID that produced this snippet
          required:
            - libraryId
    SearchContextResponse:
      allOf:
        - $ref: "#/components/schemas/ContextResponse"
        - type: object
          properties:
            codeSnippets:
              type: array
              description: Relevant code snippets with their selected library
              items:
                $ref: "#/components/schemas/SearchCodeSnippet"
            infoSnippets:
              type: array
              description: Relevant documentation snippets with their selected library
              items:
                $ref: "#/components/schemas/SearchInfoSnippet"
            rules:
              type: object
              description: Optional global rules and library-scoped guidelines
              properties:
                global:
                  type: array
                  description: Global team rules that apply to every returned library
                  items:
                    type: string
                libraries:
                  type: array
                  description: Rules scoped to a specific returned library
                  items:
                    type: object
                    properties:
                      libraryId:
                        type: string
                      libraryOwn:
                        type: array
                        items:
                          type: string
                      libraryTeam:
                        type: array
                        items:
                          type: string
                    required:
                      - libraryId
                      - libraryOwn
                      - libraryTeam
    Error:
      type: object
      description: Standard error response
      properties:
        error:
          type: string
          description: Error code identifier
        message:
          type: string
          description: Human-readable error message
      required:
        - error
        - message
  responses:
    BadRequestError:
      description: Bad Request - Invalid input parameters
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          examples:
            validationError:
              summary: Validation error
              value:
                error: validation_error
                message: Library name is required
            invalidLibraryId:
              summary: Invalid library ID format
              value:
                error: invalid_library_id
                message: "Invalid library ID format. Expected: `/owner/repo` for GitHub
                  repositories, or `/<source>/<id>` for other sources (the URL
                  path of the library on context7.com)"
    UnauthorizedError:
      description: Unauthorized - Invalid or missing API key
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: invalid_api_key
            message: Invalid API key. Please check your API key. API keys should start with
              'ctx7sk' prefix.
    SpendingLimitError:
      description: Payment Required - the teamspace's configured monthly spending
        limit has been reached. A teamspace owner or admin can raise the limit
        in billing settings, or the cap will reset at the start of the next
        billing month.
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: spending_limit_exceeded
            message: Monthly spending limit of $5.00 reached for this teamspace. An owner or
              admin can raise the limit at
              https://context7.com/dashboard/billing, or the cap will reset at
              the start of next month.
    RateLimitError:
      description: Too Many Requests - Rate limit exceeded
      headers:
        Retry-After:
          description: Seconds until rate limit resets
          schema:
            type: integer
        RateLimit-Limit:
          description: Request limit
          schema:
            type: integer
        RateLimit-Remaining:
          description: Remaining requests
          schema:
            type: integer
        RateLimit-Reset:
          description: Unix timestamp when limit resets
          schema:
            type: integer
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: rate_limit_exceeded
            message: Rate limit exceeded. Please try again later.
````
