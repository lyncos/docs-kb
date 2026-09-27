---
title: Refresh a library
description: Trigger a refresh of an existing library to fetch the latest documentation. Library owners have dedicated refresh limits.
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/refresh/refresh-a-library
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Refresh a library

> Trigger a refresh of an existing library to fetch the latest documentation. Library owners have dedicated refresh limits.

`POST /v1/refresh`

## OpenAPI

````yaml openapi.json post /v1/refresh
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
  /v1/refresh:
    post:
      summary: Refresh a library
      description: Trigger a refresh of an existing library to fetch the latest
        documentation. Library owners have dedicated refresh limits.
      operationId: refreshLibrary
      tags:
        - Refresh
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - libraryName
              properties:
                libraryName:
                  type: string
                  description: Library identifier — the URL path of the library on context7.com.
                    Use `/owner/repo` for GitHub repositories (e.g.,
                    `/vercel/next.js`), or `/<source>/<id>` for other sources
                    (e.g., `/websites/uploadcare`, `/llmstxt/<source>`). See
                    [Library ID format](/api-guide#library-id-format).
                branch:
                  type: string
                  description: Optional branch name to refresh
                gitToken:
                  type: string
                  description: Optional Git access token for refreshing private repositories. If
                    not provided, the stored OAuth token will be used.
            examples:
              github:
                summary: GitHub repository
                value:
                  libraryName: /vercel/next.js
              website:
                summary: Website source
                value:
                  libraryName: /websites/uploadcare
              llmstxt:
                summary: llms.txt source
                value:
                  libraryName: /llmstxt/example
      responses:
        "200":
          description: Refresh started successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                required:
                  - message
              example:
                message: Refresh started successfully
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "403":
          $ref: "#/components/responses/ForbiddenError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "429":
          $ref: "#/components/responses/RateLimitError"
        "500":
          $ref: "#/components/responses/InternalServerError"
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
