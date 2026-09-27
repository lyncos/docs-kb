---
title: Get documentation context
description: Retrieve documentation snippets for a library ranked by relevance to your query
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/context/get-documentation-context
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Get documentation context

> Retrieve documentation snippets for a library ranked by relevance to your query

`GET /v2/context`

## OpenAPI

````yaml openapi-enterprise.json get /v2/context
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
  /v2/context:
    get:
      summary: Get documentation context
      description: Retrieve documentation snippets for a library ranked by relevance
        to your query, formatted as plain text ready to inject into an LLM
        prompt. This is the endpoint MCP tools call internally.
      operationId: getContext
      tags:
        - Context
      parameters:
        - name: libraryId
          in: query
          description: Library ID returned by `GET /v2/libs/search` (e.g.,
            `/your-org/your-repo`)
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 500
          example: /vercel/next.js
        - name: query
          in: query
          description: Natural language question or topic to retrieve context for
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 500
          example: How do I use the app router?
      responses:
        "200":
          description: Relevant documentation snippets as plain text
          content:
            text/plain:
              schema:
                type: string
              example: >-
                ### useRouter()


                Source: https://github.com/vercel/next.js/...


                The `useRouter` hook allows you to programmatically change
                routes inside Client Components.


                --------------------------------


                ### app/layout.tsx


                ```tsx

                export default function Layout({ children }) {
                  return <html><body>{children}</body></html>
                }

                ```
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "500":
          $ref: "#/components/responses/InternalServerError"
      security:
        - {}
        - bearerAuth: []
components:
  schemas:
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
