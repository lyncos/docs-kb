---
title: Get parse status
description: Returns the status of all active and queued parse jobs
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/parse/get-parse-status
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Get parse status

> Returns the status of all active and queued parse jobs

`GET /parse-status`

## OpenAPI

````yaml openapi-enterprise.json get /parse-status
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
  /parse-status:
    get:
      summary: Get parse status
      description: Returns the current status of all active and queued parse jobs.
      operationId: getParseStatus
      tags:
        - Parse
      responses:
        "200":
          description: Active parse jobs and their status
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ParseStatusResponse"
              example:
                activeParses:
                  /your-org/your-repo:
                    status: parsing
                    startedAt: 2025-01-01T12:00:00.000Z
                    duration: 8.6
                    statusMessage: Scanning 16 files
                  /other-org/other-repo:
                    status: queued
                    position: 1
                    createdAt: 2025-01-01T12:00:01.000Z
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "500":
          $ref: "#/components/responses/InternalServerError"
      security:
        - {}
        - bearerAuth: []
components:
  schemas:
    ParseJobStatus:
      type: object
      properties:
        status:
          type: string
          enum:
            - queued
            - parsing
            - finalizing
          description: Current job status
        position:
          type: integer
          description: Queue position. Only present when `status` is `queued`
        createdAt:
          type: string
          format: date-time
          description: ISO 8601 timestamp when the job was queued. Only present when
            `status` is `queued`
        startedAt:
          type: string
          format: date-time
          description: ISO 8601 timestamp when the job began running. Only present when
            `status` is `parsing` or `finalizing`
        duration:
          type: number
          description: Elapsed seconds since the job started. Only present when `status`
            is `parsing` or `finalizing`
        statusMessage:
          type: string
          description: Human-readable progress detail (e.g. `Scanning 16 files`). Only
            present when `status` is `parsing`
      required:
        - status
    ParseStatusResponse:
      type: object
      properties:
        activeParses:
          type: object
          description: Map of project name to its current parse job status
          additionalProperties:
            $ref: "#/components/schemas/ParseJobStatus"
      required:
        - activeParses
    Error:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error description
      required:
        - error
  responses:
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
