---
title: update_gateway[¶](#update-gateway "Link to this heading")
description: BedrockAgentCoreControl / Client / update_gateway
product: Amazon Bedrock AgentCore
section: References / boto3.amazonaws.com
source_url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_gateway.html
fetched: '2026-09-26'
tags:
- agentcore
- boto3-amazonaws-com
- core
- reference
referenced_by:
- gateway-encryption.md
conversion: pandoc
---

[BedrockAgentCoreControl](../../bedrock-agentcore-control.html) / Client / update_gateway

# update_gateway[¶](#update-gateway "Link to this heading")

BedrockAgentCoreControl.Client.update_gateway(*\*\*kwargs*)[¶](#BedrockAgentCoreControl.Client.update_gateway "Link to this definition")  
Updates an existing gateway.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/UpdateGateway)

### Request Syntax

    response = client.update_gateway(
        gatewayIdentifier='string',
        name='string',
        description='string',
        roleArn='string',
        protocolType='MCP',
        protocolConfiguration={
            'mcp': {
                'supportedVersions': [
                    'string',
                ],
                'instructions': 'string',
                'searchType': 'SEMANTIC',
                'sessionConfiguration': {
                    'sessionTimeoutInSeconds': 123
                },
                'streamingConfiguration': {
                    'enableResponseStreaming': True|False
                }
            }
        },
        authorizerType='CUSTOM_JWT'|'AWS_IAM'|'NONE'|'AUTHENTICATE_ONLY',
        authorizerConfiguration={
            'customJWTAuthorizer': {
                'discoveryUrl': 'string',
                'allowedAudience': [
                    'string',
                ],
                'allowedClients': [
                    'string',
                ],
                'allowedScopes': [
                    'string',
                ],
                'advertisedScopeMapping': {
                    'string': 'string'
                },
                'customClaims': [
                    {
                        'inboundTokenClaimName': 'string',
                        'inboundTokenClaimValueType': 'STRING'|'STRING_ARRAY',
                        'authorizingClaimMatchValue': {
                            'claimMatchValue': {
                                'matchValueString': 'string',
                                'matchValueStringList': [
                                    'string',
                                ]
                            },
                            'claimMatchOperator': 'EQUALS'|'CONTAINS'|'CONTAINS_ANY'
                        }
                    },
                ],
                'privateEndpoint': {
                    'selfManagedLatticeResource': {
                        'resourceConfigurationIdentifier': 'string'
                    },
                    'managedVpcResource': {
                        'vpcIdentifier': 'string',
                        'subnetIds': [
                            'string',
                        ],
                        'endpointIpAddressType': 'IPV4'|'IPV6',
                        'securityGroupIds': [
                            'string',
                        ],
                        'tags': {
                            'string': 'string'
                        },
                        'routingDomain': 'string'
                    }
                },
                'privateEndpointOverrides': [
                    {
                        'domain': 'string',
                        'privateEndpoint': {
                            'selfManagedLatticeResource': {
                                'resourceConfigurationIdentifier': 'string'
                            },
                            'managedVpcResource': {
                                'vpcIdentifier': 'string',
                                'subnetIds': [
                                    'string',
                                ],
                                'endpointIpAddressType': 'IPV4'|'IPV6',
                                'securityGroupIds': [
                                    'string',
                                ],
                                'tags': {
                                    'string': 'string'
                                },
                                'routingDomain': 'string'
                            }
                        }
                    },
                ],
                'allowedWorkloadConfiguration': {
                    'hostingEnvironments': [
                        {
                            'arn': 'string'
                        },
                    ],
                    'workloadIdentities': [
                        'string',
                    ]
                }
            }
        },
        kmsKeyArn='string',
        customTransformConfiguration={
            'lambda': {
                'arn': 'string'
            }
        },
        interceptorConfigurations=[
            {
                'interceptor': {
                    'lambda': {
                        'arn': 'string'
                    }
                },
                'interceptionPoints': [
                    'REQUEST'|'RESPONSE',
                ],
                'inputConfiguration': {
                    'passRequestHeaders': True|False,
                    'payloadFilter': {
                        'exclude': [
                            {
                                'field': 'RESPONSE_BODY'
                            },
                        ]
                    }
                }
            },
        ],
        policyEngineConfiguration={
            'arn': 'string',
            'mode': 'LOG_ONLY'|'ENFORCE'
        },
        exceptionLevel='DEBUG',
        wafConfiguration={
            'failureMode': 'FAIL_CLOSE'|'FAIL_OPEN'
        }
    )

Parameters:  
- **gatewayIdentifier** (*string*) –

  **\[REQUIRED\]**

  The identifier of the gateway to update.

- **name** (*string*) –

  **\[REQUIRED\]**

  The name of the gateway. This name must be the same as the one when the gateway was created.

- **description** (*string*) – The updated description for the gateway.

- **roleArn** (*string*) –

  **\[REQUIRED\]**

  The updated IAM role ARN that provides permissions for the gateway.

- **protocolType** (*string*) – The updated protocol type for the gateway.

- **protocolConfiguration** (*dict*) –

  The configuration for a gateway protocol. This structure defines how the gateway communicates with external services.

  ### Note

  This is a Tagged Union structure. Only one of the following top level keys can be set: `mcp`.

  - **mcp** *(dict) –*

    The configuration for the Model Context Protocol (MCP). This protocol enables communication between Amazon Bedrock Agent and external tools.

    - **supportedVersions** *(list) –*

      The supported versions of the Model Context Protocol. This field specifies which versions of the protocol the gateway can use.

      - *(string) –*

    - **instructions** *(string) –*

      The instructions for using the Model Context Protocol gateway. These instructions provide guidance on how to interact with the gateway.

    - **searchType** *(string) –*

      The search type for the Model Context Protocol gateway. This field specifies how the gateway handles search operations.

    - **sessionConfiguration** *(dict) –*

      The session configuration for the MCP gateway. This configuration controls session behavior, including session timeout settings.

      - **sessionTimeoutInSeconds** *(integer) –*

        The session timeout in seconds. After this timeout, the session expires and subsequent requests to this session will receive an error. The minimum value is 900 seconds (15 minutes), the maximum value is 28800 seconds (8 hours), and the default value is 3600 seconds (1 hour).

    - **streamingConfiguration** *(dict) –*

      The streaming configuration for the MCP gateway. This configuration controls whether response streaming is enabled for the gateway.

      - **enableResponseStreaming** *(boolean) –*

        Indicates whether response streaming is enabled for the gateway. When set to `true`, the gateway streams responses from targets back to the client.

- **authorizerType** (*string*) –

  **\[REQUIRED\]**

  The updated authorizer type for the gateway.

- **authorizerConfiguration** (*dict*) –

  The updated authorizer configuration for the gateway.

  ### Note

  This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.

  - **customJWTAuthorizer** *(dict) –*

    The inbound JWT-based authorization, specifying how incoming requests should be authenticated.

    - **discoveryUrl** *(string) –* **\[REQUIRED\]**

      This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.

    - **allowedAudience** *(list) –*

      Represents individual audience values that are validated in the incoming JWT token validation process.

      - *(string) –*

    - **allowedClients** *(list) –*

      Represents individual client IDs that are validated in the incoming JWT token validation process.

      - *(string) –*

    - **allowedScopes** *(list) –*

      An array of scopes that are allowed to access the token.

      - *(string) –*

    - **advertisedScopeMapping** *(dict) –*

      A map that associates each scope in `allowedScopes` with a corresponding advertised scope value. The advertised scope appears in OAuth protected resource metadata and `WWW-Authenticate` response headers. Use this parameter when the scope that clients request from your identity provider differs from the scope in the validated token. Each key is a scope from `allowedScopes` that the service uses for token validation. Each value is the corresponding scope that the service advertises to clients. Scopes without a mapping entry appear unchanged to clients.

      - *(string) –*

        - *(string) –*

    - **customClaims** *(list) –*

      An array of objects that define a custom claim validation name, value, and operation

      - *(dict) –*

        Defines the name of a custom claim field and rules for finding matches to authenticate its value.

        - **inboundTokenClaimName** *(string) –* **\[REQUIRED\]**

          The name of the custom claim field to check.

        - **inboundTokenClaimValueType** *(string) –* **\[REQUIRED\]**

          The data type of the claim value to check for.

          - Use `STRING` if you want to find an exact match to a string you define.

          - Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.

        - **authorizingClaimMatchValue** *(dict) –* **\[REQUIRED\]**

          Defines the value or values to match for and the relationship of the match.

          - **claimMatchValue** *(dict) –* **\[REQUIRED\]**

            The value or values to match for.

            ### Note

            This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.

            - **matchValueString** *(string) –*

              The string value to match for.

            - **matchValueStringList** *(list) –*

              An array of strings to check for a match.

              - *(string) –*

          - **claimMatchOperator** *(string) –* **\[REQUIRED\]**

            Defines the relationship between the claim field value and the value or values you’re matching for.

    - **privateEndpoint** *(dict) –*

      The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.

      ### Note

      This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.

      - **selfManagedLatticeResource** *(dict) –*

        Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.

        ### Note

        This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.

        - **resourceConfigurationIdentifier** *(string) –*

          The ARN or ID of the VPC Lattice resource configuration.

      - **managedVpcResource** *(dict) –*

        Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.

        - **vpcIdentifier** *(string) –* **\[REQUIRED\]**

          The ID of the VPC that contains your private resource.

        - **subnetIds** *(list) –* **\[REQUIRED\]**

          The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.

          - *(string) –*

        - **endpointIpAddressType** *(string) –* **\[REQUIRED\]**

          The IP address type for the resource configuration endpoint.

        - **securityGroupIds** *(list) –*

          The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.

          - *(string) –*

        - **tags** *(dict) –*

          Tags to apply to the managed VPC Lattice resource gateway.

          - *(string) –*

            - *(string) –*

        - **routingDomain** *(string) –*

          An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].

    - **privateEndpointOverrides** *(list) –*

      The private endpoint overrides for the custom JWT authorizer configuration.

      - *(dict) –*

        A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.

        - **domain** *(string) –* **\[REQUIRED\]**

          The domain to override with a private endpoint.

        - **privateEndpoint** *(dict) –* **\[REQUIRED\]**

          The private endpoint configuration for the specified domain.

          ### Note

          This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.

          - **selfManagedLatticeResource** *(dict) –*

            Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.

            ### Note

            This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.

            - **resourceConfigurationIdentifier** *(string) –*

              The ARN or ID of the VPC Lattice resource configuration.

          - **managedVpcResource** *(dict) –*

            Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.

            - **vpcIdentifier** *(string) –* **\[REQUIRED\]**

              The ID of the VPC that contains your private resource.

            - **subnetIds** *(list) –* **\[REQUIRED\]**

              The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.

              - *(string) –*

            - **endpointIpAddressType** *(string) –* **\[REQUIRED\]**

              The IP address type for the resource configuration endpoint.

            - **securityGroupIds** *(list) –*

              The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.

              - *(string) –*

            - **tags** *(dict) –*

              Tags to apply to the managed VPC Lattice resource gateway.

              - *(string) –*

                - *(string) –*

            - **routingDomain** *(string) –*

              An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].

    - **allowedWorkloadConfiguration** *(dict) –*

      The configuration that restricts which workloads in the request’s identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.

      - **hostingEnvironments** *(list) –*

        The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.

        - *(dict) –*

          A hosting environment whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.

          - **arn** *(string) –* **\[REQUIRED\]**

            The Amazon Resource Name (ARN) of the hosting environment.

      - **workloadIdentities** *(list) –*

        The list of workload identities that are allowed to invoke the target.

        - *(string) –*

