---
title: Get documentation context
description: Retrieve intelligent, LLM-reranked documentation context for natural language queries. Returns the most relevant code snippets and documentation for your specific question.
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/context/get-documentation-context
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Get documentation context

> Retrieve intelligent, LLM-reranked documentation context for natural language queries. Returns the most relevant code snippets and documentation for your specific question.

`GET /v2/context`

## OpenAPI

````yaml openapi.json get /v2/context
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
  /v2/context:
    get:
      summary: Get documentation context
      description: Retrieve intelligent, LLM-reranked documentation context for
        natural language queries. Returns the most relevant code snippets and
        documentation for your specific question.
      operationId: getContext
      tags:
        - Context
      parameters:
        - $ref: "#/components/parameters/LibraryIdParam"
        - $ref: "#/components/parameters/QueryParam"
        - $ref: "#/components/parameters/TypeParam"
        - $ref: "#/components/parameters/FastParam"
      responses:
        "200":
          description: Documentation context
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ContextResponse"
              example:
                codeSnippets:
                  - codeTitle: Middleware Authentication Example
                    codeDescription: Shows how to implement authentication checks in Next.js
                      middleware
                    codeLanguage: typescript
                    codeTokens: 150
                    codeId: https://github.com/vercel/next.js/blob/canary/docs/middleware.mdx#_snippet_0
                    pageTitle: Middleware
                    codeList:
                      - language: typescript
                        code: >-
                          import { NextResponse } from 'next/server'

                          import type { NextRequest } from 'next/server'


                          export function middleware(request: NextRequest) {
                            const token = request.cookies.get('token')
                            if (!token) {
                              return NextResponse.redirect(new URL('/login', request.url))
                            }
                            return NextResponse.next()
                          }
                infoSnippets:
                  - pageId: https://github.com/vercel/next.js/blob/canary/docs/middleware.mdx
                    breadcrumb: Routing > Middleware
                    content: Middleware allows you to run code before a request is completed...
                    contentTokens: 200
            text/plain:
              schema:
                type: string
              example: |-
                ### Middleware Authentication Example

                Source: https://github.com/vercel/next.js/blob/canary/docs/middleware.mdx

                Shows how to implement authentication checks in Next.js middleware

                ```typescript
                import { NextResponse } from 'next/server'
                ...
                ```
        "202":
          $ref: "#/components/responses/AcceptedError"
        "301":
          $ref: "#/components/responses/RedirectError"
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "402":
          $ref: "#/components/responses/SpendingLimitError"
        "403":
          $ref: "#/components/responses/ForbiddenError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "422":
          $ref: "#/components/responses/UnprocessableEntityError"
        "429":
          $ref: "#/components/responses/RateLimitError"
        "500":
          $ref: "#/components/responses/InternalServerError"
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
    LibraryIdParam:
      name: libraryId
      in: query
      description: Context7-compatible library ID — the URL path of the library on
        context7.com. Use `/owner/repo` for GitHub repositories, or
        `/<source>/<id>` for other sources (websites, llms.txt,
        GitLab/Bitbucket, etc.). Optionally suffix with `/<version>` or
        `@<version>` to pin a specific version. See [Library ID
        format](/api-guide#library-id-format).
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 500
        pattern: ^/[^/]+/[^/]+([/@][^/]+)?$
      examples:
        github:
          summary: GitHub repository
          value: /vercel/next.js
        website:
          summary: Website source
          value: /websites/uploadcare
        llmstxt:
          summary: llms.txt source
          value: /llmstxt/example
        withVersion:
          summary: With specific version (slash)
          value: /vercel/next.js/v14.3.0
        withVersionAt:
          summary: With specific version (@ syntax)
          value: /vercel/next.js@v14.3.0
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
    RedirectErrorResponse:
      allOf:
        - $ref: "#/components/schemas/Error"
        - type: object
          properties:
            redirectUrl:
              type: string
              description: New location of the library
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
    ForbiddenError:
      description: Forbidden - Insufficient permissions or plan restrictions
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          examples:
            accessDenied:
              summary: Library not in allowed list
              value:
                error: access_denied
                message: "Access denied: Library /owner/repo is not included in your allowed
                  libraries"
            insufficientRole:
              summary: Insufficient team role
              value:
                error: forbidden
                message: Only team owners and admins can add private repositories
            planRequired:
              summary: Plan upgrade required
              value:
                error: forbidden
                message: Private repositories require a pro plan or team. Upgrade at
                  https://context7.com/plans
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
    AcceptedError:
      description: Accepted - Library not yet finalized
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: library_not_finalized
            message: Library /owner/repo not finalized yet.
    RedirectError:
      description: Moved Permanently - Library has been redirected
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/RedirectErrorResponse"
          example:
            error: library_redirected
            message: "Library /owner/repo has been redirected to this library:
              /new-owner/new-repo."
            redirectUrl: /new-owner/new-repo
    UnprocessableEntityError:
      description: Unprocessable Entity - Library is too large or has no code
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          examples:
            tooLarge:
              summary: Library too large
              value:
                error: library_too_large
                message: Library /owner/repo is too large to process.
            noCode:
              summary: No code found
              value:
                error: no_code_found
                message: Library /owner/repo has no or too few snippets found in documentation
                  files.
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
