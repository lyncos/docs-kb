---
title: Import a library bundle
description: Import pre-parsed libraries into an airgapped on-premise install, as a JSON body or a Context7 Cloud export file
product: Context7
section: docs
source_url: https://context7.com/docs/enterprise/api/parse/import-libraries
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Import a library bundle

> Import pre-parsed libraries into an airgapped on-premise install, as a JSON body or a Context7 Cloud export file

`POST /import-libraries`

## OpenAPI

````yaml openapi-enterprise.json post /import-libraries
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
  /import-libraries:
    post:
      summary: Import a library bundle
      description: Import pre-parsed libraries into an airgapped on-premise install.
        Accepts either a Context7 Cloud export `.zip` (`multipart/form-data`) or
        a JSON body (`application/json`) for programmatic clients. Requires a
        personal API key (or an admin session). Each library is queued as its
        own job and its snippets are re-embedded locally with this install's
        configured provider. Available only on installs running an **offline
        (airgapped) license**.
      operationId: importLibraries
      tags:
        - Parse
      parameters:
        - name: force
          in: query
          required: false
          schema:
            type: boolean
            default: false
          description: Overwrite libraries that already exist. Handy when posting a piped
            export body, which carries no `force` field. Without it, existing
            libraries are skipped.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ImportLibrariesRequest"
          multipart/form-data:
            schema:
              type: object
              required:
                - bundleFile
              properties:
                bundleFile:
                  type: string
                  format: binary
                  description: A Context7 Cloud `context7-libraries.zip` export (up to 100 MB)
                force:
                  type: boolean
                  description: Overwrite libraries that already exist on this install
                  default: false
      responses:
        "202":
          $ref: "#/components/responses/LibrariesImported"
        "400":
          $ref: "#/components/responses/BadRequestError"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "403":
          $ref: "#/components/responses/ForbiddenError"
        "500":
          $ref: "#/components/responses/InternalServerError"
      security:
        - bearerAuth: []
components:
  schemas:
    ImportLibrariesRequest:
      type: object
      required:
        - libraries
      properties:
        libraries:
          type: array
          description: The libraries to import. Each carries its full snippet content;
            embeddings are recomputed on this install.
          items:
            $ref: "#/components/schemas/ImportLibrary"
        force:
          type: boolean
          description: Overwrite libraries that already exist on this install
          default: false
    ImportLibrary:
      type: object
      required:
        - project
        - codeSnippets
        - infoSnippets
      properties:
        project:
          type: string
          description: Library identifier, e.g. `/your-org/your-repo`
          example: /vercel/next.js
        title:
          type: string
        description:
          type: string
        type:
          type: string
          description: Source type of the library (e.g. `repo`, `website`, `openapi`)
        language:
          type: string
          example: English
        branch:
          type: string
        docsRepoUrl:
          type: string
        docsSiteUrl:
          type: string
        totalTokens:
          type: integer
        codeSnippets:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              title:
                type: string
              description:
                type: string
              language:
                type: string
              codeList:
                type: array
                items:
                  type: object
                  properties:
                    language:
                      type: string
                    code:
                      type: string
              tokens:
                type: integer
        infoSnippets:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              content:
                type: string
              breadcrumb:
                type: string
              tokens:
                type: integer
    LibrariesImportedResponse:
      type: object
      properties:
        message:
          type: string
          example: Queued 2 libraries for import
        queued:
          type: array
          description: Library identifiers queued for import
          items:
            type: string
          example:
            - /vercel/next.js
            - /facebook/react
        skipped:
          type: array
          description: Libraries that were not imported, with a reason
          items:
            type: object
            properties:
              project:
                type: string
              reason:
                type: string
                example: already exists
      required:
        - message
        - queued
        - skipped
    Error:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error description
      required:
        - error
  responses:
    LibrariesImported:
      description: Libraries accepted and queued for import
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/LibrariesImportedResponse"
    ForbiddenError:
      description: Forbidden - the action is not permitted for this install or user
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
          example:
            error: Library import is available only with an offline license.
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
