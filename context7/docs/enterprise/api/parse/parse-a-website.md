---
title: Parse a website
description: Crawl and index a public website starting from the given URL
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/parse/parse-a-website
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Parse a website

> Crawl and index a public website starting from the given URL

`POST /parse-website`

## OpenAPI

````yaml openapi-enterprise.json post /parse-website
openapi: 3.0.0
info:
  title: Context7 On-Premise API
  description: REST API for the Context7 On-Premise server. Covers library parsing
    and documentation search.
  version: 1.0.0
servers:
  - url: https://your-instance.example.com/api
    description: Your on-premise deployment (replace with your actual host)
  - url: http://localhost:3000/api
    description: Local development
tags:
  - name: Search
    description: Search indexed libraries
  - name: Context
    description: Retrieve documentation context for queries
  - name: Parse
    description: Parse and index new libraries
paths:
  /parse-website:
    post:
      summary: Parse a website
      description: Crawl and index a public website starting from the given URL.
      operationId: parseWebsite
      tags:
        - Parse
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - websiteUrl
              properties:
                websiteUrl:
                  type: string
                  format: uri
                  description: Root URL to start crawling from
                projectTitle:
                  type: string
                  description: Display name for the project
                description:
                  type: string
                  description: Short description shown in the library list
                maxPages:
                  type: integer
                  description: Maximum number of pages to crawl
                  default: 100
                maxDepth:
                  type: integer
                  description: Maximum link depth from the root URL
                  default: 3
                excludePatterns:
                  type: array
                  items:
                    type: string
                  description: URL path patterns to skip (e.g., `/blog/*`)
                force:
                  type: boolean
                  description: Re-crawl even if already indexed
                  default: false
            example:
              websiteUrl: https://docs.example.com
              maxPages: 50
      responses:
        "202":
          $ref: "#/components/responses/ParseQueued"
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "500":
          $ref: "#/components/responses/InternalServerError"
      security:
        - {}
        - bearerAuth: []
components:
  schemas:
    ParseQueuedResponse:
      type: object
      properties:
        message:
          type: string
          example: Parse queued
        project:
          type: string
          description: Project identifier assigned to this library (e.g.
            `/your-org/your-repo`)
          example: /your-org/your-repo
        queueId:
          type: integer
          description: Numeric ID for this parse job
          example: 5
        position:
          type: integer
          nullable: true
          description: Position in the queue. `null` if the job started immediately
          example: 1
      required:
        - message
        - project
        - queueId
    Error:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error description
      required:
        - error
  responses:
    ParseQueued:
      description: Parse job accepted and queued
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ParseQueuedResponse"
    BadRequestError:
      description: Bad Request - invalid or missing parameters
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: repoUrl is required
    UnauthorizedError:
      description: Unauthorized - authentication required
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: Authentication required
    InternalServerError:
      description: Internal Server Error
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: An unexpected error occurred
````
