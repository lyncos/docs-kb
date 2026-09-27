---
title: Parse a Git repository
description: Queue a GitHub or GitLab repository for parsing and indexing
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/parse/parse-a-git-repository
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Parse a Git repository

> Queue a GitHub or GitLab repository for parsing and indexing

`POST /parse`

## OpenAPI

````yaml openapi-enterprise.json post /parse
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
  /parse:
    post:
      summary: Parse a Git repository
      description: Queue a GitHub or GitLab repository for parsing and indexing.
        Returns immediately with a queue position. Monitor progress with `GET
        /parse-status`.
      operationId: parseRepo
      tags:
        - Parse
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ParseRepoRequest"
            examples:
              minimal:
                summary: Minimal - index the whole repo
                value:
                  repoUrl: https://github.com/your-org/your-repo
              withOptions:
                summary: With folder and branch filters
                value:
                  repoUrl: https://github.com/your-org/your-repo
                  branch: main
                  folders:
                    - docs
                  excludeFolders:
                    - node_modules
                  force: false
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
    ParseRepoRequest:
      type: object
      required:
        - repoUrl
      properties:
        repoUrl:
          type: string
          format: uri
          description: HTTPS URL of the GitHub or GitLab repository
        branch:
          type: string
          description: Branch to parse. Defaults to the repository's default branch
        folders:
          type: array
          items:
            type: string
          description: Only index files under these paths. Empty means the entire repository
        excludeFolders:
          type: array
          items:
            type: string
          description: Paths to skip during indexing
        excludeFiles:
          type: array
          items:
            type: string
          description: Glob patterns for files to exclude
        force:
          type: boolean
          description: Re-parse even if the current commit is already indexed
          default: false
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
