---
title: Refresh a library
description: Re-parse an existing library using its stored settings
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/parse/refresh-a-library
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Refresh a library

> Re-parse an existing library using its stored settings

`POST /projects/{projectId}/refresh`

## OpenAPI

````yaml openapi-enterprise.json post /projects/{projectId}/refresh
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
  /projects/{projectId}/refresh:
    post:
      summary: Refresh a library
      description: >-
        Re-parse an existing library using its stored settings. Returns
        immediately with a queue position.


        Not available for:

        - Libraries imported from Context7 Cloud (re-import an updated bundle
        instead)

        - Uploaded OpenAPI files (re-upload the file instead)
      operationId: refreshProject
      tags:
        - Parse
      parameters:
        - name: projectId
          in: path
          required: true
          description: Project identifier without the leading slash. For repositories use
            `owner/repo` (e.g. `upstash/ratelimit-js`). For websites use
            `websites/hostname` (e.g. `websites/upstash`). For OpenAPI specs use
            `openapi/derived-name`.
          schema:
            type: string
          example: upstash/ratelimit-js
      responses:
        "202":
          $ref: "#/components/responses/ParseQueued"
        "400":
          description: Bad Request - refresh not available for this project type
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              examples:
                imported:
                  summary: Imported library
                  value:
                    error: Refresh isn't available for imported libraries. Re-import an updated
                      export from Context7 Cloud to update it.
                uploadedFile:
                  summary: Uploaded OpenAPI file
                  value:
                    error: Refresh not available for uploaded OpenAPI files. Re-upload the same file
                      to update.
                noToken:
                  summary: No git token configured
                  value:
                    error: No git token configured for GitHub. Configure a GitHub App or set a
                      personal access token.
        "404":
          $ref: "#/components/responses/NotFoundError"
        "409":
          description: Conflict - a parse job is already active or queued for this project
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: This project is already queued
                project: /upstash/ratelimit-js
                status: queued
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
    NotFoundError:
      description: Not Found - library does not exist
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: Project not found
    InternalServerError:
      description: Internal Server Error
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: An unexpected error occurred
````
