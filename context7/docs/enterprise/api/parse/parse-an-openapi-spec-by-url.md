---
title: Parse an OpenAPI spec by URL
description: Queue a remote OpenAPI specification (JSON or YAML) for parsing and indexing
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/parse/parse-an-openapi-spec-by-url
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Parse an OpenAPI spec by URL

> Queue a remote OpenAPI specification (JSON or YAML) for parsing and indexing

`POST /parse-openapi`

## OpenAPI

````yaml openapi-enterprise.json post /parse-openapi
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
  /parse-openapi:
    post:
      summary: Parse an OpenAPI spec by URL
      description: Queue a remote OpenAPI specification (JSON or YAML) for parsing and
        indexing.
      operationId: parseOpenApi
      tags:
        - Parse
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
                  description: URL of a JSON or YAML OpenAPI specification
                projectTitle:
                  type: string
                  description: Display name for the project
                description:
                  type: string
                  description: Short description shown in the library list
                force:
                  type: boolean
                  description: Re-parse even if already indexed
                  default: false
            example:
              openApiUrl: https://example.com/openapi.json
              projectTitle: My API
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
