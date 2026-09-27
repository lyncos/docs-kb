---
title: Delegation
description: Delegation is one of the use cases supported by OAuth 2.0 token exchange in PingOne. Learn more about how it works and the supported use cases in Configuring OAuth 2.0 token exchange.
product: Amazon Bedrock AgentCore
section: References / docs.pingidentity.com
source_url: https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-pingidentity-com
- reference
- related
referenced_by:
- identity-idp-pingidentity.md
conversion: native-md
---

---
title: Delegation
description: The delegation use case for token exchange allows an application in PingOne to act on behalf of a user.
component: pingone
page_id: pingone:use_cases:p1_oauth_2_token_exchange_delegation
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-25T00:00:00Z
section_ids:
  example-scenario: Example scenario
  what-youll-do: What you'll do
  example-tasks: Example tasks
  p1-delegation-dob: Adding DoB as a custom resource
  steps: Steps
  p1-add-goodies: Adding the Goodies Token Exchange application
  steps-2: Steps
  p1-delegation-goodies: Adding Goodies as a custom resource
  steps-3: Steps
  adding-yankee-coffee-as-an-application: Adding Yankee Coffee as an application
  steps-4: Steps
  required-configurations: Required configurations
  p1-delegation-runtime: Runtime process overview
---

# Delegation

Delegation is one of the use cases supported by OAuth 2.0 token exchange in PingOne. Learn more about how it works and the supported use cases in [Configuring OAuth 2.0 token exchange](p1_oauth_2_token_exchange.html).

Use delegation for token exchange to enable an application (client) to act on the user's behalf while maintaining separate identities for the user (*subject*) and the application (*actor*), such as accessing a protected resource.

In general, your organization's PingOne administrator, application, and resource server teams are responsible for collaborating to determine which attributes PingOne should include in the access tokens to represent delegation. The [OAuth 2.0 token exchange specification](https://datatracker.ietf.org/doc/html/rfc8693#section-a.2) provides a delegation token exchange example.

In delegation, the application has two tokens:

* A subject token represents the authenticated user and is obtained with the user's authorization.

* An actor token represents the identity acting on behalf of the user and is obtained for the application itself or a user it represents. The actor token is required only for delegation flows.

The application exchanges both tokens for a new token to access the protected resource. The `act` (actor) claim in the new token informs the resource server that the application using the token isn't the actual user but is acting on the user's behalf.

## Example scenario

In this scenario, users order coffee using an application, Yankee Coffee, and apply their reward points to redeem free coffee. To complete an order:

1. The application, Yankee Coffee, must retrieve the reward points balance of the user from a resource server, Goodies.

2. Goodies must verify whether the user's birthday bonus reward has been claimed, but Goodies doesn't have this information and must retrieve it from another resource server, DoB.

3. Yankee Coffee must include the identity (actor) that can act on behalf of the user to Goodies so that Goodies can include the delegation information when it requests the birthday bonus reward from DoB.

## What you'll do

To set up the example scenario for delegation, you'll add:

* Yankee Coffee application: The user interacts with this application to initiate the flow.

* Goodies custom resource: This resource has the information needed by the Yankee Coffee application.

* Goodies Token Exchange application: This application processes the token exchange request.

* DoB custom resource: This resource has the additional information the Yankee Coffee application can act on behalf of the user to retrieve.

## Example tasks

### Adding DoB as a custom resource

As a PingOne administrator, add a custom resource in PingOne for the DoB resource server.

#### Steps

1. In the PingOne admin console, go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `DoB`.

   2. For **Audience**, enter the audience for resource in the format of `https://api.example.com/d`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Click the **Gear** icon ([icon: gear, set=fa]) next to the **`sub`** attribute to open the **Advanced Expressions** modal.

   2. In the modal, enter the following and click **Save**:

      ```json
      #root.context.requestData.subjectToken.sub
      ```

      This expression populates the `sub` claim value in the issued token with the `sub` claim value from the subject token.

   3. Click **[icon: plus, set=fa]Add** to add another attribute.

   4. In the **Attribute** field, enter `act` and then click [icon: gear, set=fa]next to the attribute to open the **Advanced Expressions** modal.

   5. In the modal, enter the following and click **Save**:

      ```json
      (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?#root.context.requestData.subjectToken.may_act:null)
      ```

   6. Select the checkbox to make the `act` attribute required.

      This expression checks whether the token request uses the client credentials grant type.

      * If the token request uses the client credentials grant type, it populates `act` with a hard-coded value of `noActor` to signal to DoB that no delegation is involved.

      * If the token request doesn't use the client credentials grant type, it assumes the token request uses the token exchange grant type and checks whether the `may_act` claim value in the subject token matches the `client_id` in the actor token.

        * If the value matches, it populates `act` with the `may_act` claim value from the subject token.

        * If the value doesn't match, it sets `act` as `null`, and the token exchange token request fails because the `act` claim is marked as required.

   7. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `d.read`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding the Goodies Token Exchange application

