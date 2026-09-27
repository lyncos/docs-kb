---
title: Get library usage metrics
description: 'Retrieve full usage metrics for a library: cumulative and daily request counters broken down by surface (web page, text docs, MCP, CLI), MCP client daily unique-user breakdown, and lifetime topic and country distributions. The API key must belong to a member of the teamspace that owns the library — claim ownership from the library''s admin page on context7.com.'
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/metrics/get-library-usage-metrics
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Get library usage metrics

> Retrieve full usage metrics for a library: cumulative and daily request counters broken down by surface (web page, text docs, MCP, CLI), MCP client daily unique-user breakdown, and lifetime topic and country distributions. The API key must belong to a member of the teamspace that owns the library — claim ownership from the library's admin page on context7.com.

`GET /v2/libs/metrics`

## OpenAPI

````yaml openapi.json get /v2/libs/metrics
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
  /v2/libs/metrics:
    get:
      summary: Get library usage metrics
      description: "Retrieve full usage metrics for a library: cumulative and daily
        request counters broken down by surface (web page, text docs, MCP, CLI),
        MCP client daily unique-user breakdown, and lifetime topic and country
        distributions. The API key must belong to a member of the teamspace that
        owns the library — claim ownership from the library's admin page on
        context7.com."
      operationId: getLibraryMetrics
      tags:
        - Metrics
      parameters:
        - $ref: "#/components/parameters/LibraryIdParam"
        - $ref: "#/components/parameters/DaysParam"
      responses:
        "200":
          description: Library usage metrics
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/LibraryMetricsResponse"
              example:
                total:
                  page: 12450
                  txt: 3820
                  mcp: 95210
                  cli: 1240
                daily:
                  - date: 2025-01-14
                    page: 8
                    txt: 3
                    mcp: 42
                    cli: 1
                    total: 54
                  - date: 2025-01-15
                    page: 11
                    txt: 5
                    mcp: 67
                    cli: 0
                    total: 83
                mcpClients:
                  dailyData:
                    - date: 2025-01-14
                      uniqueUsersByClient:
                        cursor: 12
                        claude-code: 7
                      totalUniqueUsers: 18
                    - date: 2025-01-15
                      uniqueUsersByClient:
                        cursor: 15
                        claude-code: 9
                        codex: 2
                      totalUniqueUsers: 25
                topics:
                  - topic: routing
                    count: 420
                  - topic: middleware
                    count: 312
                  - topic: app-router
                    count: 187
                countries:
                  - country: US
                    count: 3120
                  - country: DE
                    count: 842
                  - country: IN
                    count: 610
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "403":
          $ref: "#/components/responses/ForbiddenError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "500":
          $ref: "#/components/responses/InternalServerError"
      security:
        - bearerAuth: []
components:
  parameters:
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
    DaysParam:
      name: days
      in: query
      description: Number of days of daily history to return (1-365). Defaults to 30.
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 365
        default: 30
      example: 30
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
    ProjectStats:
      type: object
      description: Cumulative request counts for a library, broken down by request surface
      properties:
        page:
          type: integer
          description: Requests served to the context7.com web UI
        txt:
          type: integer
          description: Plain-text documentation requests
        mcp:
          type: integer
          description: Requests served via the Context7 MCP server
        cli:
          type: integer
          description: Requests served to the Context7 CLI
      required:
        - page
        - txt
        - mcp
        - cli
    DailyStatsPoint:
      type: object
      description: Per-day request counts for a library (counts *on* this date, not
        cumulative)
      properties:
        date:
          type: string
          format: date
          description: UTC date in `YYYY-MM-DD` format
          example: 2025-01-15
        page:
          type: integer
          description: Requests served to the context7.com web UI on this date
        txt:
          type: integer
          description: Plain-text documentation requests on this date
        mcp:
          type: integer
          description: Requests served via the Context7 MCP server on this date
        cli:
          type: integer
          description: Requests served to the Context7 CLI on this date
        total:
          type: integer
          description: Sum of all request surfaces on this date (`page + txt + mcp + cli`)
      required:
        - date
        - page
        - txt
        - mcp
        - cli
        - total
    LibraryMetricsResponse:
      type: object
      description: Library usage metrics response
      properties:
        total:
          $ref: "#/components/schemas/ProjectStats"
        daily:
          type: array
          description: Per-day request counts (deltas, not cumulative), ordered from
            oldest to newest. Days with zero activity are omitted. Up to `days`
            points — fewer if the library has less history or had idle days in
            the window.
          items:
            $ref: "#/components/schemas/DailyStatsPoint"
        mcpClients:
          $ref: "#/components/schemas/McpClientMetrics"
        topics:
          type: array
          description: Lifetime topic distribution, ordered by count descending
          items:
            $ref: "#/components/schemas/TopicCount"
        countries:
          type: array
          description: Lifetime country distribution (ISO-2 codes), ordered by count
            descending
          items:
            $ref: "#/components/schemas/CountryCount"
      required:
        - total
        - daily
        - mcpClients
        - topics
        - countries
    McpClientMetrics:
      type: object
      description: MCP client usage breakdown by day
      properties:
        dailyData:
          type: array
          description: Per-day MCP client unique-user breakdown, ordered from oldest to
            newest
          items:
            $ref: "#/components/schemas/McpDailyClientData"
      required:
        - dailyData
    McpDailyClientData:
      type: object
      description: Per-day MCP client unique users for a library
      properties:
        date:
          type: string
          format: date
          description: UTC date in `YYYY-MM-DD` format
          example: 2025-01-15
        uniqueUsersByClient:
          type: object
          description: Unique user count per MCP client identifier (e.g., `cursor`,
            `claude-code`, `codex`)
          additionalProperties:
            type: integer
        totalUniqueUsers:
          type: integer
          description: Total unique users across all clients for this library on this date
      required:
        - date
        - uniqueUsersByClient
        - totalUniqueUsers
    TopicCount:
      type: object
      description: Topic with its lifetime request count
      properties:
        topic:
          type: string
          description: Normalized, lowercased topic string
          example: routing
        count:
          type: integer
          description: Number of requests that referenced this topic
      required:
        - topic
        - count
    CountryCount:
      type: object
      description: Country with its lifetime request count
      properties:
        country:
          type: string
          description: ISO 3166-1 alpha-2 country code
          example: US
        count:
          type: integer
          description: Number of requests originating from this country
      required:
        - country
        - count
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
````
