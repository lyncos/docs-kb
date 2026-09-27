---
title: Update teamspace policies
description: 'Incrementally update policy configuration for the teamspace associated with the API key. Only the fields you include in the request body are modified — omitted fields remain unchanged. For source types, use `enable`/`disable` arrays (both allowed if no overlap). For library lists, use `add`/`remove` objects or `clear: true` to remove all. Requires owner or admin role. All field names use camelCase.'
product: Context7
section: docs
source_url: https://context7.com/docs/api-reference/policies/update-teamspace-policies
fetched: '2026-09-26'
tags:
- context7
- docs
---

# Update teamspace policies

> Incrementally update policy configuration for the teamspace associated with the API key. Only the fields you include in the request body are modified — omitted fields remain unchanged. For source types, use `enable`/`disable` arrays (both allowed if no overlap). For library lists, use `add`/`remove` objects or `clear: true` to remove all. Requires owner or admin role. All field names use camelCase.

`PATCH /v2/policies`

## OpenAPI

````yaml openapi.json patch /v2/policies
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
  /v2/policies:
    patch:
      summary: Update teamspace policies
      description: "Incrementally update policy configuration for the teamspace
        associated with the API key. Only the fields you include in the request
        body are modified — omitted fields remain unchanged. For source types,
        use `enable`/`disable` arrays (both allowed if no overlap). For library
        lists, use `add`/`remove` objects or `clear: true` to remove all.
        Requires owner or admin role. All field names use camelCase."
      operationId: updatePolicies
      tags:
        - Policies
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/PatchPoliciesRequest"
            examples:
              disableSourceType:
                summary: Disable a source type
                value:
                  sourceTypes:
                    disable:
                      - websites
              setQualityFilters:
                summary: Set quality filter thresholds
                value:
                  libraryFilters:
                    quality:
                      requireVerified: true
                      minTrustScore: 4
                      repoFilters:
                        minStars: 1000
              setWebsiteFilters:
                summary: Set website quality filters
                value:
                  libraryFilters:
                    quality:
                      websiteFilters:
                        minBacklinks: 100
                        minReferringDomains: 10
                        minOrganicTraffic: 1000
              blockLibrary:
                summary: Add a library to the blocked list
                value:
                  libraryFilters:
                    quality:
                      blockedLibraries:
                        add:
                          - /org/repo
              blockDomain:
                summary: Block all libraries from a domain
                value:
                  libraryFilters:
                    quality:
                      blockedLibraries:
                        add:
                          - example.com
              exceptLibrary:
                summary: Add a library exception (bypasses all filters)
                value:
                  libraryFilters:
                    quality:
                      exceptedLibraries:
                        add:
                          - /vercel/next.js
              allowPermissiveLicenses:
                summary: Restrict public repos to permissive SPDX licenses
                value:
                  libraryFilters:
                    quality:
                      repoFilters:
                        allowedLicenses:
                          add:
                            - MIT
                            - Apache-2.0
                            - BSD-3-Clause
                            - ISC
              clearLicenseRestriction:
                summary: Remove all license restrictions
                value:
                  libraryFilters:
                    quality:
                      repoFilters:
                        allowedLicenses:
                          clear: true
              allowDomain:
                summary: Allow libraries from a specific domain (select mode)
                value:
                  libraryFilters:
                    select:
                      allowedLibraries:
                        add:
                          - stripe.com
                          - /vercel/next.js
              clearAllowedLibraries:
                summary: Clear all allowed libraries
                value:
                  libraryFilters:
                    select:
                      allowedLibraries:
                        clear: true
              combined:
                summary: Multiple changes in one request
                value:
                  sourceTypes:
                    enable:
                      - websites
                    disable:
                      - confluence
                  libraryFilters:
                    mode: quality
                    quality:
                      minTrustScore: 4
                      maxAgeDays: 365
                      blockedLibraries:
                        add:
                          - /org/repo
                        remove:
                          - /org/old-repo
                      repoFilters:
                        minStars: 100
                      websiteFilters:
                        minBacklinks: 100
      responses:
        "200":
          description: Updated policy configuration
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PolicyResponse"
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
    SourceTypeStatus:
      type: object
      description: Whether a source type is enabled or disabled
      properties:
        enabled:
          type: boolean
          description: Whether this source type is enabled
      required:
        - enabled
    PolicyResponse:
      type: object
      description: Complete teamspace policy configuration
      properties:
        sourceTypes:
          type: object
          description: Access settings for each documentation source type
          properties:
            public_repos:
              $ref: "#/components/schemas/SourceTypeStatus"
            private_sources:
              $ref: "#/components/schemas/SourceTypeStatus"
            confluence:
              $ref: "#/components/schemas/SourceTypeStatus"
            uploaded_files:
              $ref: "#/components/schemas/SourceTypeStatus"
            websites:
              $ref: "#/components/schemas/SourceTypeStatus"
            llmstxt:
              $ref: "#/components/schemas/SourceTypeStatus"
          required:
            - public_repos
            - private_sources
            - confluence
            - uploaded_files
            - websites
            - llmstxt
        libraryFilters:
          type: object
          description: Library access filters. Mode determines which sub-object is active.
          properties:
            mode:
              type: string
              nullable: true
              enum:
                - quality
                - select
                - null
              description: "Filter mode: 'quality' for threshold-based filtering, 'select' for
                manual library selection"
            quality:
              type: object
              description: Quality-mode settings (active when mode is 'quality')
              properties:
                requireVerified:
                  type: boolean
                  description: Restrict to verified libraries only
                minTrustScore:
                  type: integer
                  nullable: true
                  description: Minimum trust score, 0-10
                maxAgeDays:
                  type: integer
                  nullable: true
                  description: Maximum days since last update
                blockedLibraries:
                  type: array
                  items:
                    type: string
                  description: Libraries excluded from results
                exceptedLibraries:
                  type: array
                  items:
                    type: string
                  description: Libraries that bypass all quality filters, blocked list, and source
                    type restrictions
                repoFilters:
                  type: object
                  description: Repo-specific quality filters
                  properties:
                    minStars:
                      type: integer
                      nullable: true
                      description: Minimum GitHub stars required
                    allowedLicenses:
                      type: array
                      items:
                        type: string
                      description: SPDX license identifiers (e.g. 'MIT', 'Apache-2.0') that are
                        allowed. Empty array means no license restriction.
                        Applies to public repos only; non-repo source types pass
                        through.
                  required:
                    - minStars
                    - allowedLicenses
                websiteFilters:
                  type: object
                  description: Website-specific quality filters
                  properties:
                    minBacklinks:
                      type: integer
                      nullable: true
                      description: Minimum number of backlinks required
                    minReferringDomains:
                      type: integer
                      nullable: true
                      description: Minimum number of referring domains required
                    minOrganicTraffic:
                      type: integer
                      nullable: true
                      description: Minimum monthly organic traffic required
                  required:
                    - minBacklinks
                    - minReferringDomains
                    - minOrganicTraffic
              required:
                - requireVerified
                - minTrustScore
                - maxAgeDays
                - blockedLibraries
                - exceptedLibraries
                - repoFilters
                - websiteFilters
            select:
              type: object
              description: Select-mode settings (active when mode is 'select')
              properties:
                allowedLibraries:
                  type: array
                  items:
                    type: string
                  description: Libraries explicitly allowed
              required:
                - allowedLibraries
          required:
            - mode
            - quality
            - select
        accessibleLibraryCount:
          type: integer
          description: Number of public libraries currently accessible under these filters
      required:
        - sourceTypes
        - libraryFilters
        - accessibleLibraryCount
    ListOperation:
      type: object
      description: Incremental add/remove operation on a list of library identifiers
        or domains. Use 'clear' to remove all entries at once.
      properties:
        add:
          type: array
          items:
            type: string
          description: Identifiers to add — library paths (e.g. '/org/repo', '/org') or
            domains (e.g. 'stripe.com')
        remove:
          type: array
          items:
            type: string
          description: Identifiers to remove — library paths (e.g. '/org/repo', '/org') or
            domains (e.g. 'stripe.com')
        clear:
          type: boolean
          description: Set to true to remove all entries. Cannot be used together with
            'add' or 'remove'.
    LicenseListOperation:
      type: object
      description: Incremental add/remove operation on a list of SPDX license
        identifiers. Use 'clear' to remove all entries at once.
      properties:
        add:
          type: array
          items:
            type: string
            pattern: ^[A-Za-z0-9.+\-_]+$
            maxLength: 64
          description: SPDX license identifiers to add (e.g. 'MIT', 'Apache-2.0',
            'BSD-3-Clause')
        remove:
          type: array
          items:
            type: string
            pattern: ^[A-Za-z0-9.+\-_]+$
            maxLength: 64
          description: SPDX license identifiers to remove
        clear:
          type: boolean
          description: Set to true to remove all entries. Cannot be used together with
            'add' or 'remove'.
    PatchPoliciesRequest:
      type: object
      description: Incremental policy update. All fields are optional — only provided
        fields are modified. At least one of 'sourceTypes' or 'libraryFilters'
        must be provided.
      minProperties: 1
      properties:
        sourceTypes:
          type: object
          description: Enable or disable specific source types. Both can be provided in
            one request, but the same type cannot appear in both arrays.
          properties:
            enable:
              type: array
              items:
                type: string
                enum:
                  - public_repos
                  - private_sources
                  - confluence
                  - uploaded_files
                  - websites
                  - llmstxt
              description: Source types to enable
            disable:
              type: array
              items:
                type: string
                enum:
                  - public_repos
                  - private_sources
                  - confluence
                  - uploaded_files
                  - websites
                  - llmstxt
              description: Source types to disable
        libraryFilters:
          type: object
          description: Update library access filters.
          properties:
            mode:
              type: string
              nullable: true
              enum:
                - quality
                - select
                - null
              description: Filter mode (null to clear)
            quality:
              type: object
              description: Update quality-mode settings.
              properties:
                requireVerified:
                  type: boolean
                  description: Restrict to verified libraries only
                minTrustScore:
                  type: integer
                  nullable: true
                  minimum: 0
                  maximum: 10
                  description: Minimum trust score, 0-10 (null to clear)
                maxAgeDays:
                  type: integer
                  nullable: true
                  minimum: 1
                  description: Maximum age in days (null to clear)
                blockedLibraries:
                  $ref: "#/components/schemas/ListOperation"
                exceptedLibraries:
                  $ref: "#/components/schemas/ListOperation"
                repoFilters:
                  type: object
                  description: Update repo-specific quality filters.
                  properties:
                    minStars:
                      type: integer
                      nullable: true
                      minimum: 0
                      description: Minimum stars threshold (null to clear)
                    allowedLicenses:
                      $ref: "#/components/schemas/LicenseListOperation"
                websiteFilters:
                  type: object
                  description: Update website-specific quality filters.
                  properties:
                    minBacklinks:
                      type: integer
                      nullable: true
                      minimum: 0
                      description: Minimum backlinks threshold (null to clear)
                    minReferringDomains:
                      type: integer
                      nullable: true
                      minimum: 0
                      description: Minimum referring domains threshold (null to clear)
                    minOrganicTraffic:
                      type: integer
                      nullable: true
                      minimum: 0
                      description: Minimum organic traffic threshold (null to clear)
            select:
              type: object
              description: Update select-mode settings.
              properties:
                allowedLibraries:
                  $ref: "#/components/schemas/ListOperation"
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