Create an application to handle the token exchange requests and obtain access tokens from PingOne to send API requests to DoB. The Goodies Token Exchange application must use:

* The token exchange grant type to obtain access tokens from PingOne to send API requests to DoB to retrieve birthday reward information

* The application credentials in its token request because only applications can send token requests to PingOne, and custom resources can't.

The resulting access token contains:

* The identity of the actor acting on behalf of the user as the subject (`sub`). The subject is taken taken directly from the subject of the access token from Yankee Coffee.

* An `act` claim indicating the identity acting on behalf of the user. In this scenario, the identity is the Goodies Token Exchange application.

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `Goodies Token Exchange`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click the **Pencil** icon ([icon: pencil, set=fa]).

   2. For **Grant Type**, select **Client Credentials** and **Token Exchange**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding DoB as a custom resource](#p1-delegation-dob).

   3. Click **Save**.

5. On the **Overview** tab, click the **Copy to clipboard** icon ([icon: copy, set=fa]) for **Client ID**. You'll need the client ID to configure the subject for the `may_act` attribute in the Goodies custom resource.

### Adding Goodies as a custom resource

Add a custom resource in PingOne for the Goodies resource server.

#### Steps

1. Go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `Goodies`.

   2. For **Audience**. enter the audience for resource in the format of `https://api.example.com/g`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Leave **`sub`** mapped to **User ID** (default).

   2. Click **[icon: plus, set=fa]Add**.

   3. For **Attribute**, enter `may_act` and then click [icon: gear, set=fa]next to the attribute to open the **Advanced Expressions** modal.

   4. In the modal, enter the following, using the client ID that you copied in step 6 of [Adding the Goodies Token Exchange application](#p1-add-goodies):

      ```
      {"sub": "<client ID of the Goodies Token Exchange application>"}
      ```

   5. Click **Save**.

   6. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `g.crud`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding Yankee Coffee as an application

Add an end-user application in PingOne for Yankee Coffee and and assign the scope from the Goodies custom resource. Yankee Coffee must use the authorization code grant type to obtain access tokens from PingOne to send API requests to the Goodies custom resource to retrieve the user's reward points balance. The access tokens contain:

* The identity that can act on behalf of the user as the subject (`sub`). The subject is the user who authenticates and authorizes the application request from Yankee Coffee.

* A `may_act` claim indicating the identity that can act on behalf of the user. In this scenario, the identity is the Goodies Token Exchange application.

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `Yankee Coffee`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click [icon: pencil, set=fa].

   2. For **Grant Type**, select **Authorization Code**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding Goodies as a custom resource](#p1-delegation-goodies).

   3. Click **Save**.

5. Provide the application credentials and custom resource credentials to your organization's developers for the applications and custom resources, respectively.

## Required configurations

The following table lists the required configurations for the applications and custom resources and includes example client IDs that correspond to the [runtime process overview](#p1-delegation-runtime):

| Applications                                                                                                                                              | Custom resources                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yankee Coffee- Client ID: f6c78a5b

- Grant type: Authorization code

- Scopes:

  * **openid** (default)

  * `g.crud`                                   | Goodies- Client ID: 75d8cea3

- Audience: https\://api.example.com/g

- Scopes: `g.crud`

- Attributes:

  * `sub`: **User ID** (default)

  * `may act`: `{"sub": "45f60a71"}`                                                                                                                                                                                                                                 |
| Goodies Token Exchange- Client ID: 45f60a71

- Grant type:

  * Client credentials

  * Token exchange

- Scopes:

  * **openid** (default)

  * `d.read` | DoB- Client ID: 81ca41a2

- Audience: https\://api.example.com/d

- Scopes: `d.read`

- Attributes:

  * `sub`: `#root.context.requestData.subjectToken.sub`

  * `act`: `(#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?#root.context.requestData.subjectToken.may_act:null)` |

## Runtime process overview

The following diagram shows a high-level overview of the example delegation flow:

![A diagram of the example delegation token exchange flow.](_images/p1-token-exchange-delegation-diagram.png)

1. Yankee Coffee sends an authorization request to PingOne with `scope=openid+g.crud`, `client_id=f6c78a5b`, and other parameters.

2. PingOne authenticates the user, obtains the authorization from the user, and returns an authorization code to Yankee Coffee.

3. Yankee Coffee sends a token request using the authorization code grant type to PingOne.

4. PingOne returns an access token to Yankee Coffee.

   The payload is decoded as follows:

   ```json
   {
     "client_id": "f6c78a5b-9d39-4cd7-b94e-81dad33c8773", # the client ID of Yankee Coffee
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "54ffa426-1410-4383-8ec5-344a7b1b948e",
     "iat": 1770574186,
     "exp": 1770577786,
     "aud": [
       "https://api.example.com/g" # the audience is Goodies
     ],
     "scope": "g.crud", # the scope of this access token
     "sub": "user@example.net", # the user using Yankee Coffee
     "sid": "86635114-c633-4c13-b1eb-4a8a3f0e7dcd",
     "auth_time": 1770573761,
     "acr": "1Single_Factor",
     "may_act": {                                    # the identity that can act on behalf of the user
       "sub": "45f60a71-df8c-42d6-9410-f64f0454874d" # the client ID of Goodies Token Exchange App
     },
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
     "p1.userId": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d"
   }
   ```

5. Yankee Coffee sends an API request to Goodies. For authorization, Yankee Coffee includes the access token (from step 4) as the `Authorization` HTTP request header value in the API request.

6. Goodies evaluates the access token and determines that:

   * The issuer of the access token is PingOne.

   * The application requesting the token is Yankee Coffee.

   * The audience of the access token includes itself, Goodies.

7. Goodies sends an introspection request to PingOne to validate the access token.

   For client identification and authentication, Goodies uses the client ID and secret defined in PingOne for the custom resource (`client_id=75d8cea3`).

8. Goodies sends a token request using the client credentials grant type to PingOne.

   For client identification and authentication, Goodies uses the client ID and secret defined in PingOne for the Goodies Token Exchange application (`client_id=45f60a71`).

9. PingOne returns an access token to Goodies.

   The payload is decoded as follows:

   ```json
   {
     "client_id": "45f60a71-df8c-42d6-9410-f64f0454874d", # the client ID of Goodies Token Exchange App
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "47d54766-7b9a-4485-96d9-6c09d410b943",
     "iat": 1770574217,
     "exp": 1770577817,
     "aud": [
       "https://api.example.com/d" # the audience is DoB
     ],
     "scope": "d.read",
     "act": "noActor", # a value of `noActor' indicates (to DoB) that no delegation is involved
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
     "p1.rid": "47d54766-7b9a-4485-96d9-6c09d410b943"
   }
   ```

10. Goodies sends a token request using the token exchange grant type to PingOne.

    * For client identification and authentication, Goodies uses the client ID and secret defined in PingOne for the Goodies Token Exchange application (`client_id=45f60a71`).

    * Goodies includes the following parameters in the token request:

      * `scope=d.read`

      * `subject_token=<access token from step 5>`

      * `subject_token_type=urn:ietf:params:oauth:token-type:access_token`

      * `actor_token=<access token from step 9>`

      * `actor_token_type=urn:ietf:params:oauth:token-type:access_token`

      * `requested_token_type=urn:ietf:params:oauth:token-type:access_token`

11. PingOne validates the subject token for the following:

    * The subject token and the actor token are valid JWTs.

    * The issuer of the subject token and the actor token matches the issuer of the current PingOne environment.

    * The associated PingOne user session is valid.

12. PingOne mints an access token based on the attribute mappings defined in PingOne for DoB.

13. PingOne returns a token response containing an access token to Goodies.

    The following is the token response:

    ```json
    {
        "access_token": "eyJ…", # the access token as a result of the token exchange token request
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "d.read",
        "issued_token_type": "urn:ietf:params:oauth:token-type:access_token"
    }
    ```

    The access token is decoded as follows:

    ```json
    {
      "client_id": "45f60a71-df8c-42d6-9410-f64f0454874d", # the client ID of Goodies Token Exchange App
      "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
      "jti": "337a5736-bea4-44dd-9692-dc5f696ef710",
      "iat": 1770574249,
      "exp": 1770577849,
      "aud": [
        "https://api.example.com/d" # the audience is DoB
      ],
      "scope": "d.read",
      "sub": "user@example.net", # the user using Yankee Coffee
      "sid": "86635114-c633-4c13-b1eb-4a8a3f0e7dcd",
      "auth_time": 1770573761,
      "acr": "1Single_Factor",
      "act": {                                        # the identity acting on behalf of the user
        "sub": "45f60a71-df8c-42d6-9410-f64f0454874d" # the client ID of Goodies Token Exchange App
      },
      "env": "6991589d-87eb-47f4-9131-284cebe106b3",
      "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
      "p1.userId": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d"
    }
    ```

14. Goodies sends an API request to DoB. For authorization, Goodies includes the access token (from step 13) as the `Authorization` HTTP request header value in the API request.

15. DoB evaluates the access token and determines that:

    * The issuer of the access token is PingOne.

    * The application requesting the token is the Goodies Token Exchange application.

    * The audience of the access token includes itself, DoB.

16. DoB sends an introspection request to PingOne to validate the access token.

17. DoB returns an API response to Goodies. At this point, Goodies as a resource server can fulfill the API request from Yankee Coffee (in step 5).

18. Goodies returns an API response to Yankee Coffee.
