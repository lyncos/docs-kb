---
title: Search for libraries
description: Search for libraries by name with intelligent LLM-powered ranking based on your query context.
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/search/search-for-libraries
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Search for libraries

> Search for libraries by name with intelligent LLM-powered ranking based on your query context.

`GET /v2/libs/search`

## OpenAPI

````yaml openapi.json get /v2/libs/search
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
  /v2/libs/search:
    get:
      summary: Search for libraries
      description: Search for libraries by name with intelligent LLM-powered ranking
        based on your query context.
      operationId: searchLibraries
      tags:
        - Search
      parameters:
        - $ref: "#/components/parameters/LibraryNameParam"
        - $ref: "#/components/parameters/QueryParam"
        - $ref: "#/components/parameters/FastParam"
      responses:
        "200":
          description: Search results ranked by relevance
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/SearchResponse"
              example:
                results:
                  - id: /facebook/react
                    title: React
                    description: A JavaScript library for building user interfaces
                    branch: main
                    lastUpdateDate: 2025-01-15T10:30:00.000Z
                    state: finalized
                    totalTokens: 500000
                    totalSnippets: 2500
                    stars: 220000
                    trustScore: 10
                    benchmarkScore: 95.5
                    versions:
                      - v18.2.0
                      - v17.0.2
                searchFilterApplied: false
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "402":
          $ref: "#/components/responses/SpendingLimitError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "429":
          $ref: "#/components/responses/RateLimitError"
        "500":
          $ref: "#/components/responses/InternalServerError"
        "503":
          $ref: "#/components/responses/ServiceUnavailableError"
      security:
        - {}
        - bearerAuth: []
components:
  parameters:
    LibraryNameParam:
      name: libraryName
      in: query
      description: Library name to search for (e.g., 'react', 'nextjs', 'express')
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 500
      example: react
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
    FastParam:
      name: fast
      in: query
      description: When `true`, skip LLM reranking and return top vector-search
        results directly. Trades relevance quality for lower latency.
      required: false
      schema:
        type: string
        enum:
          - "true"
          - "false"
        default: "false"
      example: "true"
  schemas:
    Library:
      type: object
      description: Library metadata
      properties:
        id:
          type: string
          description: Library ID — the URL path of the library on context7.com.
            `/owner/repo` for GitHub repositories, or `/<source>/<id>` for other
            sources (e.g., `/vercel/next.js`, `/websites/uploadcare`). See
            [Library ID format](/api-guide#library-id-format).
          example: /vercel/next.js
        title:
          type: string
          description: Display name of the library
          example: Next.js
        description:
          type: string
          description: Short description
          example: The React Framework
        branch:
          type: string
          description: Git branch being tracked
          example: canary
        lastUpdateDate:
          type: string
          format: date-time
          description: ISO 8601 timestamp of last update
          example: 2025-01-15T10:30:00.000Z
        state:
          type: string
          enum:
            - finalized
            - initial
            - processing
            - error
            - delete
          description: Processing state of the library
          example: finalized
        totalTokens:
          type: integer
          description: Total tokens in documentation
          example: 607822
        totalSnippets:
          type: integer
          description: Number of code snippets
          example: 3629
        stars:
          type: integer
          description: GitHub stars count
          example: 131745
        trustScore:
          type: integer
          description: Source reputation score (0-10)
          minimum: 0
          maximum: 10
          example: 10
        benchmarkScore:
          type: number
          description: Quality indicator score (0-100)
          minimum: 0
          maximum: 100
          example: 95.5
        versions:
          type: array
          description: Available version tags
          items:
            type: string
          example:
            - v15.1.8
            - v14.3.0
    SearchResponse:
      type: object
      description: Search results response
      properties:
        results:
          type: array
          description: Array of matching libraries ranked by relevance
          items:
            $ref: "#/components/schemas/Library"
        searchFilterApplied:
          type: boolean
          description: Indicates whether the search results were filtered by the
            teamspace's public library access settings. When true, some
            libraries may be excluded from results based on the teamspace's
            configuration (e.g., only verified libraries, selected libraries, or
            private repos only).
      required:
        - results
        - searchFilterApplied
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
    NotFoundError:
      description: Not Found - Resource doesn't exist
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          examples:
            libraryNotFound:
              summary: Library not found
              value:
                error: library_not_found
                message: Library "/owner/repo" not found. Please check the library ID or your
                  access permissions.
            tagNotFound:
              summary: Version tag not found
              value:
                error: tag_not_found
                message: 'Tag "v1.0.0" not found for library "/owner/repo". Available tags:
                  v2.0.0, v1.5.0'
            noSnippetsFound:
              summary: No snippets found
              value:
                error: no_snippets_found
                message: Could not fetch documentation snippets from the library.
            teamNotFound:
              summary: Team not found
              value:
                error: team_not_found
                message: Team not found or access denied
            userNotFound:
              summary: User not found
              value:
                error: user_not_found
                message: User not found
            noLibrariesFound:
              summary: No libraries matched search query
              value:
                error: no_libraries_found
                message: No libraries found for "nonexistent-lib". Try a different search term.
    InternalServerError:
      description: Internal Server Error
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: internal_error
            message: An error occurred while processing your request
    ServiceUnavailableError:
      description: Service Unavailable - Search service is temporarily unavailable
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: search_failed
            message: "Search failed: Service temporarily unavailable"
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
