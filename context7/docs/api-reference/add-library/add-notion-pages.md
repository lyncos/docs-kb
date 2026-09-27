---
title: Add Notion pages
description: Submit selected Notion pages for documentation processing. Requires a connected Notion account and a team project.
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/add-library/add-notion-pages
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Add Notion pages

> Submit selected Notion pages for documentation processing. Requires a connected Notion account and a team project.

`POST /v2/add/notion`

## OpenAPI

````yaml openapi.json post /v2/add/notion
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
  /v2/add/notion:
    post:
      summary: Add Notion pages
      description: Submit selected Notion pages for documentation processing. Requires
        a connected Notion account and a team project.
      operationId: addNotion
      tags:
        - Add Library
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - workspaceId
                - workspaceName
                - pageIds
                - title
                - description
              properties:
                workspaceId:
                  type: string
                  description: The Notion workspace ID
                workspaceName:
                  type: string
                  description: The Notion workspace name
                pageIds:
                  type: array
                  items:
                    type: string
                  description: List of Notion page IDs to index.
                title:
                  type: string
                  description: Title for the library
                description:
                  type: string
                  description: Description of the library
                projectId:
                  type: string
                  description: The team project ID to associate these Notion pages with
            example:
              workspaceId: workspace-uuid
              workspaceName: Acme Workspace
              pageIds:
                - page-1
                - page-2
              title: Product Docs
              description: Internal Notion knowledge base
              projectId: project-uuid
      responses:
        "200":
          $ref: "#/components/responses/AddLibrarySuccess"
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "403":
          $ref: "#/components/responses/ForbiddenError"
        "409":
          $ref: "#/components/responses/DuplicateError"
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
    DuplicateError:
      description: Conflict - Resource already exists
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: duplicate_repo
            message: This private repository is already in your team
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
