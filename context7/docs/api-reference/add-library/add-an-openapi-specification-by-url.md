---
title: Add an OpenAPI specification by URL
description: Submit an OpenAPI specification URL for documentation processing.
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/add-library/add-an-openapi-specification-by-url
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Add an OpenAPI specification by URL

> Submit an OpenAPI specification URL for documentation processing.

`POST /v2/add/openapi`

## OpenAPI

````yaml openapi.json post /v2/add/openapi
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
  /v2/add/openapi:
    post:
      summary: Add an OpenAPI specification by URL
      description: Submit an OpenAPI specification URL for documentation processing.
      operationId: addOpenApi
      tags:
        - Add Library
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - openApiUrl
              properties:
                openApiUrl:
                  type: string
                  format: uri
                  description: URL pointing to an OpenAPI specification (JSON or YAML)
            example:
              openApiUrl: https://api.example.com/openapi.json
      responses:
        "200":
          $ref: "#/components/responses/AddLibrarySuccess"
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "429":
          $ref: "#/components/responses/RateLimitError"
        "500":
          $ref: "#/components/responses/InternalServerError"
        "504":
          $ref: "#/components/responses/GatewayTimeoutError"
      security:
        - bearerAuth: []
components:
  schemas:
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
    AddLibraryResponse:
      type: object
      description: Response after successfully submitting a library
      properties:
        libraryName:
          type: string
          description: The library identifier assigned — the URL path of the library on
            context7.com. `/owner/repo` for GitHub repositories, or
            `/<source>/<id>` for other sources (e.g., `/vercel/next.js`,
            `/websites/uploadcare`). See [Library ID
            format](/api-guide#library-id-format).
        message:
          type: string
          description: Human-readable success message
      required:
        - libraryName
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
    InternalServerError:
      description: Internal Server Error
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: internal_error
            message: An error occurred while processing your request
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
    AddLibrarySuccess:
      description: Library submitted successfully for processing
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/AddLibraryResponse"
          example:
            libraryName: /owner/repo
            message: Repository submitted successfully
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
    GatewayTimeoutError:
      description: Gateway Timeout - Processing timed out waiting for logs
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: timeout
            message: Request timed out. Please try again.
````