- **kmsKeyArn** (*string*) – The updated ARN of the KMS key used to encrypt the gateway.

- **customTransformConfiguration** (*dict*) –

  The updated custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.

  - **lambda** *(dict) –*

    The Lambda configuration for custom transformations. This configuration defines how the gateway uses a Lambda function to transform data.

    - **arn** *(string) –*

      The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to transform data.

- **interceptorConfigurations** (*list*) –

  The updated interceptor configurations for the gateway.

  - *(dict) –*

    The configuration for an interceptor on a gateway. This structure defines settings for an interceptor that will be invoked during the invocation of the gateway.

    - **interceptor** *(dict) –* **\[REQUIRED\]**

      The infrastructure settings of an interceptor configuration. This structure defines how the interceptor can be invoked.

      ### Note

      This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`.

      - **lambda** *(dict) –*

        The details of the lambda function used for the interceptor.

        - **arn** *(string) –* **\[REQUIRED\]**

          The arn of the lambda function to be invoked for the interceptor.

    - **interceptionPoints** *(list) –* **\[REQUIRED\]**

      The supported points of interception. This field specifies which points during the gateway invocation to invoke the interceptor

      - *(string) –*

    - **inputConfiguration** *(dict) –*

      The configuration for the input of the interceptor. This field specifies how the input to the interceptor is constructed

      - **passRequestHeaders** *(boolean) –* **\[REQUIRED\]**

        Indicates whether to pass request headers as input into the interceptor. When set to true, request headers will be passed.

      - **payloadFilter** *(dict) –*

        The filter that determines which parts of the request or response payload are passed as input to the interceptor.

        - **exclude** *(list) –* **\[REQUIRED\]**

          The list of selectors that identify payload fields to exclude from the interceptor input.

          - *(dict) –*

            A selector that identifies a payload field to exclude from the interceptor input.

            ### Note

            This is a Tagged Union structure. Only one of the following top level keys can be set: `field`.

            - **field** *(string) –*

              The field to exclude from the interceptor input.

- **policyEngineConfiguration** (*dict*) –

  The updated policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.

  - **arn** *(string) –* **\[REQUIRED\]**

    The ARN of the policy engine. The policy engine contains Cedar or Dogwood policies that define fine-grained authorization rules specifying who can perform what actions on which resources as agents interact through the gateway.

  - **mode** *(string) –* **\[REQUIRED\]**

    The enforcement mode for the policy engine. Valid values include:

    - `LOG_ONLY` - The policy engine evaluates each action against your policies and adds traces on whether tool calls would be allowed or denied, but does not enforce the decision. Use this mode to test and validate policies before enabling enforcement.

    - `ENFORCE` - The policy engine evaluates actions against your policies and enforces decisions by allowing or denying agent operations. Test and validate policies in `LOG_ONLY` mode before enabling enforcement to avoid unintended denials or adversely affecting production traffic.

- **exceptionLevel** (*string*) –

  The level of detail in error messages returned when invoking the gateway.

  - If the value is `DEBUG`, granular exception messages are returned to help a user debug the gateway.

  - If the value is omitted, a generic error message is returned to the end user.

- **wafConfiguration** (*dict*) –

  The updated Amazon Web Services WAF configuration for the gateway.

  - **failureMode** *(string) –*

    The failure mode that determines how the gateway handles requests when Amazon Web Services WAF is unreachable or times out. Valid values include:

    - `FAIL_CLOSE` - The gateway blocks requests when Amazon Web Services WAF cannot be evaluated.

    - `FAIL_OPEN` - The gateway allows requests when Amazon Web Services WAF cannot be evaluated.

Return type:  
dict

Returns:  
### Response Syntax

    {
        'gatewayArn': 'string',
        'gatewayId': 'string',
        'gatewayUrl': 'string',
        'createdAt': datetime(2015, 1, 1),
        'updatedAt': datetime(2015, 1, 1),
        'status': 'CREATING'|'UPDATING'|'UPDATE_UNSUCCESSFUL'|'DELETING'|'READY'|'FAILED',
        'statusReasons': [
            'string',
        ],
        'name': 'string',
        'description': 'string',
        'roleArn': 'string',
        'protocolType': 'MCP',
        'protocolConfiguration': {
            'mcp': {
                'supportedVersions': [
                    'string',
                ],
                'instructions': 'string',
                'searchType': 'SEMANTIC',
                'sessionConfiguration': {
                    'sessionTimeoutInSeconds': 123
                },
                'streamingConfiguration': {
                    'enableResponseStreaming': True|False
                }
            }
        },
        'authorizerType': 'CUSTOM_JWT'|'AWS_IAM'|'NONE'|'AUTHENTICATE_ONLY',
        'authorizerConfiguration': {
            'customJWTAuthorizer': {
                'discoveryUrl': 'string',
                'allowedAudience': [
                    'string',
                ],
                'allowedClients': [
                    'string',
                ],
                'allowedScopes': [
                    'string',
                ],
                'advertisedScopeMapping': {
                    'string': 'string'
                },
                'customClaims': [
                    {
                        'inboundTokenClaimName': 'string',
                        'inboundTokenClaimValueType': 'STRING'|'STRING_ARRAY',
                        'authorizingClaimMatchValue': {
                            'claimMatchValue': {
                                'matchValueString': 'string',
                                'matchValueStringList': [
                                    'string',
                                ]
                            },
                            'claimMatchOperator': 'EQUALS'|'CONTAINS'|'CONTAINS_ANY'
                        }
                    },
                ],
                'privateEndpoint': {
                    'selfManagedLatticeResource': {
                        'resourceConfigurationIdentifier': 'string'
                    },
                    'managedVpcResource': {
                        'vpcIdentifier': 'string',
                        'subnetIds': [
                            'string',
                        ],
                        'endpointIpAddressType': 'IPV4'|'IPV6',
                        'securityGroupIds': [
                            'string',
                        ],
                        'tags': {
                            'string': 'string'
                        },
                        'routingDomain': 'string'
                    }
                },
                'privateEndpointOverrides': [
                    {
                        'domain': 'string',
                        'privateEndpoint': {
                            'selfManagedLatticeResource': {
                                'resourceConfigurationIdentifier': 'string'
                            },
                            'managedVpcResource': {
                                'vpcIdentifier': 'string',
                                'subnetIds': [
                                    'string',
                                ],
                                'endpointIpAddressType': 'IPV4'|'IPV6',
                                'securityGroupIds': [
                                    'string',
                                ],
                                'tags': {
                                    'string': 'string'
                                },
                                'routingDomain': 'string'
                            }
                        }
                    },
                ],
                'allowedWorkloadConfiguration': {
                    'hostingEnvironments': [
                        {
                            'arn': 'string'
                        },
                    ],
                    'workloadIdentities': [
                        'string',
                    ]
                }
            }
        },
        'kmsKeyArn': 'string',
        'customTransformConfiguration': {
            'lambda': {
                'arn': 'string'
            }
        },
        'interceptorConfigurations': [
            {
                'interceptor': {
                    'lambda': {
                        'arn': 'string'
                    }
                },
                'interceptionPoints': [
                    'REQUEST'|'RESPONSE',
                ],
                'inputConfiguration': {
                    'passRequestHeaders': True|False,
                    'payloadFilter': {
                        'exclude': [
                            {
                                'field': 'RESPONSE_BODY'
                            },
                        ]
                    }
                }
            },
        ],
        'policyEngineConfiguration': {
            'arn': 'string',
            'mode': 'LOG_ONLY'|'ENFORCE'
        },
        'workloadIdentityDetails': {
            'workloadIdentityArn': 'string'
        },
        'exceptionLevel': 'DEBUG',
        'webAclArn': 'string',
        'wafConfiguration': {
            'failureMode': 'FAIL_CLOSE'|'FAIL_OPEN'
        }
    }

### Response Structure

- *(dict) –*

  - **gatewayArn** *(string) –*

    The Amazon Resource Name (ARN) of the updated gateway.

  - **gatewayId** *(string) –*

    The unique identifier of the updated gateway.

  - **gatewayUrl** *(string) –*

    An endpoint for invoking the updated gateway.

  - **createdAt** *(datetime) –*

    The timestamp when the gateway was created.

  - **updatedAt** *(datetime) –*

    The timestamp when the gateway was last updated.

  - **status** *(string) –*

    The current status of the updated gateway.

  - **statusReasons** *(list) –*

    The reasons for the current status of the updated gateway.

    - *(string) –*

  - **name** *(string) –*

    The name of the gateway.

  - **description** *(string) –*

    The updated description of the gateway.

  - **roleArn** *(string) –*

    The updated IAM role ARN that provides permissions for the gateway.

  - **protocolType** *(string) –*

    The updated protocol type for the gateway.

  - **protocolConfiguration** *(dict) –*

    The configuration for a gateway protocol. This structure defines how the gateway communicates with external services.

    ### Note

    This is a Tagged Union structure. Only one of the following top level keys will be set: `mcp`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

        'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

    - **mcp** *(dict) –*

      The configuration for the Model Context Protocol (MCP). This protocol enables communication between Amazon Bedrock Agent and external tools.

      - **supportedVersions** *(list) –*

        The supported versions of the Model Context Protocol. This field specifies which versions of the protocol the gateway can use.

        - *(string) –*

      - **instructions** *(string) –*

        The instructions for using the Model Context Protocol gateway. These instructions provide guidance on how to interact with the gateway.

      - **searchType** *(string) –*

        The search type for the Model Context Protocol gateway. This field specifies how the gateway handles search operations.

      - **sessionConfiguration** *(dict) –*

        The session configuration for the MCP gateway. This configuration controls session behavior, including session timeout settings.

        - **sessionTimeoutInSeconds** *(integer) –*

          The session timeout in seconds. After this timeout, the session expires and subsequent requests to this session will receive an error. The minimum value is 900 seconds (15 minutes), the maximum value is 28800 seconds (8 hours), and the default value is 3600 seconds (1 hour).

      - **streamingConfiguration** *(dict) –*

        The streaming configuration for the MCP gateway. This configuration controls whether response streaming is enabled for the gateway.

        - **enableResponseStreaming** *(boolean) –*

          Indicates whether response streaming is enabled for the gateway. When set to `true`, the gateway streams responses from targets back to the client.

  - **authorizerType** *(string) –*

    The updated authorizer type for the gateway.

  - **authorizerConfiguration** *(dict) –*

    The updated authorizer configuration for the gateway.

    ### Note

    This is a Tagged Union structure. Only one of the following top level keys will be set: `customJWTAuthorizer`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

        'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

    - **customJWTAuthorizer** *(dict) –*

      The inbound JWT-based authorization, specifying how incoming requests should be authenticated.

      - **discoveryUrl** *(string) –*

        This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.

      - **allowedAudience** *(list) –*

        Represents individual audience values that are validated in the incoming JWT token validation process.

        - *(string) –*

      - **allowedClients** *(list) –*

        Represents individual client IDs that are validated in the incoming JWT token validation process.

        - *(string) –*

      - **allowedScopes** *(list) –*

        An array of scopes that are allowed to access the token.

        - *(string) –*

      - **advertisedScopeMapping** *(dict) –*

        A map that associates each scope in `allowedScopes` with a corresponding advertised scope value. The advertised scope appears in OAuth protected resource metadata and `WWW-Authenticate` response headers. Use this parameter when the scope that clients request from your identity provider differs from the scope in the validated token. Each key is a scope from `allowedScopes` that the service uses for token validation. Each value is the corresponding scope that the service advertises to clients. Scopes without a mapping entry appear unchanged to clients.

        - *(string) –*

          - *(string) –*

      - **customClaims** *(list) –*

        An array of objects that define a custom claim validation name, value, and operation

        - *(dict) –*

          Defines the name of a custom claim field and rules for finding matches to authenticate its value.

          - **inboundTokenClaimName** *(string) –*

            The name of the custom claim field to check.

          - **inboundTokenClaimValueType** *(string) –*

            The data type of the claim value to check for.

            - Use `STRING` if you want to find an exact match to a string you define.

            - Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.

          - **authorizingClaimMatchValue** *(dict) –*

            Defines the value or values to match for and the relationship of the match.

            - **claimMatchValue** *(dict) –*

              The value or values to match for.

              ### Note

              This is a Tagged Union structure. Only one of the following top level keys will be set: `matchValueString`, `matchValueStringList`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

                  'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

              - **matchValueString** *(string) –*

                The string value to match for.

              - **matchValueStringList** *(list) –*

                An array of strings to check for a match.

                - *(string) –*

            - **claimMatchOperator** *(string) –*

              Defines the relationship between the claim field value and the value or values you’re matching for.

      - **privateEndpoint** *(dict) –*

        The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.

        ### Note

        This is a Tagged Union structure. Only one of the following top level keys will be set: `selfManagedLatticeResource`, `managedVpcResource`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

            'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

        - **selfManagedLatticeResource** *(dict) –*

          Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.

          ### Note

          This is a Tagged Union structure. Only one of the following top level keys will be set: `resourceConfigurationIdentifier`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

              'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

          - **resourceConfigurationIdentifier** *(string) –*

            The ARN or ID of the VPC Lattice resource configuration.

        - **managedVpcResource** *(dict) –*

          Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.

          - **vpcIdentifier** *(string) –*

            The ID of the VPC that contains your private resource.

          - **subnetIds** *(list) –*

            The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.

            - *(string) –*

          - **endpointIpAddressType** *(string) –*

            The IP address type for the resource configuration endpoint.

          - **securityGroupIds** *(list) –*

            The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.

            - *(string) –*

          - **tags** *(dict) –*

            Tags to apply to the managed VPC Lattice resource gateway.

            - *(string) –*

              - *(string) –*

          - **routingDomain** *(string) –*

            An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].

      - **privateEndpointOverrides** *(list) –*

        The private endpoint overrides for the custom JWT authorizer configuration.

        - *(dict) –*

          A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.

          - **domain** *(string) –*

            The domain to override with a private endpoint.

          - **privateEndpoint** *(dict) –*

            The private endpoint configuration for the specified domain.

            ### Note

            This is a Tagged Union structure. Only one of the following top level keys will be set: `selfManagedLatticeResource`, `managedVpcResource`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

                'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

            - **selfManagedLatticeResource** *(dict) –*

              Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.

              ### Note

              This is a Tagged Union structure. Only one of the following top level keys will be set: `resourceConfigurationIdentifier`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

                  'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

              - **resourceConfigurationIdentifier** *(string) –*

                The ARN or ID of the VPC Lattice resource configuration.

            - **managedVpcResource** *(dict) –*

              Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.

              - **vpcIdentifier** *(string) –*

                The ID of the VPC that contains your private resource.

              - **subnetIds** *(list) –*

                The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.

                - *(string) –*

              - **endpointIpAddressType** *(string) –*

                The IP address type for the resource configuration endpoint.

              - **securityGroupIds** *(list) –*

                The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.

                - *(string) –*

              - **tags** *(dict) –*

                Tags to apply to the managed VPC Lattice resource gateway.

                - *(string) –*

                  - *(string) –*

              - **routingDomain** *(string) –*

                An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].

      - **allowedWorkloadConfiguration** *(dict) –*

        The configuration that restricts which workloads in the request’s identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.

        - **hostingEnvironments** *(list) –*

          The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.

          - *(dict) –*

            A hosting environment whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.

            - **arn** *(string) –*

              The Amazon Resource Name (ARN) of the hosting environment.

        - **workloadIdentities** *(list) –*

          The list of workload identities that are allowed to invoke the target.

          - *(string) –*

  - **kmsKeyArn** *(string) –*

    The updated ARN of the KMS key used to encrypt the gateway.

  - **customTransformConfiguration** *(dict) –*

    The custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.

    - **lambda** *(dict) –*

      The Lambda configuration for custom transformations. This configuration defines how the gateway uses a Lambda function to transform data.

      - **arn** *(string) –*

        The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to transform data.

  - **interceptorConfigurations** *(list) –*

    The updated interceptor configurations for the gateway.

    - *(dict) –*

      The configuration for an interceptor on a gateway. This structure defines settings for an interceptor that will be invoked during the invocation of the gateway.

      - **interceptor** *(dict) –*

        The infrastructure settings of an interceptor configuration. This structure defines how the interceptor can be invoked.

        ### Note

        This is a Tagged Union structure. Only one of the following top level keys will be set: `lambda`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

            'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

        - **lambda** *(dict) –*

          The details of the lambda function used for the interceptor.

          - **arn** *(string) –*

            The arn of the lambda function to be invoked for the interceptor.

      - **interceptionPoints** *(list) –*

        The supported points of interception. This field specifies which points during the gateway invocation to invoke the interceptor

        - *(string) –*

      - **inputConfiguration** *(dict) –*

        The configuration for the input of the interceptor. This field specifies how the input to the interceptor is constructed

        - **passRequestHeaders** *(boolean) –*

          Indicates whether to pass request headers as input into the interceptor. When set to true, request headers will be passed.

        - **payloadFilter** *(dict) –*

          The filter that determines which parts of the request or response payload are passed as input to the interceptor.

          - **exclude** *(list) –*

            The list of selectors that identify payload fields to exclude from the interceptor input.

            - *(dict) –*

              A selector that identifies a payload field to exclude from the interceptor input.

              ### Note

              This is a Tagged Union structure. Only one of the following top level keys will be set: `field`. If a client receives an unknown member it will set `SDK_UNKNOWN_MEMBER` as the top level key, which maps to the name or tag of the unknown member. The structure of `SDK_UNKNOWN_MEMBER` is as follows:

                  'SDK_UNKNOWN_MEMBER': {'name': 'UnknownMemberName'}

              - **field** *(string) –*

                The field to exclude from the interceptor input.

  - **policyEngineConfiguration** *(dict) –*

    The updated policy engine configuration for the gateway.

    - **arn** *(string) –*

      The ARN of the policy engine. The policy engine contains Cedar or Dogwood policies that define fine-grained authorization rules specifying who can perform what actions on which resources as agents interact through the gateway.

    - **mode** *(string) –*

      The enforcement mode for the policy engine. Valid values include:

      - `LOG_ONLY` - The policy engine evaluates each action against your policies and adds traces on whether tool calls would be allowed or denied, but does not enforce the decision. Use this mode to test and validate policies before enabling enforcement.

      - `ENFORCE` - The policy engine evaluates actions against your policies and enforces decisions by allowing or denying agent operations. Test and validate policies in `LOG_ONLY` mode before enabling enforcement to avoid unintended denials or adversely affecting production traffic.

  - **workloadIdentityDetails** *(dict) –*

    The workload identity details for the updated gateway.

    - **workloadIdentityArn** *(string) –*

      The ARN associated with the workload identity.

  - **exceptionLevel** *(string) –*

    The level of detail in error messages returned when invoking the gateway.

    - If the value is `DEBUG`, granular exception messages are returned to help a user debug the gateway.

    - If the value is omitted, a generic error message is returned to the end user.

  - **webAclArn** *(string) –*

    The Amazon Resource Name (ARN) of the Amazon Web Services WAF web ACL associated with the gateway.

  - **wafConfiguration** *(dict) –*

    The Amazon Web Services WAF configuration for the gateway.

    - **failureMode** *(string) –*

      The failure mode that determines how the gateway handles requests when Amazon Web Services WAF is unreachable or times out. Valid values include:

      - `FAIL_CLOSE` - The gateway blocks requests when Amazon Web Services WAF cannot be evaluated.

      - `FAIL_OPEN` - The gateway allows requests when Amazon Web Services WAF cannot be evaluated.

### Exceptions

- `BedrockAgentCoreControl.Client.exceptions.ServiceQuotaExceededException`

- `BedrockAgentCoreControl.Client.exceptions.ConflictException`

- `BedrockAgentCoreControl.Client.exceptions.ValidationException`

- `BedrockAgentCoreControl.Client.exceptions.AccessDeniedException`

- `BedrockAgentCoreControl.Client.exceptions.ThrottlingException`

- `BedrockAgentCoreControl.Client.exceptions.ResourceNotFoundException`

- `BedrockAgentCoreControl.Client.exceptions.InternalServerException`
