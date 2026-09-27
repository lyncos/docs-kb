---
title: Search for libraries
description: Search locally indexed libraries by name
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/search/search-for-libraries
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Search for libraries

> Search locally indexed libraries by name

`GET /v2/libs/search`

## OpenAPI

````yaml openapi-enterprise.json get /v2/libs/search
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
  /v2/libs/search:
    get:
      summary: Search for libraries
      description: Search locally indexed libraries by name. Results may also include
        public libraries from Context7 Cloud depending on your policy settings.
      operationId: searchLibraries
      tags:
        - Search
      parameters:
        - name: libraryName
          in: query
          description: Library name to search for (e.g., `react`, `nextjs`)
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 500
          example: react
        - name: query
          in: query
          description: User's original question or task - used for relevance ranking
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 500
          example: How to manage state with hooks
      responses:
        "200":
          description: Search results ranked by relevance
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/SearchResponse"
              example:
                results:
                  - id: /your-org/your-repo
                    title: Your Repo
                    description: Internal tooling docs
                    totalSnippets: 150
                    source: Local (Private)
                    trustScore: 10
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
    Library:
      type: object
      description: An indexed library
      properties:
        id:
          type: string
          description: Library ID to pass to `GET /v2/context`
          example: /your-org/your-repo
        title:
          type: string
          description: Display name
          example: Your Repo
        description:
          type: string
          description: Short description
          example: Internal tooling docs
        totalSnippets:
          type: integer
          description: Number of indexed snippets
          example: 150
        source:
          type: string
          description: Where the library was indexed from
          example: Local (Private)
        trustScore:
          type: integer
          description: Source reputation score (0–10)
          example: 10
    SearchResponse:
      type: object
      properties:
        results:
          type: array
          description: Matching libraries ranked by relevance
          items:
            $ref: "#/components/schemas/Library"
      required:
        - results
    Error:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error description
      required:
        - error
  responses:
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
