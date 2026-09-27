# Amazon Bedrock AgentCore Data Plane API Reference

-----
*****Copyright &copy; Amazon Web Services, Inc. and/or its affiliates. All rights reserved.*****

-----
Amazon's trademarks and trade dress may not be used in
connection with any product or service that is not Amazon's,
in any manner that is likely to cause confusion among customers,
or in any manner that disparages or discredits Amazon. All other
trademarks not owned by Amazon are the property of their respective
owners, who may or may not be affiliated with, connected to, or
sponsored by Amazon.

-----
## Contents
+ [Welcome](#Welcome)
+ [Actions](#API_Operations)
   + [BatchCreateMemoryRecords](#API_BatchCreateMemoryRecords)
   + [BatchDeleteMemoryRecords](#API_BatchDeleteMemoryRecords)
   + [BatchUpdateMemoryRecords](#API_BatchUpdateMemoryRecords)
   + [CompleteResourceTokenAuth](#API_CompleteResourceTokenAuth)
   + [CreateABTest](#API_CreateABTest)
   + [CreateEvent](#API_CreateEvent)
   + [CreatePaymentInstrument](#API_CreatePaymentInstrument)
   + [CreatePaymentSession](#API_CreatePaymentSession)
   + [DeleteABTest](#API_DeleteABTest)
   + [DeleteBatchEvaluation](#API_DeleteBatchEvaluation)
   + [DeleteCapacityProviderSession](#API_DeleteCapacityProviderSession)
   + [DeleteEvent](#API_DeleteEvent)
   + [DeleteMemoryRecord](#API_DeleteMemoryRecord)
   + [DeletePaymentInstrument](#API_DeletePaymentInstrument)
   + [DeletePaymentSession](#API_DeletePaymentSession)
   + [DeleteRecommendation](#API_DeleteRecommendation)
   + [Evaluate](#API_Evaluate)
   + [GetABTest](#API_GetABTest)
   + [GetAgentCard](#API_GetAgentCard)
   + [GetBatchEvaluation](#API_GetBatchEvaluation)
   + [GetBrowserSession](#API_GetBrowserSession)
   + [GetCodeInterpreterSession](#API_GetCodeInterpreterSession)
   + [GetEvent](#API_GetEvent)
   + [GetMemoryRecord](#API_GetMemoryRecord)
   + [GetPaymentInstrument](#API_GetPaymentInstrument)
   + [GetPaymentInstrumentBalance](#API_GetPaymentInstrumentBalance)
   + [GetPaymentSession](#API_GetPaymentSession)
   + [GetRecommendation](#API_GetRecommendation)
   + [GetResourceApiKey](#API_GetResourceApiKey)
   + [GetResourceOauth2Token](#API_GetResourceOauth2Token)
   + [GetResourcePaymentToken](#API_GetResourcePaymentToken)
   + [GetWorkloadAccessToken](#API_GetWorkloadAccessToken)
   + [GetWorkloadAccessTokenForJWT](#API_GetWorkloadAccessTokenForJWT)
   + [GetWorkloadAccessTokenForUserId](#API_GetWorkloadAccessTokenForUserId)
   + [IngestData](#API_IngestData)
   + [InvokeAgentRuntime](#API_InvokeAgentRuntime)
   + [InvokeAgentRuntimeCommand](#API_InvokeAgentRuntimeCommand)
   + [InvokeBrowser](#API_InvokeBrowser)
   + [InvokeCodeInterpreter](#API_InvokeCodeInterpreter)
   + [InvokeHarness](#API_InvokeHarness)
   + [ListABTests](#API_ListABTests)
   + [ListActors](#API_ListActors)
   + [ListBatchEvaluations](#API_ListBatchEvaluations)
   + [ListBrowserSessions](#API_ListBrowserSessions)
   + [ListCodeInterpreterSessions](#API_ListCodeInterpreterSessions)
   + [ListEvents](#API_ListEvents)
   + [ListMemoryExtractionJobs](#API_ListMemoryExtractionJobs)
   + [ListMemoryRecords](#API_ListMemoryRecords)
   + [ListPaymentInstruments](#API_ListPaymentInstruments)
   + [ListPaymentSessions](#API_ListPaymentSessions)
   + [ListRecommendations](#API_ListRecommendations)
   + [ListSessions](#API_ListSessions)
   + [ProcessPayment](#API_ProcessPayment)
   + [RetrieveMemoryRecords](#API_RetrieveMemoryRecords)
   + [SaveBrowserSessionProfile](#API_SaveBrowserSessionProfile)
   + [SearchRegistryRecords](#API_SearchRegistryRecords)
   + [StartBatchEvaluation](#API_StartBatchEvaluation)
   + [StartBrowserSession](#API_StartBrowserSession)
   + [StartCodeInterpreterSession](#API_StartCodeInterpreterSession)
   + [StartMemoryExtractionJob](#API_StartMemoryExtractionJob)
   + [StartRecommendation](#API_StartRecommendation)
   + [StopBatchEvaluation](#API_StopBatchEvaluation)
   + [StopBrowserSession](#API_StopBrowserSession)
   + [StopCodeInterpreterSession](#API_StopCodeInterpreterSession)
   + [StopRuntimeSession](#API_StopRuntimeSession)
   + [UpdateABTest](#API_UpdateABTest)
   + [UpdateBrowserStream](#API_UpdateBrowserStream)
+ [Data Types](#API_Types)
   + [A2aDescriptor](#API_A2aDescriptor)
   + [ABTestEvaluationConfig](#API_ABTestEvaluationConfig)
   + [ABTestResults](#API_ABTestResults)
   + [ABTestSummary](#API_ABTestSummary)
   + [ActorSummary](#API_ActorSummary)
   + [AffectedSession](#API_AffectedSession)
   + [AgentCardDefinition](#API_AgentCardDefinition)
   + [AgentSkillsDescriptor](#API_AgentSkillsDescriptor)
   + [AgentTracesConfig](#API_AgentTracesConfig)
   + [Amount](#API_Amount)
   + [AutomationStream](#API_AutomationStream)
   + [AutomationStreamUpdate](#API_AutomationStreamUpdate)
   + [AvailableLimits](#API_AvailableLimits)
   + [BasicAuth](#API_BasicAuth)
   + [BatchEvaluationSummary](#API_BatchEvaluationSummary)
   + [BatchEvaluationTraceConfig](#API_BatchEvaluationTraceConfig)
   + [Branch](#API_Branch)
   + [BranchFilter](#API_BranchFilter)
   + [BrowserAction](#API_BrowserAction)
   + [BrowserActionResult](#API_BrowserActionResult)
   + [BrowserEnterprisePolicy](#API_BrowserEnterprisePolicy)
   + [BrowserExtension](#API_BrowserExtension)
   + [BrowserProfileConfiguration](#API_BrowserProfileConfiguration)
   + [BrowserSessionStream](#API_BrowserSessionStream)
   + [BrowserSessionSummary](#API_BrowserSessionSummary)
   + [Certificate](#API_Certificate)
   + [CertificateLocation](#API_CertificateLocation)
   + [CloudWatchFilterConfig](#API_CloudWatchFilterConfig)
   + [CloudWatchLogsFilter](#API_CloudWatchLogsFilter)
   + [CloudWatchLogsRule](#API_CloudWatchLogsRule)
   + [CloudWatchLogsSource](#API_CloudWatchLogsSource)
   + [CloudWatchLogsTraceConfig](#API_CloudWatchLogsTraceConfig)
   + [CloudWatchOutputConfig](#API_CloudWatchOutputConfig)
   + [CodeInterpreterResult](#API_CodeInterpreterResult)
   + [CodeInterpreterSessionSummary](#API_CodeInterpreterSessionSummary)
   + [CodeInterpreterStreamOutput](#API_CodeInterpreterStreamOutput)
   + [CoinbaseCdpTokenRequestInput](#API_CoinbaseCdpTokenRequestInput)
   + [CoinbaseCdpTokenResponseOutput](#API_CoinbaseCdpTokenResponseOutput)
   + [ConfidenceInterval](#API_ConfidenceInterval)
   + [ConfigurationBundleRef](#API_ConfigurationBundleRef)
   + [ConfigurationBundleToolEntry](#API_ConfigurationBundleToolEntry)
   + [Content](#API_Content)
   + [ContentBlock](#API_ContentBlock)
   + [ContentDeltaEvent](#API_ContentDeltaEvent)
   + [ContentSource](#API_ContentSource)
   + [ContentStartEvent](#API_ContentStartEvent)
   + [ContentStopEvent](#API_ContentStopEvent)
   + [Context](#API_Context)
   + [ControlStats](#API_ControlStats)
   + [Conversational](#API_Conversational)
   + [CryptoX402PaymentInput](#API_CryptoX402PaymentInput)
   + [CryptoX402PaymentOutput](#API_CryptoX402PaymentOutput)
   + [CustomDescriptor](#API_CustomDescriptor)
   + [DataSourceConfig](#API_DataSourceConfig)
   + [Descriptors](#API_Descriptors)
   + [EfsConfiguration](#API_EfsConfiguration)
   + [EmbeddedCryptoWallet](#API_EmbeddedCryptoWallet)
   + [EvaluationContent](#API_EvaluationContent)
   + [EvaluationExpectedTrajectory](#API_EvaluationExpectedTrajectory)
   + [EvaluationInput](#API_EvaluationInput)
   + [EvaluationJobResults](#API_EvaluationJobResults)
   + [EvaluationMetadata](#API_EvaluationMetadata)
   + [EvaluationReferenceInput](#API_EvaluationReferenceInput)
   + [EvaluationResultContent](#API_EvaluationResultContent)
   + [EvaluationTarget](#API_EvaluationTarget)
   + [Evaluator](#API_Evaluator)
   + [EvaluatorMetric](#API_EvaluatorMetric)
   + [EvaluatorStatistics](#API_EvaluatorStatistics)
   + [EvaluatorSummary](#API_EvaluatorSummary)
   + [Event](#API_Event)
   + [EventMetadataFilterExpression](#API_EventMetadataFilterExpression)
   + [ExecutionSummaryAffectedSession](#API_ExecutionSummaryAffectedSession)
   + [ExecutionSummaryCluster](#API_ExecutionSummaryCluster)
   + [ExecutionSummaryClusteringResultContent](#API_ExecutionSummaryClusteringResultContent)
   + [ExternalProxy](#API_ExternalProxy)
   + [ExtractionConfig](#API_ExtractionConfig)
   + [ExtractionJob](#API_ExtractionJob)
   + [ExtractionJobFilterInput](#API_ExtractionJobFilterInput)
   + [ExtractionJobMessages](#API_ExtractionJobMessages)
   + [ExtractionJobMetadata](#API_ExtractionJobMetadata)
   + [FailureAnalysisResultContent](#API_FailureAnalysisResultContent)
   + [FailureCategoryCluster](#API_FailureCategoryCluster)
   + [FailureSpanDetail](#API_FailureSpanDetail)
   + [FailureSubCategoryCluster](#API_FailureSubCategoryCluster)
   + [FilterInput](#API_FilterInput)
   + [FilterValue](#API_FilterValue)
   + [GatewayFilter](#API_GatewayFilter)
   + [GroundTruthSource](#API_GroundTruthSource)
   + [GroundTruthTurn](#API_GroundTruthTurn)
   + [GroundTruthTurnInput](#API_GroundTruthTurnInput)
   + [HarnessAgentCoreBrowserConfig](#API_HarnessAgentCoreBrowserConfig)
   + [HarnessAgentCoreCodeInterpreterConfig](#API_HarnessAgentCoreCodeInterpreterConfig)
   + [HarnessAgentCoreGatewayConfig](#API_HarnessAgentCoreGatewayConfig)
   + [HarnessBedrockModelConfig](#API_HarnessBedrockModelConfig)
   + [HarnessContentBlock](#API_HarnessContentBlock)
   + [HarnessContentBlockDelta](#API_HarnessContentBlockDelta)
   + [HarnessContentBlockDeltaEvent](#API_HarnessContentBlockDeltaEvent)
   + [HarnessContentBlockStart](#API_HarnessContentBlockStart)
   + [HarnessContentBlockStartEvent](#API_HarnessContentBlockStartEvent)
   + [HarnessContentBlockStopEvent](#API_HarnessContentBlockStopEvent)
   + [HarnessGatewayOutboundAuth](#API_HarnessGatewayOutboundAuth)
   + [HarnessGeminiModelConfig](#API_HarnessGeminiModelConfig)
   + [HarnessInlineFunctionConfig](#API_HarnessInlineFunctionConfig)
   + [HarnessLiteLlmModelConfig](#API_HarnessLiteLlmModelConfig)
   + [HarnessMessage](#API_HarnessMessage)
   + [HarnessMessageStartEvent](#API_HarnessMessageStartEvent)
   + [HarnessMessageStopEvent](#API_HarnessMessageStopEvent)
   + [HarnessMetadataEvent](#API_HarnessMetadataEvent)
   + [HarnessModelConfiguration](#API_HarnessModelConfiguration)
   + [HarnessOpenAiModelConfig](#API_HarnessOpenAiModelConfig)
   + [HarnessReasoningContentBlock](#API_HarnessReasoningContentBlock)
   + [HarnessReasoningContentBlockDelta](#API_HarnessReasoningContentBlockDelta)
   + [HarnessReasoningTextBlock](#API_HarnessReasoningTextBlock)
   + [HarnessRemoteMcpConfig](#API_HarnessRemoteMcpConfig)
   + [HarnessSkill](#API_HarnessSkill)
   + [HarnessSkillAwsSkillsSource](#API_HarnessSkillAwsSkillsSource)
   + [HarnessSkillGitAuth](#API_HarnessSkillGitAuth)
   + [HarnessSkillGitSource](#API_HarnessSkillGitSource)
   + [HarnessSkillS3Source](#API_HarnessSkillS3Source)
   + [HarnessStreamMetrics](#API_HarnessStreamMetrics)
   + [HarnessSystemContentBlock](#API_HarnessSystemContentBlock)
   + [HarnessTokenUsage](#API_HarnessTokenUsage)
   + [HarnessTool](#API_HarnessTool)
   + [HarnessToolConfiguration](#API_HarnessToolConfiguration)
   + [HarnessToolResultBlock](#API_HarnessToolResultBlock)
   + [HarnessToolResultBlockDelta](#API_HarnessToolResultBlockDelta)
   + [HarnessToolResultBlockStart](#API_HarnessToolResultBlockStart)
   + [HarnessToolResultContentBlock](#API_HarnessToolResultContentBlock)
   + [HarnessToolResultMetadataBlockDelta](#API_HarnessToolResultMetadataBlockDelta)
   + [HarnessToolUseBlock](#API_HarnessToolUseBlock)
   + [HarnessToolUseBlockDelta](#API_HarnessToolUseBlockDelta)
   + [HarnessToolUseBlockStart](#API_HarnessToolUseBlockStart)
   + [IngestPayloadType](#API_IngestPayloadType)
   + [InlineGroundTruth](#API_InlineGroundTruth)
   + [InlineMemoryContent](#API_InlineMemoryContent)
   + [InputContentBlock](#API_InputContentBlock)
   + [Insight](#API_Insight)
   + [InsightsFailureSignal](#API_InsightsFailureSignal)
   + [InvokeAgentRuntimeCommandRequestBody](#API_InvokeAgentRuntimeCommandRequestBody)
   + [InvokeAgentRuntimeCommandStreamOutput](#API_InvokeAgentRuntimeCommandStreamOutput)
   + [InvokeHarnessStreamOutput](#API_InvokeHarnessStreamOutput)
   + [KeyPressArguments](#API_KeyPressArguments)
   + [KeyPressResult](#API_KeyPressResult)
   + [KeyShortcutArguments](#API_KeyShortcutArguments)
   + [KeyShortcutResult](#API_KeyShortcutResult)
   + [KeyTypeArguments](#API_KeyTypeArguments)
   + [KeyTypeResult](#API_KeyTypeResult)
   + [LeftExpression](#API_LeftExpression)
   + [LinkedAccount](#API_LinkedAccount)
   + [LinkedAccountDeveloperJwt](#API_LinkedAccountDeveloperJwt)
   + [LinkedAccountEmail](#API_LinkedAccountEmail)
   + [LinkedAccountOAuth2](#API_LinkedAccountOAuth2)
   + [LinkedAccountSms](#API_LinkedAccountSms)
   + [LiveViewStream](#API_LiveViewStream)
   + [McpDescriptor](#API_McpDescriptor)
   + [MemoryContent](#API_MemoryContent)
   + [MemoryJsonData](#API_MemoryJsonData)
   + [MemoryMetadataFilterExpression](#API_MemoryMetadataFilterExpression)
   + [MemoryRecord](#API_MemoryRecord)
   + [MemoryRecordCreateInput](#API_MemoryRecordCreateInput)
   + [MemoryRecordDeleteInput](#API_MemoryRecordDeleteInput)
   + [MemoryRecordLeftExpression](#API_MemoryRecordLeftExpression)
   + [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue)
   + [MemoryRecordOutput](#API_MemoryRecordOutput)
   + [MemoryRecordRightExpression](#API_MemoryRecordRightExpression)
   + [MemoryRecordSummary](#API_MemoryRecordSummary)
   + [MemoryRecordUpdateInput](#API_MemoryRecordUpdateInput)
   + [MessageMetadata](#API_MessageMetadata)
   + [MetadataValue](#API_MetadataValue)
   + [MouseClickArguments](#API_MouseClickArguments)
   + [MouseClickResult](#API_MouseClickResult)
   + [MouseDragArguments](#API_MouseDragArguments)
   + [MouseDragResult](#API_MouseDragResult)
   + [MouseMoveArguments](#API_MouseMoveArguments)
   + [MouseMoveResult](#API_MouseMoveResult)
   + [MouseScrollArguments](#API_MouseScrollArguments)
   + [MouseScrollResult](#API_MouseScrollResult)
   + [MppPaymentInput](#API_MppPaymentInput)
   + [MppPaymentOutput](#API_MppPaymentOutput)
   + [OAuth2Authentication](#API_OAuth2Authentication)
   + [OAuthCredentialProvider](#API_OAuthCredentialProvider)
   + [OnlineEvaluationConfigSource](#API_OnlineEvaluationConfigSource)
   + [OnlineEvaluationTraceConfig](#API_OnlineEvaluationTraceConfig)
   + [OutputConfig](#API_OutputConfig)
   + [PayloadType](#API_PayloadType)
   + [PaymentInput](#API_PaymentInput)
   + [PaymentInstrument](#API_PaymentInstrument)
   + [PaymentInstrumentDetails](#API_PaymentInstrumentDetails)
   + [PaymentInstrumentSummary](#API_PaymentInstrumentSummary)
   + [PaymentOutput](#API_PaymentOutput)
   + [PaymentSession](#API_PaymentSession)
   + [PaymentSessionSummary](#API_PaymentSessionSummary)
   + [PaymentTokenRequestInput](#API_PaymentTokenRequestInput)
   + [PaymentTokenResponseOutput](#API_PaymentTokenResponseOutput)
   + [PerVariantOnlineEvaluationConfig](#API_PerVariantOnlineEvaluationConfig)
   + [Proxy](#API_Proxy)
   + [ProxyBypass](#API_ProxyBypass)
   + [ProxyConfiguration](#API_ProxyConfiguration)
   + [ProxyCredentials](#API_ProxyCredentials)
   + [RecommendationConfig](#API_RecommendationConfig)
   + [RecommendationEvaluationConfig](#API_RecommendationEvaluationConfig)
   + [RecommendationEvaluatorReference](#API_RecommendationEvaluatorReference)
   + [RecommendationResult](#API_RecommendationResult)
   + [RecommendationResultConfigurationBundle](#API_RecommendationResultConfigurationBundle)
   + [RecommendationSummary](#API_RecommendationSummary)
   + [RegistryRecordSummary](#API_RegistryRecordSummary)
   + [ResourceContent](#API_ResourceContent)
   + [ResourceLocation](#API_ResourceLocation)
   + [ResponseChunk](#API_ResponseChunk)
   + [RightExpression](#API_RightExpression)
   + [RootCauseCluster](#API_RootCauseCluster)
   + [S3FilesConfiguration](#API_S3FilesConfiguration)
   + [S3Location](#API_S3Location)
   + [ScreenshotArguments](#API_ScreenshotArguments)
   + [ScreenshotResult](#API_ScreenshotResult)
   + [SearchCriteria](#API_SearchCriteria)
   + [SecretsManagerLocation](#API_SecretsManagerLocation)
   + [ServerDefinition](#API_ServerDefinition)
   + [SessionFilter](#API_SessionFilter)
   + [SessionFilterConfig](#API_SessionFilterConfig)
   + [SessionLimits](#API_SessionLimits)
   + [SessionMetadataShape](#API_SessionMetadataShape)
   + [SessionSummary](#API_SessionSummary)
   + [SessionTraceIds](#API_SessionTraceIds)
   + [SkillDefinition](#API_SkillDefinition)
   + [SkillMdDefinition](#API_SkillMdDefinition)
   + [SpanContext](#API_SpanContext)
   + [StreamUpdate](#API_StreamUpdate)
   + [StripePrivyTokenRequestInput](#API_StripePrivyTokenRequestInput)
   + [StripePrivyTokenResponseOutput](#API_StripePrivyTokenResponseOutput)
   + [SystemPromptConfig](#API_SystemPromptConfig)
   + [SystemPromptConfigurationBundle](#API_SystemPromptConfigurationBundle)
   + [SystemPromptRecommendationConfig](#API_SystemPromptRecommendationConfig)
   + [SystemPromptRecommendationResult](#API_SystemPromptRecommendationResult)
   + [TargetRef](#API_TargetRef)
   + [TokenBalance](#API_TokenBalance)
   + [TokenUsage](#API_TokenUsage)
   + [ToolArguments](#API_ToolArguments)
   + [ToolDescriptionConfig](#API_ToolDescriptionConfig)
   + [ToolDescriptionConfigurationBundle](#API_ToolDescriptionConfigurationBundle)
   + [ToolDescriptionInput](#API_ToolDescriptionInput)
   + [ToolDescriptionOutput](#API_ToolDescriptionOutput)
   + [ToolDescriptionRecommendationConfig](#API_ToolDescriptionRecommendationConfig)
   + [ToolDescriptionRecommendationResult](#API_ToolDescriptionRecommendationResult)
   + [ToolDescriptionSource](#API_ToolDescriptionSource)
   + [ToolDescriptionTextInput](#API_ToolDescriptionTextInput)
   + [ToolResultStructuredContent](#API_ToolResultStructuredContent)
   + [ToolsDefinition](#API_ToolsDefinition)
   + [ToolsFileSystemConfiguration](#API_ToolsFileSystemConfiguration)
   + [UserIdentifier](#API_UserIdentifier)
   + [UserIntentAffectedSession](#API_UserIntentAffectedSession)
   + [UserIntentCluster](#API_UserIntentCluster)
   + [UserIntentClusteringResultContent](#API_UserIntentClusteringResultContent)
   + [ValidationExceptionField](#API_ValidationExceptionField)
   + [Variant](#API_Variant)
   + [VariantConfiguration](#API_VariantConfiguration)
   + [VariantResult](#API_VariantResult)
   + [ViewPort](#API_ViewPort)
+ [Common Parameters](#CommonParameters)
+ [Common Error Types](#CommonErrors)

-----



# Welcome
<a name="Welcome"></a>

Welcome to the Amazon Bedrock AgentCore Data Plane API reference. Data Plane actions process and handle data or workloads within AWS services. 

This document was last published on September 25, 2026. 

# Actions
<a name="API_Operations"></a>

The following actions are supported:
+  [BatchCreateMemoryRecords](#API_BatchCreateMemoryRecords) 
+  [BatchDeleteMemoryRecords](#API_BatchDeleteMemoryRecords) 
+  [BatchUpdateMemoryRecords](#API_BatchUpdateMemoryRecords) 
+  [CompleteResourceTokenAuth](#API_CompleteResourceTokenAuth) 
+  [CreateABTest](#API_CreateABTest) 
+  [CreateEvent](#API_CreateEvent) 
+  [CreatePaymentInstrument](#API_CreatePaymentInstrument) 
+  [CreatePaymentSession](#API_CreatePaymentSession) 
+  [DeleteABTest](#API_DeleteABTest) 
+  [DeleteBatchEvaluation](#API_DeleteBatchEvaluation) 
+  [DeleteCapacityProviderSession](#API_DeleteCapacityProviderSession) 
+  [DeleteEvent](#API_DeleteEvent) 
+  [DeleteMemoryRecord](#API_DeleteMemoryRecord) 
+  [DeletePaymentInstrument](#API_DeletePaymentInstrument) 
+  [DeletePaymentSession](#API_DeletePaymentSession) 
+  [DeleteRecommendation](#API_DeleteRecommendation) 
+  [Evaluate](#API_Evaluate) 
+  [GetABTest](#API_GetABTest) 
+  [GetAgentCard](#API_GetAgentCard) 
+  [GetBatchEvaluation](#API_GetBatchEvaluation) 
+  [GetBrowserSession](#API_GetBrowserSession) 
+  [GetCodeInterpreterSession](#API_GetCodeInterpreterSession) 
+  [GetEvent](#API_GetEvent) 
+  [GetMemoryRecord](#API_GetMemoryRecord) 
+  [GetPaymentInstrument](#API_GetPaymentInstrument) 
+  [GetPaymentInstrumentBalance](#API_GetPaymentInstrumentBalance) 
+  [GetPaymentSession](#API_GetPaymentSession) 
+  [GetRecommendation](#API_GetRecommendation) 
+  [GetResourceApiKey](#API_GetResourceApiKey) 
+  [GetResourceOauth2Token](#API_GetResourceOauth2Token) 
+  [GetResourcePaymentToken](#API_GetResourcePaymentToken) 
+  [GetWorkloadAccessToken](#API_GetWorkloadAccessToken) 
+  [GetWorkloadAccessTokenForJWT](#API_GetWorkloadAccessTokenForJWT) 
+  [GetWorkloadAccessTokenForUserId](#API_GetWorkloadAccessTokenForUserId) 
+  [IngestData](#API_IngestData) 
+  [InvokeAgentRuntime](#API_InvokeAgentRuntime) 
+  [InvokeAgentRuntimeCommand](#API_InvokeAgentRuntimeCommand) 
+  [InvokeBrowser](#API_InvokeBrowser) 
+  [InvokeCodeInterpreter](#API_InvokeCodeInterpreter) 
+  [InvokeHarness](#API_InvokeHarness) 
+  [ListABTests](#API_ListABTests) 
+  [ListActors](#API_ListActors) 
+  [ListBatchEvaluations](#API_ListBatchEvaluations) 
+  [ListBrowserSessions](#API_ListBrowserSessions) 
+  [ListCodeInterpreterSessions](#API_ListCodeInterpreterSessions) 
+  [ListEvents](#API_ListEvents) 
+  [ListMemoryExtractionJobs](#API_ListMemoryExtractionJobs) 
+  [ListMemoryRecords](#API_ListMemoryRecords) 
+  [ListPaymentInstruments](#API_ListPaymentInstruments) 
+  [ListPaymentSessions](#API_ListPaymentSessions) 
+  [ListRecommendations](#API_ListRecommendations) 
+  [ListSessions](#API_ListSessions) 
+  [ProcessPayment](#API_ProcessPayment) 
+  [RetrieveMemoryRecords](#API_RetrieveMemoryRecords) 
+  [SaveBrowserSessionProfile](#API_SaveBrowserSessionProfile) 
+  [SearchRegistryRecords](#API_SearchRegistryRecords) 
+  [StartBatchEvaluation](#API_StartBatchEvaluation) 
+  [StartBrowserSession](#API_StartBrowserSession) 
+  [StartCodeInterpreterSession](#API_StartCodeInterpreterSession) 
+  [StartMemoryExtractionJob](#API_StartMemoryExtractionJob) 
+  [StartRecommendation](#API_StartRecommendation) 
+  [StopBatchEvaluation](#API_StopBatchEvaluation) 
+  [StopBrowserSession](#API_StopBrowserSession) 
+  [StopCodeInterpreterSession](#API_StopCodeInterpreterSession) 
+  [StopRuntimeSession](#API_StopRuntimeSession) 
+  [UpdateABTest](#API_UpdateABTest) 
+  [UpdateBrowserStream](#API_UpdateBrowserStream) 

## BatchCreateMemoryRecords
<a name="API_BatchCreateMemoryRecords"></a>

Creates multiple memory records in a single batch operation for the specified memory with custom content.

### Request Syntax
<a name="API_BatchCreateMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/memoryRecords/batchCreate HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "records": [ 
      { 
         "content": { ... },
         "memoryStrategyId": "{{string}}",
         "metadata": { 
            "{{string}}" : { ... }
         },
         "namespaces": [ "{{string}}" ],
         "requestIdentifier": "{{string}}",
         "timestamp": {{number}}
      }
   ]
}
```

### URI Request Parameters
<a name="API_BatchCreateMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_BatchCreateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-request-uri-memoryId"></a>
The unique ID of the memory resource where records will be created.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_BatchCreateMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_BatchCreateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotent processing of the batch request.  
Type: String  
Required: No

 ** [records](#API_BatchCreateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-request-records"></a>
A list of memory record creation inputs to be processed in the batch operation.  
Type: Array of [MemoryRecordCreateInput](#API_MemoryRecordCreateInput) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

### Response Syntax
<a name="API_BatchCreateMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "failedRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ],
   "successfulRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ]
}
```

### Response Elements
<a name="API_BatchCreateMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [failedRecords](#API_BatchCreateMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-response-failedRecords"></a>
A list of memory records that failed to be created, including error details for each failure.  
Type: Array of [MemoryRecordOutput](#API_MemoryRecordOutput) objects

 ** [successfulRecords](#API_BatchCreateMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-response-successfulRecords"></a>
A list of memory records that were successfully created during the batch operation.  
Type: Array of [MemoryRecordOutput](#API_MemoryRecordOutput) objects

### Errors
<a name="API_BatchCreateMemoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_BatchCreateMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 

## BatchDeleteMemoryRecords
<a name="API_BatchDeleteMemoryRecords"></a>

Deletes multiple memory records in a single batch operation from the specified memory.

### Request Syntax
<a name="API_BatchDeleteMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/memoryRecords/batchDelete HTTP/1.1
Content-type: application/json

{
   "records": [ 
      { 
         "memoryRecordId": "{{string}}",
         "namespace": "{{string}}"
      }
   ]
}
```

### URI Request Parameters
<a name="API_BatchDeleteMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_BatchDeleteMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchDeleteMemoryRecords-request-uri-memoryId"></a>
The unique ID of the memory resource where records will be deleted.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_BatchDeleteMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [records](#API_BatchDeleteMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchDeleteMemoryRecords-request-records"></a>
A list of memory record deletion inputs to be processed in the batch operation.  
Type: Array of [MemoryRecordDeleteInput](#API_MemoryRecordDeleteInput) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

### Response Syntax
<a name="API_BatchDeleteMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ],
   "successfulRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ]
}
```

### Response Elements
<a name="API_BatchDeleteMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedRecords](#API_BatchDeleteMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchDeleteMemoryRecords-response-failedRecords"></a>
A list of memory records that failed to be deleted, including error details for each failure.  
Type: Array of [MemoryRecordOutput](#API_MemoryRecordOutput) objects

 ** [successfulRecords](#API_BatchDeleteMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchDeleteMemoryRecords-response-successfulRecords"></a>
A list of memory records that were successfully deleted during the batch operation.  
Type: Array of [MemoryRecordOutput](#API_MemoryRecordOutput) objects

### Errors
<a name="API_BatchDeleteMemoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_BatchDeleteMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords) 

## BatchUpdateMemoryRecords
<a name="API_BatchUpdateMemoryRecords"></a>

Updates multiple memory records with custom content in a single batch operation within the specified memory.

### Request Syntax
<a name="API_BatchUpdateMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/memoryRecords/batchUpdate HTTP/1.1
Content-type: application/json

{
   "records": [ 
      { 
         "content": { ... },
         "memoryRecordId": "{{string}}",
         "memoryStrategyId": "{{string}}",
         "metadata": { 
            "{{string}}" : { ... }
         },
         "namespaces": [ "{{string}}" ],
         "sourceNamespaces": [ "{{string}}" ],
         "timestamp": {{number}}
      }
   ]
}
```

### URI Request Parameters
<a name="API_BatchUpdateMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_BatchUpdateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchUpdateMemoryRecords-request-uri-memoryId"></a>
The unique ID of the memory resource where records will be updated.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_BatchUpdateMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [records](#API_BatchUpdateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchUpdateMemoryRecords-request-records"></a>
A list of memory record update inputs to be processed in the batch operation.  
Type: Array of [MemoryRecordUpdateInput](#API_MemoryRecordUpdateInput) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

### Response Syntax
<a name="API_BatchUpdateMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ],
   "successfulRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ]
}
```

### Response Elements
<a name="API_BatchUpdateMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedRecords](#API_BatchUpdateMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchUpdateMemoryRecords-response-failedRecords"></a>
A list of memory records that failed to be updated, including error details for each failure.  
Type: Array of [MemoryRecordOutput](#API_MemoryRecordOutput) objects

 ** [successfulRecords](#API_BatchUpdateMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchUpdateMemoryRecords-response-successfulRecords"></a>
A list of memory records that were successfully updated during the batch operation.  
Type: Array of [MemoryRecordOutput](#API_MemoryRecordOutput) objects

### Errors
<a name="API_BatchUpdateMemoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_BatchUpdateMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchUpdateMemoryRecords) 

## CompleteResourceTokenAuth
<a name="API_CompleteResourceTokenAuth"></a>

Confirms the user authentication session for obtaining OAuth2.0 tokens for a resource.

### Request Syntax
<a name="API_CompleteResourceTokenAuth_RequestSyntax"></a>

```
POST /identities/CompleteResourceTokenAuth HTTP/1.1
Content-type: application/json

{
   "sessionUri": "{{string}}",
   "userIdentifier": { ... }
}
```

### URI Request Parameters
<a name="API_CompleteResourceTokenAuth_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_CompleteResourceTokenAuth_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sessionUri](#API_CompleteResourceTokenAuth_RequestSyntax) **   <a name="BedrockAgentCore-CompleteResourceTokenAuth-request-sessionUri"></a>
Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `urn:ietf:params:oauth:request_uri:[a-zA-Z0-9-._~]+`   
Required: Yes

 ** [userIdentifier](#API_CompleteResourceTokenAuth_RequestSyntax) **   <a name="BedrockAgentCore-CompleteResourceTokenAuth-request-userIdentifier"></a>
The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.  
Type: [UserIdentifier](#API_UserIdentifier) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### Response Syntax
<a name="API_CompleteResourceTokenAuth_ResponseSyntax"></a>

```
HTTP/1.1 200
```

### Response Elements
<a name="API_CompleteResourceTokenAuth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

### Errors
<a name="API_CompleteResourceTokenAuth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_CompleteResourceTokenAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CompleteResourceTokenAuth) 

## CreateABTest
<a name="API_CreateABTest"></a>

Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.

### Request Syntax
<a name="API_CreateABTest_RequestSyntax"></a>

```
POST /ab-tests HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "enableOnCreate": {{boolean}},
   "evaluationConfig": { ... },
   "gatewayArn": "{{string}}",
   "gatewayFilter": { 
      "targetPaths": [ "{{string}}" ]
   },
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "variants": [ 
      { 
         "name": "{{string}}",
         "variantConfiguration": { 
            "configurationBundle": { 
               "bundleArn": "{{string}}",
               "bundleVersion": "{{string}}"
            },
            "target": { 
               "name": "{{string}}"
            }
         },
         "weight": {{number}}
      }
   ]
}
```

### URI Request Parameters
<a name="API_CreateABTest_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_CreateABTest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-description"></a>
The description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [enableOnCreate](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-enableOnCreate"></a>
Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.  
Type: Boolean  
Required: No

 ** [evaluationConfig](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-evaluationConfig"></a>
The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.  
Type: [ABTestEvaluationConfig](#API_ABTestEvaluationConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [gatewayArn](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** [gatewayFilter](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-gatewayFilter"></a>
Optional filter to restrict which gateway target paths are included in the A/B test.  
Type: [GatewayFilter](#API_GatewayFilter) object  
Required: No

 ** [name](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-name"></a>
The name of the A/B test. Must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [roleArn](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-roleArn"></a>
The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [tags](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-tags"></a>
A map of tag keys and values to associate with the A/B test.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [variants](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-variants"></a>
The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.  
Type: Array of [Variant](#API_Variant) objects  
Array Members: Fixed number of 2 items.  
Required: Yes

### Response Syntax
<a name="API_CreateABTest_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "createdAt": number,
   "executionStatus": "string",
   "name": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_CreateABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the created A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-abTestId"></a>
The unique identifier of the created A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-createdAt"></a>
The timestamp when the A/B test was created.  
Type: Timestamp

 ** [executionStatus](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-executionStatus"></a>
The execution status indicating whether the A/B test is currently running.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED` 

 ** [name](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-name"></a>
The name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [status](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-status"></a>
The status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

### Errors
<a name="API_CreateABTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_CreateABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CreateABTest) 

## CreateEvent
<a name="API_CreateEvent"></a>

Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.

To use this operation, you must have the `bedrock-agentcore:CreateEvent` permission.

This operation is subject to request rate limiting.

### Request Syntax
<a name="API_CreateEvent_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/events HTTP/1.1
Content-type: application/json

{
   "actorId": "{{string}}",
   "branch": { 
      "name": "{{string}}",
      "rootEventId": "{{string}}"
   },
   "clientToken": "{{string}}",
   "eventTimestamp": {{number}},
   "extractionConfig": { 
      "namespaceVariables": { 
         "{{string}}" : "{{string}}" 
      }
   },
   "extractionMode": "{{string}}",
   "metadata": { 
      "{{string}}" : { ... }
   },
   "payload": [ 
      { ... }
   ],
   "sessionId": "{{string}}"
}
```

### URI Request Parameters
<a name="API_CreateEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource in which to create the event.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_CreateEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorId](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-actorId"></a>
The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [branch](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-branch"></a>
The branch information for this event. Branches allow for organizing events into different conversation threads or paths.  
Type: [Branch](#API_Branch) object  
Required: No

 ** [clientToken](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.  
Type: String  
Required: No

 ** [eventTimestamp](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-eventTimestamp"></a>
The timestamp when the event occurred. If not specified, the current time is used.  
Type: Timestamp  
Required: Yes

 ** [extractionConfig](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-extractionConfig"></a>
The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.  
Type: [ExtractionConfig](#API_ExtractionConfig) object  
Required: No

 ** [extractionMode](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-extractionMode"></a>
Controls long-term memory extraction for this event. When set to `SKIP`, the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.  
Type: String  
Valid Values: `SKIP`   
Required: No

 ** [metadata](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-metadata"></a>
The key-value metadata to attach to the event.  
Type: String to [MetadataValue](#API_MetadataValue) object map  
Map Entries: Minimum number of 0 items. Maximum number of 15 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [payload](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-payload"></a>
The content payload of the event. This can include conversational data, JSON data, or binary content.  
Type: Array of [PayloadType](#API_PayloadType) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

 ** [sessionId](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-sessionId"></a>
The identifier of the session in which this event occurs. A session represents a sequence of related events.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

### Response Syntax
<a name="API_CreateEvent_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "event": { 
      "actorId": "string",
      "branch": { 
         "name": "string",
         "rootEventId": "string"
      },
      "eventId": "string",
      "eventTimestamp": number,
      "memoryId": "string",
      "metadata": { 
         "string" : { ... }
      },
      "payload": [ 
         { ... }
      ],
      "sessionId": "string"
   }
}
```

### Response Elements
<a name="API_CreateEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [event](#API_CreateEvent_ResponseSyntax) **   <a name="BedrockAgentCore-CreateEvent-response-event"></a>
The event that was created.  
Type: [Event](#API_Event) object

### Errors
<a name="API_CreateEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_CreateEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CreateEvent) 

## CreatePaymentInstrument
<a name="API_CreatePaymentInstrument"></a>

Create a new payment instrument for a connector.

### Request Syntax
<a name="API_CreatePaymentInstrument_RequestSyntax"></a>

```
POST /payments/createPaymentInstrument HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "clientToken": "{{string}}",
   "paymentConnectorId": "{{string}}",
   "paymentInstrumentDetails": { ... },
   "paymentInstrumentType": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

### URI Request Parameters
<a name="API_CreatePaymentInstrument_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-userId"></a>
The user ID associated with this payment instrument.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_CreatePaymentInstrument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [paymentConnectorId](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-paymentConnectorId"></a>
The ID of the payment connector to use for this instrument.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [paymentInstrumentDetails](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-paymentInstrumentDetails"></a>
The details of the payment instrument.  
Type: [PaymentInstrumentDetails](#API_PaymentInstrumentDetails) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [paymentInstrumentType](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-paymentInstrumentType"></a>
The type of payment instrument being created.  
Type: String  
Valid Values: `EMBEDDED_CRYPTO_WALLET`   
Required: Yes

 ** [paymentManagerArn](#API_CreatePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-request-paymentManagerArn"></a>
The ARN of the payment manager that owns this payment instrument.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

### Response Syntax
<a name="API_CreatePaymentInstrument_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "paymentInstrument": { 
      "createdAt": "string",
      "paymentConnectorId": "string",
      "paymentInstrumentDetails": { ... },
      "paymentInstrumentId": "string",
      "paymentInstrumentType": "string",
      "paymentManagerArn": "string",
      "status": "string",
      "updatedAt": "string",
      "userId": "string"
   }
}
```

### Response Elements
<a name="API_CreatePaymentInstrument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [paymentInstrument](#API_CreatePaymentInstrument_ResponseSyntax) **   <a name="BedrockAgentCore-CreatePaymentInstrument-response-paymentInstrument"></a>
The created payment instrument.  
Type: [PaymentInstrument](#API_PaymentInstrument) object

### Errors
<a name="API_CreatePaymentInstrument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** SubscriptionRequiredException **   
Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.    
 ** productName **   
The name of the product that requires a Marketplace subscription.  
 ** subscriptionUrl **   
The URL to the Marketplace listing where you can subscribe.
HTTP Status Code: 403

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_CreatePaymentInstrument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CreatePaymentInstrument) 

## CreatePaymentSession
<a name="API_CreatePaymentSession"></a>

Create a new payment session.

### Request Syntax
<a name="API_CreatePaymentSession_RequestSyntax"></a>

```
POST /payments/createPaymentSession HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "clientToken": "{{string}}",
   "expiryTimeInMinutes": {{number}},
   "limits": { 
      "maxSpendAmount": { 
         "currency": "{{string}}",
         "value": "{{string}}"
      }
   },
   "paymentManagerArn": "{{string}}"
}
```

### URI Request Parameters
<a name="API_CreatePaymentSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_CreatePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_CreatePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-request-userId"></a>
The user ID associated with this payment session.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_CreatePaymentSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [expiryTimeInMinutes](#API_CreatePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-request-expiryTimeInMinutes"></a>
The session expiry time in minutes. Must be between 15 and 480 minutes.  
Type: Integer  
Valid Range: Minimum value of 15. Maximum value of 480.  
Required: Yes

 ** [limits](#API_CreatePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-request-limits"></a>
The spending limits for this payment session.  
Type: [SessionLimits](#API_SessionLimits) object  
Required: No

 ** [paymentManagerArn](#API_CreatePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-request-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

### Response Syntax
<a name="API_CreatePaymentSession_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "paymentSession": { 
      "availableLimits": { 
         "availableSpendAmount": { 
            "currency": "string",
            "value": "string"
         },
         "updatedAt": "string"
      },
      "createdAt": "string",
      "expiryTimeInMinutes": number,
      "limits": { 
         "maxSpendAmount": { 
            "currency": "string",
            "value": "string"
         }
      },
      "paymentManagerArn": "string",
      "paymentSessionId": "string",
      "updatedAt": "string",
      "userId": "string"
   }
}
```

### Response Elements
<a name="API_CreatePaymentSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [paymentSession](#API_CreatePaymentSession_ResponseSyntax) **   <a name="BedrockAgentCore-CreatePaymentSession-response-paymentSession"></a>
The created payment session.  
Type: [PaymentSession](#API_PaymentSession) object

### Errors
<a name="API_CreatePaymentSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** SubscriptionRequiredException **   
Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.    
 ** productName **   
The name of the product that requires a Marketplace subscription.  
 ** subscriptionUrl **   
The URL to the Marketplace listing where you can subscribe.
HTTP Status Code: 403

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_CreatePaymentSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CreatePaymentSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CreatePaymentSession) 

## DeleteABTest
<a name="API_DeleteABTest"></a>

Deletes an A/B test and its associated gateway rules.

### Request Syntax
<a name="API_DeleteABTest_RequestSyntax"></a>

```
DELETE /ab-tests/{{abTestId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteABTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [abTestId](#API_DeleteABTest_RequestSyntax) **   <a name="BedrockAgentCore-DeleteABTest-request-uri-abTestId"></a>
The unique identifier of the A/B test to delete.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_DeleteABTest_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteABTest_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_DeleteABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_DeleteABTest_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the deleted A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_DeleteABTest_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteABTest-response-abTestId"></a>
The unique identifier of the deleted A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteABTest_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteABTest-response-status"></a>
The status of the A/B test deletion operation.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

### Errors
<a name="API_DeleteABTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeleteABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteABTest) 

## DeleteBatchEvaluation
<a name="API_DeleteBatchEvaluation"></a>

Deletes a batch evaluation and its associated results.

### Request Syntax
<a name="API_DeleteBatchEvaluation_RequestSyntax"></a>

```
DELETE /evaluations/batch-evaluate/{{batchEvaluationId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteBatchEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchEvaluationId](#API_DeleteBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-DeleteBatchEvaluation-request-uri-batchEvaluationId"></a>
The unique identifier of the batch evaluation to delete.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_DeleteBatchEvaluation_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteBatchEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "batchEvaluationArn": "string",
   "batchEvaluationId": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_DeleteBatchEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluationArn](#API_DeleteBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteBatchEvaluation-response-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the deleted batch evaluation.  
Type: String

 ** [batchEvaluationId](#API_DeleteBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteBatchEvaluation-response-batchEvaluationId"></a>
The unique identifier of the deleted batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteBatchEvaluation-response-status"></a>
The status of the batch evaluation deletion operation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING` 

### Errors
<a name="API_DeleteBatchEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeleteBatchEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteBatchEvaluation) 

## DeleteCapacityProviderSession
<a name="API_DeleteCapacityProviderSession"></a>

Deletes a session associated with a capacity provider in Amazon Bedrock AgentCore and makes the session unavailable for further use. To delete a capacity provider session, specify both the capacity provider identifier and the session ID. After you delete a session, you cannot restart it.

### Request Syntax
<a name="API_DeleteCapacityProviderSession_RequestSyntax"></a>

```
DELETE /capacity-providers/{{capacityProviderId}}/sessions/{{sessionId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteCapacityProviderSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [capacityProviderId](#API_DeleteCapacityProviderSession_RequestSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-request-uri-capacityProviderId"></a>
The unique identifier of the capacity provider associated with the session.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_DeleteCapacityProviderSession_RequestSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-request-uri-sessionId"></a>
The unique identifier of the capacity provider session to delete.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

### Request Body
<a name="API_DeleteCapacityProviderSession_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteCapacityProviderSession_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "capacityProviderArn": "string",
   "sessionId": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_DeleteCapacityProviderSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [capacityProviderArn](#API_DeleteCapacityProviderSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-response-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider associated with the deleted session.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [sessionId](#API_DeleteCapacityProviderSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-response-sessionId"></a>
The unique identifier of the deleted capacity provider session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [status](#API_DeleteCapacityProviderSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-response-status"></a>
The current status of the capacity provider session. When the status is `Deleting`, the session is being deleted and is not available. When the status is `Deleted`, the session is no longer available.  
Type: String  
Valid Values: `Provisioning | Deprovisioning | Active | Deleting | Deleted | Stopped` 

### Errors
<a name="API_DeleteCapacityProviderSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeleteCapacityProviderSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 

## DeleteEvent
<a name="API_DeleteEvent"></a>

Deletes an event from an AgentCore Memory resource. When you delete an event, it is permanently removed.

To use this operation, you must have the `bedrock-agentcore:DeleteEvent` permission.

### Request Syntax
<a name="API_DeleteEvent_RequestSyntax"></a>

```
DELETE /memories/{{memoryId}}/actor/{{actorId}}/sessions/{{sessionId}}/events/{{eventId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actorId](#API_DeleteEvent_RequestSyntax) **   <a name="BedrockAgentCore-DeleteEvent-request-uri-actorId"></a>
The identifier of the actor associated with the event to delete.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [eventId](#API_DeleteEvent_RequestSyntax) **   <a name="BedrockAgentCore-DeleteEvent-request-uri-eventId"></a>
The identifier of the event to delete.  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: Yes

 ** [memoryId](#API_DeleteEvent_RequestSyntax) **   <a name="BedrockAgentCore-DeleteEvent-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource from which to delete the event.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_DeleteEvent_RequestSyntax) **   <a name="BedrockAgentCore-DeleteEvent-request-uri-sessionId"></a>
The identifier of the session containing the event to delete.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

### Request Body
<a name="API_DeleteEvent_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "eventId": "string"
}
```

### Response Elements
<a name="API_DeleteEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventId](#API_DeleteEvent_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteEvent-response-eventId"></a>
The identifier of the event that was deleted.  
Type: String  
Pattern: `[0-9]+#[a-fA-F0-9]+` 

### Errors
<a name="API_DeleteEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeleteEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteEvent) 

## DeleteMemoryRecord
<a name="API_DeleteMemoryRecord"></a>

Deletes a memory record from an AgentCore Memory resource. When you delete a memory record, it is permanently removed.

To use this operation, you must have the `bedrock-agentcore:DeleteMemoryRecord` permission.

### Request Syntax
<a name="API_DeleteMemoryRecord_RequestSyntax"></a>

```
DELETE /memories/{{memoryId}}/memoryRecords/{{memoryRecordId}}?namespace={{namespace}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteMemoryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_DeleteMemoryRecord_RequestSyntax) **   <a name="BedrockAgentCore-DeleteMemoryRecord-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource from which to delete the memory record.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [memoryRecordId](#API_DeleteMemoryRecord_RequestSyntax) **   <a name="BedrockAgentCore-DeleteMemoryRecord-request-uri-memoryRecordId"></a>
The identifier of the memory record to delete.  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** [namespace](#API_DeleteMemoryRecord_RequestSyntax) **   <a name="BedrockAgentCore-DeleteMemoryRecord-request-uri-namespace"></a>
The namespace of the memory record to delete. This value is used for IAM condition key authorization.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*` 

### Request Body
<a name="API_DeleteMemoryRecord_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteMemoryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memoryRecordId": "string"
}
```

### Response Elements
<a name="API_DeleteMemoryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memoryRecordId](#API_DeleteMemoryRecord_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteMemoryRecord-response-memoryRecordId"></a>
The identifier of the memory record that was deleted.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*` 

### Errors
<a name="API_DeleteMemoryRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeleteMemoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteMemoryRecord) 

## DeletePaymentInstrument
<a name="API_DeletePaymentInstrument"></a>

Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.

### Request Syntax
<a name="API_DeletePaymentInstrument_RequestSyntax"></a>

```
POST /payments/deletePaymentInstrument HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
Content-type: application/json

{
   "paymentConnectorId": "{{string}}",
   "paymentInstrumentId": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

### URI Request Parameters
<a name="API_DeletePaymentInstrument_RequestParameters"></a>

The request uses the following URI parameters.

 ** [userId](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-userId"></a>
The user ID making the delete request. Must match the instrument's userId.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_DeletePaymentInstrument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentConnectorId](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-paymentConnectorId"></a>
The payment connector ID. Must match the instrument's paymentConnectorId.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [paymentInstrumentId](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-paymentInstrumentId"></a>
The payment instrument ID to delete.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentManagerArn](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-paymentManagerArn"></a>
The payment manager ARN. Must match the instrument's paymentManagerArn.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

### Response Syntax
<a name="API_DeletePaymentInstrument_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

### Response Elements
<a name="API_DeletePaymentInstrument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeletePaymentInstrument_ResponseSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-response-status"></a>
The status of the instrument after deletion. Always DELETED for successful soft delete.  
Type: String  
Valid Values: `INITIATED | ACTIVE | FAILED | DELETED | BLOCKED` 

### Errors
<a name="API_DeletePaymentInstrument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeletePaymentInstrument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 

## DeletePaymentSession
<a name="API_DeletePaymentSession"></a>

Deletes a payment session. This permanently removes the payment session record.

### Request Syntax
<a name="API_DeletePaymentSession_RequestSyntax"></a>

```
POST /payments/deletePaymentSession HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
Content-type: application/json

{
   "paymentManagerArn": "{{string}}",
   "paymentSessionId": "{{string}}"
}
```

### URI Request Parameters
<a name="API_DeletePaymentSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [userId](#API_DeletePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentSession-request-userId"></a>
The user ID making the delete request. Must match the session's userId.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_DeletePaymentSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentManagerArn](#API_DeletePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentSession-request-paymentManagerArn"></a>
The payment manager ARN. Must match the session's paymentManagerArn.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** [paymentSessionId](#API_DeletePaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentSession-request-paymentSessionId"></a>
The payment session ID to delete.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

### Response Syntax
<a name="API_DeletePaymentSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

### Response Elements
<a name="API_DeletePaymentSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeletePaymentSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeletePaymentSession-response-status"></a>
The status of the deletion. Always DELETED for successful hard delete.  
Type: String  
Valid Values: `ACTIVE | EXPIRED | DELETED` 

### Errors
<a name="API_DeletePaymentSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeletePaymentSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeletePaymentSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeletePaymentSession) 

## DeleteRecommendation
<a name="API_DeleteRecommendation"></a>

Deletes a recommendation and its associated results.

### Request Syntax
<a name="API_DeleteRecommendation_RequestSyntax"></a>

```
DELETE /recommendations/{{recommendationId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationId](#API_DeleteRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-DeleteRecommendation-request-uri-recommendationId"></a>
The unique identifier of the recommendation to delete.  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

### Request Body
<a name="API_DeleteRecommendation_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recommendationId": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_DeleteRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recommendationId](#API_DeleteRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteRecommendation-response-recommendationId"></a>
The unique identifier of the deleted recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [status](#API_DeleteRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteRecommendation-response-status"></a>
The status of the recommendation deletion operation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

### Errors
<a name="API_DeleteRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_DeleteRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteRecommendation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteRecommendation) 

## Evaluate
<a name="API_Evaluate"></a>

 Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.

### Request Syntax
<a name="API_Evaluate_RequestSyntax"></a>

```
POST /evaluations/evaluate/{{evaluatorId}} HTTP/1.1
Content-type: application/json

{
   "evaluationInput": { ... },
   "evaluationReferenceInputs": [ 
      { 
         "assertions": [ 
            { ... }
         ],
         "context": { ... },
         "expectedResponse": { ... },
         "expectedTrajectory": { 
            "toolNames": [ "{{string}}" ]
         }
      }
   ],
   "evaluationTarget": { ... }
}
```

### URI Request Parameters
<a name="API_Evaluate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [evaluatorId](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-uri-evaluatorId"></a>
 The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., `Builtin.Helpfulness`, `Builtin.Correctness`) or a custom evaluator Id created through the control plane API.   
Length Constraints: Minimum length of 1. Maximum length of 111.  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

### Request Body
<a name="API_Evaluate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [evaluationInput](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-evaluationInput"></a>
 The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation.   
Type: [EvaluationInput](#API_EvaluationInput) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [evaluationReferenceInputs](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-evaluationReferenceInputs"></a>
 Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID.   
Type: Array of [EvaluationReferenceInput](#API_EvaluationReferenceInput) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: No

 ** [evaluationTarget](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-evaluationTarget"></a>
 The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions.   
Type: [EvaluationTarget](#API_EvaluationTarget) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### Response Syntax
<a name="API_Evaluate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "evaluationResults": [ 
      { 
         "context": { ... },
         "errorCode": "string",
         "errorMessage": "string",
         "evaluatorArn": "string",
         "evaluatorId": "string",
         "evaluatorName": "string",
         "explanation": "string",
         "ignoredReferenceInputFields": [ "string" ],
         "label": "string",
         "tokenUsage": { 
            "inputTokens": number,
            "outputTokens": number,
            "totalTokens": number
         },
         "value": number
      }
   ]
}
```

### Response Elements
<a name="API_Evaluate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evaluationResults](#API_Evaluate_ResponseSyntax) **   <a name="BedrockAgentCore-Evaluate-response-evaluationResults"></a>
 The detailed evaluation results containing scores, explanations, and metadata. Includes the evaluator information, numerical or categorical ratings based on the evaluator's rating scale, and token usage statistics for the evaluation process.   
Type: Array of [EvaluationResultContent](#API_EvaluationResultContent) objects

### Errors
<a name="API_Evaluate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** DuplicateIdException **   
 An exception thrown when attempting to create a resource with an identifier that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_Evaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Evaluate) 

## GetABTest
<a name="API_GetABTest"></a>

Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.

### Request Syntax
<a name="API_GetABTest_RequestSyntax"></a>

```
GET /ab-tests/{{abTestId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetABTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [abTestId](#API_GetABTest_RequestSyntax) **   <a name="BedrockAgentCore-GetABTest-request-uri-abTestId"></a>
The unique identifier of the A/B test to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_GetABTest_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetABTest_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "createdAt": number,
   "currentRunId": "string",
   "description": "string",
   "errorDetails": [ "string" ],
   "evaluationConfig": { ... },
   "executionStatus": "string",
   "gatewayArn": "string",
   "gatewayFilter": { 
      "targetPaths": [ "string" ]
   },
   "maxDurationExpiresAt": number,
   "name": "string",
   "results": { 
      "analysisTimestamp": number,
      "evaluatorMetrics": [ 
         { 
            "controlStats": { 
               "mean": number,
               "sampleSize": number,
               "variantName": "string"
            },
            "evaluatorArn": "string",
            "variantResults": [ 
               { 
                  "absoluteChange": number,
                  "confidenceInterval": { 
                     "lower": number,
                     "upper": number
                  },
                  "isSignificant": boolean,
                  "mean": number,
                  "percentChange": number,
                  "pValue": number,
                  "sampleSize": number,
                  "variantName": "string"
               }
            ]
         }
      ]
   },
   "roleArn": "string",
   "startedAt": number,
   "status": "string",
   "stoppedAt": number,
   "updatedAt": number,
   "variants": [ 
      { 
         "name": "string",
         "variantConfiguration": { 
            "configurationBundle": { 
               "bundleArn": "string",
               "bundleVersion": "string"
            },
            "target": { 
               "name": "string"
            }
         },
         "weight": number
      }
   ]
}
```

### Response Elements
<a name="API_GetABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-abTestId"></a>
The unique identifier of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-createdAt"></a>
The timestamp when the A/B test was created.  
Type: Timestamp

 ** [currentRunId](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-currentRunId"></a>
The identifier of the current run of the A/B test.  
Type: String

 ** [description](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-description"></a>
The description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [errorDetails](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-errorDetails"></a>
The error details if the A/B test encountered failures.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [evaluationConfig](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-evaluationConfig"></a>
The evaluation configuration for measuring variant performance.  
Type: [ABTestEvaluationConfig](#API_ABTestEvaluationConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [executionStatus](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-executionStatus"></a>
The execution status indicating whether the A/B test is currently running.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED` 

 ** [gatewayArn](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway used for traffic splitting.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [gatewayFilter](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-gatewayFilter"></a>
The gateway filter restricting which target paths are included.  
Type: [GatewayFilter](#API_GatewayFilter) object

 ** [maxDurationExpiresAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-maxDurationExpiresAt"></a>
The timestamp when the A/B test will automatically expire.  
Type: Timestamp

 ** [name](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-name"></a>
The name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [results](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-results"></a>
The statistical results of the A/B test, including per-evaluator metrics and significance analysis.  
Type: [ABTestResults](#API_ABTestResults) object

 ** [roleArn](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-roleArn"></a>
The IAM role ARN used by the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [startedAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-startedAt"></a>
The timestamp when the A/B test was started.  
Type: Timestamp

 ** [status](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-status"></a>
The current status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

 ** [stoppedAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-stoppedAt"></a>
The timestamp when the A/B test was stopped.  
Type: Timestamp

 ** [updatedAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-updatedAt"></a>
The timestamp when the A/B test was last updated.  
Type: Timestamp

 ** [variants](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-variants"></a>
The list of variants in the A/B test.  
Type: Array of [Variant](#API_Variant) objects  
Array Members: Fixed number of 2 items.

### Errors
<a name="API_GetABTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetABTest) 

## GetAgentCard
<a name="API_GetAgentCard"></a>

Retrieves the A2A agent card associated with an AgentCore Runtime agent.

### Request Syntax
<a name="API_GetAgentCard_RequestSyntax"></a>

```
GET /runtimes/{{agentRuntimeArn}}/invocations/.well-known/agent-card.json?qualifier={{qualifier}} HTTP/1.1
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
```

### URI Request Parameters
<a name="API_GetAgentCard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeArn](#API_GetAgentCard_RequestSyntax) **   <a name="BedrockAgentCore-GetAgentCard-request-uri-agentRuntimeArn"></a>
The ARN of the AgentCore Runtime agent for which you want to get the A2A agent card.  
Required: Yes

 ** [qualifier](#API_GetAgentCard_RequestSyntax) **   <a name="BedrockAgentCore-GetAgentCard-request-uri-qualifier"></a>
Optional qualifier to specify an agent alias, such as `prod`code> or `dev`. If you don't provide a value, the DEFAULT alias is used. 

 ** [runtimeSessionId](#API_GetAgentCard_RequestSyntax) **   <a name="BedrockAgentCore-GetAgentCard-request-runtimeSessionId"></a>
The session ID that the AgentCore Runtime agent is using.   
Length Constraints: Minimum length of 33. Maximum length of 256.

### Request Body
<a name="API_GetAgentCard_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetAgentCard_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
```

### Response Elements
<a name="API_GetAgentCard_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_GetAgentCard_ResponseSyntax) **   <a name="BedrockAgentCore-GetAgentCard-response-statusCode"></a>
The status code of the request.

The response returns the following HTTP headers.

 ** [runtimeSessionId](#API_GetAgentCard_ResponseSyntax) **   <a name="BedrockAgentCore-GetAgentCard-response-runtimeSessionId"></a>
The ID of the session associated with the AgentCore Runtime agent.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

### Errors
<a name="API_GetAgentCard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetAgentCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetAgentCard) 

## GetBatchEvaluation
<a name="API_GetBatchEvaluation"></a>

Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.

### Request Syntax
<a name="API_GetBatchEvaluation_RequestSyntax"></a>

```
GET /evaluations/batch-evaluate/{{batchEvaluationId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetBatchEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchEvaluationId](#API_GetBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-request-uri-batchEvaluationId"></a>
The unique identifier of the batch evaluation to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_GetBatchEvaluation_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetBatchEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchEvaluationArn": "string",
   "batchEvaluationId": "string",
   "batchEvaluationName": "string",
   "createdAt": "string",
   "dataSourceConfig": { ... },
   "description": "string",
   "errorDetails": [ "string" ],
   "evaluationResults": { 
      "evaluatorSummaries": [ 
         { 
            "evaluatorId": "string",
            "statistics": { 
               "averageScore": number
            },
            "totalEvaluated": number,
            "totalFailed": number
         }
      ],
      "numberOfSessionsCompleted": number,
      "numberOfSessionsFailed": number,
      "numberOfSessionsIgnored": number,
      "numberOfSessionsInProgress": number,
      "totalNumberOfSessions": number
   },
   "evaluators": [ 
      { 
         "evaluatorId": "string"
      }
   ],
   "executionSummaryResult": { 
      "executionSummaries": [ 
         { 
            "affectedSessionCount": number,
            "affectedSessions": [ 
               { 
                  "approachTaken": "string",
                  "finalOutcome": "string",
                  "sessionId": "string"
               }
            ],
            "clusterId": number,
            "description": "string",
            "name": "string"
         }
      ]
   },
   "failureAnalysisResult": { 
      "failures": [ 
         { 
            "affectedSessionCount": number,
            "clusterId": number,
            "description": "string",
            "name": "string",
            "subCategories": [ 
               { 
                  "affectedSessionCount": number,
                  "clusterId": number,
                  "description": "string",
                  "name": "string",
                  "rootCauses": [ 
                     { 
                        "affectedSessionCount": number,
                        "affectedSessions": [ 
                           { 
                              "explanation": "string",
                              "failureSpans": [ 
                                 { 
                                    "signals": [ 
                                       { 
                                          "category": "string",
                                          "confidence": number,
                                          "evidence": "string"
                                       }
                                    ],
                                    "spanId": "string",
                                    "traceId": "string"
                                 }
                              ],
                              "fixType": "string",
                              "recommendation": "string",
                              "sessionId": "string"
                           }
                        ],
                        "clusterId": number,
                        "name": "string",
                        "recommendation": "string",
                        "rootCause": "string"
                     }
                  ]
               }
            ]
         }
      ]
   },
   "insights": [ 
      { 
         "insightId": "string"
      }
   ],
   "kmsKeyArn": "string",
   "outputConfig": { ... },
   "status": "string",
   "updatedAt": "string",
   "userIntentResult": { 
      "userIntents": [ 
         { 
            "affectedSessionCount": number,
            "affectedSessions": [ 
               { 
                  "sessionId": "string",
                  "userMessages": [ "string" ]
               }
            ],
            "clusterId": number,
            "description": "string",
            "name": "string"
         }
      ]
   }
}
```

### Response Elements
<a name="API_GetBatchEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluationArn](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the batch evaluation.  
Type: String

 ** [batchEvaluationId](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-batchEvaluationId"></a>
The unique identifier of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [batchEvaluationName](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-batchEvaluationName"></a>
The name of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [createdAt](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-createdAt"></a>
The timestamp when the batch evaluation was created.  
Type: Timestamp

 ** [dataSourceConfig](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-dataSourceConfig"></a>
The data source configuration specifying where agent traces are pulled from.  
Type: [DataSourceConfig](#API_DataSourceConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [description](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [errorDetails](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-errorDetails"></a>
The error details if the batch evaluation encountered failures.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [evaluationResults](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-evaluationResults"></a>
The aggregated evaluation results, including session completion counts and evaluator score summaries.  
Type: [EvaluationJobResults](#API_EvaluationJobResults) object

 ** [evaluators](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-evaluators"></a>
The list of evaluators applied during the batch evaluation.  
Type: Array of [Evaluator](#API_Evaluator) objects

 ** [executionSummaryResult](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-executionSummaryResult"></a>
The execution summary clustering results from insights, containing grouped execution patterns across evaluated sessions.  
Type: [ExecutionSummaryClusteringResultContent](#API_ExecutionSummaryClusteringResultContent) object

 ** [failureAnalysisResult](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-failureAnalysisResult"></a>
The failure analysis results from insights, containing categorized failure clusters with root causes and recommendations.  
Type: [FailureAnalysisResultContent](#API_FailureAnalysisResultContent) object

 ** [insights](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-insights"></a>
The list of insight analyses applied during the batch evaluation.  
Type: Array of [Insight](#API_Insight) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [kmsKeyArn](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [outputConfig](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-outputConfig"></a>
The output configuration specifying where evaluation results are written.  
Type: [OutputConfig](#API_OutputConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-status"></a>
The current status of the batch evaluation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING` 

 ** [updatedAt](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-updatedAt"></a>
The timestamp when the batch evaluation was last updated.  
Type: Timestamp

 ** [userIntentResult](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-userIntentResult"></a>
The user intent clustering results from insights, containing grouped user intents across evaluated sessions.  
Type: [UserIntentClusteringResultContent](#API_UserIntentClusteringResultContent) object

### Errors
<a name="API_GetBatchEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetBatchEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 

## GetBrowserSession
<a name="API_GetBrowserSession"></a>

Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.

To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.

The following operations are related to `GetBrowserSession`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [ListBrowserSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html) 
+  [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html) 

### Request Syntax
<a name="API_GetBrowserSession_RequestSyntax"></a>

```
GET /browsers/{{browserIdentifier}}/sessions/get?sessionId={{sessionId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetBrowserSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_GetBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-request-uri-browserIdentifier"></a>
The unique identifier of the browser associated with the session.  
Required: Yes

 ** [sessionId](#API_GetBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-request-uri-sessionId"></a>
The unique identifier of the browser session to retrieve.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

### Request Body
<a name="API_GetBrowserSession_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetBrowserSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "createdAt": "string",
   "enterprisePolicies": [ 
      { 
         "location": { ... },
         "type": "string"
      }
   ],
   "extensions": [ 
      { 
         "location": { ... }
      }
   ],
   "filesystemConfigurations": [ 
      { ... }
   ],
   "lastUpdatedAt": "string",
   "name": "string",
   "profileConfiguration": { 
      "profileIdentifier": "string"
   },
   "proxyConfiguration": { 
      "bypass": { 
         "domainPatterns": [ "string" ]
      },
      "proxies": [ 
         { ... }
      ]
   },
   "sessionId": "string",
   "sessionReplayArtifact": "string",
   "sessionTimeoutSeconds": number,
   "status": "string",
   "streams": { 
      "automationStream": { 
         "streamEndpoint": "string",
         "streamStatus": "string"
      },
      "liveViewStream": { 
         "streamEndpoint": "string"
      }
   },
   "viewPort": { 
      "height": number,
      "width": number
   }
}
```

### Response Elements
<a name="API_GetBrowserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [certificates](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-certificates"></a>
The list of certificates installed in the browser session.  
Type: Array of [Certificate](#API_Certificate) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [createdAt](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-createdAt"></a>
The time at which the browser session was created.  
Type: Timestamp

 ** [enterprisePolicies](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-enterprisePolicies"></a>
A list of files containing enterprise policies for the browser session.  
Type: Array of [BrowserEnterprisePolicy](#API_BrowserEnterprisePolicy) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [extensions](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-extensions"></a>
The list of browser extensions that are configured in the browser session.  
Type: Array of [BrowserExtension](#API_BrowserExtension) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [filesystemConfigurations](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-filesystemConfigurations"></a>
The file system configurations for the browser session. Each entry describes an access point and its mount path.  
Type: Array of [ToolsFileSystemConfiguration](#API_ToolsFileSystemConfiguration) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [lastUpdatedAt](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-lastUpdatedAt"></a>
The time at which the browser session was last updated.  
Type: Timestamp

 ** [name](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-name"></a>
The name of the browser session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [profileConfiguration](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-profileConfiguration"></a>
The browser profile configuration associated with this session. Contains the profile identifier that links to persistent browser data such as cookies and local storage.  
Type: [BrowserProfileConfiguration](#API_BrowserProfileConfiguration) object

 ** [proxyConfiguration](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-proxyConfiguration"></a>
The active proxy configuration for this browser session. This field is only present if proxy configuration was provided when the session was started using `StartBrowserSession`. The configuration includes proxy servers, domain bypass rules and the proxy authentication credentials.  
Type: [ProxyConfiguration](#API_ProxyConfiguration) object

 ** [sessionId](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-sessionId"></a>
The identifier of the browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [sessionReplayArtifact](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-sessionReplayArtifact"></a>
The artifact containing the session replay information.  
Type: String

 ** [sessionTimeoutSeconds](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-sessionTimeoutSeconds"></a>
The timeout period for the browser session in seconds.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.

 ** [status](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-status"></a>
The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED` 

 ** [streams](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-streams"></a>
The streams associated with this browser session. These include the automation stream and live view stream.  
Type: [BrowserSessionStream](#API_BrowserSessionStream) object

 ** [viewPort](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-viewPort"></a>
The configuration that defines the dimensions of a browser viewport in a browser session. The viewport determines the visible area of web content and affects how web pages are rendered and displayed. Proper viewport configuration ensures that web content is displayed correctly for the agent's browsing tasks.  
Type: [ViewPort](#API_ViewPort) object

### Errors
<a name="API_GetBrowserSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetBrowserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetBrowserSession) 

## GetCodeInterpreterSession
<a name="API_GetCodeInterpreterSession"></a>

Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.

To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.

The following operations are related to `GetCodeInterpreterSession`:
+  [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html) 
+  [ListCodeInterpreterSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html) 
+  [StopCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html) 

### Request Syntax
<a name="API_GetCodeInterpreterSession_RequestSyntax"></a>

```
GET /code-interpreters/{{codeInterpreterIdentifier}}/sessions/get?sessionId={{sessionId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetCodeInterpreterSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_GetCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session.  
Required: Yes

 ** [sessionId](#API_GetCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-request-uri-sessionId"></a>
The unique identifier of the code interpreter session to retrieve.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

### Request Body
<a name="API_GetCodeInterpreterSession_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetCodeInterpreterSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "codeInterpreterIdentifier": "string",
   "createdAt": "string",
   "filesystemConfigurations": [ 
      { ... }
   ],
   "name": "string",
   "sessionId": "string",
   "sessionTimeoutSeconds": number,
   "status": "string"
}
```

### Response Elements
<a name="API_GetCodeInterpreterSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificates](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-certificates"></a>
The list of certificates installed in the code interpreter session.  
Type: Array of [Certificate](#API_Certificate) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [codeInterpreterIdentifier](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-codeInterpreterIdentifier"></a>
The identifier of the code interpreter.  
Type: String

 ** [createdAt](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-createdAt"></a>
The time at which the code interpreter session was created.  
Type: Timestamp

 ** [filesystemConfigurations](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-filesystemConfigurations"></a>
The file system configurations for the code interpreter session. Each entry describes an access point and its mount path.  
Type: Array of [ToolsFileSystemConfiguration](#API_ToolsFileSystemConfiguration) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [name](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-name"></a>
The name of the code interpreter session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [sessionId](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-sessionId"></a>
The identifier of the code interpreter session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [sessionTimeoutSeconds](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-sessionTimeoutSeconds"></a>
The timeout period for the code interpreter session in seconds.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.

 ** [status](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-status"></a>
The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED` 

### Errors
<a name="API_GetCodeInterpreterSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetCodeInterpreterSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 

## GetEvent
<a name="API_GetEvent"></a>

Retrieves information about a specific event in an AgentCore Memory resource.

To use this operation, you must have the `bedrock-agentcore:GetEvent` permission.

### Request Syntax
<a name="API_GetEvent_RequestSyntax"></a>

```
GET /memories/{{memoryId}}/actor/{{actorId}}/sessions/{{sessionId}}/events/{{eventId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actorId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-actorId"></a>
The identifier of the actor associated with the event.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [eventId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-eventId"></a>
The identifier of the event to retrieve.  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: Yes

 ** [memoryId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource containing the event.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-sessionId"></a>
The identifier of the session containing the event.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

### Request Body
<a name="API_GetEvent_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "event": { 
      "actorId": "string",
      "branch": { 
         "name": "string",
         "rootEventId": "string"
      },
      "eventId": "string",
      "eventTimestamp": number,
      "memoryId": "string",
      "metadata": { 
         "string" : { ... }
      },
      "payload": [ 
         { ... }
      ],
      "sessionId": "string"
   }
}
```

### Response Elements
<a name="API_GetEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [event](#API_GetEvent_ResponseSyntax) **   <a name="BedrockAgentCore-GetEvent-response-event"></a>
The requested event information.  
Type: [Event](#API_Event) object

### Errors
<a name="API_GetEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetEvent) 

## GetMemoryRecord
<a name="API_GetMemoryRecord"></a>

Retrieves a specific memory record from an AgentCore Memory resource.

To use this operation, you must have the `bedrock-agentcore:GetMemoryRecord` permission.

### Request Syntax
<a name="API_GetMemoryRecord_RequestSyntax"></a>

```
GET /memories/{{memoryId}}/memoryRecord/{{memoryRecordId}}?namespace={{namespace}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetMemoryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_GetMemoryRecord_RequestSyntax) **   <a name="BedrockAgentCore-GetMemoryRecord-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource containing the memory record.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [memoryRecordId](#API_GetMemoryRecord_RequestSyntax) **   <a name="BedrockAgentCore-GetMemoryRecord-request-uri-memoryRecordId"></a>
The identifier of the memory record to retrieve.  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** [namespace](#API_GetMemoryRecord_RequestSyntax) **   <a name="BedrockAgentCore-GetMemoryRecord-request-uri-namespace"></a>
The namespace of the memory record to retrieve. This value is used for IAM condition key authorization.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*` 

### Request Body
<a name="API_GetMemoryRecord_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetMemoryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memoryRecord": { 
      "content": { ... },
      "createdAt": number,
      "memoryRecordId": "string",
      "memoryStrategyId": "string",
      "metadata": { 
         "string" : { ... }
      },
      "namespaces": [ "string" ]
   }
}
```

### Response Elements
<a name="API_GetMemoryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memoryRecord](#API_GetMemoryRecord_ResponseSyntax) **   <a name="BedrockAgentCore-GetMemoryRecord-response-memoryRecord"></a>
The requested memory record.  
Type: [MemoryRecord](#API_MemoryRecord) object

### Errors
<a name="API_GetMemoryRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetMemoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetMemoryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetMemoryRecord) 

## GetPaymentInstrument
<a name="API_GetPaymentInstrument"></a>

Get a payment instrument by ID.

### Request Syntax
<a name="API_GetPaymentInstrument_RequestSyntax"></a>

```
POST /payments/getPaymentInstrument HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "paymentConnectorId": "{{string}}",
   "paymentInstrumentId": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetPaymentInstrument_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_GetPaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrument-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_GetPaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrument-request-userId"></a>
The user ID associated with this payment instrument.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_GetPaymentInstrument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentConnectorId](#API_GetPaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrument-request-paymentConnectorId"></a>
The ID of the payment connector.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: No

 ** [paymentInstrumentId](#API_GetPaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrument-request-paymentInstrumentId"></a>
The ID of the payment instrument to retrieve.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentManagerArn](#API_GetPaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrument-request-paymentManagerArn"></a>
The ARN of the payment manager that owns this payment instrument.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

### Response Syntax
<a name="API_GetPaymentInstrument_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "paymentInstrument": { 
      "createdAt": "string",
      "paymentConnectorId": "string",
      "paymentInstrumentDetails": { ... },
      "paymentInstrumentId": "string",
      "paymentInstrumentType": "string",
      "paymentManagerArn": "string",
      "status": "string",
      "updatedAt": "string",
      "userId": "string"
   }
}
```

### Response Elements
<a name="API_GetPaymentInstrument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [paymentInstrument](#API_GetPaymentInstrument_ResponseSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrument-response-paymentInstrument"></a>
The payment instrument details.  
Type: [PaymentInstrument](#API_PaymentInstrument) object

### Errors
<a name="API_GetPaymentInstrument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetPaymentInstrument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetPaymentInstrument) 

## GetPaymentInstrumentBalance
<a name="API_GetPaymentInstrumentBalance"></a>

Get the balance of a payment instrument.

### Request Syntax
<a name="API_GetPaymentInstrumentBalance_RequestSyntax"></a>

```
POST /payments/getPaymentInstrumentBalance HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "chain": "{{string}}",
   "paymentConnectorId": "{{string}}",
   "paymentInstrumentId": "{{string}}",
   "paymentManagerArn": "{{string}}",
   "token": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetPaymentInstrumentBalance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-userId"></a>
The user ID associated with this payment instrument.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_GetPaymentInstrumentBalance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [chain](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-chain"></a>
The specific blockchain chain to query balance on. Required because balances are chain-specific.  
Type: String  
Valid Values: `BASE | BASE_SEPOLIA | ETHEREUM | SOLANA | SOLANA_DEVNET`   
Required: Yes

 ** [paymentConnectorId](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-paymentConnectorId"></a>
The ID of the payment connector associated with this instrument.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [paymentInstrumentId](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-paymentInstrumentId"></a>
The ID of the payment instrument to query balance for.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentManagerArn](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-paymentManagerArn"></a>
The ARN of the payment manager that owns this payment instrument.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** [token](#API_GetPaymentInstrumentBalance_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-request-token"></a>
The token to query balance for. Only tokens supported for X402 payments are returned.  
Type: String  
Valid Values: `USDC`   
Required: Yes

### Response Syntax
<a name="API_GetPaymentInstrumentBalance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "paymentInstrumentId": "string",
   "tokenBalance": { 
      "amount": "string",
      "chain": "string",
      "decimals": number,
      "network": "string",
      "token": "string"
   }
}
```

### Response Elements
<a name="API_GetPaymentInstrumentBalance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [paymentInstrumentId](#API_GetPaymentInstrumentBalance_ResponseSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-response-paymentInstrumentId"></a>
The ID of the payment instrument.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}` 

 ** [tokenBalance](#API_GetPaymentInstrumentBalance_ResponseSyntax) **   <a name="BedrockAgentCore-GetPaymentInstrumentBalance-response-tokenBalance"></a>
The balance of the supported token on the requested chain.  
Type: [TokenBalance](#API_TokenBalance) object

### Errors
<a name="API_GetPaymentInstrumentBalance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetPaymentInstrumentBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance) 

## GetPaymentSession
<a name="API_GetPaymentSession"></a>

Get a payment session.

### Request Syntax
<a name="API_GetPaymentSession_RequestSyntax"></a>

```
POST /payments/getPaymentSession HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "paymentManagerArn": "{{string}}",
   "paymentSessionId": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetPaymentSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-userId"></a>
The user ID associated with this payment session.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_GetPaymentSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentManagerArn](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** [paymentSessionId](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-paymentSessionId"></a>
The ID of the payment session to retrieve.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

### Response Syntax
<a name="API_GetPaymentSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "paymentSession": { 
      "availableLimits": { 
         "availableSpendAmount": { 
            "currency": "string",
            "value": "string"
         },
         "updatedAt": "string"
      },
      "createdAt": "string",
      "expiryTimeInMinutes": number,
      "limits": { 
         "maxSpendAmount": { 
            "currency": "string",
            "value": "string"
         }
      },
      "paymentManagerArn": "string",
      "paymentSessionId": "string",
      "updatedAt": "string",
      "userId": "string"
   }
}
```

### Response Elements
<a name="API_GetPaymentSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [paymentSession](#API_GetPaymentSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-response-paymentSession"></a>
The payment session details.  
Type: [PaymentSession](#API_PaymentSession) object

### Errors
<a name="API_GetPaymentSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetPaymentSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetPaymentSession) 

## GetRecommendation
<a name="API_GetRecommendation"></a>

Retrieves detailed information about a recommendation, including its configuration, status, and results.

### Request Syntax
<a name="API_GetRecommendation_RequestSyntax"></a>

```
GET /recommendations/{{recommendationId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationId](#API_GetRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-GetRecommendation-request-uri-recommendationId"></a>
The unique identifier of the recommendation to retrieve.  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

### Request Body
<a name="API_GetRecommendation_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "kmsKeyArn": "string",
   "name": "string",
   "recommendationArn": "string",
   "recommendationConfig": { ... },
   "recommendationId": "string",
   "recommendationResult": { ... },
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_GetRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-createdAt"></a>
The timestamp when the recommendation was created.  
Type: Timestamp

 ** [description](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [kmsKeyArn](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt recommendation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-name"></a>
The name of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}` 

 ** [recommendationArn](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [recommendationConfig](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationConfig"></a>
The configuration for the recommendation.  
Type: [RecommendationConfig](#API_RecommendationConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [recommendationId](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationId"></a>
The unique identifier of the recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [recommendationResult](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationResult"></a>
The result of the recommendation, containing the optimized system prompt or tool descriptions. Only present when the recommendation status is `COMPLETED`.  
Type: [RecommendationResult](#API_RecommendationResult) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-status"></a>
The current status of the recommendation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

 ** [type](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-type"></a>
The type of recommendation.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION` 

 ** [updatedAt](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-updatedAt"></a>
The timestamp when the recommendation was last updated.  
Type: Timestamp

### Errors
<a name="API_GetRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetRecommendation) 

## GetResourceApiKey
<a name="API_GetResourceApiKey"></a>

Retrieves the API key associated with an API key credential provider.

### Request Syntax
<a name="API_GetResourceApiKey_RequestSyntax"></a>

```
POST /identities/api-key HTTP/1.1
Content-type: application/json

{
   "resourceCredentialProviderName": "{{string}}",
   "workloadIdentityToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetResourceApiKey_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_GetResourceApiKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceCredentialProviderName](#API_GetResourceApiKey_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceApiKey-request-resourceCredentialProviderName"></a>
The credential provider name for the resource from which you are retrieving the API key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [workloadIdentityToken](#API_GetResourceApiKey_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceApiKey-request-workloadIdentityToken"></a>
The identity token of the workload from which you want to retrieve the API key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Required: Yes

### Response Syntax
<a name="API_GetResourceApiKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiKey": "string"
}
```

### Response Elements
<a name="API_GetResourceApiKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKey](#API_GetResourceApiKey_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceApiKey-response-apiKey"></a>
The API key associated with the resource requested.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.

### Errors
<a name="API_GetResourceApiKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetResourceApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetResourceApiKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetResourceApiKey) 

## GetResourceOauth2Token
<a name="API_GetResourceOauth2Token"></a>

Returns the OAuth 2.0 token of the provided resource.

### Request Syntax
<a name="API_GetResourceOauth2Token_RequestSyntax"></a>

```
POST /identities/oauth2/token HTTP/1.1
Content-type: application/json

{
   "audiences": [ "{{string}}" ],
   "customParameters": { 
      "{{string}}" : "{{string}}" 
   },
   "customState": "{{string}}",
   "forceAuthentication": {{boolean}},
   "oauth2Flow": "{{string}}",
   "resourceCredentialProviderName": "{{string}}",
   "resourceOauth2ReturnUrl": "{{string}}",
   "resources": [ "{{string}}" ],
   "scopes": [ "{{string}}" ],
   "sessionUri": "{{string}}",
   "workloadIdentityToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetResourceOauth2Token_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_GetResourceOauth2Token_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audiences](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-audiences"></a>
The audiences to include in the token request. These are used to specify the intended recipients of the OAuth2 token.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [customParameters](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-customParameters"></a>
A map of custom parameters to include in the authorization request to the resource credential provider. These parameters are in addition to the standard OAuth 2.0 flow parameters, and will not override them.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Key Pattern: `[a-zA-Z0-9\-_\.]+`   
Value Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [customState](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-customState"></a>
An opaque string that will be sent back to the callback URL provided in resourceOauth2ReturnUrl. This state should be used to protect the callback URL of your application against CSRF attacks by ensuring the response corresponds to the original request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [forceAuthentication](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-forceAuthentication"></a>
Indicates whether to always initiate a new three-legged OAuth (3LO) flow, regardless of any existing session.  
Type: Boolean  
Required: No

 ** [oauth2Flow](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-oauth2Flow"></a>
The type of flow to be performed.  
Type: String  
Valid Values: `USER_FEDERATION | M2M | ON_BEHALF_OF_TOKEN_EXCHANGE`   
Required: Yes

 ** [resourceCredentialProviderName](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-resourceCredentialProviderName"></a>
The name of the resource's credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [resourceOauth2ReturnUrl](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-resourceOauth2ReturnUrl"></a>
The callback URL to redirect to after the OAuth 2.0 token retrieval is complete. This URL must be one of the provided URLs configured for the workload identity.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\w+:(\/?\/?)[^\s]+`   
Required: No

 ** [resources](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-resources"></a>
The resources to include in the token request. These are used to specify the target resources for which the OAuth2 token is being requested.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [scopes](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-scopes"></a>
The OAuth scopes being requested.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [sessionUri](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-sessionUri"></a>
Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `urn:ietf:params:oauth:request_uri:[a-zA-Z0-9-._~]+`   
Required: No

 ** [workloadIdentityToken](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-workloadIdentityToken"></a>
The identity token of the workload from which you want to retrieve the OAuth2 token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Required: Yes

### Response Syntax
<a name="API_GetResourceOauth2Token_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessToken": "string",
   "authorizationUrl": "string",
   "sessionStatus": "string",
   "sessionUri": "string"
}
```

### Response Elements
<a name="API_GetResourceOauth2Token_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessToken](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-accessToken"></a>
The OAuth 2.0 access token to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.

 ** [authorizationUrl](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-authorizationUrl"></a>
The URL to initiate the authorization process, provided when the access token requires user authorization.  
Type: String  
Length Constraints: Minimum length of 1.

 ** [sessionStatus](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-sessionStatus"></a>
Status indicating whether the user's authorization session is in progress or has failed. This helps determine the next steps in the OAuth2 authentication flow.  
Type: String  
Valid Values: `IN_PROGRESS | FAILED` 

 ** [sessionUri](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-sessionUri"></a>
Unique identifier for the user's authorization session for retrieving OAuth2 tokens. This matches the sessionId from the request and can be used to track the session state.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `urn:ietf:params:oauth:request_uri:[a-zA-Z0-9-._~]+` 

### Errors
<a name="API_GetResourceOauth2Token_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetResourceOauth2Token_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 

## GetResourcePaymentToken
<a name="API_GetResourcePaymentToken"></a>

Generates authentication tokens for payment providers that use vendor-specific authentication mechanisms.

### Request Syntax
<a name="API_GetResourcePaymentToken_RequestSyntax"></a>

```
POST /identities/payment/token HTTP/1.1
Content-type: application/json

{
   "paymentTokenRequest": { ... },
   "resourceCredentialProviderName": "{{string}}",
   "workloadIdentityToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetResourcePaymentToken_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_GetResourcePaymentToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentTokenRequest](#API_GetResourcePaymentToken_RequestSyntax) **   <a name="BedrockAgentCore-GetResourcePaymentToken-request-paymentTokenRequest"></a>
Vendor-specific token request input. Contains all request parameters in a type-safe, vendor-specific structure.  
Type: [PaymentTokenRequestInput](#API_PaymentTokenRequestInput) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [resourceCredentialProviderName](#API_GetResourcePaymentToken_RequestSyntax) **   <a name="BedrockAgentCore-GetResourcePaymentToken-request-resourceCredentialProviderName"></a>
Name of the payment credential provider to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [workloadIdentityToken](#API_GetResourcePaymentToken_RequestSyntax) **   <a name="BedrockAgentCore-GetResourcePaymentToken-request-workloadIdentityToken"></a>
Workload access token for authorization.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Required: Yes

### Response Syntax
<a name="API_GetResourcePaymentToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "paymentTokenResponse": { ... }
}
```

### Response Elements
<a name="API_GetResourcePaymentToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [paymentTokenResponse](#API_GetResourcePaymentToken_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourcePaymentToken-response-paymentTokenResponse"></a>
Vendor-specific token response output. Contains all response data in a type-safe, vendor-specific structure.  
Type: [PaymentTokenResponseOutput](#API_PaymentTokenResponseOutput) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

### Errors
<a name="API_GetResourcePaymentToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetResourcePaymentToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetResourcePaymentToken) 

## GetWorkloadAccessToken
<a name="API_GetWorkloadAccessToken"></a>

Obtains a workload access token for agentic workloads not acting on behalf of a user.

### Request Syntax
<a name="API_GetWorkloadAccessToken_RequestSyntax"></a>

```
POST /identities/GetWorkloadAccessToken HTTP/1.1
Content-type: application/json

{
   "workloadName": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetWorkloadAccessToken_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_GetWorkloadAccessToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [workloadName](#API_GetWorkloadAccessToken_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessToken-request-workloadName"></a>
The unique identifier for the registered workload.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: Yes

### Response Syntax
<a name="API_GetWorkloadAccessToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workloadAccessToken": "string"
}
```

### Response Elements
<a name="API_GetWorkloadAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workloadAccessToken](#API_GetWorkloadAccessToken_ResponseSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessToken-response-workloadAccessToken"></a>
An opaque token representing the identity of both the workload and the user.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.

### Errors
<a name="API_GetWorkloadAccessToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetWorkloadAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessToken) 

## GetWorkloadAccessTokenForJWT
<a name="API_GetWorkloadAccessTokenForJWT"></a>

Obtains a workload access token for agentic workloads acting on behalf of a user, using a JWT token.

### Request Syntax
<a name="API_GetWorkloadAccessTokenForJWT_RequestSyntax"></a>

```
POST /identities/GetWorkloadAccessTokenForJWT HTTP/1.1
Content-type: application/json

{
   "userToken": "{{string}}",
   "workloadName": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetWorkloadAccessTokenForJWT_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_GetWorkloadAccessTokenForJWT_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [userToken](#API_GetWorkloadAccessTokenForJWT_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForJWT-request-userToken"></a>
The OAuth 2.0 token issued by the user's identity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`   
Required: Yes

 ** [workloadName](#API_GetWorkloadAccessTokenForJWT_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForJWT-request-workloadName"></a>
The unique identifier for the registered workload.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: Yes

### Response Syntax
<a name="API_GetWorkloadAccessTokenForJWT_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workloadAccessToken": "string"
}
```

### Response Elements
<a name="API_GetWorkloadAccessTokenForJWT_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workloadAccessToken](#API_GetWorkloadAccessTokenForJWT_ResponseSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForJWT-response-workloadAccessToken"></a>
An opaque token representing the identity of both the workload and the user.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.

### Errors
<a name="API_GetWorkloadAccessTokenForJWT_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetWorkloadAccessTokenForJWT_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 

## GetWorkloadAccessTokenForUserId
<a name="API_GetWorkloadAccessTokenForUserId"></a>

Obtains a workload access token for agentic workloads acting on behalf of a user, using the user's ID.

### Request Syntax
<a name="API_GetWorkloadAccessTokenForUserId_RequestSyntax"></a>

```
POST /identities/GetWorkloadAccessTokenForUserId HTTP/1.1
Content-type: application/json

{
   "userId": "{{string}}",
   "workloadName": "{{string}}"
}
```

### URI Request Parameters
<a name="API_GetWorkloadAccessTokenForUserId_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_GetWorkloadAccessTokenForUserId_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [userId](#API_GetWorkloadAccessTokenForUserId_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForUserId-request-userId"></a>
The ID of the user for whom you are retrieving the access token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [workloadName](#API_GetWorkloadAccessTokenForUserId_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForUserId-request-workloadName"></a>
The name of the workload from which you want to retrieve the access token.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: Yes

### Response Syntax
<a name="API_GetWorkloadAccessTokenForUserId_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workloadAccessToken": "string"
}
```

### Response Elements
<a name="API_GetWorkloadAccessTokenForUserId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workloadAccessToken](#API_GetWorkloadAccessTokenForUserId_ResponseSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForUserId-response-workloadAccessToken"></a>
The access token for the specified workload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.

### Errors
<a name="API_GetWorkloadAccessTokenForUserId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_GetWorkloadAccessTokenForUserId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForUserId) 

## IngestData
<a name="API_IngestData"></a>

Submits content directly for ingestion to generate long-term memory records in a AgentCore Memory resource.

To use this operation, you must have the `bedrock-agentcore:IngestData` permission.

### Request Syntax
<a name="API_IngestData_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/ingest HTTP/1.1
Content-type: application/json

{
   "actorId": "{{string}}",
   "clientToken": "{{string}}",
   "contentTimestamp": {{number}},
   "extractionConfig": { 
      "namespaceVariables": { 
         "{{string}}" : "{{string}}" 
      }
   },
   "metadata": { 
      "{{string}}" : { ... }
   },
   "sessionId": "{{string}}",
   "source": { ... }
}
```

### URI Request Parameters
<a name="API_IngestData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource to ingest content into.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_IngestData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorId](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-actorId"></a>
The identifier of the actor associated with this content. An actor represents an entity that participates in sessions and generates content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [clientToken](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.  
Type: String  
Required: No

 ** [contentTimestamp](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-contentTimestamp"></a>
The timestamp of when the content occurred.  
Type: Timestamp  
Required: Yes

 ** [extractionConfig](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-extractionConfig"></a>
The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.  
Type: [ExtractionConfig](#API_ExtractionConfig) object  
Required: No

 ** [metadata](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-metadata"></a>
The key-value metadata to attach to the content.  
Type: String to [MetadataValue](#API_MetadataValue) object map  
Map Entries: Minimum number of 0 items. Maximum number of 15 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [sessionId](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-sessionId"></a>
The identifier of the session that the content belongs to. If not provided, a session identifier is generated and returned in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** [source](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-source"></a>
The content to ingest. Only inline content is supported.  
Type: [ContentSource](#API_ContentSource) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### Response Syntax
<a name="API_IngestData_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "sessionId": "string"
}
```

### Response Elements
<a name="API_IngestData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [sessionId](#API_IngestData_ResponseSyntax) **   <a name="BedrockAgentCore-IngestData-response-sessionId"></a>
The identifier of the session that the service ingested the content into. This value echoes the session identifier from the request, or the identifier that the service generated when you did not provide one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

### Errors
<a name="API_IngestData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_IngestData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/IngestData) 

## InvokeAgentRuntime
<a name="API_InvokeAgentRuntime"></a>

Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time. 

To invoke an agent, you can specify either the AgentCore Runtime ARN or the agent ID with an account ID, and provide a payload containing your request. When you use the agent ID instead of the full ARN, you don't need to URL-encode the identifier. You can optionally specify a qualifier to target a specific endpoint of the agent.

This operation supports streaming responses, allowing you to receive partial responses as they become available. We recommend using pagination to ensure that the operation returns quickly and successfully when processing large responses.

For example code, see [Invoke an AgentCore Runtime agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html). 

If you're integrating your agent with OAuth, you can't use the AWS SDK to call `InvokeAgentRuntime`. Instead, make a HTTPS request to `InvokeAgentRuntime`. For an example, see [Authenticate and authorize with Inbound Auth and Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html).

To use this operation, you must have the `bedrock-agentcore:InvokeAgentRuntime` permission. If you are making a call to `InvokeAgentRuntime` on behalf of a user ID with the `X-Amzn-Bedrock-AgentCore-Runtime-User-Id` header, You require permissions to both actions (`bedrock-agentcore:InvokeAgentRuntime` and `bedrock-agentcore:InvokeAgentRuntimeForUser`). 

### Request Syntax
<a name="API_InvokeAgentRuntime_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeArn}}/invocations?accountId={{accountId}}&qualifier={{qualifier}} HTTP/1.1
Content-Type: {{contentType}}
Accept: {{accept}}
Mcp-Session-Id: {{mcpSessionId}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
Mcp-Protocol-Version: {{mcpProtocolVersion}}
Mcp-Method: {{mcpMethod}}
Mcp-Name: {{mcpName}}
X-Amzn-Bedrock-AgentCore-Runtime-User-Id: {{runtimeUserId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}

{{payload}}
```

### URI Request Parameters
<a name="API_InvokeAgentRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-accept"></a>
The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [accountId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-uri-accountId"></a>
The identifier of the AWS account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for `agentRuntimeArn`.  
Pattern: `[0-9]{12}` 

 ** [agentRuntimeArn](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-uri-agentRuntimeArn"></a>
The identifier of the agent runtime to invoke. You can specify either the full AWS Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the `accountId` query parameter.  
Required: Yes

 ** [baggage](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-baggage"></a>
Additional context information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [contentType](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-contentType"></a>
The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [mcpMethod](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-mcpMethod"></a>
The MCP method being invoked. For example, `tools/call`, `resources/read`, or `prompts/get`.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [mcpName](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-mcpName"></a>
The name of the MCP resource, tool, or prompt being accessed. The value depends on the method:  
+  `tools/call` – The tool name.
+  `resources/read` – The resource URI.
+  `prompts/get` – The prompt name.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [mcpProtocolVersion](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-mcpProtocolVersion"></a>
The version of the MCP protocol being used.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [mcpSessionId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-mcpSessionId"></a>
The identifier of the MCP session.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [qualifier](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-uri-qualifier"></a>
The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.

 ** [runtimeSessionId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-runtimeSessionId"></a>
The identifier of the runtime session.  
Length Constraints: Minimum length of 33. Maximum length of 256.

 ** [runtimeUserId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-runtimeUserId"></a>
The identifier of the runtime user.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [traceId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [traceParent](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [traceState](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-traceState"></a>
The trace state information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 512.

### Request Body
<a name="API_InvokeAgentRuntime_RequestBody"></a>

The request accepts the following binary data.

 ** [payload](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-payload"></a>
The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user's request.  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: Yes

### Response Syntax
<a name="API_InvokeAgentRuntime_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
Mcp-Session-Id: {{mcpSessionId}}
Mcp-Protocol-Version: {{mcpProtocolVersion}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}
Content-Type: {{contentType}}

{{response}}
```

### Response Elements
<a name="API_InvokeAgentRuntime_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-statusCode"></a>
The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.

The response returns the following HTTP headers.

 ** [baggage](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-baggage"></a>
Additional context information for distributed tracing.

 ** [contentType](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-contentType"></a>
The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.

 ** [mcpProtocolVersion](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-mcpProtocolVersion"></a>
The version of the MCP protocol being used.

 ** [mcpSessionId](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-mcpSessionId"></a>
The identifier of the MCP session.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [runtimeSessionId](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-runtimeSessionId"></a>
The identifier of the runtime session.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [traceId](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-traceId"></a>
The trace identifier for request tracking.

 ** [traceParent](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-traceParent"></a>
The parent trace information for distributed tracing.

 ** [traceState](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-traceState"></a>
The trace state information for distributed tracing.

The response returns the following as the HTTP body.

 ** [response](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-response"></a>
The response data from the agent runtime. The format of this data depends on the specific agent configuration and the requested accept type. For most agents, this is a JSON object containing the agent's response to the user's request.

### Errors
<a name="API_InvokeAgentRuntime_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_InvokeAgentRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 

## InvokeAgentRuntimeCommand
<a name="API_InvokeAgentRuntimeCommand"></a>

Executes a command in a runtime session container and streams the output back to the caller. This operation allows you to run shell commands within the agent runtime environment and receive real-time streaming responses including standard output and standard error.

To invoke a command, you must specify the agent runtime ARN and a runtime session ID. The command execution supports streaming responses, allowing you to receive output as it becomes available through `contentStart`, `contentDelta`, and `contentStop` events.

To use this operation, you must have the `bedrock-agentcore:InvokeAgentRuntimeCommand` permission.

### Request Syntax
<a name="API_InvokeAgentRuntimeCommand_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeArn}}/commands?accountId={{accountId}}&qualifier={{qualifier}} HTTP/1.1
Content-Type: {{contentType}}
Accept: {{accept}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}
Content-type: application/json

{
   "command": "{{string}}",
   "timeout": {{number}}
}
```

### URI Request Parameters
<a name="API_InvokeAgentRuntimeCommand_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-accept"></a>
The desired MIME type for the response from the agent runtime command. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [accountId](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-uri-accountId"></a>
The identifier of the AWS account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for `agentRuntimeArn`.  
Pattern: `[0-9]{12}` 

 ** [agentRuntimeArn](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-uri-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the agent runtime on which to execute the command. This identifies the specific agent runtime environment where the command will run.  
Required: Yes

 ** [baggage](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-baggage"></a>
Additional context information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [contentType](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-contentType"></a>
The MIME type of the input data in the request payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [qualifier](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-uri-qualifier"></a>
The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.

 ** [runtimeSessionId](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-runtimeSessionId"></a>
The unique identifier of the runtime session in which to execute the command. This session ID is used to maintain state and context across multiple command invocations.  
Length Constraints: Minimum length of 33. Maximum length of 256.

 ** [traceId](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceState](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-traceState"></a>
The trace state information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 512.

### Request Body
<a name="API_InvokeAgentRuntimeCommand_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [command](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-command"></a>
The shell command to execute on the agent runtime. This command is executed in the runtime environment and its output is streamed back to the caller.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Required: Yes

 ** [timeout](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-timeout"></a>
The maximum duration in seconds to wait for the command to complete. If the command execution exceeds this timeout, it will be terminated. Default is 300 seconds. Minimum is 1 second. Maximum is 3600 seconds.  
Type: Integer  
Required: No

### Response Syntax
<a name="API_InvokeAgentRuntimeCommand_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}
Content-Type: {{contentType}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "chunk": { 
      "contentDelta": { 
         "stderr": "string",
         "stdout": "string"
      },
      "contentStart": { 
      },
      "contentStop": { 
         "exitCode": number,
         "status": "string"
      }
   },
   "internalServerException": { 
   },
   "resourceNotFoundException": { 
   },
   "runtimeClientError": { 
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

### Response Elements
<a name="API_InvokeAgentRuntimeCommand_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-statusCode"></a>
The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.

The response returns the following HTTP headers.

 ** [baggage](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-baggage"></a>
Additional context information for distributed tracing.

 ** [contentType](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-contentType"></a>
The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.

 ** [runtimeSessionId](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-runtimeSessionId"></a>
The unique identifier of the runtime session in which the command was executed.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [traceId](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-traceId"></a>
The trace identifier for request tracking.

 ** [traceParent](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-traceParent"></a>
The parent trace information for distributed tracing.

 ** [traceState](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-traceState"></a>
The trace state information for distributed tracing.

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-accessDeniedException"></a>
Exception events for error streaming.  
Type: Exception  
HTTP Status Code: 403

 ** [chunk](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-chunk"></a>
A response chunk containing command execution events such as content start, content delta, or content stop events.  
Type: [ResponseChunk](#API_ResponseChunk) object

 ** [internalServerException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404

 ** [runtimeClientError](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-runtimeClientError"></a>
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
Type: Exception  
HTTP Status Code: 424

 ** [serviceQuotaExceededException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402

 ** [throttlingException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400

### Errors
<a name="API_InvokeAgentRuntimeCommand_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_InvokeAgentRuntimeCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 

## InvokeBrowser
<a name="API_InvokeBrowser"></a>

Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.

You send a request with exactly one action in the `BrowserAction` union, and receive a corresponding result in the `BrowserActionResult` union.

The following operations are related to `InvokeBrowser`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 
+  [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html) 

### Request Syntax
<a name="API_InvokeBrowser_RequestSyntax"></a>

```
POST /browsers/{{browserIdentifier}}/sessions/invoke HTTP/1.1
x-amzn-browser-session-id: {{sessionId}}
Content-type: application/json

{
   "action": { ... }
}
```

### URI Request Parameters
<a name="API_InvokeBrowser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_InvokeBrowser_RequestSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-request-uri-browserIdentifier"></a>
The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with `StartBrowserSession`.  
Required: Yes

 ** [sessionId](#API_InvokeBrowser_RequestSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-request-sessionId"></a>
The unique identifier of the browser session on which to perform the action. This must be an active session created with `StartBrowserSession`.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

### Request Body
<a name="API_InvokeBrowser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_InvokeBrowser_RequestSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-request-action"></a>
The browser action to perform. Exactly one member of the `BrowserAction` union must be set per request.  
Type: [BrowserAction](#API_BrowserAction) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### Response Syntax
<a name="API_InvokeBrowser_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-browser-session-id: {{sessionId}}
Content-type: application/json

{
   "result": { ... }
}
```

### Response Elements
<a name="API_InvokeBrowser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [sessionId](#API_InvokeBrowser_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-response-sessionId"></a>
The unique identifier of the browser session on which the action was performed.  
Pattern: `[0-9a-zA-Z]{1,40}` 

The following data is returned in JSON format by the service.

 ** [result](#API_InvokeBrowser_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-response-result"></a>
The result of the browser action. The member set in the result corresponds to the action that was performed.  
Type: [BrowserActionResult](#API_BrowserActionResult) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

### Errors
<a name="API_InvokeBrowser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_InvokeBrowser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeBrowser) 

## InvokeCodeInterpreter
<a name="API_InvokeCodeInterpreter"></a>

Executes code within an active code interpreter session in Amazon Bedrock AgentCore. This operation processes the provided code, runs it in a secure environment, and returns the execution results including output, errors, and generated visualizations.

To execute code, you must specify the code interpreter identifier, session ID, and the code to run in the arguments parameter. The operation returns a stream containing the execution results, which can include text output, error messages, and data visualizations.

This operation is subject to request rate limiting based on your account's service quotas.

The following operations are related to `InvokeCodeInterpreter`:
+  [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html) 
+  [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html) 

### Request Syntax
<a name="API_InvokeCodeInterpreter_RequestSyntax"></a>

```
POST /code-interpreters/{{codeInterpreterIdentifier}}/tools/invoke HTTP/1.1
x-amzn-code-interpreter-session-id: {{sessionId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "arguments": { 
      "clearContext": {{boolean}},
      "code": "{{string}}",
      "command": "{{string}}",
      "content": [ 
         { 
            "blob": {{blob}},
            "path": "{{string}}",
            "text": "{{string}}"
         }
      ],
      "directoryPath": "{{string}}",
      "language": "{{string}}",
      "path": "{{string}}",
      "paths": [ "{{string}}" ],
      "runtime": "{{string}}",
      "taskId": "{{string}}"
   },
   "name": "{{string}}"
}
```

### URI Request Parameters
<a name="API_InvokeCodeInterpreter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with `StartCodeInterpreterSession`.  
Required: Yes

 ** [sessionId](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-sessionId"></a>
The unique identifier of the code interpreter session to use. This must be an active session created with `StartCodeInterpreterSession`. If the session has expired or been stopped, the request will fail.  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [traceId](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

### Request Body
<a name="API_InvokeCodeInterpreter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arguments](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-arguments"></a>
The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.  
Type: [ToolArguments](#API_ToolArguments) object  
Required: No

 ** [name](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-name"></a>
The name of the code interpreter to invoke.  
Type: String  
Valid Values: `executeCode | executeCommand | readFiles | listFiles | removeFiles | writeFiles | startCommandExecution | getTask | stopTask`   
Required: Yes

### Response Syntax
<a name="API_InvokeCodeInterpreter_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-code-interpreter-session-id: {{sessionId}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "conflictException": { 
   },
   "internalServerException": { 
   },
   "resourceNotFoundException": { 
   },
   "result": { 
      "content": [ 
         { 
            "data": blob,
            "description": "string",
            "mimeType": "string",
            "name": "string",
            "resource": { 
               "blob": blob,
               "mimeType": "string",
               "text": "string",
               "type": "string",
               "uri": "string"
            },
            "size": number,
            "text": "string",
            "type": "string",
            "uri": "string"
         }
      ],
      "isError": boolean,
      "structuredContent": { 
         "executionTime": number,
         "exitCode": number,
         "stderr": "string",
         "stdout": "string",
         "taskId": "string",
         "taskStatus": "string"
      }
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

### Response Elements
<a name="API_InvokeCodeInterpreter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [sessionId](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-sessionId"></a>
The identifier of the code interpreter session.  
Pattern: `[0-9a-zA-Z]{1,40}` 

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-accessDeniedException"></a>
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
Type: Exception  
HTTP Status Code: 403

 ** [conflictException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-conflictException"></a>
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
Type: Exception  
HTTP Status Code: 409

 ** [internalServerException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404

 ** [result](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-result"></a>
The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore. This structure contains the results of code execution, including textual output, structured data, and error information. Agents use these results to generate responses that incorporate computation, data analysis, and visualization.  
Type: [CodeInterpreterResult](#API_CodeInterpreterResult) object

 ** [serviceQuotaExceededException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402

 ** [throttlingException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400

### Errors
<a name="API_InvokeCodeInterpreter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_InvokeCodeInterpreter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 

## InvokeHarness
<a name="API_InvokeHarness"></a>

Operation to invoke a Harness.

### Request Syntax
<a name="API_InvokeHarness_RequestSyntax"></a>

```
POST /harnesses/invoke?harnessArn={{harnessArn}}&qualifier={{qualifier}} HTTP/1.1
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
X-Amzn-Bedrock-AgentCore-Runtime-User-Id: {{runtimeUserId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
X-Amzn-Trace-Id: {{traceId}}
baggage: {{baggage}}
Content-type: application/json

{
   "actorId": "{{string}}",
   "allowedTools": [ "{{string}}" ],
   "maxIterations": {{number}},
   "maxTokens": {{number}},
   "messages": [ 
      { 
         "content": [ 
            { ... }
         ],
         "role": "{{string}}"
      }
   ],
   "model": { ... },
   "skills": [ 
      { ... }
   ],
   "systemPrompt": [ 
      { ... }
   ],
   "timeoutSeconds": {{number}},
   "tools": [ 
      { 
         "config": { ... },
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

### URI Request Parameters
<a name="API_InvokeHarness_RequestParameters"></a>

The request uses the following URI parameters.

 ** [baggage](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-baggage"></a>
W3C Baggage header for user-defined context propagation. Format: key1=value1,key2=value2  
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [harnessArn](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-uri-harnessArn"></a>
The ARN of the harness to invoke.  
Pattern: `arn:([^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:harness/[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [qualifier](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-uri-qualifier"></a>
The endpoint name to invoke. If omitted, the DEFAULT endpoint is used.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [runtimeSessionId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-runtimeSessionId"></a>
The session ID for the invocation. Use the same session ID across requests to continue a conversation.  
Length Constraints: Minimum length of 33. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** [runtimeUserId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-runtimeUserId"></a>
An identifier for the end user making the request. This value is passed through to the runtime container.

 ** [traceId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-traceId"></a>
Trace ID for maintaining observability through the operation.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-traceParent"></a>
W3C trace context parent header containing version, trace ID, parent span ID, and trace flags.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceState](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-traceState"></a>
W3C trace context state header for vendor-specific trace information.  
Length Constraints: Minimum length of 0. Maximum length of 512.

### Request Body
<a name="API_InvokeHarness_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-actorId"></a>
The actor ID for memory operations. Overrides the actor ID configured on the harness.  
Type: String  
Required: No

 ** [allowedTools](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-allowedTools"></a>
The tools that the agent is allowed to use for this invocation. If specified, overrides the harness default.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `(\*|@?[^/]+(/[^/]+)?)`   
Required: No

 ** [maxIterations](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-maxIterations"></a>
The maximum number of iterations the agent loop can execute. If specified, overrides the harness default.  
Type: Integer  
Required: No

 ** [maxTokens](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-maxTokens"></a>
The maximum number of tokens the agent can generate per iteration. If specified, overrides the harness default.  
Type: Integer  
Required: No

 ** [messages](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-messages"></a>
The messages to send to the agent.  
Type: Array of [HarnessMessage](#API_HarnessMessage) objects  
Required: Yes

 ** [model](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-model"></a>
The model configuration to use for this invocation. If specified, overrides the harness default.  
Type: [HarnessModelConfiguration](#API_HarnessModelConfiguration) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [skills](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-skills"></a>
The skills available to the agent for this invocation. If specified, overrides the harness default.  
Type: Array of [HarnessSkill](#API_HarnessSkill) objects  
Required: No

 ** [systemPrompt](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-systemPrompt"></a>
The system prompt to use for this invocation. If specified, overrides the harness default.  
Type: Array of [HarnessSystemContentBlock](#API_HarnessSystemContentBlock) objects  
Required: No

 ** [timeoutSeconds](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-timeoutSeconds"></a>
The maximum duration in seconds for the agent loop execution. If specified, overrides the harness default.  
Type: Integer  
Required: No

 ** [tools](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-tools"></a>
The tools available to the agent for this invocation. If specified, overrides the harness default.  
Type: Array of [HarnessTool](#API_HarnessTool) objects  
Required: No

### Response Syntax
<a name="API_InvokeHarness_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contentBlockDelta": { 
      "contentBlockIndex": number,
      "delta": { ... }
   },
   "contentBlockStart": { 
      "contentBlockIndex": number,
      "start": { ... }
   },
   "contentBlockStop": { 
      "contentBlockIndex": number
   },
   "internalServerException": { 
   },
   "messageStart": { 
      "role": "string"
   },
   "messageStop": { 
      "stopReason": "string"
   },
   "metadata": { 
      "metrics": { 
         "latencyMs": number
      },
      "usage": { 
         "cacheReadInputTokens": number,
         "cacheWriteInputTokens": number,
         "inputTokens": number,
         "outputTokens": number,
         "totalTokens": number
      }
   },
   "runtimeClientError": { 
   },
   "validationException": { 
   }
}
```

### Response Elements
<a name="API_InvokeHarness_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contentBlockDelta](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-contentBlockDelta"></a>
A delta update to the current content block.  
Type: [HarnessContentBlockDeltaEvent](#API_HarnessContentBlockDeltaEvent) object

 ** [contentBlockStart](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-contentBlockStart"></a>
Indicates the start of a new content block.  
Type: [HarnessContentBlockStartEvent](#API_HarnessContentBlockStartEvent) object

 ** [contentBlockStop](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-contentBlockStop"></a>
Indicates the end of the current content block.  
Type: [HarnessContentBlockStopEvent](#API_HarnessContentBlockStopEvent) object

 ** [internalServerException](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500

 ** [messageStart](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-messageStart"></a>
Indicates the start of a new message from the agent.  
Type: [HarnessMessageStartEvent](#API_HarnessMessageStartEvent) object

 ** [messageStop](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-messageStop"></a>
Indicates the end of the current message.  
Type: [HarnessMessageStopEvent](#API_HarnessMessageStopEvent) object

 ** [metadata](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-metadata"></a>
Token usage and latency metrics for the invocation.  
Type: [HarnessMetadataEvent](#API_HarnessMetadataEvent) object

 ** [runtimeClientError](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-runtimeClientError"></a>
An error returned by the runtime container during agent execution.  
Type: Exception  
HTTP Status Code: 424

 ** [validationException](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400

### Errors
<a name="API_InvokeHarness_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_InvokeHarness_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeHarness) 

## ListABTests
<a name="API_ListABTests"></a>

Lists all A/B tests in the account.

### Request Syntax
<a name="API_ListABTests_RequestSyntax"></a>

```
GET /ab-tests?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

### URI Request Parameters
<a name="API_ListABTests_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListABTests_RequestSyntax) **   <a name="BedrockAgentCore-ListABTests-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListABTests_RequestSyntax) **   <a name="BedrockAgentCore-ListABTests-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.

### Request Body
<a name="API_ListABTests_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_ListABTests_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "abTests": [ 
      { 
         "abTestArn": "string",
         "abTestId": "string",
         "createdAt": number,
         "description": "string",
         "executionStatus": "string",
         "gatewayArn": "string",
         "name": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListABTests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [abTests](#API_ListABTests_ResponseSyntax) **   <a name="BedrockAgentCore-ListABTests-response-abTests"></a>
The list of A/B test summaries.  
Type: Array of [ABTestSummary](#API_ABTestSummary) objects

 ** [nextToken](#API_ListABTests_ResponseSyntax) **   <a name="BedrockAgentCore-ListABTests-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String

### Errors
<a name="API_ListABTests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListABTests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListABTests) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListABTests) 

## ListActors
<a name="API_ListActors"></a>

Lists all actors in an AgentCore Memory resource. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:ListActors` permission.

### Request Syntax
<a name="API_ListActors_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/actors HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListActors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_ListActors_RequestSyntax) **   <a name="BedrockAgentCore-ListActors-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource for which to list actors.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_ListActors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListActors_RequestSyntax) **   <a name="BedrockAgentCore-ListActors-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListActors_RequestSyntax) **   <a name="BedrockAgentCore-ListActors-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

### Response Syntax
<a name="API_ListActors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actorSummaries": [ 
      { 
         "actorId": "string"
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListActors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actorSummaries](#API_ListActors_ResponseSyntax) **   <a name="BedrockAgentCore-ListActors-response-actorSummaries"></a>
The list of actor summaries.  
Type: Array of [ActorSummary](#API_ActorSummary) objects

 ** [nextToken](#API_ListActors_ResponseSyntax) **   <a name="BedrockAgentCore-ListActors-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

### Errors
<a name="API_ListActors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListActors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListActors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListActors) 

## ListBatchEvaluations
<a name="API_ListBatchEvaluations"></a>

Lists all batch evaluations in the account, providing summary information about each evaluation's status and configuration.

### Request Syntax
<a name="API_ListBatchEvaluations_RequestSyntax"></a>

```
GET /evaluations/batch-evaluate?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

### URI Request Parameters
<a name="API_ListBatchEvaluations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListBatchEvaluations_RequestSyntax) **   <a name="BedrockAgentCore-ListBatchEvaluations-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListBatchEvaluations_RequestSyntax) **   <a name="BedrockAgentCore-ListBatchEvaluations-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.

### Request Body
<a name="API_ListBatchEvaluations_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_ListBatchEvaluations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchEvaluations": [ 
      { 
         "batchEvaluationArn": "string",
         "batchEvaluationId": "string",
         "batchEvaluationName": "string",
         "createdAt": "string",
         "description": "string",
         "errorDetails": [ "string" ],
         "evaluationResults": { 
            "evaluatorSummaries": [ 
               { 
                  "evaluatorId": "string",
                  "statistics": { 
                     "averageScore": number
                  },
                  "totalEvaluated": number,
                  "totalFailed": number
               }
            ],
            "numberOfSessionsCompleted": number,
            "numberOfSessionsFailed": number,
            "numberOfSessionsIgnored": number,
            "numberOfSessionsInProgress": number,
            "totalNumberOfSessions": number
         },
         "evaluators": [ 
            { 
               "evaluatorId": "string"
            }
         ],
         "insights": [ 
            { 
               "insightId": "string"
            }
         ],
         "kmsKeyArn": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListBatchEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluations](#API_ListBatchEvaluations_ResponseSyntax) **   <a name="BedrockAgentCore-ListBatchEvaluations-response-batchEvaluations"></a>
The list of batch evaluation summaries.  
Type: Array of [BatchEvaluationSummary](#API_BatchEvaluationSummary) objects

 ** [nextToken](#API_ListBatchEvaluations_ResponseSyntax) **   <a name="BedrockAgentCore-ListBatchEvaluations-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String

### Errors
<a name="API_ListBatchEvaluations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListBatchEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListBatchEvaluations) 

## ListBrowserSessions
<a name="API_ListBrowserSessions"></a>

Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.

You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.

We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.

The following operations are related to `ListBrowserSessions`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 

### Request Syntax
<a name="API_ListBrowserSessions_RequestSyntax"></a>

```
POST /browsers/{{browserIdentifier}}/sessions/list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListBrowserSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-uri-browserIdentifier"></a>
The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.  
Required: Yes

### Request Body
<a name="API_ListBrowserSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned `nextToken` value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [status](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-status"></a>
The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: No

### Response Syntax
<a name="API_ListBrowserSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [ 
      { 
         "browserIdentifier": "string",
         "createdAt": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "sessionId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListBrowserSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListBrowserSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-response-items"></a>
The list of browser sessions that match the specified criteria.  
Type: Array of [BrowserSessionSummary](#API_BrowserSessionSummary) objects

 ** [nextToken](#API_ListBrowserSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-response-nextToken"></a>
The token to use in a subsequent `ListBrowserSessions` request to get the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

### Errors
<a name="API_ListBrowserSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListBrowserSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 

## ListCodeInterpreterSessions
<a name="API_ListCodeInterpreterSessions"></a>

Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.

You can filter the results by code interpreter identifier and session status. The operation supports pagination to handle large result sets efficiently.

We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.

The following operations are related to `ListCodeInterpreterSessions`:
+  [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html) 
+  [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html) 

### Request Syntax
<a name="API_ListCodeInterpreterSessions_RequestSyntax"></a>

```
POST /code-interpreters/{{codeInterpreterIdentifier}}/sessions/list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListCodeInterpreterSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_ListCodeInterpreterSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListCodeInterpreterSessions-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter to list sessions for. If specified, only sessions for this code interpreter are returned. If not specified, sessions for all code interpreters are returned.  
Required: Yes

### Request Body
<a name="API_ListCodeInterpreterSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListCodeInterpreterSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListCodeInterpreterSessions-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned `nextToken` value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListCodeInterpreterSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListCodeInterpreterSessions-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [status](#API_ListCodeInterpreterSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListCodeInterpreterSessions-request-status"></a>
The status of the code interpreter sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: No

### Response Syntax
<a name="API_ListCodeInterpreterSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [ 
      { 
         "codeInterpreterIdentifier": "string",
         "createdAt": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "sessionId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListCodeInterpreterSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListCodeInterpreterSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListCodeInterpreterSessions-response-items"></a>
The list of code interpreter sessions that match the specified criteria.  
Type: Array of [CodeInterpreterSessionSummary](#API_CodeInterpreterSessionSummary) objects

 ** [nextToken](#API_ListCodeInterpreterSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListCodeInterpreterSessions-response-nextToken"></a>
The token to use in a subsequent `ListCodeInterpreterSessions` request to get the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

### Errors
<a name="API_ListCodeInterpreterSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListCodeInterpreterSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListCodeInterpreterSessions) 

## ListEvents
<a name="API_ListEvents"></a>

Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:ListEvents` permission.

### Request Syntax
<a name="API_ListEvents_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/actor/{{actorId}}/sessions/{{sessionId}} HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "branch": { 
         "includeParentBranches": {{boolean}},
         "name": "{{string}}"
      },
      "eventMetadata": [ 
         { 
            "left": { ... },
            "operator": "{{string}}",
            "right": { ... }
         }
      ]
   },
   "includePayloads": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actorId](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-uri-actorId"></a>
The identifier of the actor for which to list events.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [memoryId](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource for which to list events.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-uri-sessionId"></a>
The identifier of the session for which to list events.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

### Request Body
<a name="API_ListEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-filter"></a>
Filter criteria to apply when listing events.  
Type: [FilterInput](#API_FilterInput) object  
Required: No

 ** [includePayloads](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-includePayloads"></a>
Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.  
Type: Boolean  
Required: No

 ** [maxResults](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

### Response Syntax
<a name="API_ListEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "events": [ 
      { 
         "actorId": "string",
         "branch": { 
            "name": "string",
            "rootEventId": "string"
         },
         "eventId": "string",
         "eventTimestamp": number,
         "memoryId": "string",
         "metadata": { 
            "string" : { ... }
         },
         "payload": [ 
            { ... }
         ],
         "sessionId": "string"
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListEvents_ResponseSyntax) **   <a name="BedrockAgentCore-ListEvents-response-events"></a>
The list of events that match the specified criteria.  
Type: Array of [Event](#API_Event) objects

 ** [nextToken](#API_ListEvents_ResponseSyntax) **   <a name="BedrockAgentCore-ListEvents-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

### Errors
<a name="API_ListEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListEvents) 

## ListMemoryExtractionJobs
<a name="API_ListMemoryExtractionJobs"></a>

Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.

To use this operation, you must have the `bedrock-agentcore:ListMemoryExtractionJobs` permission.

### Request Syntax
<a name="API_ListMemoryExtractionJobs_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/extractionJobs HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "actorId": "{{string}}",
      "sessionId": "{{string}}",
      "status": "{{string}}",
      "strategyId": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListMemoryExtractionJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-uri-memoryId"></a>
The unique identifier of the memory to list extraction jobs for.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_ListMemoryExtractionJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-filter"></a>
Filter criteria to apply when listing extraction jobs.  
Type: [ExtractionJobFilterInput](#API_ExtractionJobFilterInput) object  
Required: No

 ** [maxResults](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [nextToken](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

### Response Syntax
<a name="API_ListMemoryExtractionJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [ 
      { 
         "actorId": "string",
         "failureReason": "string",
         "jobID": "string",
         "messages": { ... },
         "sessionId": "string",
         "status": "string",
         "strategyId": "string"
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListMemoryExtractionJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListMemoryExtractionJobs_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-response-jobs"></a>
List of extraction job metadata matching the specified criteria.  
Type: Array of [ExtractionJobMetadata](#API_ExtractionJobMetadata) objects

 ** [nextToken](#API_ListMemoryExtractionJobs_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-response-nextToken"></a>
Token to retrieve the next page of results, if available.  
Type: String

### Errors
<a name="API_ListMemoryExtractionJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListMemoryExtractionJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 

## ListMemoryRecords
<a name="API_ListMemoryRecords"></a>

Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:ListMemoryRecords` permission.

### Request Syntax
<a name="API_ListMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/memoryRecords HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "memoryStrategyId": "{{string}}",
   "metadataFilters": [ 
      { 
         "left": { ... },
         "operator": "{{string}}",
         "right": { ... }
      }
   ],
   "namespace": "{{string}}",
   "namespacePath": "{{string}}",
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource for which to list memory records.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_ListMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [memoryStrategyId](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-memoryStrategyId"></a>
The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** [metadataFilters](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-metadataFilters"></a>
A list of metadata filter expressions to scope the returned memory records.  
Type: Array of [MemoryMetadataFilterExpression](#API_MemoryMetadataFilterExpression) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

 ** [namespace](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-namespace"></a>
The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either `namespace` or `namespacePath` is required.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** [namespacePath](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-namespacePath"></a>
Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either `namespace` or `namespacePath` is required.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** [nextToken](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

### Response Syntax
<a name="API_ListMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memoryRecordSummaries": [ 
      { 
         "content": { ... },
         "createdAt": number,
         "memoryRecordId": "string",
         "memoryStrategyId": "string",
         "metadata": { 
            "string" : { ... }
         },
         "namespaces": [ "string" ],
         "score": number
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_ListMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memoryRecordSummaries](#API_ListMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-response-memoryRecordSummaries"></a>
The list of memory record summaries that match the specified criteria.  
Type: Array of [MemoryRecordSummary](#API_MemoryRecordSummary) objects

 ** [nextToken](#API_ListMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

### Errors
<a name="API_ListMemoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 

## ListPaymentInstruments
<a name="API_ListPaymentInstruments"></a>

List payment instruments for a manager.

### Request Syntax
<a name="API_ListPaymentInstruments_RequestSyntax"></a>

```
POST /payments/listPaymentInstruments HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "paymentConnectorId": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListPaymentInstruments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_ListPaymentInstruments_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_ListPaymentInstruments_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-request-userId"></a>
The user ID associated with the payment instruments.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_ListPaymentInstruments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPaymentInstruments_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-request-maxResults"></a>
Maximum number of results to return in a single response.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListPaymentInstruments_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-request-nextToken"></a>
Token for pagination to retrieve the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [paymentConnectorId](#API_ListPaymentInstruments_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-request-paymentConnectorId"></a>
The ID of the payment connector to filter by.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: No

 ** [paymentManagerArn](#API_ListPaymentInstruments_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-request-paymentManagerArn"></a>
The ARN of the payment manager that owns the payment instruments.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

### Response Syntax
<a name="API_ListPaymentInstruments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "paymentInstruments": [ 
      { 
         "createdAt": "string",
         "paymentConnectorId": "string",
         "paymentInstrumentId": "string",
         "paymentInstrumentType": "string",
         "paymentManagerArn": "string",
         "status": "string",
         "updatedAt": "string",
         "userId": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListPaymentInstruments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPaymentInstruments_ResponseSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-response-nextToken"></a>
Token for pagination to retrieve the next set of results.  
Type: String

 ** [paymentInstruments](#API_ListPaymentInstruments_ResponseSyntax) **   <a name="BedrockAgentCore-ListPaymentInstruments-response-paymentInstruments"></a>
List of payment instrument summaries matching the request criteria.  
Type: Array of [PaymentInstrumentSummary](#API_PaymentInstrumentSummary) objects

### Errors
<a name="API_ListPaymentInstruments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListPaymentInstruments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListPaymentInstruments) 

## ListPaymentSessions
<a name="API_ListPaymentSessions"></a>

List payment sessions.

### Request Syntax
<a name="API_ListPaymentSessions_RequestSyntax"></a>

```
POST /payments/listPaymentSessions HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListPaymentSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-userId"></a>
The user ID associated with the payment sessions.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_ListPaymentSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-maxResults"></a>
Maximum number of results to return in a single response.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-nextToken"></a>
Token for pagination to retrieve the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [paymentManagerArn](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-paymentManagerArn"></a>
The ARN of the payment manager that owns the sessions.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

### Response Syntax
<a name="API_ListPaymentSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "paymentSessions": [ 
      { 
         "createdAt": "string",
         "expiryTimeInMinutes": number,
         "paymentManagerArn": "string",
         "paymentSessionId": "string",
         "updatedAt": "string",
         "userId": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListPaymentSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPaymentSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-response-nextToken"></a>
Token for pagination to retrieve the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [paymentSessions](#API_ListPaymentSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-response-paymentSessions"></a>
List of payment session summaries matching the request criteria.  
Type: Array of [PaymentSessionSummary](#API_PaymentSessionSummary) objects

### Errors
<a name="API_ListPaymentSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListPaymentSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 

## ListRecommendations
<a name="API_ListRecommendations"></a>

Lists all recommendations in the account, with optional filtering by status.

### Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
GET /recommendations?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{statusFilter}} HTTP/1.1
```

### URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRecommendations_RequestSyntax) **   <a name="BedrockAgentCore-ListRecommendations-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListRecommendations_RequestSyntax) **   <a name="BedrockAgentCore-ListRecommendations-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [statusFilter](#API_ListRecommendations_RequestSyntax) **   <a name="BedrockAgentCore-ListRecommendations-request-uri-statusFilter"></a>
Optional filter to return only recommendations with the specified status.  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

### Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendationSummaries": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "name": "string",
         "recommendationArn": "string",
         "recommendationId": "string",
         "status": "string",
         "type": "string",
         "updatedAt": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="BedrockAgentCore-ListRecommendations-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [recommendationSummaries](#API_ListRecommendations_ResponseSyntax) **   <a name="BedrockAgentCore-ListRecommendations-response-recommendationSummaries"></a>
The list of recommendation summaries.  
Type: Array of [RecommendationSummary](#API_RecommendationSummary) objects

### Errors
<a name="API_ListRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListRecommendations) 

## ListSessions
<a name="API_ListSessions"></a>

Lists sessions in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

Empty sessions are automatically deleted after one day.

To use this operation, you must have the `bedrock-agentcore:ListSessions` permission.

### Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/actor/{{actorId}}/sessions HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "eventFilter": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actorId](#API_ListSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListSessions-request-uri-actorId"></a>
The identifier of the actor for which to list sessions.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [memoryId](#API_ListSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListSessions-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource for which to list sessions.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_ListSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListSessions-request-filter"></a>
Filter criteria to apply when listing sessions.  
Type: [SessionFilter](#API_SessionFilter) object  
Required: No

 ** [maxResults](#API_ListSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListSessions-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListSessions-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

### Response Syntax
<a name="API_ListSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sessionSummaries": [ 
      { 
         "actorId": "string",
         "createdAt": number,
         "sessionId": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListSessions-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

 ** [sessionSummaries](#API_ListSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListSessions-response-sessionSummaries"></a>
The list of session summaries that match the specified criteria.  
Type: Array of [SessionSummary](#API_SessionSummary) objects

### Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListSessions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListSessions) 

## ProcessPayment
<a name="API_ProcessPayment"></a>

Processes a payment using a payment instrument within a payment session.

### Request Syntax
<a name="API_ProcessPayment_RequestSyntax"></a>

```
POST /payments/processPayment HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "clientToken": "{{string}}",
   "paymentInput": { ... },
   "paymentInstrumentId": "{{string}}",
   "paymentManagerArn": "{{string}}",
   "paymentSessionId": "{{string}}",
   "paymentType": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ProcessPayment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-userId"></a>
The user ID associated with this payment.  
Length Constraints: Minimum length of 0. Maximum length of 120.

### Request Body
<a name="API_ProcessPayment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [paymentInput](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentInput"></a>
The payment input details specific to the payment type.  
Type: [PaymentInput](#API_PaymentInput) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [paymentInstrumentId](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentInstrumentId"></a>
The ID of the payment instrument to use.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentManagerArn](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentManagerArn"></a>
The ARN of the payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** [paymentSessionId](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentSessionId"></a>
The ID of the payment session.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentType](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentType"></a>
The type of payment to process.  
Type: String  
Valid Values: `CRYPTO_X402 | MPP`   
Required: Yes

### Response Syntax
<a name="API_ProcessPayment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "paymentInstrumentId": "string",
   "paymentManagerArn": "string",
   "paymentOutput": { ... },
   "paymentSessionId": "string",
   "paymentType": "string",
   "processPaymentId": "string",
   "status": "string",
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_ProcessPayment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-createdAt"></a>
The timestamp when the payment was created.  
Type: Timestamp

 ** [paymentInstrumentId](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentInstrumentId"></a>
The ID of the payment instrument used.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}` 

 ** [paymentManagerArn](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentManagerArn"></a>
The ARN of the payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}` 

 ** [paymentOutput](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentOutput"></a>
The payment output details specific to the payment type.  
Type: [PaymentOutput](#API_PaymentOutput) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [paymentSessionId](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentSessionId"></a>
The ID of the payment session used.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}` 

 ** [paymentType](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentType"></a>
The type of payment processed.  
Type: String  
Valid Values: `CRYPTO_X402 | MPP` 

 ** [processPaymentId](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-processPaymentId"></a>
The unique identifier of the processed payment.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

 ** [status](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-status"></a>
The status of the payment.  
Type: String  
Valid Values: `PROOF_GENERATED` 

 ** [updatedAt](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-updatedAt"></a>
The timestamp when the payment was last updated.  
Type: Timestamp

### Errors
<a name="API_ProcessPayment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** SubscriptionRequiredException **   
Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.    
 ** productName **   
The name of the product that requires a Marketplace subscription.  
 ** subscriptionUrl **   
The URL to the Marketplace listing where you can subscribe.
HTTP Status Code: 403

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_ProcessPayment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProcessPayment) 

## RetrieveMemoryRecords
<a name="API_RetrieveMemoryRecords"></a>

Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:RetrieveMemoryRecords` permission.

### Request Syntax
<a name="API_RetrieveMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/retrieve HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "namespace": "{{string}}",
   "namespacePath": "{{string}}",
   "nextToken": "{{string}}",
   "searchCriteria": { 
      "memoryStrategyId": "{{string}}",
      "metadataFilters": [ 
         { 
            "left": { ... },
            "operator": "{{string}}",
            "right": { ... }
         }
      ],
      "searchQuery": "{{string}}",
      "topK": {{number}}
   }
}
```

### URI Request Parameters
<a name="API_RetrieveMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_RetrieveMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource from which to retrieve memory records.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_RetrieveMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_RetrieveMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [namespace](#API_RetrieveMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-request-namespace"></a>
The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either `namespace` or `namespacePath` is required.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** [namespacePath](#API_RetrieveMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-request-namespacePath"></a>
Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either `namespace` or `namespacePath` is required.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** [nextToken](#API_RetrieveMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

 ** [searchCriteria](#API_RetrieveMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-request-searchCriteria"></a>
The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.  
Type: [SearchCriteria](#API_SearchCriteria) object  
Required: Yes

### Response Syntax
<a name="API_RetrieveMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memoryRecordSummaries": [ 
      { 
         "content": { ... },
         "createdAt": number,
         "memoryRecordId": "string",
         "memoryStrategyId": "string",
         "metadata": { 
            "string" : { ... }
         },
         "namespaces": [ "string" ],
         "score": number
      }
   ],
   "nextToken": "string"
}
```

### Response Elements
<a name="API_RetrieveMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memoryRecordSummaries](#API_RetrieveMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-response-memoryRecordSummaries"></a>
The list of memory record summaries that match the search criteria, ordered by relevance.  
Type: Array of [MemoryRecordSummary](#API_MemoryRecordSummary) objects

 ** [nextToken](#API_RetrieveMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-RetrieveMemoryRecords-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

### Errors
<a name="API_RetrieveMemoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_RetrieveMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords) 

## SaveBrowserSessionProfile
<a name="API_SaveBrowserSessionProfile"></a>

Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.

To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the `StartBrowserSession` operation to initialize new sessions with the stored browser state.

Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.

The following operations are related to `SaveBrowserSessionProfile`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 

### Request Syntax
<a name="API_SaveBrowserSessionProfile_RequestSyntax"></a>

```
PUT /browser-profiles/{{profileIdentifier}}/save HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "browserIdentifier": "{{string}}",
   "clientToken": "{{string}}",
   "sessionId": "{{string}}"
}
```

### URI Request Parameters
<a name="API_SaveBrowserSessionProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileIdentifier](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-uri-profileIdentifier"></a>
The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [traceId](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

### Request Body
<a name="API_SaveBrowserSessionProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [browserIdentifier](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-browserIdentifier"></a>
The unique identifier of the browser associated with the session from which to save the profile.  
Type: String  
Required: Yes

 ** [clientToken](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [sessionId](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-sessionId"></a>
The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

### Response Syntax
<a name="API_SaveBrowserSessionProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "lastUpdatedAt": "string",
   "profileIdentifier": "string",
   "sessionId": "string"
}
```

### Response Elements
<a name="API_SaveBrowserSessionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-browserIdentifier"></a>
The unique identifier of the browser associated with the session from which the profile was saved.  
Type: String

 ** [lastUpdatedAt](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-lastUpdatedAt"></a>
The timestamp when the browser profile was last updated. This value is in ISO 8601 format.  
Type: Timestamp

 ** [profileIdentifier](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-profileIdentifier"></a>
The unique identifier of the saved browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [sessionId](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-sessionId"></a>
The unique identifier of the browser session from which the profile was saved.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

### Errors
<a name="API_SaveBrowserSessionProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_SaveBrowserSessionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 

## SearchRegistryRecords
<a name="API_SearchRegistryRecords"></a>

 Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.

### Request Syntax
<a name="API_SearchRegistryRecords_RequestSyntax"></a>

```
POST /registry-records/search HTTP/1.1
Content-type: application/json

{
   "filters": {{JSON value}},
   "maxResults": {{number}},
   "registryIds": [ "{{string}}" ],
   "searchQuery": "{{string}}"
}
```

### URI Request Parameters
<a name="API_SearchRegistryRecords_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_SearchRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-filters"></a>
 A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (`$eq`, `$ne`, `$in`) and logical operators (`$and`, `$or`) on filterable fields (`name`, `descriptorType`, `version`). For example, to filter by descriptor type: `{"descriptorType": {"$eq": "MCP"}}`. To combine filters: `{"$and": [{"descriptorType": {"$eq": "MCP"}}, {"name": {"$eq": "my-tool"}}]}`.  
Type: JSON value  
Required: No

 ** [maxResults](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-maxResults"></a>
 The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 20.  
Required: No

 ** [registryIds](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-registryIds"></a>
 The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full AWS Resource Name (ARN) or the 12-character alphanumeric registry ID.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** [searchQuery](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-searchQuery"></a>
 The search query to find matching registry records.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

### Response Syntax
<a name="API_SearchRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "registryRecords": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "descriptors": { 
            "a2a": { 
               "agentCard": { 
                  "inlineContent": "string",
                  "schemaVersion": "string"
               }
            },
            "agentSkills": { 
               "skillDefinition": { 
                  "inlineContent": "string",
                  "schemaVersion": "string"
               },
               "skillMd": { 
                  "inlineContent": "string"
               }
            },
            "custom": { 
               "inlineContent": "string"
            },
            "mcp": { 
               "server": { 
                  "inlineContent": "string",
                  "schemaVersion": "string"
               },
               "tools": { 
                  "inlineContent": "string",
                  "protocolVersion": "string"
               }
            }
         },
         "descriptorType": "string",
         "name": "string",
         "recordArn": "string",
         "recordId": "string",
         "registryArn": "string",
         "status": "string",
         "updatedAt": "string",
         "version": "string"
      }
   ]
}
```

### Response Elements
<a name="API_SearchRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryRecords](#API_SearchRegistryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-response-registryRecords"></a>
 The list of registry records that match the search query, ordered by relevance.  
Type: Array of [RegistryRecordSummary](#API_RegistryRecordSummary) objects

### Errors
<a name="API_SearchRegistryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_SearchRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 

## StartBatchEvaluation
<a name="API_StartBatchEvaluation"></a>

Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.

### Request Syntax
<a name="API_StartBatchEvaluation_RequestSyntax"></a>

```
POST /evaluations/batch-evaluate HTTP/1.1
Content-type: application/json

{
   "batchEvaluationName": "{{string}}",
   "clientToken": "{{string}}",
   "dataSourceConfig": { ... },
   "description": "{{string}}",
   "evaluationMetadata": { ... },
   "evaluators": [ 
      { 
         "evaluatorId": "{{string}}"
      }
   ],
   "insights": [ 
      { 
         "insightId": "{{string}}"
      }
   ],
   "kmsKeyArn": "{{string}}",
   "outputConfig": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

### URI Request Parameters
<a name="API_StartBatchEvaluation_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_StartBatchEvaluation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [batchEvaluationName](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-batchEvaluationName"></a>
The name of the batch evaluation. Must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [clientToken](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [dataSourceConfig](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-dataSourceConfig"></a>
The data source configuration that specifies where to pull agent session traces from for evaluation.  
Type: [DataSourceConfig](#API_DataSourceConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [description](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Required: No

 ** [evaluationMetadata](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-evaluationMetadata"></a>
Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.  
Type: [EvaluationMetadata](#API_EvaluationMetadata) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [evaluators](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-evaluators"></a>
The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.  
Type: Array of [Evaluator](#API_Evaluator) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [insights](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-insights"></a>
The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.  
Type: Array of [Insight](#API_Insight) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [kmsKeyArn](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [outputConfig](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-outputConfig"></a>
Output destination configuration.  
Type: [OutputConfig](#API_OutputConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [tags](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-tags"></a>
A map of tag keys and values to associate with the batch evaluation.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### Response Syntax
<a name="API_StartBatchEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "batchEvaluationArn": "string",
   "batchEvaluationId": "string",
   "batchEvaluationName": "string",
   "createdAt": "string",
   "description": "string",
   "evaluators": [ 
      { 
         "evaluatorId": "string"
      }
   ],
   "insights": [ 
      { 
         "insightId": "string"
      }
   ],
   "kmsKeyArn": "string",
   "outputConfig": { ... },
   "status": "string",
   "tags": { 
      "string" : "string" 
   }
}
```

### Response Elements
<a name="API_StartBatchEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluationArn](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the created batch evaluation.  
Type: String

 ** [batchEvaluationId](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-batchEvaluationId"></a>
The unique identifier of the created batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [batchEvaluationName](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-batchEvaluationName"></a>
The name of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [createdAt](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-createdAt"></a>
The timestamp when the batch evaluation was created.  
Type: Timestamp

 ** [description](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [evaluators](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-evaluators"></a>
The list of evaluators applied during the batch evaluation.  
Type: Array of [Evaluator](#API_Evaluator) objects

 ** [insights](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-insights"></a>
The list of insight analyses applied during the batch evaluation.  
Type: Array of [Insight](#API_Insight) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [kmsKeyArn](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [outputConfig](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-outputConfig"></a>
The output configuration specifying where evaluation results are written.  
Type: [OutputConfig](#API_OutputConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-status"></a>
The status of the batch evaluation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING` 

 ** [tags](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-tags"></a>
The tags associated with the batch evaluation.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

### Errors
<a name="API_StartBatchEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StartBatchEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 

## StartBrowserSession
<a name="API_StartBrowserSession"></a>

Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.

To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the `StopBrowserSession` operation.

The following operations are related to `StartBrowserSession`:
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 
+  [UpdateBrowserStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html) 
+  [SaveBrowserSessionProfile](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html) 
+  [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html) 
+  [InvokeBrowser](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html) 

### Request Syntax
<a name="API_StartBrowserSession_RequestSyntax"></a>

```
PUT /browsers/{{browserIdentifier}}/sessions/start HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "clientToken": "{{string}}",
   "enterprisePolicies": [ 
      { 
         "location": { ... },
         "type": "{{string}}"
      }
   ],
   "extensions": [ 
      { 
         "location": { ... }
      }
   ],
   "filesystemConfigurations": [ 
      { ... }
   ],
   "name": "{{string}}",
   "profileConfiguration": { 
      "profileIdentifier": "{{string}}"
   },
   "proxyConfiguration": { 
      "bypass": { 
         "domainPatterns": [ "{{string}}" ]
      },
      "proxies": [ 
         { ... }
      ]
   },
   "sessionTimeoutSeconds": {{number}},
   "viewPort": { 
      "height": {{number}},
      "width": {{number}}
   }
}
```

### URI Request Parameters
<a name="API_StartBrowserSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-uri-browserIdentifier"></a>
The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.  
Required: Yes

 ** [traceId](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

### Request Body
<a name="API_StartBrowserSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificates](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-certificates"></a>
A list of certificates to install in the browser session.  
Type: Array of [Certificate](#API_Certificate) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [clientToken](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [enterprisePolicies](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-enterprisePolicies"></a>
A list of files containing enterprise policies for the browser.  
Type: Array of [BrowserEnterprisePolicy](#API_BrowserEnterprisePolicy) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: No

 ** [extensions](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-extensions"></a>
A list of browser extensions to load into the browser session.  
Type: Array of [BrowserExtension](#API_BrowserExtension) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [filesystemConfigurations](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-filesystemConfigurations"></a>
The file system configurations to mount into the browser session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.  
Type: Array of [ToolsFileSystemConfiguration](#API_ToolsFileSystemConfiguration) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [name](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-name"></a>
The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [profileConfiguration](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-profileConfiguration"></a>
The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.  
Type: [BrowserProfileConfiguration](#API_BrowserProfileConfiguration) object  
Required: No

 ** [proxyConfiguration](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-proxyConfiguration"></a>
Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via AWS Secrets Manager and domain-based routing rules. Requires `secretsmanager:GetSecretValue` IAM permission for the specified secret ARNs.  
Type: [ProxyConfiguration](#API_ProxyConfiguration) object  
Required: No

 ** [sessionTimeoutSeconds](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-sessionTimeoutSeconds"></a>
The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.  
Required: No

 ** [viewPort](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-viewPort"></a>
The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.  
Type: [ViewPort](#API_ViewPort) object  
Required: No

### Response Syntax
<a name="API_StartBrowserSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "createdAt": "string",
   "sessionId": "string",
   "streams": { 
      "automationStream": { 
         "streamEndpoint": "string",
         "streamStatus": "string"
      },
      "liveViewStream": { 
         "streamEndpoint": "string"
      }
   }
}
```

### Response Elements
<a name="API_StartBrowserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [createdAt](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-createdAt"></a>
The timestamp when the browser session was created.  
Type: Timestamp

 ** [sessionId](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-sessionId"></a>
The unique identifier of the created browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [streams](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-streams"></a>
The streams associated with this browser session. These include the automation stream and live view stream.  
Type: [BrowserSessionStream](#API_BrowserSessionStream) object

### Errors
<a name="API_StartBrowserSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StartBrowserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartBrowserSession) 

## StartCodeInterpreterSession
<a name="API_StartCodeInterpreterSession"></a>

Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.

To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the `StopCodeInterpreterSession` operation.

The following operations are related to `StartCodeInterpreterSession`:
+  [InvokeCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html) 
+  [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html) 
+  [StopCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html) 

### Request Syntax
<a name="API_StartCodeInterpreterSession_RequestSyntax"></a>

```
PUT /code-interpreters/{{codeInterpreterIdentifier}}/sessions/start HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "clientToken": "{{string}}",
   "filesystemConfigurations": [ 
      { ... }
   ],
   "name": "{{string}}",
   "sessionTimeoutSeconds": {{number}}
}
```

### URI Request Parameters
<a name="API_StartCodeInterpreterSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.  
Required: Yes

 ** [traceId](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

### Request Body
<a name="API_StartCodeInterpreterSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificates](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-certificates"></a>
A list of certificates to install in the code interpreter session.  
Type: Array of [Certificate](#API_Certificate) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [clientToken](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [filesystemConfigurations](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-filesystemConfigurations"></a>
The file system configurations to mount into the code interpreter session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.  
Type: Array of [ToolsFileSystemConfiguration](#API_ToolsFileSystemConfiguration) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [name](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-name"></a>
The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [sessionTimeoutSeconds](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-sessionTimeoutSeconds"></a>
The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.  
Required: No

### Response Syntax
<a name="API_StartCodeInterpreterSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeInterpreterIdentifier": "string",
   "createdAt": "string",
   "sessionId": "string"
}
```

### Response Elements
<a name="API_StartCodeInterpreterSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeInterpreterIdentifier](#API_StartCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-response-codeInterpreterIdentifier"></a>
The identifier of the code interpreter.  
Type: String

 ** [createdAt](#API_StartCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-response-createdAt"></a>
The time at which the code interpreter session was created.  
Type: Timestamp

 ** [sessionId](#API_StartCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-response-sessionId"></a>
The unique identifier of the created code interpreter session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

### Errors
<a name="API_StartCodeInterpreterSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StartCodeInterpreterSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 

## StartMemoryExtractionJob
<a name="API_StartMemoryExtractionJob"></a>

 Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records. When earlier extraction attempts have left events unprocessed, this job will pick up and extract those as well. 

To use this operation, you must have the `bedrock-agentcore:StartMemoryExtractionJob` permission.

### Request Syntax
<a name="API_StartMemoryExtractionJob_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/extractionJobs/start HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "extractionJob": { 
      "jobId": "{{string}}"
   }
}
```

### URI Request Parameters
<a name="API_StartMemoryExtractionJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_StartMemoryExtractionJob_RequestSyntax) **   <a name="BedrockAgentCore-StartMemoryExtractionJob-request-uri-memoryId"></a>
The unique identifier of the memory for which to start extraction jobs.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_StartMemoryExtractionJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartMemoryExtractionJob_RequestSyntax) **   <a name="BedrockAgentCore-StartMemoryExtractionJob-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotent processing of the request.  
Type: String  
Required: No

 ** [extractionJob](#API_StartMemoryExtractionJob_RequestSyntax) **   <a name="BedrockAgentCore-StartMemoryExtractionJob-request-extractionJob"></a>
Extraction job to start in this operation.  
Type: [ExtractionJob](#API_ExtractionJob) object  
Required: Yes

### Response Syntax
<a name="API_StartMemoryExtractionJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string"
}
```

### Response Elements
<a name="API_StartMemoryExtractionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_StartMemoryExtractionJob_ResponseSyntax) **   <a name="BedrockAgentCore-StartMemoryExtractionJob-response-jobId"></a>
Extraction Job ID that was attempted to start.  
Type: String

### Errors
<a name="API_StartMemoryExtractionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StartMemoryExtractionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartMemoryExtractionJob) 

## StartRecommendation
<a name="API_StartRecommendation"></a>

Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.

### Request Syntax
<a name="API_StartRecommendation_RequestSyntax"></a>

```
POST /recommendations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "recommendationConfig": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "type": "{{string}}"
}
```

### URI Request Parameters
<a name="API_StartRecommendation_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_StartRecommendation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Required: No

 ** [kmsKeyArn](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [name](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-name"></a>
The name of the recommendation. Must be unique within your account.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`   
Required: Yes

 ** [recommendationConfig](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-recommendationConfig"></a>
The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.  
Type: [RecommendationConfig](#API_RecommendationConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-tags"></a>
A map of tag keys and values to associate with the recommendation.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [type](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-type"></a>
The type of recommendation to generate. Valid values are `SYSTEM_PROMPT_RECOMMENDATION` for system prompt optimization or `TOOL_DESCRIPTION_RECOMMENDATION` for tool description optimization.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION`   
Required: Yes

### Response Syntax
<a name="API_StartRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "name": "string",
   "recommendationArn": "string",
   "recommendationConfig": { ... },
   "recommendationId": "string",
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_StartRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-createdAt"></a>
The timestamp when the recommendation was created.  
Type: Timestamp

 ** [description](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [name](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-name"></a>
The name of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}` 

 ** [recommendationArn](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-recommendationArn"></a>
The Amazon Resource Name (ARN) of the created recommendation.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [recommendationConfig](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-recommendationConfig"></a>
The configuration for the recommendation.  
Type: [RecommendationConfig](#API_RecommendationConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [recommendationId](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-recommendationId"></a>
The unique identifier of the created recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [status](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-status"></a>
The status of the recommendation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

 ** [type](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-type"></a>
The type of recommendation.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION` 

 ** [updatedAt](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-updatedAt"></a>
The timestamp when the recommendation was last updated.  
Type: Timestamp

### Errors
<a name="API_StartRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StartRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartRecommendation) 

## StopBatchEvaluation
<a name="API_StopBatchEvaluation"></a>

Stops a running batch evaluation. Sessions that have already been evaluated retain their results.

### Request Syntax
<a name="API_StopBatchEvaluation_RequestSyntax"></a>

```
POST /evaluations/batch-evaluate/{{batchEvaluationId}}/stop HTTP/1.1
```

### URI Request Parameters
<a name="API_StopBatchEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchEvaluationId](#API_StopBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StopBatchEvaluation-request-uri-batchEvaluationId"></a>
The unique identifier of the batch evaluation to stop.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_StopBatchEvaluation_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_StopBatchEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "batchEvaluationArn": "string",
   "batchEvaluationId": "string",
   "description": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_StopBatchEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluationArn](#API_StopBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StopBatchEvaluation-response-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the stopped batch evaluation.  
Type: String

 ** [batchEvaluationId](#API_StopBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StopBatchEvaluation-response-batchEvaluationId"></a>
The unique identifier of the stopped batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [description](#API_StopBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StopBatchEvaluation-response-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [status](#API_StopBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StopBatchEvaluation-response-status"></a>
The status of the batch evaluation after the stop request.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING` 

### Errors
<a name="API_StopBatchEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StopBatchEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StopBatchEvaluation) 

## StopBrowserSession
<a name="API_StopBrowserSession"></a>

Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.

To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using `StartBrowserSession`.

The following operations are related to `StopBrowserSession`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 

### Request Syntax
<a name="API_StopBrowserSession_RequestSyntax"></a>

```
PUT /browsers/{{browserIdentifier}}/sessions/stop?sessionId={{sessionId}} HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_StopBrowserSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-uri-browserIdentifier"></a>
The unique identifier of the browser associated with the session.  
Required: Yes

 ** [sessionId](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-uri-sessionId"></a>
The unique identifier of the browser session to stop.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** [traceId](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

### Request Body
<a name="API_StopBrowserSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

### Response Syntax
<a name="API_StopBrowserSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "lastUpdatedAt": "string",
   "sessionId": "string"
}
```

### Response Elements
<a name="API_StopBrowserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_StopBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [lastUpdatedAt](#API_StopBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-response-lastUpdatedAt"></a>
The time at which the browser session was last updated.  
Type: Timestamp

 ** [sessionId](#API_StopBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-response-sessionId"></a>
The identifier of the browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

### Errors
<a name="API_StopBrowserSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StopBrowserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StopBrowserSession) 

## StopCodeInterpreterSession
<a name="API_StopCodeInterpreterSession"></a>

Terminates an active code interpreter session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.

To stop a code interpreter session, you must specify both the code interpreter identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using `StartCodeInterpreterSession`.

The following operations are related to `StopCodeInterpreterSession`:
+  [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html) 
+  [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html) 

### Request Syntax
<a name="API_StopCodeInterpreterSession_RequestSyntax"></a>

```
PUT /code-interpreters/{{codeInterpreterIdentifier}}/sessions/stop?sessionId={{sessionId}} HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_StopCodeInterpreterSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_StopCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session.  
Required: Yes

 ** [sessionId](#API_StopCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-request-uri-sessionId"></a>
The unique identifier of the code interpreter session to stop.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** [traceId](#API_StopCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StopCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

### Request Body
<a name="API_StopCodeInterpreterSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StopCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

### Response Syntax
<a name="API_StopCodeInterpreterSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeInterpreterIdentifier": "string",
   "lastUpdatedAt": "string",
   "sessionId": "string"
}
```

### Response Elements
<a name="API_StopCodeInterpreterSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeInterpreterIdentifier](#API_StopCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-response-codeInterpreterIdentifier"></a>
The identifier of the code interpreter.  
Type: String

 ** [lastUpdatedAt](#API_StopCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-response-lastUpdatedAt"></a>
The timestamp when the code interpreter session was last updated.  
Type: Timestamp

 ** [sessionId](#API_StopCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopCodeInterpreterSession-response-sessionId"></a>
The identifier of the code interpreter session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

### Errors
<a name="API_StopCodeInterpreterSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StopCodeInterpreterSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StopCodeInterpreterSession) 

## StopRuntimeSession
<a name="API_StopRuntimeSession"></a>

Stops a session that is running in an running AgentCore Runtime agent.

### Request Syntax
<a name="API_StopRuntimeSession_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeArn}}/stopruntimesession?qualifier={{qualifier}} HTTP/1.1
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_StopRuntimeSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeArn](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-uri-agentRuntimeArn"></a>
The ARN of the agent that contains the session that you want to stop.  
Required: Yes

 ** [qualifier](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-uri-qualifier"></a>
Optional qualifier to specify an agent alias, such as `prod`code> or `dev`. If you don't provide a value, the DEFAULT alias is used. 

 ** [runtimeSessionId](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-runtimeSessionId"></a>
The ID of the session that you want to stop.  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Required: Yes

### Request Body
<a name="API_StopRuntimeSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-clientToken"></a>
Idempotent token used to identify the request. If you use the same token with multiple requests, the same response is returned. Use ClientToken to prevent the same request from being processed more than once.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

### Response Syntax
<a name="API_StopRuntimeSession_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
```

### Response Elements
<a name="API_StopRuntimeSession_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_StopRuntimeSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-response-statusCode"></a>
The status code of the request to stop the session.

The response returns the following HTTP headers.

 ** [runtimeSessionId](#API_StopRuntimeSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-response-runtimeSessionId"></a>
The ID of the session that you requested to stop.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

### Errors
<a name="API_StopRuntimeSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_StopRuntimeSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 

## UpdateABTest
<a name="API_UpdateABTest"></a>

Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.

### Request Syntax
<a name="API_UpdateABTest_RequestSyntax"></a>

```
PUT /ab-tests/{{abTestId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "evaluationConfig": { ... },
   "executionStatus": "{{string}}",
   "gatewayFilter": { 
      "targetPaths": [ "{{string}}" ]
   },
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "variants": [ 
      { 
         "name": "{{string}}",
         "variantConfiguration": { 
            "configurationBundle": { 
               "bundleArn": "{{string}}",
               "bundleVersion": "{{string}}"
            },
            "target": { 
               "name": "{{string}}"
            }
         },
         "weight": {{number}}
      }
   ]
}
```

### URI Request Parameters
<a name="API_UpdateABTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [abTestId](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-uri-abTestId"></a>
The unique identifier of the A/B test to update.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### Request Body
<a name="API_UpdateABTest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-description"></a>
The updated description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [evaluationConfig](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-evaluationConfig"></a>
The updated evaluation configuration.  
Type: [ABTestEvaluationConfig](#API_ABTestEvaluationConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [executionStatus](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-executionStatus"></a>
The updated execution status to enable or disable the A/B test.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED`   
Required: No

 ** [gatewayFilter](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-gatewayFilter"></a>
The updated gateway filter.  
Type: [GatewayFilter](#API_GatewayFilter) object  
Required: No

 ** [name](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-name"></a>
The updated name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: No

 ** [roleArn](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-roleArn"></a>
The updated IAM role ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

 ** [variants](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-variants"></a>
The updated list of variants.  
Type: Array of [Variant](#API_Variant) objects  
Array Members: Fixed number of 2 items.  
Required: No

### Response Syntax
<a name="API_UpdateABTest_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "executionStatus": "string",
   "status": "string",
   "updatedAt": number
}
```

### Response Elements
<a name="API_UpdateABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the updated A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-abTestId"></a>
The unique identifier of the updated A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [executionStatus](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-executionStatus"></a>
The execution status of the A/B test.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED` 

 ** [status](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-status"></a>
The status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

 ** [updatedAt](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-updatedAt"></a>
The timestamp when the A/B test was updated.  
Type: Timestamp

### Errors
<a name="API_UpdateABTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_UpdateABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UpdateABTest) 

## UpdateBrowserStream
<a name="API_UpdateBrowserStream"></a>

Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.

### Request Syntax
<a name="API_UpdateBrowserStream_RequestSyntax"></a>

```
PUT /browsers/{{browserIdentifier}}/sessions/streams/update?sessionId={{sessionId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "streamUpdate": { ... }
}
```

### URI Request Parameters
<a name="API_UpdateBrowserStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-uri-browserIdentifier"></a>
The identifier of the browser.  
Required: Yes

 ** [sessionId](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-uri-sessionId"></a>
The identifier of the browser session.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

### Request Body
<a name="API_UpdateBrowserStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [streamUpdate](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-streamUpdate"></a>
The update to apply to the browser stream.  
Type: [StreamUpdate](#API_StreamUpdate) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### Response Syntax
<a name="API_UpdateBrowserStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "sessionId": "string",
   "streams": { 
      "automationStream": { 
         "streamEndpoint": "string",
         "streamStatus": "string"
      },
      "liveViewStream": { 
         "streamEndpoint": "string"
      }
   },
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_UpdateBrowserStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [sessionId](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-sessionId"></a>
The identifier of the browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [streams](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-streams"></a>
The collection of streams associated with a browser session in Amazon Bedrock AgentCore. These streams provide different ways to interact with and observe the browser session, including programmatic control and visual representation of the browser content.  
Type: [BrowserSessionStream](#API_BrowserSessionStream) object

 ** [updatedAt](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-updatedAt"></a>
The time at which the browser stream was updated.  
Type: Timestamp

### Errors
<a name="API_UpdateBrowserStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

### See Also
<a name="API_UpdateBrowserStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 

# Data Types
<a name="API_Types"></a>

The Amazon Bedrock AgentCore API contains several data types that various actions use. This section describes each data type in detail.

**Note**  
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [A2aDescriptor](#API_A2aDescriptor) 
+  [ABTestEvaluationConfig](#API_ABTestEvaluationConfig) 
+  [ABTestResults](#API_ABTestResults) 
+  [ABTestSummary](#API_ABTestSummary) 
+  [ActorSummary](#API_ActorSummary) 
+  [AffectedSession](#API_AffectedSession) 
+  [AgentCardDefinition](#API_AgentCardDefinition) 
+  [AgentSkillsDescriptor](#API_AgentSkillsDescriptor) 
+  [AgentTracesConfig](#API_AgentTracesConfig) 
+  [Amount](#API_Amount) 
+  [AutomationStream](#API_AutomationStream) 
+  [AutomationStreamUpdate](#API_AutomationStreamUpdate) 
+  [AvailableLimits](#API_AvailableLimits) 
+  [BasicAuth](#API_BasicAuth) 
+  [BatchEvaluationSummary](#API_BatchEvaluationSummary) 
+  [BatchEvaluationTraceConfig](#API_BatchEvaluationTraceConfig) 
+  [Branch](#API_Branch) 
+  [BranchFilter](#API_BranchFilter) 
+  [BrowserAction](#API_BrowserAction) 
+  [BrowserActionResult](#API_BrowserActionResult) 
+  [BrowserEnterprisePolicy](#API_BrowserEnterprisePolicy) 
+  [BrowserExtension](#API_BrowserExtension) 
+  [BrowserProfileConfiguration](#API_BrowserProfileConfiguration) 
+  [BrowserSessionStream](#API_BrowserSessionStream) 
+  [BrowserSessionSummary](#API_BrowserSessionSummary) 
+  [Certificate](#API_Certificate) 
+  [CertificateLocation](#API_CertificateLocation) 
+  [CloudWatchFilterConfig](#API_CloudWatchFilterConfig) 
+  [CloudWatchLogsFilter](#API_CloudWatchLogsFilter) 
+  [CloudWatchLogsRule](#API_CloudWatchLogsRule) 
+  [CloudWatchLogsSource](#API_CloudWatchLogsSource) 
+  [CloudWatchLogsTraceConfig](#API_CloudWatchLogsTraceConfig) 
+  [CloudWatchOutputConfig](#API_CloudWatchOutputConfig) 
+  [CodeInterpreterResult](#API_CodeInterpreterResult) 
+  [CodeInterpreterSessionSummary](#API_CodeInterpreterSessionSummary) 
+  [CodeInterpreterStreamOutput](#API_CodeInterpreterStreamOutput) 
+  [CoinbaseCdpTokenRequestInput](#API_CoinbaseCdpTokenRequestInput) 
+  [CoinbaseCdpTokenResponseOutput](#API_CoinbaseCdpTokenResponseOutput) 
+  [ConfidenceInterval](#API_ConfidenceInterval) 
+  [ConfigurationBundleRef](#API_ConfigurationBundleRef) 
+  [ConfigurationBundleToolEntry](#API_ConfigurationBundleToolEntry) 
+  [Content](#API_Content) 
+  [ContentBlock](#API_ContentBlock) 
+  [ContentDeltaEvent](#API_ContentDeltaEvent) 
+  [ContentSource](#API_ContentSource) 
+  [ContentStartEvent](#API_ContentStartEvent) 
+  [ContentStopEvent](#API_ContentStopEvent) 
+  [Context](#API_Context) 
+  [ControlStats](#API_ControlStats) 
+  [Conversational](#API_Conversational) 
+  [CryptoX402PaymentInput](#API_CryptoX402PaymentInput) 
+  [CryptoX402PaymentOutput](#API_CryptoX402PaymentOutput) 
+  [CustomDescriptor](#API_CustomDescriptor) 
+  [DataSourceConfig](#API_DataSourceConfig) 
+  [Descriptors](#API_Descriptors) 
+  [EfsConfiguration](#API_EfsConfiguration) 
+  [EmbeddedCryptoWallet](#API_EmbeddedCryptoWallet) 
+  [EvaluationContent](#API_EvaluationContent) 
+  [EvaluationExpectedTrajectory](#API_EvaluationExpectedTrajectory) 
+  [EvaluationInput](#API_EvaluationInput) 
+  [EvaluationJobResults](#API_EvaluationJobResults) 
+  [EvaluationMetadata](#API_EvaluationMetadata) 
+  [EvaluationReferenceInput](#API_EvaluationReferenceInput) 
+  [EvaluationResultContent](#API_EvaluationResultContent) 
+  [EvaluationTarget](#API_EvaluationTarget) 
+  [Evaluator](#API_Evaluator) 
+  [EvaluatorMetric](#API_EvaluatorMetric) 
+  [EvaluatorStatistics](#API_EvaluatorStatistics) 
+  [EvaluatorSummary](#API_EvaluatorSummary) 
+  [Event](#API_Event) 
+  [EventMetadataFilterExpression](#API_EventMetadataFilterExpression) 
+  [ExecutionSummaryAffectedSession](#API_ExecutionSummaryAffectedSession) 
+  [ExecutionSummaryCluster](#API_ExecutionSummaryCluster) 
+  [ExecutionSummaryClusteringResultContent](#API_ExecutionSummaryClusteringResultContent) 
+  [ExternalProxy](#API_ExternalProxy) 
+  [ExtractionConfig](#API_ExtractionConfig) 
+  [ExtractionJob](#API_ExtractionJob) 
+  [ExtractionJobFilterInput](#API_ExtractionJobFilterInput) 
+  [ExtractionJobMessages](#API_ExtractionJobMessages) 
+  [ExtractionJobMetadata](#API_ExtractionJobMetadata) 
+  [FailureAnalysisResultContent](#API_FailureAnalysisResultContent) 
+  [FailureCategoryCluster](#API_FailureCategoryCluster) 
+  [FailureSpanDetail](#API_FailureSpanDetail) 
+  [FailureSubCategoryCluster](#API_FailureSubCategoryCluster) 
+  [FilterInput](#API_FilterInput) 
+  [FilterValue](#API_FilterValue) 
+  [GatewayFilter](#API_GatewayFilter) 
+  [GroundTruthSource](#API_GroundTruthSource) 
+  [GroundTruthTurn](#API_GroundTruthTurn) 
+  [GroundTruthTurnInput](#API_GroundTruthTurnInput) 
+  [HarnessAgentCoreBrowserConfig](#API_HarnessAgentCoreBrowserConfig) 
+  [HarnessAgentCoreCodeInterpreterConfig](#API_HarnessAgentCoreCodeInterpreterConfig) 
+  [HarnessAgentCoreGatewayConfig](#API_HarnessAgentCoreGatewayConfig) 
+  [HarnessBedrockModelConfig](#API_HarnessBedrockModelConfig) 
+  [HarnessContentBlock](#API_HarnessContentBlock) 
+  [HarnessContentBlockDelta](#API_HarnessContentBlockDelta) 
+  [HarnessContentBlockDeltaEvent](#API_HarnessContentBlockDeltaEvent) 
+  [HarnessContentBlockStart](#API_HarnessContentBlockStart) 
+  [HarnessContentBlockStartEvent](#API_HarnessContentBlockStartEvent) 
+  [HarnessContentBlockStopEvent](#API_HarnessContentBlockStopEvent) 
+  [HarnessGatewayOutboundAuth](#API_HarnessGatewayOutboundAuth) 
+  [HarnessGeminiModelConfig](#API_HarnessGeminiModelConfig) 
+  [HarnessInlineFunctionConfig](#API_HarnessInlineFunctionConfig) 
+  [HarnessLiteLlmModelConfig](#API_HarnessLiteLlmModelConfig) 
+  [HarnessMessage](#API_HarnessMessage) 
+  [HarnessMessageStartEvent](#API_HarnessMessageStartEvent) 
+  [HarnessMessageStopEvent](#API_HarnessMessageStopEvent) 
+  [HarnessMetadataEvent](#API_HarnessMetadataEvent) 
+  [HarnessModelConfiguration](#API_HarnessModelConfiguration) 
+  [HarnessOpenAiModelConfig](#API_HarnessOpenAiModelConfig) 
+  [HarnessReasoningContentBlock](#API_HarnessReasoningContentBlock) 
+  [HarnessReasoningContentBlockDelta](#API_HarnessReasoningContentBlockDelta) 
+  [HarnessReasoningTextBlock](#API_HarnessReasoningTextBlock) 
+  [HarnessRemoteMcpConfig](#API_HarnessRemoteMcpConfig) 
+  [HarnessSkill](#API_HarnessSkill) 
+  [HarnessSkillAwsSkillsSource](#API_HarnessSkillAwsSkillsSource) 
+  [HarnessSkillGitAuth](#API_HarnessSkillGitAuth) 
+  [HarnessSkillGitSource](#API_HarnessSkillGitSource) 
+  [HarnessSkillS3Source](#API_HarnessSkillS3Source) 
+  [HarnessStreamMetrics](#API_HarnessStreamMetrics) 
+  [HarnessSystemContentBlock](#API_HarnessSystemContentBlock) 
+  [HarnessTokenUsage](#API_HarnessTokenUsage) 
+  [HarnessTool](#API_HarnessTool) 
+  [HarnessToolConfiguration](#API_HarnessToolConfiguration) 
+  [HarnessToolResultBlock](#API_HarnessToolResultBlock) 
+  [HarnessToolResultBlockDelta](#API_HarnessToolResultBlockDelta) 
+  [HarnessToolResultBlockStart](#API_HarnessToolResultBlockStart) 
+  [HarnessToolResultContentBlock](#API_HarnessToolResultContentBlock) 
+  [HarnessToolResultMetadataBlockDelta](#API_HarnessToolResultMetadataBlockDelta) 
+  [HarnessToolUseBlock](#API_HarnessToolUseBlock) 
+  [HarnessToolUseBlockDelta](#API_HarnessToolUseBlockDelta) 
+  [HarnessToolUseBlockStart](#API_HarnessToolUseBlockStart) 
+  [IngestPayloadType](#API_IngestPayloadType) 
+  [InlineGroundTruth](#API_InlineGroundTruth) 
+  [InlineMemoryContent](#API_InlineMemoryContent) 
+  [InputContentBlock](#API_InputContentBlock) 
+  [Insight](#API_Insight) 
+  [InsightsFailureSignal](#API_InsightsFailureSignal) 
+  [InvokeAgentRuntimeCommandRequestBody](#API_InvokeAgentRuntimeCommandRequestBody) 
+  [InvokeAgentRuntimeCommandStreamOutput](#API_InvokeAgentRuntimeCommandStreamOutput) 
+  [InvokeHarnessStreamOutput](#API_InvokeHarnessStreamOutput) 
+  [KeyPressArguments](#API_KeyPressArguments) 
+  [KeyPressResult](#API_KeyPressResult) 
+  [KeyShortcutArguments](#API_KeyShortcutArguments) 
+  [KeyShortcutResult](#API_KeyShortcutResult) 
+  [KeyTypeArguments](#API_KeyTypeArguments) 
+  [KeyTypeResult](#API_KeyTypeResult) 
+  [LeftExpression](#API_LeftExpression) 
+  [LinkedAccount](#API_LinkedAccount) 
+  [LinkedAccountDeveloperJwt](#API_LinkedAccountDeveloperJwt) 
+  [LinkedAccountEmail](#API_LinkedAccountEmail) 
+  [LinkedAccountOAuth2](#API_LinkedAccountOAuth2) 
+  [LinkedAccountSms](#API_LinkedAccountSms) 
+  [LiveViewStream](#API_LiveViewStream) 
+  [McpDescriptor](#API_McpDescriptor) 
+  [MemoryContent](#API_MemoryContent) 
+  [MemoryJsonData](#API_MemoryJsonData) 
+  [MemoryMetadataFilterExpression](#API_MemoryMetadataFilterExpression) 
+  [MemoryRecord](#API_MemoryRecord) 
+  [MemoryRecordCreateInput](#API_MemoryRecordCreateInput) 
+  [MemoryRecordDeleteInput](#API_MemoryRecordDeleteInput) 
+  [MemoryRecordLeftExpression](#API_MemoryRecordLeftExpression) 
+  [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue) 
+  [MemoryRecordOutput](#API_MemoryRecordOutput) 
+  [MemoryRecordRightExpression](#API_MemoryRecordRightExpression) 
+  [MemoryRecordSummary](#API_MemoryRecordSummary) 
+  [MemoryRecordUpdateInput](#API_MemoryRecordUpdateInput) 
+  [MessageMetadata](#API_MessageMetadata) 
+  [MetadataValue](#API_MetadataValue) 
+  [MouseClickArguments](#API_MouseClickArguments) 
+  [MouseClickResult](#API_MouseClickResult) 
+  [MouseDragArguments](#API_MouseDragArguments) 
+  [MouseDragResult](#API_MouseDragResult) 
+  [MouseMoveArguments](#API_MouseMoveArguments) 
+  [MouseMoveResult](#API_MouseMoveResult) 
+  [MouseScrollArguments](#API_MouseScrollArguments) 
+  [MouseScrollResult](#API_MouseScrollResult) 
+  [MppPaymentInput](#API_MppPaymentInput) 
+  [MppPaymentOutput](#API_MppPaymentOutput) 
+  [OAuth2Authentication](#API_OAuth2Authentication) 
+  [OAuthCredentialProvider](#API_OAuthCredentialProvider) 
+  [OnlineEvaluationConfigSource](#API_OnlineEvaluationConfigSource) 
+  [OnlineEvaluationTraceConfig](#API_OnlineEvaluationTraceConfig) 
+  [OutputConfig](#API_OutputConfig) 
+  [PayloadType](#API_PayloadType) 
+  [PaymentInput](#API_PaymentInput) 
+  [PaymentInstrument](#API_PaymentInstrument) 
+  [PaymentInstrumentDetails](#API_PaymentInstrumentDetails) 
+  [PaymentInstrumentSummary](#API_PaymentInstrumentSummary) 
+  [PaymentOutput](#API_PaymentOutput) 
+  [PaymentSession](#API_PaymentSession) 
+  [PaymentSessionSummary](#API_PaymentSessionSummary) 
+  [PaymentTokenRequestInput](#API_PaymentTokenRequestInput) 
+  [PaymentTokenResponseOutput](#API_PaymentTokenResponseOutput) 
+  [PerVariantOnlineEvaluationConfig](#API_PerVariantOnlineEvaluationConfig) 
+  [Proxy](#API_Proxy) 
+  [ProxyBypass](#API_ProxyBypass) 
+  [ProxyConfiguration](#API_ProxyConfiguration) 
+  [ProxyCredentials](#API_ProxyCredentials) 
+  [RecommendationConfig](#API_RecommendationConfig) 
+  [RecommendationEvaluationConfig](#API_RecommendationEvaluationConfig) 
+  [RecommendationEvaluatorReference](#API_RecommendationEvaluatorReference) 
+  [RecommendationResult](#API_RecommendationResult) 
+  [RecommendationResultConfigurationBundle](#API_RecommendationResultConfigurationBundle) 
+  [RecommendationSummary](#API_RecommendationSummary) 
+  [RegistryRecordSummary](#API_RegistryRecordSummary) 
+  [ResourceContent](#API_ResourceContent) 
+  [ResourceLocation](#API_ResourceLocation) 
+  [ResponseChunk](#API_ResponseChunk) 
+  [RightExpression](#API_RightExpression) 
+  [RootCauseCluster](#API_RootCauseCluster) 
+  [S3FilesConfiguration](#API_S3FilesConfiguration) 
+  [S3Location](#API_S3Location) 
+  [ScreenshotArguments](#API_ScreenshotArguments) 
+  [ScreenshotResult](#API_ScreenshotResult) 
+  [SearchCriteria](#API_SearchCriteria) 
+  [SecretsManagerLocation](#API_SecretsManagerLocation) 
+  [ServerDefinition](#API_ServerDefinition) 
+  [SessionFilter](#API_SessionFilter) 
+  [SessionFilterConfig](#API_SessionFilterConfig) 
+  [SessionLimits](#API_SessionLimits) 
+  [SessionMetadataShape](#API_SessionMetadataShape) 
+  [SessionSummary](#API_SessionSummary) 
+  [SessionTraceIds](#API_SessionTraceIds) 
+  [SkillDefinition](#API_SkillDefinition) 
+  [SkillMdDefinition](#API_SkillMdDefinition) 
+  [SpanContext](#API_SpanContext) 
+  [StreamUpdate](#API_StreamUpdate) 
+  [StripePrivyTokenRequestInput](#API_StripePrivyTokenRequestInput) 
+  [StripePrivyTokenResponseOutput](#API_StripePrivyTokenResponseOutput) 
+  [SystemPromptConfig](#API_SystemPromptConfig) 
+  [SystemPromptConfigurationBundle](#API_SystemPromptConfigurationBundle) 
+  [SystemPromptRecommendationConfig](#API_SystemPromptRecommendationConfig) 
+  [SystemPromptRecommendationResult](#API_SystemPromptRecommendationResult) 
+  [TargetRef](#API_TargetRef) 
+  [TokenBalance](#API_TokenBalance) 
+  [TokenUsage](#API_TokenUsage) 
+  [ToolArguments](#API_ToolArguments) 
+  [ToolDescriptionConfig](#API_ToolDescriptionConfig) 
+  [ToolDescriptionConfigurationBundle](#API_ToolDescriptionConfigurationBundle) 
+  [ToolDescriptionInput](#API_ToolDescriptionInput) 
+  [ToolDescriptionOutput](#API_ToolDescriptionOutput) 
+  [ToolDescriptionRecommendationConfig](#API_ToolDescriptionRecommendationConfig) 
+  [ToolDescriptionRecommendationResult](#API_ToolDescriptionRecommendationResult) 
+  [ToolDescriptionSource](#API_ToolDescriptionSource) 
+  [ToolDescriptionTextInput](#API_ToolDescriptionTextInput) 
+  [ToolResultStructuredContent](#API_ToolResultStructuredContent) 
+  [ToolsDefinition](#API_ToolsDefinition) 
+  [ToolsFileSystemConfiguration](#API_ToolsFileSystemConfiguration) 
+  [UserIdentifier](#API_UserIdentifier) 
+  [UserIntentAffectedSession](#API_UserIntentAffectedSession) 
+  [UserIntentCluster](#API_UserIntentCluster) 
+  [UserIntentClusteringResultContent](#API_UserIntentClusteringResultContent) 
+  [ValidationExceptionField](#API_ValidationExceptionField) 
+  [Variant](#API_Variant) 
+  [VariantConfiguration](#API_VariantConfiguration) 
+  [VariantResult](#API_VariantResult) 
+  [ViewPort](#API_ViewPort) 

## A2aDescriptor
<a name="API_A2aDescriptor"></a>

 The A2A (Agent-to-Agent) descriptor configuration for a registry record.

### Contents
<a name="API_A2aDescriptor_Contents"></a>

 ** agentCard **   <a name="BedrockAgentCore-Type-A2aDescriptor-agentCard"></a>
 The agent card definition that describes the agent's capabilities and interface.  
Type: [AgentCardDefinition](#API_AgentCardDefinition) object  
Required: Yes

### See Also
<a name="API_A2aDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/A2aDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/A2aDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/A2aDescriptor) 

## ABTestEvaluationConfig
<a name="API_ABTestEvaluationConfig"></a>

The evaluation configuration for an A/B test, specifying which online evaluation configurations to use for measuring variant performance.

### Contents
<a name="API_ABTestEvaluationConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-ABTestEvaluationConfig-onlineEvaluationConfigArn"></a>
The Amazon Resource Name (ARN) of a single online evaluation configuration to use for both variants.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: No

 ** perVariantOnlineEvaluationConfig **   <a name="BedrockAgentCore-Type-ABTestEvaluationConfig-perVariantOnlineEvaluationConfig"></a>
Per-variant online evaluation configurations, allowing different evaluation settings for each variant.  
Type: Array of [PerVariantOnlineEvaluationConfig](#API_PerVariantOnlineEvaluationConfig) objects  
Array Members: Fixed number of 2 items.  
Required: No

### See Also
<a name="API_ABTestEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ABTestEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ABTestEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ABTestEvaluationConfig) 

## ABTestResults
<a name="API_ABTestResults"></a>

The statistical results of an A/B test.

### Contents
<a name="API_ABTestResults_Contents"></a>

 ** evaluatorMetrics **   <a name="BedrockAgentCore-Type-ABTestResults-evaluatorMetrics"></a>
The per-evaluator metrics comparing control and treatment variants.  
Type: Array of [EvaluatorMetric](#API_EvaluatorMetric) objects  
Required: Yes

 ** analysisTimestamp **   <a name="BedrockAgentCore-Type-ABTestResults-analysisTimestamp"></a>
The timestamp when the analysis was performed.  
Type: Timestamp  
Required: No

### See Also
<a name="API_ABTestResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ABTestResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ABTestResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ABTestResults) 

## ABTestSummary
<a name="API_ABTestSummary"></a>

Summary information about an A/B test.

### Contents
<a name="API_ABTestSummary_Contents"></a>

 ** abTestArn **   <a name="BedrockAgentCore-Type-ABTestSummary-abTestArn"></a>
The Amazon Resource Name (ARN) of the A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** abTestId **   <a name="BedrockAgentCore-Type-ABTestSummary-abTestId"></a>
The unique identifier of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-ABTestSummary-createdAt"></a>
The timestamp when the A/B test was created.  
Type: Timestamp  
Required: Yes

 ** executionStatus **   <a name="BedrockAgentCore-Type-ABTestSummary-executionStatus"></a>
The execution status of the A/B test.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED`   
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-ABTestSummary-name"></a>
The name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-ABTestSummary-status"></a>
The current status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-ABTestSummary-updatedAt"></a>
The timestamp when the A/B test was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-ABTestSummary-description"></a>
The description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** gatewayArn **   <a name="BedrockAgentCore-Type-ABTestSummary-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway used for traffic splitting.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: No

### See Also
<a name="API_ABTestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ABTestSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ABTestSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ABTestSummary) 

## ActorSummary
<a name="API_ActorSummary"></a>

Contains summary information about an actor in an AgentCore Memory resource.

### Contents
<a name="API_ActorSummary_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-ActorSummary-actorId"></a>
The unique identifier of the actor.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

### See Also
<a name="API_ActorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ActorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ActorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ActorSummary) 

## AffectedSession
<a name="API_AffectedSession"></a>

A session affected by a detected failure pattern, including root cause details.

### Contents
<a name="API_AffectedSession_Contents"></a>

 ** explanation **   <a name="BedrockAgentCore-Type-AffectedSession-explanation"></a>
An explanation of how the failure manifested in this session.  
Type: String  
Required: Yes

 ** failureSpans **   <a name="BedrockAgentCore-Type-AffectedSession-failureSpans"></a>
The list of spans where failures were detected in this session.  
Type: Array of [FailureSpanDetail](#API_FailureSpanDetail) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** fixType **   <a name="BedrockAgentCore-Type-AffectedSession-fixType"></a>
The type of fix recommended for this failure.  
Type: String  
Required: Yes

 ** recommendation **   <a name="BedrockAgentCore-Type-AffectedSession-recommendation"></a>
The specific fix recommendation for this session.  
Type: String  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-AffectedSession-sessionId"></a>
The unique identifier of the affected session.  
Type: String  
Required: Yes

### See Also
<a name="API_AffectedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AffectedSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AffectedSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AffectedSession) 

## AgentCardDefinition
<a name="API_AgentCardDefinition"></a>

 The agent card definition for A2A descriptors, including the schema version and inline content that describes the agent's capabilities.

### Contents
<a name="API_AgentCardDefinition_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-AgentCardDefinition-inlineContent"></a>
 The inline content of the agent card definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

 ** schemaVersion **   <a name="BedrockAgentCore-Type-AgentCardDefinition-schemaVersion"></a>
 The schema version of the agent card definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_AgentCardDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentCardDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentCardDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentCardDefinition) 

## AgentSkillsDescriptor
<a name="API_AgentSkillsDescriptor"></a>

 The agent skills descriptor configuration for a registry record.

### Contents
<a name="API_AgentSkillsDescriptor_Contents"></a>

 ** skillMd **   <a name="BedrockAgentCore-Type-AgentSkillsDescriptor-skillMd"></a>
 The skill description in markdown format.  
Type: [SkillMdDefinition](#API_SkillMdDefinition) object  
Required: Yes

 ** skillDefinition **   <a name="BedrockAgentCore-Type-AgentSkillsDescriptor-skillDefinition"></a>
 The structured skill definition with a schema version and content.  
Type: [SkillDefinition](#API_SkillDefinition) object  
Required: No

### See Also
<a name="API_AgentSkillsDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentSkillsDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentSkillsDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentSkillsDescriptor) 

## AgentTracesConfig
<a name="API_AgentTracesConfig"></a>

The configuration specifying where to read agent traces from for recommendation analysis.

### Contents
<a name="API_AgentTracesConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** batchEvaluation **   <a name="BedrockAgentCore-Type-AgentTracesConfig-batchEvaluation"></a>
Use a completed batch evaluation as the source of agent traces.  
Type: [BatchEvaluationTraceConfig](#API_BatchEvaluationTraceConfig) object  
Required: No

 ** cloudwatchLogs **   <a name="BedrockAgentCore-Type-AgentTracesConfig-cloudwatchLogs"></a>
Agent traces read from CloudWatch Logs.  
Type: [CloudWatchLogsTraceConfig](#API_CloudWatchLogsTraceConfig) object  
Required: No

 ** onlineEvaluation **   <a name="BedrockAgentCore-Type-AgentTracesConfig-onlineEvaluation"></a>
Agent traces from an online evaluation configuration over a specified time range.  
Type: [OnlineEvaluationTraceConfig](#API_OnlineEvaluationTraceConfig) object  
Required: No

 ** sessionSpans **   <a name="BedrockAgentCore-Type-AgentTracesConfig-sessionSpans"></a>
Agent traces provided as inline session spans in OpenTelemetry format.  
Type: Array of JSON values  
Array Members: Minimum number of 1 item. Maximum number of 20000 items.  
Required: No

### See Also
<a name="API_AgentTracesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentTracesConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentTracesConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentTracesConfig) 

## Amount
<a name="API_Amount"></a>

Represents a monetary amount with a currency.

### Contents
<a name="API_Amount_Contents"></a>

 ** currency **   <a name="BedrockAgentCore-Type-Amount-currency"></a>
The currency code for the amount.  
Type: String  
Valid Values: `USD`   
Required: Yes

 ** value **   <a name="BedrockAgentCore-Type-Amount-value"></a>
The numeric value of the amount.  
Type: String  
Required: Yes

### See Also
<a name="API_Amount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Amount) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Amount) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Amount) 

## AutomationStream
<a name="API_AutomationStream"></a>

The configuration for a stream that enables programmatic control of a browser session in Amazon Bedrock AgentCore. This stream provides a bidirectional communication channel for sending commands to the browser and receiving responses, allowing agents to automate web interactions such as navigation, form filling, and element clicking.

### Contents
<a name="API_AutomationStream_Contents"></a>

 ** streamEndpoint **   <a name="BedrockAgentCore-Type-AutomationStream-streamEndpoint"></a>
The endpoint URL for the automation stream. This URL is used to establish a WebSocket connection to the stream for sending commands and receiving responses.  
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 512.  
Required: Yes

 ** streamStatus **   <a name="BedrockAgentCore-Type-AutomationStream-streamStatus"></a>
The current status of the automation stream. This indicates whether the stream is available for use. Possible values include ACTIVE, CONNECTING, and DISCONNECTED.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

### See Also
<a name="API_AutomationStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AutomationStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AutomationStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AutomationStream) 

## AutomationStreamUpdate
<a name="API_AutomationStreamUpdate"></a>

Contains information about an update to an automation stream.

### Contents
<a name="API_AutomationStreamUpdate_Contents"></a>

 ** streamStatus **   <a name="BedrockAgentCore-Type-AutomationStreamUpdate-streamStatus"></a>
The status of the automation stream.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

### See Also
<a name="API_AutomationStreamUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AutomationStreamUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AutomationStreamUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AutomationStreamUpdate) 

## AvailableLimits
<a name="API_AvailableLimits"></a>

The available spending limits for a payment session.

### Contents
<a name="API_AvailableLimits_Contents"></a>

 ** availableSpendAmount **   <a name="BedrockAgentCore-Type-AvailableLimits-availableSpendAmount"></a>
The remaining available amount that can be spent.  
Type: [Amount](#API_Amount) object  
Required: No

 ** updatedAt **   <a name="BedrockAgentCore-Type-AvailableLimits-updatedAt"></a>
The timestamp when the available limits were last updated.  
Type: Timestamp  
Required: No

### See Also
<a name="API_AvailableLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AvailableLimits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AvailableLimits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AvailableLimits) 

## BasicAuth
<a name="API_BasicAuth"></a>

Configuration for HTTP Basic Authentication using credentials stored in AWS Secrets Manager. The secret must contain a JSON object with `username` and `password` string fields. Username allows alphanumeric characters and `@._+=-` symbols (pattern: `^[a-zA-Z0-9@._+=\-]+$`). Password allows alphanumeric characters and `@._+=-!#$%&*` symbols (pattern: `^[a-zA-Z0-9@._+=\-!#$%&*]+$`). Both fields have a maximum length of 256 characters.

### Contents
<a name="API_BasicAuth_Contents"></a>

 ** secretArn **   <a name="BedrockAgentCore-Type-BasicAuth-secretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing proxy credentials. The secret must be a JSON object with `username` and `password` string fields that meet validation requirements. The caller must have `secretsmanager:GetSecretValue` permission for this ARN. Example secret format: `{"username": "proxy_user", "password": "secure_password"}`   
Type: String  
Pattern: `arn:aws(-[a-z-]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`   
Required: Yes

### See Also
<a name="API_BasicAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BasicAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BasicAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BasicAuth) 

## BatchEvaluationSummary
<a name="API_BatchEvaluationSummary"></a>

Summary representation for list responses.

### Contents
<a name="API_BatchEvaluationSummary_Contents"></a>

 ** batchEvaluationArn **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the batch evaluation.  
Type: String  
Required: Yes

 ** batchEvaluationId **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-batchEvaluationId"></a>
The unique identifier of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** batchEvaluationName **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-batchEvaluationName"></a>
The name of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-createdAt"></a>
The timestamp when the batch evaluation was created.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-status"></a>
The current status of the batch evaluation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING`   
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Required: No

 ** errorDetails **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-errorDetails"></a>
The error details if the batch evaluation encountered failures.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Required: No

 ** evaluationResults **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-evaluationResults"></a>
The aggregated evaluation results.  
Type: [EvaluationJobResults](#API_EvaluationJobResults) object  
Required: No

 ** evaluators **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-evaluators"></a>
The list of evaluators applied during the batch evaluation.  
Type: Array of [Evaluator](#API_Evaluator) objects  
Required: No

 ** insights **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-insights"></a>
The list of insight analyses applied during the batch evaluation.  
Type: Array of [Insight](#API_Insight) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** kmsKeyArn **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** updatedAt **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-updatedAt"></a>
The timestamp when the batch evaluation was last updated.  
Type: Timestamp  
Required: No

### See Also
<a name="API_BatchEvaluationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchEvaluationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchEvaluationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchEvaluationSummary) 

## BatchEvaluationTraceConfig
<a name="API_BatchEvaluationTraceConfig"></a>

Configuration for using a batch evaluation as the source of agent traces for recommendations.

### Contents
<a name="API_BatchEvaluationTraceConfig_Contents"></a>

 ** batchEvaluationArn **   <a name="BedrockAgentCore-Type-BatchEvaluationTraceConfig-batchEvaluationArn"></a>
The ARN of the completed batch evaluation to use as the trace source.  
Type: String  
Required: Yes

### See Also
<a name="API_BatchEvaluationTraceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchEvaluationTraceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchEvaluationTraceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchEvaluationTraceConfig) 

## Branch
<a name="API_Branch"></a>

Contains information about a branch in an AgentCore Memory resource. Branches allow for organizing events into different conversation threads or paths.

### Contents
<a name="API_Branch_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-Branch-name"></a>
The name of the branch.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** rootEventId **   <a name="BedrockAgentCore-Type-Branch-rootEventId"></a>
The identifier of the root event for this branch.  
Type: String  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: No

### See Also
<a name="API_Branch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Branch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Branch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Branch) 

## BranchFilter
<a name="API_BranchFilter"></a>

Contains filter criteria for branches when listing events.

### Contents
<a name="API_BranchFilter_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-BranchFilter-name"></a>
The name of the branch to filter by.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** includeParentBranches **   <a name="BedrockAgentCore-Type-BranchFilter-includeParentBranches"></a>
Specifies whether to include parent branches in the results. Set to true to include parent branches, or false to exclude them.  
Type: Boolean  
Required: No

### See Also
<a name="API_BranchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BranchFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BranchFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BranchFilter) 

## BrowserAction
<a name="API_BrowserAction"></a>

The browser action to perform. Exactly one member must be set per request.

### Contents
<a name="API_BrowserAction_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** keyPress **   <a name="BedrockAgentCore-Type-BrowserAction-keyPress"></a>
Press a key one or more times.  
Type: [KeyPressArguments](#API_KeyPressArguments) object  
Required: No

 ** keyShortcut **   <a name="BedrockAgentCore-Type-BrowserAction-keyShortcut"></a>
Press a key combination.  
Type: [KeyShortcutArguments](#API_KeyShortcutArguments) object  
Required: No

 ** keyType **   <a name="BedrockAgentCore-Type-BrowserAction-keyType"></a>
Type a string of text.  
Type: [KeyTypeArguments](#API_KeyTypeArguments) object  
Required: No

 ** mouseClick **   <a name="BedrockAgentCore-Type-BrowserAction-mouseClick"></a>
Click at the specified coordinates.  
Type: [MouseClickArguments](#API_MouseClickArguments) object  
Required: No

 ** mouseDrag **   <a name="BedrockAgentCore-Type-BrowserAction-mouseDrag"></a>
Drag from a start position to an end position.  
Type: [MouseDragArguments](#API_MouseDragArguments) object  
Required: No

 ** mouseMove **   <a name="BedrockAgentCore-Type-BrowserAction-mouseMove"></a>
Move the cursor to the specified coordinates.  
Type: [MouseMoveArguments](#API_MouseMoveArguments) object  
Required: No

 ** mouseScroll **   <a name="BedrockAgentCore-Type-BrowserAction-mouseScroll"></a>
Scroll at the specified position.  
Type: [MouseScrollArguments](#API_MouseScrollArguments) object  
Required: No

 ** screenshot **   <a name="BedrockAgentCore-Type-BrowserAction-screenshot"></a>
Capture a full-screen screenshot.  
Type: [ScreenshotArguments](#API_ScreenshotArguments) object  
Required: No

### See Also
<a name="API_BrowserAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserAction) 

## BrowserActionResult
<a name="API_BrowserActionResult"></a>

The result of a browser action execution. Exactly one member is set, matching the action that was performed.

### Contents
<a name="API_BrowserActionResult_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** keyPress **   <a name="BedrockAgentCore-Type-BrowserActionResult-keyPress"></a>
The result of a key press action.  
Type: [KeyPressResult](#API_KeyPressResult) object  
Required: No

 ** keyShortcut **   <a name="BedrockAgentCore-Type-BrowserActionResult-keyShortcut"></a>
The result of a key shortcut action.  
Type: [KeyShortcutResult](#API_KeyShortcutResult) object  
Required: No

 ** keyType **   <a name="BedrockAgentCore-Type-BrowserActionResult-keyType"></a>
The result of a key type action.  
Type: [KeyTypeResult](#API_KeyTypeResult) object  
Required: No

 ** mouseClick **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseClick"></a>
The result of a mouse click action.  
Type: [MouseClickResult](#API_MouseClickResult) object  
Required: No

 ** mouseDrag **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseDrag"></a>
The result of a mouse drag action.  
Type: [MouseDragResult](#API_MouseDragResult) object  
Required: No

 ** mouseMove **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseMove"></a>
The result of a mouse move action.  
Type: [MouseMoveResult](#API_MouseMoveResult) object  
Required: No

 ** mouseScroll **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseScroll"></a>
The result of a mouse scroll action.  
Type: [MouseScrollResult](#API_MouseScrollResult) object  
Required: No

 ** screenshot **   <a name="BedrockAgentCore-Type-BrowserActionResult-screenshot"></a>
The result of a screenshot action.  
Type: [ScreenshotResult](#API_ScreenshotResult) object  
Required: No

### See Also
<a name="API_BrowserActionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserActionResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserActionResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserActionResult) 

## BrowserEnterprisePolicy
<a name="API_BrowserEnterprisePolicy"></a>

Browser enterprise policy configuration.

### Contents
<a name="API_BrowserEnterprisePolicy_Contents"></a>

 ** location **   <a name="BedrockAgentCore-Type-BrowserEnterprisePolicy-location"></a>
The location of the enterprise policy file.  
Type: [ResourceLocation](#API_ResourceLocation) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** type **   <a name="BedrockAgentCore-Type-BrowserEnterprisePolicy-type"></a>
The enterprise policy type. See BrowserEnterprisePolicyType.  
Type: String  
Valid Values: `MANAGED | RECOMMENDED`   
Required: No

### See Also
<a name="API_BrowserEnterprisePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserEnterprisePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserEnterprisePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserEnterprisePolicy) 

## BrowserExtension
<a name="API_BrowserExtension"></a>

Browser extension configuration.

### Contents
<a name="API_BrowserExtension_Contents"></a>

 ** location **   <a name="BedrockAgentCore-Type-BrowserExtension-location"></a>
The location where the browser extension files are stored. This specifies the source from which the extension will be loaded and installed.  
Type: [ResourceLocation](#API_ResourceLocation) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_BrowserExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserExtension) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserExtension) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserExtension) 

## BrowserProfileConfiguration
<a name="API_BrowserProfileConfiguration"></a>

The configuration for a browser profile in Amazon Bedrock AgentCore. A browser profile contains persistent browser data such as cookies and local storage that can be saved from one browser session and reused in subsequent sessions. Browser profiles enable continuity for tasks that require authentication, maintain user preferences, or depend on previously stored browser state.

### Contents
<a name="API_BrowserProfileConfiguration_Contents"></a>

 ** profileIdentifier **   <a name="BedrockAgentCore-Type-BrowserProfileConfiguration-profileIdentifier"></a>
The unique identifier of the browser profile. This identifier is used to reference the profile when starting new browser sessions or saving session data to the profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

### See Also
<a name="API_BrowserProfileConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserProfileConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserProfileConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserProfileConfiguration) 

## BrowserSessionStream
<a name="API_BrowserSessionStream"></a>

The collection of streams associated with a browser session in Amazon Bedrock AgentCore. These streams provide different ways to interact with and observe the browser session, including programmatic control and visual representation of the browser content.

### Contents
<a name="API_BrowserSessionStream_Contents"></a>

 ** automationStream **   <a name="BedrockAgentCore-Type-BrowserSessionStream-automationStream"></a>
The stream that enables programmatic control of the browser. This stream allows agents to perform actions such as navigating to URLs, clicking elements, and filling forms.  
Type: [AutomationStream](#API_AutomationStream) object  
Required: Yes

 ** liveViewStream **   <a name="BedrockAgentCore-Type-BrowserSessionStream-liveViewStream"></a>
The stream that provides a visual representation of the browser content. This stream allows agents to observe the current state of the browser, including rendered web pages and visual elements.  
Type: [LiveViewStream](#API_LiveViewStream) object  
Required: No

### See Also
<a name="API_BrowserSessionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserSessionStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserSessionStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserSessionStream) 

## BrowserSessionSummary
<a name="API_BrowserSessionSummary"></a>

A condensed representation of a browser session in Amazon Bedrock AgentCore. This structure contains key information about a browser session, including identifiers, status, and timestamps, without the full details of the session configuration and streams.

### Contents
<a name="API_BrowserSessionSummary_Contents"></a>

 ** browserIdentifier **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-browserIdentifier"></a>
The unique identifier of the browser associated with the session. This identifier specifies which browser environment is used for the session.  
Type: String  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-createdAt"></a>
The timestamp when the browser session was created. This value is in ISO 8601 format.  
Type: Timestamp  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-sessionId"></a>
The unique identifier of the browser session. This identifier is used in operations that interact with the session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-status"></a>
The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: Yes

 ** lastUpdatedAt **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-lastUpdatedAt"></a>
The timestamp when the browser session was last updated. This value is in ISO 8601 format.  
Type: Timestamp  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-name"></a>
The name of the browser session. This name helps identify and manage the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

### See Also
<a name="API_BrowserSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserSessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserSessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserSessionSummary) 

## Certificate
<a name="API_Certificate"></a>

A certificate to install in the browser or code interpreter session.

### Contents
<a name="API_Certificate_Contents"></a>

 ** location **   <a name="BedrockAgentCore-Type-Certificate-location"></a>
The location of the certificate.  
Type: [CertificateLocation](#API_CertificateLocation) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Certificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Certificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Certificate) 

## CertificateLocation
<a name="API_CertificateLocation"></a>

The location from which to retrieve a certificate.

### Contents
<a name="API_CertificateLocation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** secretsManager **   <a name="BedrockAgentCore-Type-CertificateLocation-secretsManager"></a>
The AWS Secrets Manager location of the certificate.  
Type: [SecretsManagerLocation](#API_SecretsManagerLocation) object  
Required: No

### See Also
<a name="API_CertificateLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CertificateLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CertificateLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CertificateLocation) 

## CloudWatchFilterConfig
<a name="API_CloudWatchFilterConfig"></a>

Filter configuration for narrowing down CloudWatch Logs sessions for evaluation.

### Contents
<a name="API_CloudWatchFilterConfig_Contents"></a>

 ** sessionIds **   <a name="BedrockAgentCore-Type-CloudWatchFilterConfig-sessionIds"></a>
A list of specific session IDs to evaluate. If specified, only these sessions are included in the evaluation.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Required: No

 ** sessionTraceIds **   <a name="BedrockAgentCore-Type-CloudWatchFilterConfig-sessionTraceIds"></a>
A list of session and trace ID pairs that restrict evaluation to specific traces within a session. If specified, only the listed traces are evaluated instead of the entire session.  
Type: Array of [SessionTraceIds](#API_SessionTraceIds) objects  
Array Members: Minimum number of 1 item. Maximum number of 500 items.  
Required: No

 ** timeRange **   <a name="BedrockAgentCore-Type-CloudWatchFilterConfig-timeRange"></a>
The time range filter for selecting sessions to evaluate.  
Type: [SessionFilterConfig](#API_SessionFilterConfig) object  
Required: No

### See Also
<a name="API_CloudWatchFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchFilterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchFilterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchFilterConfig) 

## CloudWatchLogsFilter
<a name="API_CloudWatchLogsFilter"></a>

A filter for narrowing down agent traces from CloudWatch Logs based on key-value comparisons.

### Contents
<a name="API_CloudWatchLogsFilter_Contents"></a>

 ** key **   <a name="BedrockAgentCore-Type-CloudWatchLogsFilter-key"></a>
The key or field name to filter on within the agent trace data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

 ** operator **   <a name="BedrockAgentCore-Type-CloudWatchLogsFilter-operator"></a>
The comparison operator to use for filtering.  
Type: String  
Valid Values: `Equals | NotEquals | GreaterThan | LessThan | GreaterThanOrEqual | LessThanOrEqual | Contains | NotContains`   
Required: Yes

 ** value **   <a name="BedrockAgentCore-Type-CloudWatchLogsFilter-value"></a>
The value to compare against using the specified operator.  
Type: [FilterValue](#API_FilterValue) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_CloudWatchLogsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsFilter) 

## CloudWatchLogsRule
<a name="API_CloudWatchLogsRule"></a>

A rule configuration for filtering agent traces from CloudWatch Logs.

### Contents
<a name="API_CloudWatchLogsRule_Contents"></a>

 ** filters **   <a name="BedrockAgentCore-Type-CloudWatchLogsRule-filters"></a>
The list of filters to apply when reading agent traces.  
Type: Array of [CloudWatchLogsFilter](#API_CloudWatchLogsFilter) objects  
Required: No

### See Also
<a name="API_CloudWatchLogsRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsRule) 

## CloudWatchLogsSource
<a name="API_CloudWatchLogsSource"></a>

The configuration for reading agent traces from CloudWatch Logs.

### Contents
<a name="API_CloudWatchLogsSource_Contents"></a>

 ** serviceNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-serviceNames"></a>
The list of agent service names to filter traces within the specified log groups.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** filterConfig **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-filterConfig"></a>
Optional filter configuration to narrow down which sessions to evaluate.  
Type: [CloudWatchFilterConfig](#API_CloudWatchFilterConfig) object  
Required: No

 ** logGroupNamePrefixes **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-logGroupNamePrefixes"></a>
The list of CloudWatch log group name prefixes to read agent traces from. Specify this instead of `logGroupNames` to match log groups by prefix. Maximum of 5 prefixes. Specify either `logGroupNames` or `logGroupNamePrefixes`, not both. One of the two is required.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[.\-_/#A-Za-z0-9]+`   
Required: No

 ** logGroupNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-logGroupNames"></a>
The list of CloudWatch log group names to read agent traces from. Maximum of 10 log groups.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Pattern: `[.\-_/#A-Za-z0-9]+`   
Required: No

### See Also
<a name="API_CloudWatchLogsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsSource) 

## CloudWatchLogsTraceConfig
<a name="API_CloudWatchLogsTraceConfig"></a>

Configuration for reading agent traces from CloudWatch Logs for recommendation analysis.

### Contents
<a name="API_CloudWatchLogsTraceConfig_Contents"></a>

 ** endTime **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-endTime"></a>
The end time of the time range to read traces from.  
Type: Timestamp  
Required: Yes

 ** logGroupArns **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-logGroupArns"></a>
The list of CloudWatch log group ARNs to read agent traces from.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** serviceNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-serviceNames"></a>
The list of service names to filter traces within the specified log groups.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

 ** startTime **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-startTime"></a>
The start time of the time range to read traces from.  
Type: Timestamp  
Required: Yes

 ** rule **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-rule"></a>
Optional rule configuration for filtering traces.  
Type: [CloudWatchLogsRule](#API_CloudWatchLogsRule) object  
Required: No

### See Also
<a name="API_CloudWatchLogsTraceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsTraceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsTraceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsTraceConfig) 

## CloudWatchOutputConfig
<a name="API_CloudWatchOutputConfig"></a>

CloudWatch Logs destination for batch evaluation results.

### Contents
<a name="API_CloudWatchOutputConfig_Contents"></a>

 ** logGroupName **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-logGroupName"></a>
The name of the CloudWatch log group where evaluation results will be written. This value doesn't apply when `resultDestination` is `SOURCE_LOG_GROUP`, because results are written back to the trace source log group. The name can't be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from the service-managed default group.  
Type: String  
Pattern: `$|^[.\-_/#A-Za-z0-9]+`   
Required: No

 ** logStreamName **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-logStreamName"></a>
The name of the CloudWatch log stream where evaluation results will be written.  
Type: String  
Pattern: `[^:*]*`   
Required: No

 ** metricsNamespace **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-metricsNamespace"></a>
The CloudWatch metrics namespace where evaluation result metrics are published. If you omit this value, the service publishes metrics to `Bedrock-AgentCore/Evaluations`. This value can't begin with `AWS/`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9._#/:-]+`   
Required: No

 ** resultDestination **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-resultDestination"></a>
The destination where evaluation results are written. Valid values:  
+  `DEDICATED_LOG_GROUP` (default) – Writes results to a dedicated result log group.
+  `SOURCE_LOG_GROUP` – Writes results back to the log group that the agent traces were read from. If you use this value, don't specify `logGroupName`.
Type: String  
Valid Values: `DEDICATED_LOG_GROUP | SOURCE_LOG_GROUP`   
Required: No

### See Also
<a name="API_CloudWatchOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchOutputConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchOutputConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchOutputConfig) 

## CodeInterpreterResult
<a name="API_CodeInterpreterResult"></a>

The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore. This structure contains the results of code execution, including textual output, structured data, and error information. Agents use these results to generate responses that incorporate computation, data analysis, and visualization.

### Contents
<a name="API_CodeInterpreterResult_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-CodeInterpreterResult-content"></a>
The textual content of the execution result. This includes standard output from the code execution, such as print statements, console output, and text representations of results.  
Type: Array of [ContentBlock](#API_ContentBlock) objects  
Required: Yes

 ** isError **   <a name="BedrockAgentCore-Type-CodeInterpreterResult-isError"></a>
Indicates whether the result represents an error. If true, the content contains error messages or exception information. If false, the content contains successful execution results.  
Type: Boolean  
Required: No

 ** structuredContent **   <a name="BedrockAgentCore-Type-CodeInterpreterResult-structuredContent"></a>
The structured content of the execution result. This includes additional metadata about the execution, such as execution time, memory usage, and structured representations of output data. The format depends on the specific code interpreter and execution context.  
Type: [ToolResultStructuredContent](#API_ToolResultStructuredContent) object  
Required: No

### See Also
<a name="API_CodeInterpreterResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CodeInterpreterResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CodeInterpreterResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CodeInterpreterResult) 

## CodeInterpreterSessionSummary
<a name="API_CodeInterpreterSessionSummary"></a>

A condensed representation of a code interpreter session in Amazon Bedrock AgentCore. This structure contains key information about a code interpreter session, including identifiers, status, and timestamps, without the full details of the session configuration.

### Contents
<a name="API_CodeInterpreterSessionSummary_Contents"></a>

 ** codeInterpreterIdentifier **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session. This identifier specifies which code interpreter environment is used for the session.  
Type: String  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-createdAt"></a>
The timestamp when the code interpreter session was created. This value is in ISO 8601 format.  
Type: Timestamp  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-sessionId"></a>
The unique identifier of the code interpreter session. This identifier is used in operations that interact with the session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-status"></a>
The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: Yes

 ** lastUpdatedAt **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-lastUpdatedAt"></a>
The timestamp when the code interpreter session was last updated. This value is in ISO 8601 format.  
Type: Timestamp  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-name"></a>
The name of the code interpreter session. This name helps identify and manage the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

### See Also
<a name="API_CodeInterpreterSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CodeInterpreterSessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CodeInterpreterSessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CodeInterpreterSessionSummary) 

## CodeInterpreterStreamOutput
<a name="API_CodeInterpreterStreamOutput"></a>

Contains output from a code interpreter stream.

### Contents
<a name="API_CodeInterpreterStreamOutput_Contents"></a>

 ** accessDeniedException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-accessDeniedException"></a>
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** conflictException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-conflictException"></a>
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** internalServerException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** resourceNotFoundException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** result **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-result"></a>
The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore. This structure contains the results of code execution, including textual output, structured data, and error information. Agents use these results to generate responses that incorporate computation, data analysis, and visualization.  
Type: [CodeInterpreterResult](#API_CodeInterpreterResult) object  
Required: No

 ** serviceQuotaExceededException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402  
Required: No

 ** throttlingException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

### See Also
<a name="API_CodeInterpreterStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CodeInterpreterStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CodeInterpreterStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CodeInterpreterStreamOutput) 

## CoinbaseCdpTokenRequestInput
<a name="API_CoinbaseCdpTokenRequestInput"></a>

Coinbase CDP token request parameters.

### Contents
<a name="API_CoinbaseCdpTokenRequestInput_Contents"></a>

 ** requestMethod **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestMethod"></a>
The HTTP method for the payment API request.  
Type: String  
Valid Values: `GET | POST | PUT | DELETE | PATCH`   
Required: Yes

 ** requestPath **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestPath"></a>
The path of the payment API request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `/[a-zA-Z0-9/_\-\.~%?=&]+`   
Required: Yes

 ** includeWalletAuthToken **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-includeWalletAuthToken"></a>
Set to true for wallet write operations (requires walletSecret configured).  
Type: Boolean  
Required: No

 ** requestBody **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestBody"></a>
Request body JSON — used to generate wallet auth JWT.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16384.  
Pattern: `[\u0009\u000A\u000D\u0020-\u007E]+`   
Required: No

 ** requestHost **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestHost"></a>
The host for the payment API request. Defaults to "api.cdp.coinbase.com".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\-\.]+`   
Required: No

### See Also
<a name="API_CoinbaseCdpTokenRequestInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenRequestInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenRequestInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenRequestInput) 

## CoinbaseCdpTokenResponseOutput
<a name="API_CoinbaseCdpTokenResponseOutput"></a>

Coinbase CDP token response.

### Contents
<a name="API_CoinbaseCdpTokenResponseOutput_Contents"></a>

 ** bearerToken **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenResponseOutput-bearerToken"></a>
Bearer Token for Authorization header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: Yes

 ** walletAuthToken **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenResponseOutput-walletAuthToken"></a>
Wallet Auth Token for X-Wallet-Auth header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

### See Also
<a name="API_CoinbaseCdpTokenResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenResponseOutput) 

## ConfidenceInterval
<a name="API_ConfidenceInterval"></a>

A confidence interval for a statistical measurement.

### Contents
<a name="API_ConfidenceInterval_Contents"></a>

 ** lower **   <a name="BedrockAgentCore-Type-ConfidenceInterval-lower"></a>
The lower bound of the confidence interval.  
Type: Double  
Required: No

 ** upper **   <a name="BedrockAgentCore-Type-ConfidenceInterval-upper"></a>
The upper bound of the confidence interval.  
Type: Double  
Required: No

### See Also
<a name="API_ConfidenceInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ConfidenceInterval) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ConfidenceInterval) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ConfidenceInterval) 

## ConfigurationBundleRef
<a name="API_ConfigurationBundleRef"></a>

A reference to a specific version of a configuration bundle.

### Contents
<a name="API_ConfigurationBundleRef_Contents"></a>

 ** bundleArn **   <a name="BedrockAgentCore-Type-ConfigurationBundleRef-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** bundleVersion **   <a name="BedrockAgentCore-Type-ConfigurationBundleRef-bundleVersion"></a>
The version of the configuration bundle.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

### See Also
<a name="API_ConfigurationBundleRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ConfigurationBundleRef) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ConfigurationBundleRef) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ConfigurationBundleRef) 

## ConfigurationBundleToolEntry
<a name="API_ConfigurationBundleToolEntry"></a>

Maps a tool name to its JSON path within a configuration bundle.

### Contents
<a name="API_ConfigurationBundleToolEntry_Contents"></a>

 ** toolDescriptionJsonPath **   <a name="BedrockAgentCore-Type-ConfigurationBundleToolEntry-toolDescriptionJsonPath"></a>
The JSON path within the configuration bundle's components that contains the tool description.  
Type: String  
Required: Yes

 ** toolName **   <a name="BedrockAgentCore-Type-ConfigurationBundleToolEntry-toolName"></a>
The name of the tool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_\-\.]+`   
Required: Yes

### See Also
<a name="API_ConfigurationBundleToolEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ConfigurationBundleToolEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ConfigurationBundleToolEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ConfigurationBundleToolEntry) 

## Content
<a name="API_Content"></a>

Contains the content of a memory item.

### Contents
<a name="API_Content_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="BedrockAgentCore-Type-Content-text"></a>
The text content of the memory item.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: No

### See Also
<a name="API_Content_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Content) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Content) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Content) 

## ContentBlock
<a name="API_ContentBlock"></a>

A block of content in a response.

### Contents
<a name="API_ContentBlock_Contents"></a>

 ** type **   <a name="BedrockAgentCore-Type-ContentBlock-type"></a>
The type of content in the block.  
Type: String  
Valid Values: `text | image | resource | resource_link`   
Required: Yes

 ** data **   <a name="BedrockAgentCore-Type-ContentBlock-data"></a>
The binary data content of the block.  
Type: Base64-encoded binary data object  
Required: No

 ** description **   <a name="BedrockAgentCore-Type-ContentBlock-description"></a>
The description of the content block.  
Type: String  
Required: No

 ** mimeType **   <a name="BedrockAgentCore-Type-ContentBlock-mimeType"></a>
The MIME type of the content.  
Type: String  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-ContentBlock-name"></a>
The name of the content block.  
Type: String  
Required: No

 ** resource **   <a name="BedrockAgentCore-Type-ContentBlock-resource"></a>
The resource associated with the content block.  
Type: [ResourceContent](#API_ResourceContent) object  
Required: No

 ** size **   <a name="BedrockAgentCore-Type-ContentBlock-size"></a>
The size of the content in bytes.  
Type: Long  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-ContentBlock-text"></a>
The text content of the block.  
Type: String  
Required: No

 ** uri **   <a name="BedrockAgentCore-Type-ContentBlock-uri"></a>
The URI of the content.  
Type: String  
Required: No

### See Also
<a name="API_ContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentBlock) 

## ContentDeltaEvent
<a name="API_ContentDeltaEvent"></a>

An event that contains incremental output from a command execution. This event streams standard output and standard error content as it becomes available during command execution.

### Contents
<a name="API_ContentDeltaEvent_Contents"></a>

 ** stderr **   <a name="BedrockAgentCore-Type-ContentDeltaEvent-stderr"></a>
The standard error content from the command execution. This field contains the incremental output written to stderr by the executing command.  
Type: String  
Required: No

 ** stdout **   <a name="BedrockAgentCore-Type-ContentDeltaEvent-stdout"></a>
The standard output content from the command execution. This field contains the incremental output written to stdout by the executing command.  
Type: String  
Required: No

### See Also
<a name="API_ContentDeltaEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentDeltaEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentDeltaEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentDeltaEvent) 

## ContentSource
<a name="API_ContentSource"></a>

The source of the content to ingest. Only inline content is supported.

### Contents
<a name="API_ContentSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inline **   <a name="BedrockAgentCore-Type-ContentSource-inline"></a>
The content included directly in the request.  
Type: [InlineMemoryContent](#API_InlineMemoryContent) object  
Required: No

### See Also
<a name="API_ContentSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentSource) 

## ContentStartEvent
<a name="API_ContentStartEvent"></a>

An event that signals the start of content streaming from a command execution. This event is sent when the command begins producing output.

### Contents
<a name="API_ContentStartEvent_Contents"></a>

The members of this exception structure are context-dependent.

### See Also
<a name="API_ContentStartEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentStartEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentStartEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentStartEvent) 

## ContentStopEvent
<a name="API_ContentStopEvent"></a>

An event that signals the completion of a command execution. This event contains the final status and exit code of the executed command.

### Contents
<a name="API_ContentStopEvent_Contents"></a>

 ** exitCode **   <a name="BedrockAgentCore-Type-ContentStopEvent-exitCode"></a>
The exit code returned by the executed command. An exit code of 0 indicates successful execution, -1 indicates a platform error, and values greater than 0 indicate command-specific errors.  
Type: Integer  
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-ContentStopEvent-status"></a>
The final status of the command execution. Valid values are `COMPLETED` for successful completion or `TIMED_OUT` if the command exceeded the specified timeout.  
Type: String  
Valid Values: `COMPLETED | TIMED_OUT`   
Required: Yes

### See Also
<a name="API_ContentStopEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentStopEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentStopEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentStopEvent) 

## Context
<a name="API_Context"></a>

 The contextual information associated with an evaluation, including span context details that identify the specific traces and sessions being evaluated within the agent's execution flow. 

### Contents
<a name="API_Context_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** spanContext **   <a name="BedrockAgentCore-Type-Context-spanContext"></a>
 The span context information that uniquely identifies the trace and span being evaluated, including session ID, trace ID, and span ID for precise targeting within the agent's execution flow.   
Type: [SpanContext](#API_SpanContext) object  
Required: No

### See Also
<a name="API_Context_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Context) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Context) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Context) 

## ControlStats
<a name="API_ControlStats"></a>

Statistics for the control variant in an A/B test.

### Contents
<a name="API_ControlStats_Contents"></a>

 ** mean **   <a name="BedrockAgentCore-Type-ControlStats-mean"></a>
The mean evaluation score for the control variant.  
Type: Double  
Required: Yes

 ** sampleSize **   <a name="BedrockAgentCore-Type-ControlStats-sampleSize"></a>
The number of sessions evaluated for the control variant.  
Type: Integer  
Required: Yes

 ** variantName **   <a name="BedrockAgentCore-Type-ControlStats-variantName"></a>
The name of the control variant.  
Type: String  
Required: Yes

### See Also
<a name="API_ControlStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ControlStats) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ControlStats) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ControlStats) 

## Conversational
<a name="API_Conversational"></a>

Contains conversational content for an event payload.

### Contents
<a name="API_Conversational_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-Conversational-content"></a>
The content of the conversation message.  
Type: [Content](#API_Content) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** role **   <a name="BedrockAgentCore-Type-Conversational-role"></a>
The role of the participant in the conversation (for example, "user" or "assistant").  
Type: String  
Valid Values: `ASSISTANT | USER | TOOL | OTHER`   
Required: Yes

### See Also
<a name="API_Conversational_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Conversational) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Conversational) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Conversational) 

## CryptoX402PaymentInput
<a name="API_CryptoX402PaymentInput"></a>

The input for a crypto X402 payment.

### Contents
<a name="API_CryptoX402PaymentInput_Contents"></a>

 ** payload **   <a name="BedrockAgentCore-Type-CryptoX402PaymentInput-payload"></a>
The X402 payment payload.  
Type: JSON value  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-CryptoX402PaymentInput-version"></a>
The version of the X402 protocol.  
Type: String  
Required: Yes

 ** permit2AllowanceLimit **   <a name="BedrockAgentCore-Type-CryptoX402PaymentInput-permit2AllowanceLimit"></a>
The maximum on-chain Permit2 allowance to grant before signing the payment authorization, in the asset's smallest denomination. This field is valid only for the `upto` (metered) scheme; supplying it for the `exact` scheme returns a validation error.  
When set, the service approves an ERC-20 allowance for this amount before processing the payment. The approval sets, rather than adds to, the wallet's allowance. Set this field only when the wallet needs approving, for example on its first `upto` payment, to avoid a redundant on-chain transaction. Omit the field to skip allowance handling. This is the default, and the only behavior for the `exact` scheme.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 78.  
Pattern: `[0-9]+`   
Required: No

### See Also
<a name="API_CryptoX402PaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CryptoX402PaymentInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CryptoX402PaymentInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CryptoX402PaymentInput) 

## CryptoX402PaymentOutput
<a name="API_CryptoX402PaymentOutput"></a>

The output from a crypto X402 payment.

### Contents
<a name="API_CryptoX402PaymentOutput_Contents"></a>

 ** payload **   <a name="BedrockAgentCore-Type-CryptoX402PaymentOutput-payload"></a>
The X402 payment response payload.  
Type: JSON value  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-CryptoX402PaymentOutput-version"></a>
The version of the X402 protocol.  
Type: String  
Required: Yes

### See Also
<a name="API_CryptoX402PaymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CryptoX402PaymentOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CryptoX402PaymentOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CryptoX402PaymentOutput) 

## CustomDescriptor
<a name="API_CustomDescriptor"></a>

 A custom descriptor configuration for a registry record.

### Contents
<a name="API_CustomDescriptor_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-CustomDescriptor-inlineContent"></a>
 The inline content of the custom descriptor.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

### See Also
<a name="API_CustomDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CustomDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CustomDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CustomDescriptor) 

## DataSourceConfig
<a name="API_DataSourceConfig"></a>

Configuration for the data source used in evaluation.

### Contents
<a name="API_DataSourceConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudWatchLogs **   <a name="BedrockAgentCore-Type-DataSourceConfig-cloudWatchLogs"></a>
Configuration for pulling agent session traces from CloudWatch Logs.  
Type: [CloudWatchLogsSource](#API_CloudWatchLogsSource) object  
Required: No

 ** onlineEvaluationConfigSource **   <a name="BedrockAgentCore-Type-DataSourceConfig-onlineEvaluationConfigSource"></a>
A reference to an existing online evaluation configuration to use as the data source for batch evaluation.  
Type: [OnlineEvaluationConfigSource](#API_OnlineEvaluationConfigSource) object  
Required: No

### See Also
<a name="API_DataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DataSourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DataSourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DataSourceConfig) 

## Descriptors
<a name="API_Descriptors"></a>

 Contains the descriptor configuration for a registry record. Only the field that matches the record's `descriptorType` is populated.

### Contents
<a name="API_Descriptors_Contents"></a>

 ** a2a **   <a name="BedrockAgentCore-Type-Descriptors-a2a"></a>
 The A2A (Agent-to-Agent) descriptor configuration. Populated when the record's `descriptorType` is `A2A`.  
Type: [A2aDescriptor](#API_A2aDescriptor) object  
Required: No

 ** agentSkills **   <a name="BedrockAgentCore-Type-Descriptors-agentSkills"></a>
 The agent skills descriptor configuration. Populated when the record's `descriptorType` is `AGENT_SKILLS`.  
Type: [AgentSkillsDescriptor](#API_AgentSkillsDescriptor) object  
Required: No

 ** custom **   <a name="BedrockAgentCore-Type-Descriptors-custom"></a>
 The custom descriptor configuration. Populated when the record's `descriptorType` is `CUSTOM`.  
Type: [CustomDescriptor](#API_CustomDescriptor) object  
Required: No

 ** mcp **   <a name="BedrockAgentCore-Type-Descriptors-mcp"></a>
 The MCP (Model Context Protocol) descriptor configuration. Populated when the record's `descriptorType` is `MCP`.  
Type: [McpDescriptor](#API_McpDescriptor) object  
Required: No

### See Also
<a name="API_Descriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Descriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Descriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Descriptors) 

## EfsConfiguration
<a name="API_EfsConfiguration"></a>

The configuration for mounting an Amazon Elastic File System (Amazon EFS) access point that you own into a session.

### Contents
<a name="API_EfsConfiguration_Contents"></a>

 ** accessPointArn **   <a name="BedrockAgentCore-Type-EfsConfiguration-accessPointArn"></a>
The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) access point to mount.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}`   
Required: Yes

 ** fileSystemArn **   <a name="BedrockAgentCore-Type-EfsConfiguration-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) file system that owns the access point.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:elasticfilesystem:[a-z0-9-]+:[0-9]{12}:file-system/fs-[0-9a-f]{8,40}`   
Required: Yes

 ** mountPath **   <a name="BedrockAgentCore-Type-EfsConfiguration-mountPath"></a>
The absolute path within the session at which the access point is mounted, for example `/mnt/efs`. Each mount path must be unique across all file system configurations in the session.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 200.  
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`   
Required: Yes

### See Also
<a name="API_EfsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EfsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EfsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EfsConfiguration) 

## EmbeddedCryptoWallet
<a name="API_EmbeddedCryptoWallet"></a>

Embedded crypto wallet instrument details.

### Contents
<a name="API_EmbeddedCryptoWallet_Contents"></a>

 ** linkedAccounts **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-linkedAccounts"></a>
List of linked accounts linked to this wallet. Each represents a way the end user can authenticate to this wallet.  
Type: Array of [LinkedAccount](#API_LinkedAccount) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: Yes

 ** network **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-network"></a>
The blockchain network for this embedded crypto wallet. Supported networks: ETHEREUM, SOLANA.  
Type: String  
Valid Values: `ETHEREUM | SOLANA`   
Required: Yes

 ** redirectUrl **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-redirectUrl"></a>
URL for the end user to complete a provider-specific action such as wallet linking or onboarding.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** walletAddress **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-walletAddress"></a>
The wallet address on the specified blockchain network.  
Type: String  
Required: No

### See Also
<a name="API_EmbeddedCryptoWallet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EmbeddedCryptoWallet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EmbeddedCryptoWallet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EmbeddedCryptoWallet) 

## EvaluationContent
<a name="API_EvaluationContent"></a>

 A content block for ground truth data in evaluation reference inputs. Supports text content for expected responses and assertions. 

### Contents
<a name="API_EvaluationContent_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="BedrockAgentCore-Type-EvaluationContent-text"></a>
 The text content of the ground truth data. Used for expected response text and assertion statements.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: No

### See Also
<a name="API_EvaluationContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationContent) 

## EvaluationExpectedTrajectory
<a name="API_EvaluationExpectedTrajectory"></a>

 The expected tool call trajectory for trajectory-based evaluation. 

### Contents
<a name="API_EvaluationExpectedTrajectory_Contents"></a>

 ** toolNames **   <a name="BedrockAgentCore-Type-EvaluationExpectedTrajectory-toolNames"></a>
 The list of tool names representing the expected tool call sequence.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1000 items.  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

### See Also
<a name="API_EvaluationExpectedTrajectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationExpectedTrajectory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationExpectedTrajectory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationExpectedTrajectory) 

## EvaluationInput
<a name="API_EvaluationInput"></a>

 The input data structure containing agent session spans in OpenTelemetry format. Supports traces from frameworks like Strands (AgentCore Runtime) and LangGraph with OpenInference instrumentation for comprehensive evaluation. 

### Contents
<a name="API_EvaluationInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** sessionSpans **   <a name="BedrockAgentCore-Type-EvaluationInput-sessionSpans"></a>
 The collection of spans representing agent execution traces within a session. Each span contains detailed information about tool calls, model interactions, and other agent activities that can be evaluated for quality and performance.   
Type: Array of JSON values  
Array Members: Minimum number of 1 item. Maximum number of 20000 items.  
Required: No

### See Also
<a name="API_EvaluationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationInput) 

## EvaluationJobResults
<a name="API_EvaluationJobResults"></a>

Aggregated results from a batch evaluation, including session completion counts and evaluator score summaries.

### Contents
<a name="API_EvaluationJobResults_Contents"></a>

 ** evaluatorSummaries **   <a name="BedrockAgentCore-Type-EvaluationJobResults-evaluatorSummaries"></a>
A list of per-evaluator summary statistics.  
Type: Array of [EvaluatorSummary](#API_EvaluatorSummary) objects  
Required: No

 ** numberOfSessionsCompleted **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsCompleted"></a>
The number of sessions that have been successfully evaluated.  
Type: Integer  
Required: No

 ** numberOfSessionsFailed **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsFailed"></a>
The number of sessions that failed evaluation.  
Type: Integer  
Required: No

 ** numberOfSessionsIgnored **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsIgnored"></a>
The number of sessions that were ignored during evaluation.  
Type: Integer  
Required: No

 ** numberOfSessionsInProgress **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsInProgress"></a>
The number of sessions currently being evaluated.  
Type: Integer  
Required: No

 ** totalNumberOfSessions **   <a name="BedrockAgentCore-Type-EvaluationJobResults-totalNumberOfSessions"></a>
The total number of sessions included in the batch evaluation.  
Type: Integer  
Required: No

### See Also
<a name="API_EvaluationJobResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationJobResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationJobResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationJobResults) 

## EvaluationMetadata
<a name="API_EvaluationMetadata"></a>

Metadata for the evaluation, including session-specific ground truth data.

### Contents
<a name="API_EvaluationMetadata_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** sessionMetadata **   <a name="BedrockAgentCore-Type-EvaluationMetadata-sessionMetadata"></a>
A list of session metadata entries containing ground truth data and test scenario identifiers for specific sessions.  
Type: Array of [SessionMetadataShape](#API_SessionMetadataShape) objects  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Required: No

### See Also
<a name="API_EvaluationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationMetadata) 

## EvaluationReferenceInput
<a name="API_EvaluationReferenceInput"></a>

 A reference input containing ground truth data for evaluation, scoped to a specific context level (session or trace) through its span context. 

### Contents
<a name="API_EvaluationReferenceInput_Contents"></a>

 ** context **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-context"></a>
 The span context that identifies which session or trace this reference input applies to, used for correlating ground truth with agent output.   
Type: [Context](#API_Context) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** assertions **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-assertions"></a>
 A list of assertion statements for session-level evaluation. Each assertion describes an expected behavior or outcome the agent should demonstrate during the session.   
Type: Array of [EvaluationContent](#API_EvaluationContent) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** expectedResponse **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-expectedResponse"></a>
 The expected response for trace-level evaluation. Built-in evaluators that support this field compare the agent's actual response against this value for assessment. Custom evaluators can access it through the `{expected_response}` placeholder in their instructions.   
Type: [EvaluationContent](#API_EvaluationContent) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** expectedTrajectory **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-expectedTrajectory"></a>
 The expected tool call sequence for session-level trajectory evaluation. Contains a list of tool names representing the tools the agent is expected to invoke.   
Type: [EvaluationExpectedTrajectory](#API_EvaluationExpectedTrajectory) object  
Required: No

### See Also
<a name="API_EvaluationReferenceInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationReferenceInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationReferenceInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationReferenceInput) 

## EvaluationResultContent
<a name="API_EvaluationResultContent"></a>

 The comprehensive result of an evaluation containing the score, explanation, evaluator metadata, and execution details. Provides both quantitative ratings and qualitative insights about agent performance. 

### Contents
<a name="API_EvaluationResultContent_Contents"></a>

 ** context **   <a name="BedrockAgentCore-Type-EvaluationResultContent-context"></a>
 The contextual information associated with this evaluation result, including span context details that identify the specific traces and sessions that were evaluated.   
Type: [Context](#API_Context) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** evaluatorArn **   <a name="BedrockAgentCore-Type-EvaluationResultContent-evaluatorArn"></a>
 The Amazon Resource Name (ARN) of the evaluator used to generate this result. For custom evaluators, this is the full ARN; for built-in evaluators, this follows the pattern `Builtin.{EvaluatorName}`.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/(Builtin|ThirdParty)\.[a-zA-Z0-9._-]+`   
Required: Yes

 ** evaluatorId **   <a name="BedrockAgentCore-Type-EvaluationResultContent-evaluatorId"></a>
 The unique identifier of the evaluator that produced this result. This matches the `evaluatorId` provided in the evaluation request and can be used to identify which evaluator generated specific results.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 111.  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** evaluatorName **   <a name="BedrockAgentCore-Type-EvaluationResultContent-evaluatorName"></a>
 The human-readable name of the evaluator used for this evaluation. For built-in evaluators, this is the descriptive name (e.g., "Helpfulness", "Correctness"); for custom evaluators, this is the user-defined name.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9_]{0,47})`   
Required: Yes

 ** errorCode **   <a name="BedrockAgentCore-Type-EvaluationResultContent-errorCode"></a>
 The error code indicating the type of failure that occurred during evaluation. Used to programmatically identify and handle different categories of evaluation errors.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-EvaluationResultContent-errorMessage"></a>
 The error message describing what went wrong if the evaluation failed. Provides detailed information about evaluation failures to help diagnose and resolve issues with evaluator configuration or input data.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** explanation **   <a name="BedrockAgentCore-Type-EvaluationResultContent-explanation"></a>
 The detailed explanation provided by the evaluator describing the reasoning behind the assigned score. This qualitative feedback helps understand why specific ratings were given and provides actionable insights for improvement.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** ignoredReferenceInputFields **   <a name="BedrockAgentCore-Type-EvaluationResultContent-ignoredReferenceInputFields"></a>
 The list of reference input field names that were provided but not used by the evaluator. Helps identify which ground truth data was not consumed during evaluation.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** label **   <a name="BedrockAgentCore-Type-EvaluationResultContent-label"></a>
 The categorical label assigned by the evaluator when using a categorical rating scale. This provides a human-readable description of the evaluation result (e.g., "Excellent", "Good", "Poor") corresponding to the numerical value. For numerical scales, this field is optional and provides a natural language explanation of what the value means (e.g., value 0.5 = "Somewhat Helpful").   
Type: String  
Required: No

 ** tokenUsage **   <a name="BedrockAgentCore-Type-EvaluationResultContent-tokenUsage"></a>
 The token consumption statistics for this evaluation, including input tokens, output tokens, and total tokens used by the underlying language model during the evaluation process.   
Type: [TokenUsage](#API_TokenUsage) object  
Required: No

 ** value **   <a name="BedrockAgentCore-Type-EvaluationResultContent-value"></a>
 The numerical score assigned by the evaluator according to its configured rating scale. For numerical scales, this is a decimal value within the defined range. This field is not allowed for categorical scales.   
Type: Double  
Required: No

### See Also
<a name="API_EvaluationResultContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationResultContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationResultContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationResultContent) 

## EvaluationTarget
<a name="API_EvaluationTarget"></a>

 The specification of which trace or span IDs to evaluate within the provided input data. Allows precise targeting of evaluation at different levels: tool calls, traces, or sessions. 

### Contents
<a name="API_EvaluationTarget_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** spanIds **   <a name="BedrockAgentCore-Type-EvaluationTarget-spanIds"></a>
 The list of specific span IDs to evaluate within the provided traces. Used to target evaluation at individual tool calls or specific operations within the agent's execution flow.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Fixed length of 16.  
Required: No

 ** traceIds **   <a name="BedrockAgentCore-Type-EvaluationTarget-traceIds"></a>
 The list of trace IDs to evaluate, representing complete request-response interactions. Used to evaluate entire conversation turns or specific agent interactions within a session.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Fixed length of 32.  
Required: No

### See Also
<a name="API_EvaluationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationTarget) 

## Evaluator
<a name="API_Evaluator"></a>

An evaluator to run against sessions during batch evaluation.

### Contents
<a name="API_Evaluator_Contents"></a>

 ** evaluatorId **   <a name="BedrockAgentCore-Type-Evaluator-evaluatorId"></a>
The unique identifier of the evaluator. Can reference built-in evaluators (e.g., `Builtin.Helpfulness`) or custom evaluators.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 111.  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

### See Also
<a name="API_Evaluator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Evaluator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Evaluator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Evaluator) 

## EvaluatorMetric
<a name="API_EvaluatorMetric"></a>

Statistical metrics for a single evaluator comparing control and treatment variants.

### Contents
<a name="API_EvaluatorMetric_Contents"></a>

 ** controlStats **   <a name="BedrockAgentCore-Type-EvaluatorMetric-controlStats"></a>
The statistics for the control variant.  
Type: [ControlStats](#API_ControlStats) object  
Required: Yes

 ** evaluatorArn **   <a name="BedrockAgentCore-Type-EvaluatorMetric-evaluatorArn"></a>
The Amazon Resource Name (ARN) of the evaluator.  
Type: String  
Required: Yes

 ** variantResults **   <a name="BedrockAgentCore-Type-EvaluatorMetric-variantResults"></a>
The results for each treatment variant compared against the control.  
Type: Array of [VariantResult](#API_VariantResult) objects  
Required: Yes

### See Also
<a name="API_EvaluatorMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluatorMetric) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluatorMetric) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluatorMetric) 

## EvaluatorStatistics
<a name="API_EvaluatorStatistics"></a>

Aggregated statistics for an evaluator.

### Contents
<a name="API_EvaluatorStatistics_Contents"></a>

 ** averageScore **   <a name="BedrockAgentCore-Type-EvaluatorStatistics-averageScore"></a>
The average score across all evaluated sessions for this evaluator.  
Type: Double  
Required: No

### See Also
<a name="API_EvaluatorStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluatorStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluatorStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluatorStatistics) 

## EvaluatorSummary
<a name="API_EvaluatorSummary"></a>

Summary statistics for a single evaluator within a batch evaluation.

### Contents
<a name="API_EvaluatorSummary_Contents"></a>

 ** evaluatorId **   <a name="BedrockAgentCore-Type-EvaluatorSummary-evaluatorId"></a>
The unique identifier of the evaluator.  
Type: String  
Required: No

 ** statistics **   <a name="BedrockAgentCore-Type-EvaluatorSummary-statistics"></a>
The aggregated statistics for this evaluator.  
Type: [EvaluatorStatistics](#API_EvaluatorStatistics) object  
Required: No

 ** totalEvaluated **   <a name="BedrockAgentCore-Type-EvaluatorSummary-totalEvaluated"></a>
The total number of sessions evaluated by this evaluator.  
Type: Integer  
Required: No

 ** totalFailed **   <a name="BedrockAgentCore-Type-EvaluatorSummary-totalFailed"></a>
The total number of sessions that failed evaluation by this evaluator.  
Type: Integer  
Required: No

### See Also
<a name="API_EvaluatorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluatorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluatorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluatorSummary) 

## Event
<a name="API_Event"></a>

Contains information about an event in an AgentCore Memory resource.

### Contents
<a name="API_Event_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-Event-actorId"></a>
The identifier of the actor associated with the event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** eventId **   <a name="BedrockAgentCore-Type-Event-eventId"></a>
The unique identifier of the event.  
Type: String  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: Yes

 ** eventTimestamp **   <a name="BedrockAgentCore-Type-Event-eventTimestamp"></a>
The timestamp when the event occurred.  
Type: Timestamp  
Required: Yes

 ** memoryId **   <a name="BedrockAgentCore-Type-Event-memoryId"></a>
The identifier of the AgentCore Memory resource containing the event.  
Type: String  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** payload **   <a name="BedrockAgentCore-Type-Event-payload"></a>
The content payload of the event.  
Type: Array of [PayloadType](#API_PayloadType) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-Event-sessionId"></a>
The identifier of the session containing the event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** branch **   <a name="BedrockAgentCore-Type-Event-branch"></a>
The branch information for the event.  
Type: [Branch](#API_Branch) object  
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-Event-metadata"></a>
Metadata associated with an event.  
Type: String to [MetadataValue](#API_MetadataValue) object map  
Map Entries: Minimum number of 0 items. Maximum number of 15 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Event) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Event) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Event) 

## EventMetadataFilterExpression
<a name="API_EventMetadataFilterExpression"></a>

Filter expression for retrieving events based on metadata associated with an event.

### Contents
<a name="API_EventMetadataFilterExpression_Contents"></a>

 ** left **   <a name="BedrockAgentCore-Type-EventMetadataFilterExpression-left"></a>
Left operand of the event metadata filter expression.  
Type: [LeftExpression](#API_LeftExpression) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** operator **   <a name="BedrockAgentCore-Type-EventMetadataFilterExpression-operator"></a>
Operator applied to the event metadata filter expression.  
Type: String  
Valid Values: `EQUALS_TO | EXISTS | NOT_EXISTS`   
Required: Yes

 ** right **   <a name="BedrockAgentCore-Type-EventMetadataFilterExpression-right"></a>
Right operand of the event metadata filter expression.  
Type: [RightExpression](#API_RightExpression) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_EventMetadataFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EventMetadataFilterExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EventMetadataFilterExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EventMetadataFilterExpression) 

## ExecutionSummaryAffectedSession
<a name="API_ExecutionSummaryAffectedSession"></a>

A session associated with an execution summary cluster.

### Contents
<a name="API_ExecutionSummaryAffectedSession_Contents"></a>

 ** approachTaken **   <a name="BedrockAgentCore-Type-ExecutionSummaryAffectedSession-approachTaken"></a>
The approach taken by the agent during this session.  
Type: String  
Required: Yes

 ** finalOutcome **   <a name="BedrockAgentCore-Type-ExecutionSummaryAffectedSession-finalOutcome"></a>
The final outcome of the session.  
Type: String  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-ExecutionSummaryAffectedSession-sessionId"></a>
The unique identifier of the session.  
Type: String  
Required: Yes

### See Also
<a name="API_ExecutionSummaryAffectedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExecutionSummaryAffectedSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExecutionSummaryAffectedSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExecutionSummaryAffectedSession) 

## ExecutionSummaryCluster
<a name="API_ExecutionSummaryCluster"></a>

A cluster of similar execution patterns identified across sessions.

### Contents
<a name="API_ExecutionSummaryCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-affectedSessionCount"></a>
The number of sessions with this execution pattern.  
Type: Integer  
Required: Yes

 ** affectedSessions **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-affectedSessions"></a>
The list of sessions with this execution pattern.  
Type: Array of [ExecutionSummaryAffectedSession](#API_ExecutionSummaryAffectedSession) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-clusterId"></a>
The unique identifier of the execution summary cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-description"></a>
A description of the execution pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-name"></a>
The name of the execution pattern cluster.  
Type: String  
Required: Yes

### See Also
<a name="API_ExecutionSummaryCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExecutionSummaryCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExecutionSummaryCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExecutionSummaryCluster) 

## ExecutionSummaryClusteringResultContent
<a name="API_ExecutionSummaryClusteringResultContent"></a>

The execution summary clustering result containing grouped execution patterns identified across evaluated sessions.

### Contents
<a name="API_ExecutionSummaryClusteringResultContent_Contents"></a>

 ** executionSummaries **   <a name="BedrockAgentCore-Type-ExecutionSummaryClusteringResultContent-executionSummaries"></a>
The list of execution summary clusters identified across analyzed sessions.  
Type: Array of [ExecutionSummaryCluster](#API_ExecutionSummaryCluster) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

### See Also
<a name="API_ExecutionSummaryClusteringResultContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExecutionSummaryClusteringResultContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExecutionSummaryClusteringResultContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExecutionSummaryClusteringResultContent) 

## ExternalProxy
<a name="API_ExternalProxy"></a>

Configuration for a customer-managed external proxy server. Includes server location, optional domain-based routing patterns, and authentication credentials.

### Contents
<a name="API_ExternalProxy_Contents"></a>

 ** port **   <a name="BedrockAgentCore-Type-ExternalProxy-port"></a>
The port number of the proxy server. Valid range: 1-65535.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: Yes

 ** server **   <a name="BedrockAgentCore-Type-ExternalProxy-server"></a>
The hostname of the proxy server. Must be a valid DNS hostname (maximum 253 characters).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`   
Required: Yes

 ** credentials **   <a name="BedrockAgentCore-Type-ExternalProxy-credentials"></a>
Optional authentication credentials for the proxy server. If omitted, the proxy is accessed without authentication (useful for IP-allowlisted proxies).  
Type: [ProxyCredentials](#API_ProxyCredentials) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** domainPatterns **   <a name="BedrockAgentCore-Type-ExternalProxy-domainPatterns"></a>
Optional array of domain patterns that should route through this specific proxy. Supports `.example.com` for subdomain matching (matches any subdomain of example.com) or `example.com` for exact domain matching. If omitted, this proxy acts as a catch-all for domains not matched by other proxies. Maximum 100 patterns per proxy, each up to 253 characters.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\.)?[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`   
Required: No

### See Also
<a name="API_ExternalProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExternalProxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExternalProxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExternalProxy) 

## ExtractionConfig
<a name="API_ExtractionConfig"></a>

The configuration for extraction behavior. Use this structure to specify namespace variable keys and their values for namespace substitution during long-term memory extraction.

### Contents
<a name="API_ExtractionConfig_Contents"></a>

 ** namespaceVariables **   <a name="BedrockAgentCore-Type-ExtractionConfig-namespaceVariables"></a>
A map of `namespaceKeys` to their values. The service substitutes these values into `namespaceTemplates` during long-term memory extraction to control namespace hierarchy.  
Type: String to string map  
Map Entries: Maximum number of 5 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 32.  
Key Pattern: `(?!memoryStrategyId$|actorId$|sessionId$)[a-z][a-z0-9]*`   
Value Length Constraints: Minimum length of 1. Maximum length of 64.  
Value Pattern: `[a-z0-9][a-z0-9-_]*`   
Required: No

### See Also
<a name="API_ExtractionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionConfig) 

## ExtractionJob
<a name="API_ExtractionJob"></a>

Represents the metadata of a memory extraction job such as the message identifiers that compose this job.

### Contents
<a name="API_ExtractionJob_Contents"></a>

 ** jobId **   <a name="BedrockAgentCore-Type-ExtractionJob-jobId"></a>
The unique identifier of the extraction job.  
Type: String  
Required: Yes

### See Also
<a name="API_ExtractionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionJob) 

## ExtractionJobFilterInput
<a name="API_ExtractionJobFilterInput"></a>

Filters for querying memory extraction jobs based on various criteria.

### Contents
<a name="API_ExtractionJobFilterInput_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-actorId"></a>
The identifier of the actor. If specified, only extraction jobs with this actor ID are returned.  
Type: String  
Required: No

 ** sessionId **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-sessionId"></a>
The unique identifier of the session. If specified, only extraction jobs with this session ID are returned.  
Type: String  
Required: No

 ** status **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-status"></a>
The status of the extraction job. If specified, only extraction jobs with this status are returned.  
Type: String  
Valid Values: `FAILED`   
Required: No

 ** strategyId **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-strategyId"></a>
The memory strategy identifier to filter extraction jobs by. If specified, only extraction jobs with this strategy ID are returned.  
Type: String  
Required: No

### See Also
<a name="API_ExtractionJobFilterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionJobFilterInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionJobFilterInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionJobFilterInput) 

## ExtractionJobMessages
<a name="API_ExtractionJobMessages"></a>

The list of messages that compose this extraction job.

### Contents
<a name="API_ExtractionJobMessages_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** messagesList **   <a name="BedrockAgentCore-Type-ExtractionJobMessages-messagesList"></a>
The list of messages that compose this extraction job.  
Type: Array of [MessageMetadata](#API_MessageMetadata) objects  
Required: No

### See Also
<a name="API_ExtractionJobMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionJobMessages) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionJobMessages) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionJobMessages) 

## ExtractionJobMetadata
<a name="API_ExtractionJobMetadata"></a>

Metadata information associated with this extraction job.

### Contents
<a name="API_ExtractionJobMetadata_Contents"></a>

 ** jobID **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-jobID"></a>
The unique identifier for the extraction job.  
Type: String  
Required: Yes

 ** messages **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-messages"></a>
The messages associated with the extraction job.  
Type: [ExtractionJobMessages](#API_ExtractionJobMessages) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** actorId **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-actorId"></a>
The identifier of the actor for this extraction job.  
Type: String  
Required: No

 ** failureReason **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-failureReason"></a>
The cause of failure, if the job did not complete successfully.  
Type: String  
Required: No

 ** sessionId **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-sessionId"></a>
The identifier of the session for this extraction job.  
Type: String  
Required: No

 ** status **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-status"></a>
The current status of the extraction job.  
Type: String  
Valid Values: `FAILED`   
Required: No

 ** strategyId **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-strategyId"></a>
The identifier of the memory strategy for this extraction job.  
Type: String  
Required: No

### See Also
<a name="API_ExtractionJobMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionJobMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionJobMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionJobMetadata) 

## FailureAnalysisResultContent
<a name="API_FailureAnalysisResultContent"></a>

The failure analysis clustering result containing categorized failure clusters with root causes and remediation recommendations.

### Contents
<a name="API_FailureAnalysisResultContent_Contents"></a>

 ** failures **   <a name="BedrockAgentCore-Type-FailureAnalysisResultContent-failures"></a>
The list of failure category clusters identified across analyzed sessions.  
Type: Array of [FailureCategoryCluster](#API_FailureCategoryCluster) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

### See Also
<a name="API_FailureAnalysisResultContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureAnalysisResultContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureAnalysisResultContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureAnalysisResultContent) 

## FailureCategoryCluster
<a name="API_FailureCategoryCluster"></a>

A top-level failure category identified by clustering similar failure patterns across sessions.

### Contents
<a name="API_FailureCategoryCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-affectedSessionCount"></a>
The number of sessions affected by this failure category.  
Type: Integer  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-clusterId"></a>
The unique identifier of the failure category cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-description"></a>
A description of the failure category pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-name"></a>
The name of the failure category.  
Type: String  
Required: Yes

 ** subCategories **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-subCategories"></a>
The list of failure subcategories within this category.  
Type: Array of [FailureSubCategoryCluster](#API_FailureSubCategoryCluster) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

### See Also
<a name="API_FailureCategoryCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureCategoryCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureCategoryCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureCategoryCluster) 

## FailureSpanDetail
<a name="API_FailureSpanDetail"></a>

Details about a specific span where a failure was detected.

### Contents
<a name="API_FailureSpanDetail_Contents"></a>

 ** signals **   <a name="BedrockAgentCore-Type-FailureSpanDetail-signals"></a>
The failure signals detected in this span.  
Type: Array of [InsightsFailureSignal](#API_InsightsFailureSignal) objects  
Required: Yes

 ** spanId **   <a name="BedrockAgentCore-Type-FailureSpanDetail-spanId"></a>
The unique identifier of the span where the failure occurred.  
Type: String  
Required: Yes

 ** traceId **   <a name="BedrockAgentCore-Type-FailureSpanDetail-traceId"></a>
The trace identifier associated with the failure span.  
Type: String  
Required: Yes

### See Also
<a name="API_FailureSpanDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureSpanDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureSpanDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureSpanDetail) 

## FailureSubCategoryCluster
<a name="API_FailureSubCategoryCluster"></a>

A subcategory of failures within a top-level failure category.

### Contents
<a name="API_FailureSubCategoryCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-affectedSessionCount"></a>
The number of sessions affected by this failure subcategory.  
Type: Integer  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-clusterId"></a>
The unique identifier of the failure subcategory cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-description"></a>
A description of the failure subcategory pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-name"></a>
The name of the failure subcategory.  
Type: String  
Required: Yes

 ** rootCauses **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-rootCauses"></a>
The list of root cause clusters identified within this subcategory.  
Type: Array of [RootCauseCluster](#API_RootCauseCluster) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

### See Also
<a name="API_FailureSubCategoryCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureSubCategoryCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureSubCategoryCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureSubCategoryCluster) 

## FilterInput
<a name="API_FilterInput"></a>

Contains filter criteria for listing events.

### Contents
<a name="API_FilterInput_Contents"></a>

 ** branch **   <a name="BedrockAgentCore-Type-FilterInput-branch"></a>
The branch filter criteria to apply when listing events.  
Type: [BranchFilter](#API_BranchFilter) object  
Required: No

 ** eventMetadata **   <a name="BedrockAgentCore-Type-FilterInput-eventMetadata"></a>
Event metadata filter criteria to apply when retrieving events.  
Type: Array of [EventMetadataFilterExpression](#API_EventMetadataFilterExpression) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

### See Also
<a name="API_FilterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FilterInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FilterInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FilterInput) 

## FilterValue
<a name="API_FilterValue"></a>

A value used in filter comparisons, supporting different data types.

### Contents
<a name="API_FilterValue_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** booleanValue **   <a name="BedrockAgentCore-Type-FilterValue-booleanValue"></a>
A boolean value for true/false filtering conditions.  
Type: Boolean  
Required: No

 ** doubleValue **   <a name="BedrockAgentCore-Type-FilterValue-doubleValue"></a>
A numeric value for numerical filtering and comparisons.  
Type: Double  
Required: No

 ** stringValue **   <a name="BedrockAgentCore-Type-FilterValue-stringValue"></a>
A string value for text-based filtering.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

### See Also
<a name="API_FilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FilterValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FilterValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FilterValue) 

## GatewayFilter
<a name="API_GatewayFilter"></a>

A filter to restrict which gateway target paths are included in the A/B test.

### Contents
<a name="API_GatewayFilter_Contents"></a>

 ** targetPaths **   <a name="BedrockAgentCore-Type-GatewayFilter-targetPaths"></a>
A list of target path patterns to include in the A/B test.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

### See Also
<a name="API_GatewayFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GatewayFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GatewayFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GatewayFilter) 

## GroundTruthSource
<a name="API_GroundTruthSource"></a>

Where to pull ground truth from.

### Contents
<a name="API_GroundTruthSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inline **   <a name="BedrockAgentCore-Type-GroundTruthSource-inline"></a>
Inline ground truth data provided directly in the request.  
Type: [InlineGroundTruth](#API_InlineGroundTruth) object  
Required: No

### See Also
<a name="API_GroundTruthSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GroundTruthSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GroundTruthSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GroundTruthSource) 

## GroundTruthTurn
<a name="API_GroundTruthTurn"></a>

Ground truth data for a single conversation turn.

### Contents
<a name="API_GroundTruthTurn_Contents"></a>

 ** expectedResponse **   <a name="BedrockAgentCore-Type-GroundTruthTurn-expectedResponse"></a>
The expected response for this conversation turn.  
Type: [EvaluationContent](#API_EvaluationContent) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** input **   <a name="BedrockAgentCore-Type-GroundTruthTurn-input"></a>
The input for this conversation turn.  
Type: [GroundTruthTurnInput](#API_GroundTruthTurnInput) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_GroundTruthTurn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GroundTruthTurn) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GroundTruthTurn) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GroundTruthTurn) 

## GroundTruthTurnInput
<a name="API_GroundTruthTurnInput"></a>

The input for a ground truth conversation turn.

### Contents
<a name="API_GroundTruthTurnInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** prompt **   <a name="BedrockAgentCore-Type-GroundTruthTurnInput-prompt"></a>
The text prompt for this conversation turn.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4000.  
Required: No

### See Also
<a name="API_GroundTruthTurnInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GroundTruthTurnInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GroundTruthTurnInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GroundTruthTurnInput) 

## HarnessAgentCoreBrowserConfig
<a name="API_HarnessAgentCoreBrowserConfig"></a>

Configuration for AgentCore Browser.

### Contents
<a name="API_HarnessAgentCoreBrowserConfig_Contents"></a>

 ** browserArn **   <a name="BedrockAgentCore-Type-HarnessAgentCoreBrowserConfig-browserArn"></a>
If not populated, the built-in Browser ARN is used.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: No

### See Also
<a name="API_HarnessAgentCoreBrowserConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessAgentCoreBrowserConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessAgentCoreBrowserConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessAgentCoreBrowserConfig) 

## HarnessAgentCoreCodeInterpreterConfig
<a name="API_HarnessAgentCoreCodeInterpreterConfig"></a>

Configuration for AgentCore Code Interpreter.

### Contents
<a name="API_HarnessAgentCoreCodeInterpreterConfig_Contents"></a>

 ** codeInterpreterArn **   <a name="BedrockAgentCore-Type-HarnessAgentCoreCodeInterpreterConfig-codeInterpreterArn"></a>
If not populated, the built-in Code Interpreter ARN is used.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: No

### See Also
<a name="API_HarnessAgentCoreCodeInterpreterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessAgentCoreCodeInterpreterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessAgentCoreCodeInterpreterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessAgentCoreCodeInterpreterConfig) 

## HarnessAgentCoreGatewayConfig
<a name="API_HarnessAgentCoreGatewayConfig"></a>

Configuration for AgentCore Gateway.

### Contents
<a name="API_HarnessAgentCoreGatewayConfig_Contents"></a>

 ** gatewayArn **   <a name="BedrockAgentCore-Type-HarnessAgentCoreGatewayConfig-gatewayArn"></a>
The ARN of the desired AgentCore Gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** outboundAuth **   <a name="BedrockAgentCore-Type-HarnessAgentCoreGatewayConfig-outboundAuth"></a>
How harness authenticates to this Gateway. Defaults to AWS\_IAM (SigV4) if omitted.  
Type: [HarnessGatewayOutboundAuth](#API_HarnessGatewayOutboundAuth) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_HarnessAgentCoreGatewayConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessAgentCoreGatewayConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessAgentCoreGatewayConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessAgentCoreGatewayConfig) 

## HarnessBedrockModelConfig
<a name="API_HarnessBedrockModelConfig"></a>

Configuration for an Amazon Bedrock model provider.

### Contents
<a name="API_HarnessBedrockModelConfig_Contents"></a>

 ** modelId **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-modelId"></a>
The Bedrock model ID.  
Type: String  
Required: Yes

 ** additionalParams **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.  
Type: JSON value  
Required: No

 ** apiFormat **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-apiFormat"></a>
The API format to use when calling the Bedrock provider.  
Type: String  
Valid Values: `converse_stream | responses | chat_completions`   
Required: No

 ** maxTokens **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topP **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

### See Also
<a name="API_HarnessBedrockModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessBedrockModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessBedrockModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessBedrockModelConfig) 

## HarnessContentBlock
<a name="API_HarnessContentBlock"></a>

A content block within a message.

### Contents
<a name="API_HarnessContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoningContent **   <a name="BedrockAgentCore-Type-HarnessContentBlock-reasoningContent"></a>
Model reasoning content.  
Type: [HarnessReasoningContentBlock](#API_HarnessReasoningContentBlock) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessContentBlock-text"></a>
Text content.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** toolResult **   <a name="BedrockAgentCore-Type-HarnessContentBlock-toolResult"></a>
A tool execution result.  
Type: [HarnessToolResultBlock](#API_HarnessToolResultBlock) object  
Required: No

 ** toolUse **   <a name="BedrockAgentCore-Type-HarnessContentBlock-toolUse"></a>
A tool use request from the model.  
Type: [HarnessToolUseBlock](#API_HarnessToolUseBlock) object  
Required: No

### See Also
<a name="API_HarnessContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlock) 

## HarnessContentBlockDelta
<a name="API_HarnessContentBlockDelta"></a>

A delta update to a content block.

### Contents
<a name="API_HarnessContentBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoningContent **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-reasoningContent"></a>
A reasoning content delta.  
Type: [HarnessReasoningContentBlockDelta](#API_HarnessReasoningContentBlockDelta) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-text"></a>
A text delta.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** toolResult **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-toolResult"></a>
A tool result delta.  
Type: Array of [HarnessToolResultBlockDelta](#API_HarnessToolResultBlockDelta) objects  
Required: No

 ** toolResultMetadata **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-toolResultMetadata"></a>
A tool result metadata delta.  
Type: [HarnessToolResultMetadataBlockDelta](#API_HarnessToolResultMetadataBlockDelta) object  
Required: No

 ** toolUse **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-toolUse"></a>
A tool use input delta.  
Type: [HarnessToolUseBlockDelta](#API_HarnessToolUseBlockDelta) object  
Required: No

### See Also
<a name="API_HarnessContentBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockDelta) 

## HarnessContentBlockDeltaEvent
<a name="API_HarnessContentBlockDeltaEvent"></a>

Event containing a delta update to a content block.

### Contents
<a name="API_HarnessContentBlockDeltaEvent_Contents"></a>

 ** contentBlockIndex **   <a name="BedrockAgentCore-Type-HarnessContentBlockDeltaEvent-contentBlockIndex"></a>
The index of the content block being updated.  
Type: Integer  
Required: Yes

 ** delta **   <a name="BedrockAgentCore-Type-HarnessContentBlockDeltaEvent-delta"></a>
The delta payload.  
Type: [HarnessContentBlockDelta](#API_HarnessContentBlockDelta) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_HarnessContentBlockDeltaEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockDeltaEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockDeltaEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockDeltaEvent) 

## HarnessContentBlockStart
<a name="API_HarnessContentBlockStart"></a>

The start payload for a content block.

### Contents
<a name="API_HarnessContentBlockStart_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** toolResult **   <a name="BedrockAgentCore-Type-HarnessContentBlockStart-toolResult"></a>
Start of a tool result content block.  
Type: [HarnessToolResultBlockStart](#API_HarnessToolResultBlockStart) object  
Required: No

 ** toolUse **   <a name="BedrockAgentCore-Type-HarnessContentBlockStart-toolUse"></a>
Start of a tool use content block.  
Type: [HarnessToolUseBlockStart](#API_HarnessToolUseBlockStart) object  
Required: No

### See Also
<a name="API_HarnessContentBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockStart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockStart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockStart) 

## HarnessContentBlockStartEvent
<a name="API_HarnessContentBlockStartEvent"></a>

Event indicating the start of a content block.

### Contents
<a name="API_HarnessContentBlockStartEvent_Contents"></a>

 ** contentBlockIndex **   <a name="BedrockAgentCore-Type-HarnessContentBlockStartEvent-contentBlockIndex"></a>
The index of the content block within the message.  
Type: Integer  
Required: Yes

 ** start **   <a name="BedrockAgentCore-Type-HarnessContentBlockStartEvent-start"></a>
The content block start payload.  
Type: [HarnessContentBlockStart](#API_HarnessContentBlockStart) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_HarnessContentBlockStartEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockStartEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockStartEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockStartEvent) 

## HarnessContentBlockStopEvent
<a name="API_HarnessContentBlockStopEvent"></a>

Event indicating the end of a content block.

### Contents
<a name="API_HarnessContentBlockStopEvent_Contents"></a>

 ** contentBlockIndex **   <a name="BedrockAgentCore-Type-HarnessContentBlockStopEvent-contentBlockIndex"></a>
The index of the content block that ended.  
Type: Integer  
Required: Yes

### See Also
<a name="API_HarnessContentBlockStopEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockStopEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockStopEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockStopEvent) 

## HarnessGatewayOutboundAuth
<a name="API_HarnessGatewayOutboundAuth"></a>

Authentication method for calling a Gateway.

### Contents
<a name="API_HarnessGatewayOutboundAuth_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsIam **   <a name="BedrockAgentCore-Type-HarnessGatewayOutboundAuth-awsIam"></a>
SigV4-sign requests using the agent's execution role.  
Type: Structure  
Required: No

 ** none **   <a name="BedrockAgentCore-Type-HarnessGatewayOutboundAuth-none"></a>
No authentication.  
Type: Structure  
Required: No

 ** oauth **   <a name="BedrockAgentCore-Type-HarnessGatewayOutboundAuth-oauth"></a>
OAuth 2.0 authentication via AgentCore Identity.  
Type: [OAuthCredentialProvider](#API_OAuthCredentialProvider) object  
Required: No

### See Also
<a name="API_HarnessGatewayOutboundAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessGatewayOutboundAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessGatewayOutboundAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessGatewayOutboundAuth) 

## HarnessGeminiModelConfig
<a name="API_HarnessGeminiModelConfig"></a>

Configuration for a Google Gemini model provider. Requires an API key stored in AgentCore Identity.

### Contents
<a name="API_HarnessGeminiModelConfig_Contents"></a>

 ** apiKeyArn **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-apiKeyArn"></a>
The ARN of your Gemini API key on AgentCore Identity.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** modelId **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-modelId"></a>
The Gemini model ID.  
Type: String  
Required: Yes

 ** additionalParams **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the Gemini model provider unchanged.  
Type: JSON value  
Required: No

 ** maxTokens **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topK **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-topK"></a>
The topK set when calling the model.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 500.  
Required: No

 ** topP **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

### See Also
<a name="API_HarnessGeminiModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessGeminiModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessGeminiModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessGeminiModelConfig) 

## HarnessInlineFunctionConfig
<a name="API_HarnessInlineFunctionConfig"></a>

Configuration for an inline function tool. When the agent calls this tool, the tool call is returned to the caller for external execution.

### Contents
<a name="API_HarnessInlineFunctionConfig_Contents"></a>

 ** description **   <a name="BedrockAgentCore-Type-HarnessInlineFunctionConfig-description"></a>
Description of what the tool does, provided to the model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: Yes

 ** inputSchema **   <a name="BedrockAgentCore-Type-HarnessInlineFunctionConfig-inputSchema"></a>
JSON Schema describing the tool's input parameters.  
Type: JSON value  
Required: Yes

### See Also
<a name="API_HarnessInlineFunctionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessInlineFunctionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessInlineFunctionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessInlineFunctionConfig) 

## HarnessLiteLlmModelConfig
<a name="API_HarnessLiteLlmModelConfig"></a>

Configuration for a LiteLLM model provider, enabling connection to third-party model providers.

### Contents
<a name="API_HarnessLiteLlmModelConfig_Contents"></a>

 ** modelId **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-modelId"></a>
The LiteLLM model identifier (e.g., "anthropic/claude-3-sonnet").  
Type: String  
Required: Yes

 ** additionalParams **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.  
Type: JSON value  
Required: No

 ** apiBase **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-apiBase"></a>
The base URL for the model provider's API endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16383.  
Required: No

 ** apiKeyArn **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-apiKeyArn"></a>
The ARN of the API key in AgentCore Identity for authenticating with the model provider.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: No

 ** maxTokens **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topP **   <a name="BedrockAgentCore-Type-HarnessLiteLlmModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

### See Also
<a name="API_HarnessLiteLlmModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessLiteLlmModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessLiteLlmModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessLiteLlmModelConfig) 

## HarnessMessage
<a name="API_HarnessMessage"></a>

A message in the conversation.

### Contents
<a name="API_HarnessMessage_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-HarnessMessage-content"></a>
The content blocks of the message.  
Type: Array of [HarnessContentBlock](#API_HarnessContentBlock) objects  
Required: Yes

 ** role **   <a name="BedrockAgentCore-Type-HarnessMessage-role"></a>
The role of the message sender.  
Type: String  
Valid Values: `user | assistant`   
Required: Yes

### See Also
<a name="API_HarnessMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessMessage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessMessage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessMessage) 

## HarnessMessageStartEvent
<a name="API_HarnessMessageStartEvent"></a>

Event indicating the start of a message.

### Contents
<a name="API_HarnessMessageStartEvent_Contents"></a>

 ** role **   <a name="BedrockAgentCore-Type-HarnessMessageStartEvent-role"></a>
The role of the message sender.  
Type: String  
Valid Values: `user | assistant`   
Required: Yes

### See Also
<a name="API_HarnessMessageStartEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessMessageStartEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessMessageStartEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessMessageStartEvent) 

## HarnessMessageStopEvent
<a name="API_HarnessMessageStopEvent"></a>

Event indicating the end of a message.

### Contents
<a name="API_HarnessMessageStopEvent_Contents"></a>

 ** stopReason **   <a name="BedrockAgentCore-Type-HarnessMessageStopEvent-stopReason"></a>
The reason the agent stopped generating.  
Type: String  
Valid Values: `end_turn | tool_use | tool_result | max_tokens | stop_sequence | content_filtered | malformed_model_output | malformed_tool_use | interrupted | partial_turn | model_context_window_exceeded | max_iterations_exceeded | max_output_tokens_exceeded | timeout_exceeded`   
Required: Yes

### See Also
<a name="API_HarnessMessageStopEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessMessageStopEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessMessageStopEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessMessageStopEvent) 

## HarnessMetadataEvent
<a name="API_HarnessMetadataEvent"></a>

Token usage and latency metrics for the invocation.

### Contents
<a name="API_HarnessMetadataEvent_Contents"></a>

 ** metrics **   <a name="BedrockAgentCore-Type-HarnessMetadataEvent-metrics"></a>
Latency metrics.  
Type: [HarnessStreamMetrics](#API_HarnessStreamMetrics) object  
Required: Yes

 ** usage **   <a name="BedrockAgentCore-Type-HarnessMetadataEvent-usage"></a>
Token usage counts.  
Type: [HarnessTokenUsage](#API_HarnessTokenUsage) object  
Required: Yes

### See Also
<a name="API_HarnessMetadataEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessMetadataEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessMetadataEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessMetadataEvent) 

## HarnessModelConfiguration
<a name="API_HarnessModelConfiguration"></a>

Specification of which model to use.

### Contents
<a name="API_HarnessModelConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bedrockModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-bedrockModelConfig"></a>
Configuration for an Amazon Bedrock model.  
Type: [HarnessBedrockModelConfig](#API_HarnessBedrockModelConfig) object  
Required: No

 ** geminiModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-geminiModelConfig"></a>
Configuration for a Google Gemini model.  
Type: [HarnessGeminiModelConfig](#API_HarnessGeminiModelConfig) object  
Required: No

 ** liteLlmModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-liteLlmModelConfig"></a>
The LiteLLM model configuration for connecting to third-party model providers.  
Type: [HarnessLiteLlmModelConfig](#API_HarnessLiteLlmModelConfig) object  
Required: No

 ** openAiModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-openAiModelConfig"></a>
Configuration for an OpenAI model.  
Type: [HarnessOpenAiModelConfig](#API_HarnessOpenAiModelConfig) object  
Required: No

### See Also
<a name="API_HarnessModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessModelConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessModelConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessModelConfiguration) 

## HarnessOpenAiModelConfig
<a name="API_HarnessOpenAiModelConfig"></a>

Configuration for an OpenAI model provider. Requires an API key stored in AgentCore Identity.

### Contents
<a name="API_HarnessOpenAiModelConfig_Contents"></a>

 ** apiKeyArn **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-apiKeyArn"></a>
The ARN of your OpenAI API key on AgentCore Identity.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** modelId **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-modelId"></a>
The OpenAI model ID.  
Type: String  
Required: Yes

 ** additionalParams **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.  
Type: JSON value  
Required: No

 ** apiFormat **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-apiFormat"></a>
The API format to use when calling the OpenAI provider.  
Type: String  
Valid Values: `chat_completions | responses`   
Required: No

 ** maxTokens **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topP **   <a name="BedrockAgentCore-Type-HarnessOpenAiModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

### See Also
<a name="API_HarnessOpenAiModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessOpenAiModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessOpenAiModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessOpenAiModelConfig) 

## HarnessReasoningContentBlock
<a name="API_HarnessReasoningContentBlock"></a>

Reasoning content from the model.

### Contents
<a name="API_HarnessReasoningContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoningText **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlock-reasoningText"></a>
The reasoning text.  
Type: [HarnessReasoningTextBlock](#API_HarnessReasoningTextBlock) object  
Required: No

 ** redactedContent **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlock-redactedContent"></a>
Redacted reasoning content.  
Type: Base64-encoded binary data object  
Required: No

### See Also
<a name="API_HarnessReasoningContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlock) 

## HarnessReasoningContentBlockDelta
<a name="API_HarnessReasoningContentBlockDelta"></a>

A delta update to a reasoning content block.

### Contents
<a name="API_HarnessReasoningContentBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** redactedContent **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlockDelta-redactedContent"></a>
Redacted reasoning content.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** signature **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlockDelta-signature"></a>
Signature for the reasoning content.  
Type: String  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlockDelta-text"></a>
Reasoning text delta.  
Type: String  
Required: No

### See Also
<a name="API_HarnessReasoningContentBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlockDelta) 

## HarnessReasoningTextBlock
<a name="API_HarnessReasoningTextBlock"></a>

A block of reasoning text from the model.

### Contents
<a name="API_HarnessReasoningTextBlock_Contents"></a>

 ** text **   <a name="BedrockAgentCore-Type-HarnessReasoningTextBlock-text"></a>
The reasoning text.  
Type: String  
Required: Yes

 ** signature **   <a name="BedrockAgentCore-Type-HarnessReasoningTextBlock-signature"></a>
Signature for verifying the reasoning content.  
Type: String  
Required: No

### See Also
<a name="API_HarnessReasoningTextBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessReasoningTextBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessReasoningTextBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessReasoningTextBlock) 

## HarnessRemoteMcpConfig
<a name="API_HarnessRemoteMcpConfig"></a>

Configuration for connecting to a remote MCP server.

### Contents
<a name="API_HarnessRemoteMcpConfig_Contents"></a>

 ** url **   <a name="BedrockAgentCore-Type-HarnessRemoteMcpConfig-url"></a>
URL of the MCP endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16383.  
Required: Yes

 ** headers **   <a name="BedrockAgentCore-Type-HarnessRemoteMcpConfig-headers"></a>
Custom headers to include when connecting to the remote MCP server.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 16383.  
Value Length Constraints: Minimum length of 1. Maximum length of 16383.  
Required: No

### See Also
<a name="API_HarnessRemoteMcpConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessRemoteMcpConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessRemoteMcpConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessRemoteMcpConfig) 

## HarnessSkill
<a name="API_HarnessSkill"></a>

A skill available to the agent.

### Contents
<a name="API_HarnessSkill_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsSkills **   <a name="BedrockAgentCore-Type-HarnessSkill-awsSkills"></a>
AWS Skills baked into the Harness's underlying Runtime.  
Type: [HarnessSkillAwsSkillsSource](#API_HarnessSkillAwsSkillsSource) object  
Required: No

 ** git **   <a name="BedrockAgentCore-Type-HarnessSkill-git"></a>
A git repository containing the skill.  
Type: [HarnessSkillGitSource](#API_HarnessSkillGitSource) object  
Required: No

 ** path **   <a name="BedrockAgentCore-Type-HarnessSkill-path"></a>
The filesystem path to the skill definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** s3 **   <a name="BedrockAgentCore-Type-HarnessSkill-s3"></a>
An S3 source containing the skill.  
Type: [HarnessSkillS3Source](#API_HarnessSkillS3Source) object  
Required: No

### See Also
<a name="API_HarnessSkill_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkill) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkill) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkill) 

## HarnessSkillAwsSkillsSource
<a name="API_HarnessSkillAwsSkillsSource"></a>

Passed to show that AWS Skills should be included.

### Contents
<a name="API_HarnessSkillAwsSkillsSource_Contents"></a>

 ** paths **   <a name="BedrockAgentCore-Type-HarnessSkillAwsSkillsSource-paths"></a>
Optionally filter allowed skills with glob syntax, e.g., ['core-skills/\*'].  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `([^*?\[\]]|\*)+`   
Required: No

### See Also
<a name="API_HarnessSkillAwsSkillsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkillAwsSkillsSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkillAwsSkillsSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkillAwsSkillsSource) 

## HarnessSkillGitAuth
<a name="API_HarnessSkillGitAuth"></a>

Authentication configuration for accessing a private git repository.

### Contents
<a name="API_HarnessSkillGitAuth_Contents"></a>

 ** credentialArn **   <a name="BedrockAgentCore-Type-HarnessSkillGitAuth-credentialArn"></a>
The ARN of the credential in AgentCore Identity containing the password or personal access token.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** username **   <a name="BedrockAgentCore-Type-HarnessSkillGitAuth-username"></a>
Username for authentication. Defaults to 'oauth2' if not specified.  
Type: String  
Required: No

### See Also
<a name="API_HarnessSkillGitAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkillGitAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkillGitAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkillGitAuth) 

## HarnessSkillGitSource
<a name="API_HarnessSkillGitSource"></a>

A git repository source for a skill.

### Contents
<a name="API_HarnessSkillGitSource_Contents"></a>

 ** url **   <a name="BedrockAgentCore-Type-HarnessSkillGitSource-url"></a>
The HTTPS URL of the git repository.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 16383.  
Pattern: `https://[^#@]+`   
Required: Yes

 ** auth **   <a name="BedrockAgentCore-Type-HarnessSkillGitSource-auth"></a>
Authentication configuration for private repositories.  
Type: [HarnessSkillGitAuth](#API_HarnessSkillGitAuth) object  
Required: No

 ** path **   <a name="BedrockAgentCore-Type-HarnessSkillGitSource-path"></a>
Subdirectory within the repository containing the skill.  
Type: String  
Required: No

### See Also
<a name="API_HarnessSkillGitSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkillGitSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkillGitSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkillGitSource) 

## HarnessSkillS3Source
<a name="API_HarnessSkillS3Source"></a>

An S3 source for a skill.

### Contents
<a name="API_HarnessSkillS3Source_Contents"></a>

 ** uri **   <a name="BedrockAgentCore-Type-HarnessSkillS3Source-uri"></a>
The S3 URI pointing to the skill directory (e.g., s3://bucket/skills/my-skill/).  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 16383.  
Pattern: `s3://.*`   
Required: Yes

### See Also
<a name="API_HarnessSkillS3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkillS3Source) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkillS3Source) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkillS3Source) 

## HarnessStreamMetrics
<a name="API_HarnessStreamMetrics"></a>

Latency metrics for the invocation.

### Contents
<a name="API_HarnessStreamMetrics_Contents"></a>

 ** latencyMs **   <a name="BedrockAgentCore-Type-HarnessStreamMetrics-latencyMs"></a>
The end-to-end latency of the invocation in milliseconds.  
Type: Long  
Required: Yes

### See Also
<a name="API_HarnessStreamMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessStreamMetrics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessStreamMetrics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessStreamMetrics) 

## HarnessSystemContentBlock
<a name="API_HarnessSystemContentBlock"></a>

A content block in the system prompt.

### Contents
<a name="API_HarnessSystemContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="BedrockAgentCore-Type-HarnessSystemContentBlock-text"></a>
The text content of the system prompt block.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

### See Also
<a name="API_HarnessSystemContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSystemContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSystemContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSystemContentBlock) 

## HarnessTokenUsage
<a name="API_HarnessTokenUsage"></a>

Token usage counts for the invocation.

### Contents
<a name="API_HarnessTokenUsage_Contents"></a>

 ** inputTokens **   <a name="BedrockAgentCore-Type-HarnessTokenUsage-inputTokens"></a>
The number of input tokens consumed.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** outputTokens **   <a name="BedrockAgentCore-Type-HarnessTokenUsage-outputTokens"></a>
The number of output tokens generated.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** totalTokens **   <a name="BedrockAgentCore-Type-HarnessTokenUsage-totalTokens"></a>
The total number of tokens consumed.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** cacheReadInputTokens **   <a name="BedrockAgentCore-Type-HarnessTokenUsage-cacheReadInputTokens"></a>
The number of input tokens read from cache.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** cacheWriteInputTokens **   <a name="BedrockAgentCore-Type-HarnessTokenUsage-cacheWriteInputTokens"></a>
The number of input tokens written to cache.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

### See Also
<a name="API_HarnessTokenUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessTokenUsage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessTokenUsage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessTokenUsage) 

## HarnessTool
<a name="API_HarnessTool"></a>

A tool available to the agent loop.

### Contents
<a name="API_HarnessTool_Contents"></a>

 ** type **   <a name="BedrockAgentCore-Type-HarnessTool-type"></a>
The type of tool.  
Type: String  
Valid Values: `remote_mcp | agentcore_browser | agentcore_gateway | inline_function | agentcore_code_interpreter`   
Required: Yes

 ** config **   <a name="BedrockAgentCore-Type-HarnessTool-config"></a>
Tool-specific configuration.  
Type: [HarnessToolConfiguration](#API_HarnessToolConfiguration) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-HarnessTool-name"></a>
Unique name for the tool. If not provided, a name will be inferred or generated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

### See Also
<a name="API_HarnessTool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessTool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessTool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessTool) 

## HarnessToolConfiguration
<a name="API_HarnessToolConfiguration"></a>

Configuration union for different tool types.

### Contents
<a name="API_HarnessToolConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentCoreBrowser **   <a name="BedrockAgentCore-Type-HarnessToolConfiguration-agentCoreBrowser"></a>
Configuration for AgentCore Browser.  
Type: [HarnessAgentCoreBrowserConfig](#API_HarnessAgentCoreBrowserConfig) object  
Required: No

 ** agentCoreCodeInterpreter **   <a name="BedrockAgentCore-Type-HarnessToolConfiguration-agentCoreCodeInterpreter"></a>
Configuration for AgentCore Code Interpreter.  
Type: [HarnessAgentCoreCodeInterpreterConfig](#API_HarnessAgentCoreCodeInterpreterConfig) object  
Required: No

 ** agentCoreGateway **   <a name="BedrockAgentCore-Type-HarnessToolConfiguration-agentCoreGateway"></a>
Configuration for AgentCore Gateway.  
Type: [HarnessAgentCoreGatewayConfig](#API_HarnessAgentCoreGatewayConfig) object  
Required: No

 ** inlineFunction **   <a name="BedrockAgentCore-Type-HarnessToolConfiguration-inlineFunction"></a>
Configuration for an inline function tool.  
Type: [HarnessInlineFunctionConfig](#API_HarnessInlineFunctionConfig) object  
Required: No

 ** remoteMcp **   <a name="BedrockAgentCore-Type-HarnessToolConfiguration-remoteMcp"></a>
Configuration for remote MCP server.  
Type: [HarnessRemoteMcpConfig](#API_HarnessRemoteMcpConfig) object  
Required: No

### See Also
<a name="API_HarnessToolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolConfiguration) 

## HarnessToolResultBlock
<a name="API_HarnessToolResultBlock"></a>

The result of a tool execution.

### Contents
<a name="API_HarnessToolResultBlock_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-content"></a>
The content of the tool result.  
Type: Array of [HarnessToolResultContentBlock](#API_HarnessToolResultContentBlock) objects  
Required: Yes

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-toolUseId"></a>
The tool use ID that this result corresponds to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-status"></a>
The status of the tool execution.  
Type: String  
Valid Values: `success | error`   
Required: No

 ** type **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-type"></a>
The type of tool use that produced this result.  
Type: String  
Valid Values: `tool_use | server_tool_use | mcp_tool_use`   
Required: No

### See Also
<a name="API_HarnessToolResultBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultBlock) 

## HarnessToolResultBlockDelta
<a name="API_HarnessToolResultBlockDelta"></a>

A delta update to a tool result content block.

### Contents
<a name="API_HarnessToolResultBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** json **   <a name="BedrockAgentCore-Type-HarnessToolResultBlockDelta-json"></a>
A JSON tool result delta.  
Type: JSON value  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessToolResultBlockDelta-text"></a>
A text tool result delta.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

### See Also
<a name="API_HarnessToolResultBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultBlockDelta) 

## HarnessToolResultBlockStart
<a name="API_HarnessToolResultBlockStart"></a>

Start payload for a tool result content block.

### Contents
<a name="API_HarnessToolResultBlockStart_Contents"></a>

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolResultBlockStart-toolUseId"></a>
The tool use ID that this result corresponds to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-HarnessToolResultBlockStart-status"></a>
The status of the tool execution.  
Type: String  
Valid Values: `success | error`   
Required: No

### See Also
<a name="API_HarnessToolResultBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultBlockStart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultBlockStart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultBlockStart) 

## HarnessToolResultContentBlock
<a name="API_HarnessToolResultContentBlock"></a>

A content block within a tool result.

### Contents
<a name="API_HarnessToolResultContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** json **   <a name="BedrockAgentCore-Type-HarnessToolResultContentBlock-json"></a>
JSON content.  
Type: JSON value  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessToolResultContentBlock-text"></a>
Text content.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

### See Also
<a name="API_HarnessToolResultContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultContentBlock) 

## HarnessToolResultMetadataBlockDelta
<a name="API_HarnessToolResultMetadataBlockDelta"></a>

Delta payload for a tool result metadata.

### Contents
<a name="API_HarnessToolResultMetadataBlockDelta_Contents"></a>

 ** metadata **   <a name="BedrockAgentCore-Type-HarnessToolResultMetadataBlockDelta-metadata"></a>
The partial JSON-string fragment of the tool result metadata.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

### See Also
<a name="API_HarnessToolResultMetadataBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultMetadataBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultMetadataBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultMetadataBlockDelta) 

## HarnessToolUseBlock
<a name="API_HarnessToolUseBlock"></a>

A tool use request from the model.

### Contents
<a name="API_HarnessToolUseBlock_Contents"></a>

 ** input **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-input"></a>
The JSON input to pass to the tool.  
Type: JSON value  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-name"></a>
The name of the tool to call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-toolUseId"></a>
The unique ID of this tool use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** serverName **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-serverName"></a>
The name of the MCP server providing this tool.  
Type: String  
Required: No

 ** type **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-type"></a>
The type of tool use.  
Type: String  
Valid Values: `tool_use | server_tool_use | mcp_tool_use`   
Required: No

### See Also
<a name="API_HarnessToolUseBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolUseBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolUseBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolUseBlock) 

## HarnessToolUseBlockDelta
<a name="API_HarnessToolUseBlockDelta"></a>

Delta payload for tool use input.

### Contents
<a name="API_HarnessToolUseBlockDelta_Contents"></a>

 ** input **   <a name="BedrockAgentCore-Type-HarnessToolUseBlockDelta-input"></a>
The partial JSON input for the tool call.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

### See Also
<a name="API_HarnessToolUseBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolUseBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolUseBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolUseBlockDelta) 

## HarnessToolUseBlockStart
<a name="API_HarnessToolUseBlockStart"></a>

Start payload for a tool use content block.

### Contents
<a name="API_HarnessToolUseBlockStart_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-HarnessToolUseBlockStart-name"></a>
The name of the tool being called.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolUseBlockStart-toolUseId"></a>
The unique ID of this tool use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** serverName **   <a name="BedrockAgentCore-Type-HarnessToolUseBlockStart-serverName"></a>
The name of the MCP server providing this tool.  
Type: String  
Required: No

 ** type **   <a name="BedrockAgentCore-Type-HarnessToolUseBlockStart-type"></a>
The type of tool use.  
Type: String  
Valid Values: `tool_use | server_tool_use | mcp_tool_use`   
Required: No

### See Also
<a name="API_HarnessToolUseBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolUseBlockStart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolUseBlockStart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolUseBlockStart) 

## IngestPayloadType
<a name="API_IngestPayloadType"></a>

A single content payload item to ingest. A payload item contains either conversational or JSON content.

### Contents
<a name="API_IngestPayloadType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conversational **   <a name="BedrockAgentCore-Type-IngestPayloadType-conversational"></a>
The conversational content for this payload item.  
Type: [Conversational](#API_Conversational) object  
Required: No

 ** json **   <a name="BedrockAgentCore-Type-IngestPayloadType-json"></a>
The JSON content for this payload item.  
Type: [MemoryJsonData](#API_MemoryJsonData) object  
Required: No

### See Also
<a name="API_IngestPayloadType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/IngestPayloadType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/IngestPayloadType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/IngestPayloadType) 

## InlineGroundTruth
<a name="API_InlineGroundTruth"></a>

Inline ground truth data containing assertions, expected trajectories, and per-turn expected responses.

### Contents
<a name="API_InlineGroundTruth_Contents"></a>

 ** assertions **   <a name="BedrockAgentCore-Type-InlineGroundTruth-assertions"></a>
Assertions for evaluation, reuses common model EvaluationContentList.  
Type: Array of [EvaluationContent](#API_EvaluationContent) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** expectedTrajectory **   <a name="BedrockAgentCore-Type-InlineGroundTruth-expectedTrajectory"></a>
The expected tool call sequence for trajectory evaluation.  
Type: [EvaluationExpectedTrajectory](#API_EvaluationExpectedTrajectory) object  
Required: No

 ** turns **   <a name="BedrockAgentCore-Type-InlineGroundTruth-turns"></a>
A list of per-turn ground truth data, each containing an input prompt and expected response.  
Type: Array of [GroundTruthTurn](#API_GroundTruthTurn) objects  
Array Members: Minimum number of 1 item.  
Required: No

### See Also
<a name="API_InlineGroundTruth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InlineGroundTruth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InlineGroundTruth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InlineGroundTruth) 

## InlineMemoryContent
<a name="API_InlineMemoryContent"></a>

The content included directly in the request as one or more payload items.

### Contents
<a name="API_InlineMemoryContent_Contents"></a>

 ** payload **   <a name="BedrockAgentCore-Type-InlineMemoryContent-payload"></a>
The list of content payload items to ingest.  
Type: Array of [IngestPayloadType](#API_IngestPayloadType) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: Yes

### See Also
<a name="API_InlineMemoryContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InlineMemoryContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InlineMemoryContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InlineMemoryContent) 

## InputContentBlock
<a name="API_InputContentBlock"></a>

A block of input content.

### Contents
<a name="API_InputContentBlock_Contents"></a>

 ** path **   <a name="BedrockAgentCore-Type-InputContentBlock-path"></a>
The path to the input content.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: Yes

 ** blob **   <a name="BedrockAgentCore-Type-InputContentBlock-blob"></a>
The binary input content.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-InputContentBlock-text"></a>
The text input content.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

### See Also
<a name="API_InputContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InputContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InputContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InputContentBlock) 

## Insight
<a name="API_Insight"></a>

A reference to an insight analysis to run against sessions during batch evaluation. Insights provide deeper analysis beyond individual evaluator scores, including failure detection, user intent clustering, and execution summarization.

### Contents
<a name="API_Insight_Contents"></a>

 ** insightId **   <a name="BedrockAgentCore-Type-Insight-insightId"></a>
The unique identifier of the insight to run.  
Type: String  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

### See Also
<a name="API_Insight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Insight) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Insight) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Insight) 

## InsightsFailureSignal
<a name="API_InsightsFailureSignal"></a>

A signal indicating a detected failure within a span.

### Contents
<a name="API_InsightsFailureSignal_Contents"></a>

 ** category **   <a name="BedrockAgentCore-Type-InsightsFailureSignal-category"></a>
The failure category classification for this signal.  
Type: String  
Valid Values: `execution-error-category-authentication | execution-error-category-resource-not-found | execution-error-category-service-errors | execution-error-category-rate-limiting | execution-error-category-formatting | execution-error-category-timeout | execution-error-category-resource-exhaustion | execution-error-category-environment | execution-error-category-tool-schema | task-instruction-category-non-compliance | task-instruction-category-problem-id | incorrect-actions-category-tool-selection | incorrect-actions-category-poor-information-retrieval | incorrect-actions-category-clarification | incorrect-actions-category-inappropriate-info-request | context-handling-error-category-context-handling-failures | hallucination-category-hall-capabilities | hallucination-category-hall-misunderstand | hallucination-category-hall-usage | hallucination-category-hall-history | hallucination-category-hall-params | hallucination-category-fabricate-tool-outputs | repetitive-behavior-category-repetition-tool | repetitive-behavior-category-repetition-info | repetitive-behavior-category-step-repetition | orchestration-related-errors-category-reasoning-mismatch | orchestration-related-errors-category-goal-deviation | orchestration-related-errors-category-premature-termination | orchestration-related-errors-category-unaware-termination | llm-output-category-nonsensical | configuration-mismatch-category-tool-definition | coding-use-case-specific-failure-types-category-edge-case-oversights | coding-use-case-specific-failure-types-category-dependency-issues | other`   
Required: Yes

 ** confidence **   <a name="BedrockAgentCore-Type-InsightsFailureSignal-confidence"></a>
The confidence score of the failure detection.  
Type: Double  
Required: Yes

 ** evidence **   <a name="BedrockAgentCore-Type-InsightsFailureSignal-evidence"></a>
The evidence supporting the failure detection.  
Type: String  
Required: Yes

### See Also
<a name="API_InsightsFailureSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InsightsFailureSignal) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InsightsFailureSignal) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InsightsFailureSignal) 

## InvokeAgentRuntimeCommandRequestBody
<a name="API_InvokeAgentRuntimeCommandRequestBody"></a>

The request body structure for the `InvokeAgentRuntimeCommand` operation, containing the command to execute and optional configuration parameters.

### Contents
<a name="API_InvokeAgentRuntimeCommandRequestBody_Contents"></a>

 ** command **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandRequestBody-command"></a>
The shell command to execute on the agent runtime. This command is executed in the runtime environment and its output is streamed back to the caller.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Required: Yes

 ** timeout **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandRequestBody-timeout"></a>
The maximum duration in seconds to wait for the command to complete. If the command execution exceeds this timeout, it will be terminated. Default is 300 seconds. Minimum is 1 second. Maximum is 3600 seconds.  
Type: Integer  
Required: No

### See Also
<a name="API_InvokeAgentRuntimeCommandRequestBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandRequestBody) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandRequestBody) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandRequestBody) 

## InvokeAgentRuntimeCommandStreamOutput
<a name="API_InvokeAgentRuntimeCommandStreamOutput"></a>

The streaming output union for the `InvokeAgentRuntimeCommand` operation. This union delivers typed events: `contentStart` (first), `contentDelta` (middle), and `contentStop` (last).

### Contents
<a name="API_InvokeAgentRuntimeCommandStreamOutput_Contents"></a>

 ** accessDeniedException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-accessDeniedException"></a>
Exception events for error streaming.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** chunk **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-chunk"></a>
A response chunk containing command execution events such as content start, content delta, or content stop events.  
Type: [ResponseChunk](#API_ResponseChunk) object  
Required: No

 ** internalServerException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** resourceNotFoundException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** runtimeClientError **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-runtimeClientError"></a>
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** serviceQuotaExceededException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402  
Required: No

 ** throttlingException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

### See Also
<a name="API_InvokeAgentRuntimeCommandStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandStreamOutput) 

## InvokeHarnessStreamOutput
<a name="API_InvokeHarnessStreamOutput"></a>

The streaming events returned by a harness invocation.

### Contents
<a name="API_InvokeHarnessStreamOutput_Contents"></a>

 ** contentBlockDelta **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-contentBlockDelta"></a>
A delta update to the current content block.  
Type: [HarnessContentBlockDeltaEvent](#API_HarnessContentBlockDeltaEvent) object  
Required: No

 ** contentBlockStart **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-contentBlockStart"></a>
Indicates the start of a new content block.  
Type: [HarnessContentBlockStartEvent](#API_HarnessContentBlockStartEvent) object  
Required: No

 ** contentBlockStop **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-contentBlockStop"></a>
Indicates the end of the current content block.  
Type: [HarnessContentBlockStopEvent](#API_HarnessContentBlockStopEvent) object  
Required: No

 ** internalServerException **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** messageStart **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-messageStart"></a>
Indicates the start of a new message from the agent.  
Type: [HarnessMessageStartEvent](#API_HarnessMessageStartEvent) object  
Required: No

 ** messageStop **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-messageStop"></a>
Indicates the end of the current message.  
Type: [HarnessMessageStopEvent](#API_HarnessMessageStopEvent) object  
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-metadata"></a>
Token usage and latency metrics for the invocation.  
Type: [HarnessMetadataEvent](#API_HarnessMetadataEvent) object  
Required: No

 ** runtimeClientError **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-runtimeClientError"></a>
An error returned by the runtime container during agent execution.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** validationException **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

### See Also
<a name="API_InvokeHarnessStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeHarnessStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeHarnessStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeHarnessStreamOutput) 

## KeyPressArguments
<a name="API_KeyPressArguments"></a>

Arguments for a key press action.

### Contents
<a name="API_KeyPressArguments_Contents"></a>

 ** key **   <a name="BedrockAgentCore-Type-KeyPressArguments-key"></a>
The key name to press (for example, `enter`, `tab`, `escape`).  
Type: String  
Required: Yes

 ** presses **   <a name="BedrockAgentCore-Type-KeyPressArguments-presses"></a>
The number of times to press the key. Valid range: 1–100. Defaults to 1.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

### See Also
<a name="API_KeyPressArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/KeyPressArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/KeyPressArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/KeyPressArguments) 

## KeyPressResult
<a name="API_KeyPressResult"></a>

The result of a key press action.

### Contents
<a name="API_KeyPressResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-KeyPressResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-KeyPressResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_KeyPressResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/KeyPressResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/KeyPressResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/KeyPressResult) 

## KeyShortcutArguments
<a name="API_KeyShortcutArguments"></a>

Arguments for a key shortcut action.

### Contents
<a name="API_KeyShortcutArguments_Contents"></a>

 ** keys **   <a name="BedrockAgentCore-Type-KeyShortcutArguments-keys"></a>
The key combination to press (for example, `["ctrl", "s"]`). Maximum 5 keys.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

### See Also
<a name="API_KeyShortcutArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/KeyShortcutArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/KeyShortcutArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/KeyShortcutArguments) 

## KeyShortcutResult
<a name="API_KeyShortcutResult"></a>

The result of a key shortcut action.

### Contents
<a name="API_KeyShortcutResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-KeyShortcutResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-KeyShortcutResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_KeyShortcutResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/KeyShortcutResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/KeyShortcutResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/KeyShortcutResult) 

## KeyTypeArguments
<a name="API_KeyTypeArguments"></a>

Arguments for a key type action.

### Contents
<a name="API_KeyTypeArguments_Contents"></a>

 ** text **   <a name="BedrockAgentCore-Type-KeyTypeArguments-text"></a>
The text string to type. Maximum length: 10,000 characters.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10000.  
Required: Yes

### See Also
<a name="API_KeyTypeArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/KeyTypeArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/KeyTypeArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/KeyTypeArguments) 

## KeyTypeResult
<a name="API_KeyTypeResult"></a>

The result of a key type action.

### Contents
<a name="API_KeyTypeResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-KeyTypeResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-KeyTypeResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_KeyTypeResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/KeyTypeResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/KeyTypeResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/KeyTypeResult) 

## LeftExpression
<a name="API_LeftExpression"></a>

Left expression of the event metadata filter.

### Contents
<a name="API_LeftExpression_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** metadataKey **   <a name="BedrockAgentCore-Type-LeftExpression-metadataKey"></a>
Key associated with the metadata in an event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_LeftExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LeftExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LeftExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LeftExpression) 

## LinkedAccount
<a name="API_LinkedAccount"></a>

Represents different linked accounts that can be linked to an embedded wallet. Supports email, SMS, JWT, and OAuth2 approaches.

### Contents
<a name="API_LinkedAccount_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** developerJwt **   <a name="BedrockAgentCore-Type-LinkedAccount-developerJwt"></a>
Developer JWT linked account with key ID and subject.  
Type: [LinkedAccountDeveloperJwt](#API_LinkedAccountDeveloperJwt) object  
Required: No

 ** email **   <a name="BedrockAgentCore-Type-LinkedAccount-email"></a>
Email-based linked account.  
Type: [LinkedAccountEmail](#API_LinkedAccountEmail) object  
Required: No

 ** oAuth2 **   <a name="BedrockAgentCore-Type-LinkedAccount-oAuth2"></a>
OAuth2 provider linked account (Google, Apple, X, Telegram, GitHub).  
Type: [LinkedAccountOAuth2](#API_LinkedAccountOAuth2) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** sms **   <a name="BedrockAgentCore-Type-LinkedAccount-sms"></a>
SMS-based linked account using phone number.  
Type: [LinkedAccountSms](#API_LinkedAccountSms) object  
Required: No

### See Also
<a name="API_LinkedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccount) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccount) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccount) 

## LinkedAccountDeveloperJwt
<a name="API_LinkedAccountDeveloperJwt"></a>

Authentication method using JWT with key ID and subject claims.

### Contents
<a name="API_LinkedAccountDeveloperJwt_Contents"></a>

 ** kid **   <a name="BedrockAgentCore-Type-LinkedAccountDeveloperJwt-kid"></a>
The key ID (kid) from the JWT header. Identifies which key was used to sign the JWT.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9_-]{1,255}`   
Required: Yes

 ** sub **   <a name="BedrockAgentCore-Type-LinkedAccountDeveloperJwt-sub"></a>
The subject (sub) claim from the JWT payload. Identifies the principal that is the subject of the JWT.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

### See Also
<a name="API_LinkedAccountDeveloperJwt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccountDeveloperJwt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccountDeveloperJwt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccountDeveloperJwt) 

## LinkedAccountEmail
<a name="API_LinkedAccountEmail"></a>

Linked account using an email address.

### Contents
<a name="API_LinkedAccountEmail_Contents"></a>

 ** emailAddress **   <a name="BedrockAgentCore-Type-LinkedAccountEmail-emailAddress"></a>
The email address used for the linked account. Must be a valid email format.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 254.  
Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`   
Required: Yes

### See Also
<a name="API_LinkedAccountEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccountEmail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccountEmail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccountEmail) 

## LinkedAccountOAuth2
<a name="API_LinkedAccountOAuth2"></a>

Authentication method using OAuth2 providers. Supports Google, Apple, X, Telegram, and GitHub providers.

### Contents
<a name="API_LinkedAccountOAuth2_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apple **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-apple"></a>
Apple OAuth2 authentication.  
Type: [OAuth2Authentication](#API_OAuth2Authentication) object  
Required: No

 ** github **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-github"></a>
GitHub OAuth2 authentication.  
Type: [OAuth2Authentication](#API_OAuth2Authentication) object  
Required: No

 ** google **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-google"></a>
Google OAuth2 authentication.  
Type: [OAuth2Authentication](#API_OAuth2Authentication) object  
Required: No

 ** telegram **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-telegram"></a>
Telegram OAuth2 authentication.  
Type: [OAuth2Authentication](#API_OAuth2Authentication) object  
Required: No

 ** x **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-x"></a>
X (formerly Twitter) OAuth2 authentication.  
Type: [OAuth2Authentication](#API_OAuth2Authentication) object  
Required: No

### See Also
<a name="API_LinkedAccountOAuth2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccountOAuth2) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccountOAuth2) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccountOAuth2) 

## LinkedAccountSms
<a name="API_LinkedAccountSms"></a>

Linked account using a phone number in E.164 format.

### Contents
<a name="API_LinkedAccountSms_Contents"></a>

 ** phoneNumber **   <a name="BedrockAgentCore-Type-LinkedAccountSms-phoneNumber"></a>
The phone number in E.164 format (e.g., \+1234567890).  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 16.  
Pattern: `\+[1-9]\d{1,14}`   
Required: Yes

### See Also
<a name="API_LinkedAccountSms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccountSms) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccountSms) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccountSms) 

## LiveViewStream
<a name="API_LiveViewStream"></a>

The configuration for a stream that provides a visual representation of a browser session in Amazon Bedrock AgentCore. This stream enables agents to observe the current state of the browser, including rendered web pages, visual elements, and the results of interactions.

### Contents
<a name="API_LiveViewStream_Contents"></a>

 ** streamEndpoint **   <a name="BedrockAgentCore-Type-LiveViewStream-streamEndpoint"></a>
The endpoint URL for the live view stream. This URL is used to establish a connection to receive visual updates from the browser session.  
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 512.  
Required: No

### See Also
<a name="API_LiveViewStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LiveViewStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LiveViewStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LiveViewStream) 

## McpDescriptor
<a name="API_McpDescriptor"></a>

 The MCP (Model Context Protocol) descriptor configuration for a registry record. Contains the server definition and tools definition.

### Contents
<a name="API_McpDescriptor_Contents"></a>

 ** server **   <a name="BedrockAgentCore-Type-McpDescriptor-server"></a>
 The MCP server definition that describes the server configuration.  
Type: [ServerDefinition](#API_ServerDefinition) object  
Required: Yes

 ** tools **   <a name="BedrockAgentCore-Type-McpDescriptor-tools"></a>
 The MCP tools definition that describes the available tools.  
Type: [ToolsDefinition](#API_ToolsDefinition) object  
Required: Yes

### See Also
<a name="API_McpDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/McpDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/McpDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/McpDescriptor) 

## MemoryContent
<a name="API_MemoryContent"></a>

Contains the content of a memory record.

### Contents
<a name="API_MemoryContent_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="BedrockAgentCore-Type-MemoryContent-text"></a>
The text content of the memory record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16000.  
Required: No

### See Also
<a name="API_MemoryContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryContent) 

## MemoryJsonData
<a name="API_MemoryJsonData"></a>

Contains non-conversational, JSON-formatted content for an event payload. JSON payloads are extracted into long-term memory.

### Contents
<a name="API_MemoryJsonData_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-MemoryJsonData-content"></a>
The JSON content of the payload. Accepts any JSON value, including objects, arrays, strings, numbers, booleans, and null. The maximum size is 100 KB.  
Type: JSON value  
Required: Yes

### See Also
<a name="API_MemoryJsonData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryJsonData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryJsonData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryJsonData) 

## MemoryMetadataFilterExpression
<a name="API_MemoryMetadataFilterExpression"></a>

Filters to apply to metadata associated with a memory. Specify the metadata key and value in the `left` and `right` fields and use the `operator` field to define the relationship to match.

### Contents
<a name="API_MemoryMetadataFilterExpression_Contents"></a>

 ** left **   <a name="BedrockAgentCore-Type-MemoryMetadataFilterExpression-left"></a>
The metadata key to evaluate.  
Type: [MemoryRecordLeftExpression](#API_MemoryRecordLeftExpression) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** operator **   <a name="BedrockAgentCore-Type-MemoryMetadataFilterExpression-operator"></a>
The relationship between the metadata key and value to match when applying the metadata filter.  
Type: String  
Valid Values: `EQUALS_TO | EXISTS | NOT_EXISTS | BEFORE | AFTER | CONTAINS | GREATER_THAN | GREATER_THAN_OR_EQUALS | LESS_THAN | LESS_THAN_OR_EQUALS`   
Required: Yes

 ** right **   <a name="BedrockAgentCore-Type-MemoryMetadataFilterExpression-right"></a>
The value to compare against. Required for all operators except EXISTS and NOT\_EXISTS.  
Type: [MemoryRecordRightExpression](#API_MemoryRecordRightExpression) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_MemoryMetadataFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryMetadataFilterExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryMetadataFilterExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryMetadataFilterExpression) 

## MemoryRecord
<a name="API_MemoryRecord"></a>

Contains information about a memory record in an AgentCore Memory resource.

### Contents
<a name="API_MemoryRecord_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecord-content"></a>
The content of the memory record.  
Type: [MemoryContent](#API_MemoryContent) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-MemoryRecord-createdAt"></a>
The timestamp when the memory record was created.  
Type: Timestamp  
Required: Yes

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecord-memoryRecordId"></a>
The unique identifier of the memory record.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecord-memoryStrategyId"></a>
The identifier of the memory strategy associated with this record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecord-namespaces"></a>
The namespaces associated with this memory record. Namespaces help organize and categorize memory records.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: Yes

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecord-metadata"></a>
A map of metadata key-value pairs associated with a memory record.  
Type: String to [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_MemoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecord) 

## MemoryRecordCreateInput
<a name="API_MemoryRecordCreateInput"></a>

Input structure to create a new memory record.

### Contents
<a name="API_MemoryRecordCreateInput_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-content"></a>
The content to be stored within the memory record.  
Type: [MemoryContent](#API_MemoryContent) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-namespaces"></a>
A list of namespace identifiers that categorize or group the memory record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: Yes

 ** requestIdentifier **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-requestIdentifier"></a>
A client-provided identifier for tracking this specific record creation request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** timestamp **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-timestamp"></a>
Time at which the memory record was created.  
Type: Timestamp  
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-memoryStrategyId"></a>
The ID of the memory strategy that defines how this memory record is grouped.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-metadata"></a>
Metadata key-value pairs to be stored with the memory record.  
Type: String to [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_MemoryRecordCreateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordCreateInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordCreateInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordCreateInput) 

## MemoryRecordDeleteInput
<a name="API_MemoryRecordDeleteInput"></a>

Input structure to delete an existing memory record.

### Contents
<a name="API_MemoryRecordDeleteInput_Contents"></a>

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordDeleteInput-memoryRecordId"></a>
The unique ID of the memory record to be deleted.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** namespace **   <a name="BedrockAgentCore-Type-MemoryRecordDeleteInput-namespace"></a>
The namespace of the memory record being deleted. This value is used for IAM condition key authorization.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

### See Also
<a name="API_MemoryRecordDeleteInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordDeleteInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordDeleteInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordDeleteInput) 

## MemoryRecordLeftExpression
<a name="API_MemoryRecordLeftExpression"></a>

The left-hand side of a memory record metadata filter expression.

### Contents
<a name="API_MemoryRecordLeftExpression_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** metadataKey **   <a name="BedrockAgentCore-Type-MemoryRecordLeftExpression-metadataKey"></a>
The metadata key to filter on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_MemoryRecordLeftExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordLeftExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordLeftExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordLeftExpression) 

## MemoryRecordMetadataValue
<a name="API_MemoryRecordMetadataValue"></a>

The value of a memory record metadata entry.

### Contents
<a name="API_MemoryRecordMetadataValue_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dateTimeValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-dateTimeValue"></a>
A timestamp value in ISO 8601 UTC format.  
Type: Timestamp  
Required: No

 ** numberValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-numberValue"></a>
A numeric value.  
Type: Double  
Required: No

 ** stringListValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-stringListValue"></a>
A list of string values.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** stringValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-stringValue"></a>
A string value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_MemoryRecordMetadataValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordMetadataValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordMetadataValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordMetadataValue) 

## MemoryRecordOutput
<a name="API_MemoryRecordOutput"></a>

Output information returned after processing a memory record operation.

### Contents
<a name="API_MemoryRecordOutput_Contents"></a>

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-memoryRecordId"></a>
The unique ID associated to the memory record.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-status"></a>
The status of the memory record operation (e.g., SUCCEEDED, FAILED).  
Type: String  
Valid Values: `SUCCEEDED | FAILED`   
Required: Yes

 ** errorCode **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-errorCode"></a>
The error code returned when the memory record operation fails.  
Type: Integer  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-errorMessage"></a>
A human-readable error message describing why the memory record operation failed.  
Type: String  
Required: No

 ** requestIdentifier **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-requestIdentifier"></a>
The client-provided identifier that was used to track this record operation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

### See Also
<a name="API_MemoryRecordOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordOutput) 

## MemoryRecordRightExpression
<a name="API_MemoryRecordRightExpression"></a>

The right-hand side of a memory record metadata filter expression.

### Contents
<a name="API_MemoryRecordRightExpression_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** metadataValue **   <a name="BedrockAgentCore-Type-MemoryRecordRightExpression-metadataValue"></a>
The metadata value to compare against.  
Type: [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_MemoryRecordRightExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordRightExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordRightExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordRightExpression) 

## MemoryRecordSummary
<a name="API_MemoryRecordSummary"></a>

Contains summary information about a memory record.

### Contents
<a name="API_MemoryRecordSummary_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-content"></a>
The content of the memory record.  
Type: [MemoryContent](#API_MemoryContent) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-createdAt"></a>
The timestamp when the memory record was created.  
Type: Timestamp  
Required: Yes

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-memoryRecordId"></a>
The unique identifier of the memory record.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-memoryStrategyId"></a>
The identifier of the memory strategy associated with this record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-namespaces"></a>
The namespaces associated with this memory record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: Yes

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-metadata"></a>
A map of metadata key-value pairs associated with a memory record.  
Type: String to [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** score **   <a name="BedrockAgentCore-Type-MemoryRecordSummary-score"></a>
The relevance score of the memory record when returned as part of a search result. Higher values indicate greater relevance to the search query.  
Type: Double  
Required: No

### See Also
<a name="API_MemoryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordSummary) 

## MemoryRecordUpdateInput
<a name="API_MemoryRecordUpdateInput"></a>

Input structure to update an existing memory record.

### Contents
<a name="API_MemoryRecordUpdateInput_Contents"></a>

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-memoryRecordId"></a>
The unique ID of the memory record to be updated.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** timestamp **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-timestamp"></a>
Time at which the memory record was updated  
Type: Timestamp  
Required: Yes

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-content"></a>
The content to be stored within the memory record.  
Type: [MemoryContent](#API_MemoryContent) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-memoryStrategyId"></a>
The updated ID of the memory strategy that defines how this memory record is grouped.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-metadata"></a>
Metadata key-value pairs to be stored with the memory record.  
Type: String to [MemoryRecordMetadataValue](#API_MemoryRecordMetadataValue) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-namespaces"></a>
The updated list of namespace identifiers for categorizing the memory record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** sourceNamespaces **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-sourceNamespaces"></a>
The namespaces of the source memory record being updated. This value is used for IAM condition key authorization.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

### See Also
<a name="API_MemoryRecordUpdateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordUpdateInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordUpdateInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordUpdateInput) 

## MessageMetadata
<a name="API_MessageMetadata"></a>

Metadata information associated with this message.

### Contents
<a name="API_MessageMetadata_Contents"></a>

 ** eventId **   <a name="BedrockAgentCore-Type-MessageMetadata-eventId"></a>
The identifier of the event associated with this message.  
Type: String  
Required: Yes

 ** messageIndex **   <a name="BedrockAgentCore-Type-MessageMetadata-messageIndex"></a>
The position of this message within that event’s ordered list of messages.  
Type: Integer  
Required: Yes

### See Also
<a name="API_MessageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MessageMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MessageMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MessageMetadata) 

## MetadataValue
<a name="API_MetadataValue"></a>

Value associated with the `eventMetadata` key.

### Contents
<a name="API_MetadataValue_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** stringValue **   <a name="BedrockAgentCore-Type-MetadataValue-stringValue"></a>
Value associated with the `eventMetadata` key.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_MetadataValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MetadataValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MetadataValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MetadataValue) 

## MouseClickArguments
<a name="API_MouseClickArguments"></a>

Arguments for a mouse click action.

### Contents
<a name="API_MouseClickArguments_Contents"></a>

 ** x **   <a name="BedrockAgentCore-Type-MouseClickArguments-x"></a>
The X coordinate on screen where the click occurs.  
Type: Integer  
Required: Yes

 ** y **   <a name="BedrockAgentCore-Type-MouseClickArguments-y"></a>
The Y coordinate on screen where the click occurs.  
Type: Integer  
Required: Yes

 ** button **   <a name="BedrockAgentCore-Type-MouseClickArguments-button"></a>
The mouse button to use. Defaults to `LEFT`.  
Type: String  
Valid Values: `LEFT | RIGHT | MIDDLE`   
Required: No

 ** clickCount **   <a name="BedrockAgentCore-Type-MouseClickArguments-clickCount"></a>
The number of clicks to perform. Valid range: 1–10. Defaults to 1.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: No

### See Also
<a name="API_MouseClickArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseClickArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseClickArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseClickArguments) 

## MouseClickResult
<a name="API_MouseClickResult"></a>

The result of a mouse click action.

### Contents
<a name="API_MouseClickResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-MouseClickResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-MouseClickResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_MouseClickResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseClickResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseClickResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseClickResult) 

## MouseDragArguments
<a name="API_MouseDragArguments"></a>

Arguments for a mouse drag action.

### Contents
<a name="API_MouseDragArguments_Contents"></a>

 ** endX **   <a name="BedrockAgentCore-Type-MouseDragArguments-endX"></a>
The ending X coordinate for the drag.  
Type: Integer  
Required: Yes

 ** endY **   <a name="BedrockAgentCore-Type-MouseDragArguments-endY"></a>
The ending Y coordinate for the drag.  
Type: Integer  
Required: Yes

 ** startX **   <a name="BedrockAgentCore-Type-MouseDragArguments-startX"></a>
The starting X coordinate for the drag.  
Type: Integer  
Required: Yes

 ** startY **   <a name="BedrockAgentCore-Type-MouseDragArguments-startY"></a>
The starting Y coordinate for the drag.  
Type: Integer  
Required: Yes

 ** button **   <a name="BedrockAgentCore-Type-MouseDragArguments-button"></a>
The mouse button to use for the drag. Defaults to `LEFT`.  
Type: String  
Valid Values: `LEFT | RIGHT | MIDDLE`   
Required: No

### See Also
<a name="API_MouseDragArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseDragArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseDragArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseDragArguments) 

## MouseDragResult
<a name="API_MouseDragResult"></a>

The result of a mouse drag action.

### Contents
<a name="API_MouseDragResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-MouseDragResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-MouseDragResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_MouseDragResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseDragResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseDragResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseDragResult) 

## MouseMoveArguments
<a name="API_MouseMoveArguments"></a>

Arguments for a mouse move action.

### Contents
<a name="API_MouseMoveArguments_Contents"></a>

 ** x **   <a name="BedrockAgentCore-Type-MouseMoveArguments-x"></a>
The target X coordinate on screen.  
Type: Integer  
Required: Yes

 ** y **   <a name="BedrockAgentCore-Type-MouseMoveArguments-y"></a>
The target Y coordinate on screen.  
Type: Integer  
Required: Yes

### See Also
<a name="API_MouseMoveArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseMoveArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseMoveArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseMoveArguments) 

## MouseMoveResult
<a name="API_MouseMoveResult"></a>

The result of a mouse move action.

### Contents
<a name="API_MouseMoveResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-MouseMoveResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-MouseMoveResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_MouseMoveResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseMoveResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseMoveResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseMoveResult) 

## MouseScrollArguments
<a name="API_MouseScrollArguments"></a>

Arguments for a mouse scroll action.

### Contents
<a name="API_MouseScrollArguments_Contents"></a>

 ** x **   <a name="BedrockAgentCore-Type-MouseScrollArguments-x"></a>
The X coordinate on screen where the scroll occurs.  
Type: Integer  
Required: Yes

 ** y **   <a name="BedrockAgentCore-Type-MouseScrollArguments-y"></a>
The Y coordinate on screen where the scroll occurs.  
Type: Integer  
Required: Yes

 ** deltaX **   <a name="BedrockAgentCore-Type-MouseScrollArguments-deltaX"></a>
The horizontal scroll delta. Valid range: -1000 to 1000.  
Type: Integer  
Valid Range: Minimum value of -1000. Maximum value of 1000.  
Required: No

 ** deltaY **   <a name="BedrockAgentCore-Type-MouseScrollArguments-deltaY"></a>
The vertical scroll delta. Valid range: -1000 to 1000. Negative values scroll down.  
Type: Integer  
Valid Range: Minimum value of -1000. Maximum value of 1000.  
Required: No

### See Also
<a name="API_MouseScrollArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseScrollArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseScrollArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseScrollArguments) 

## MouseScrollResult
<a name="API_MouseScrollResult"></a>

The result of a mouse scroll action.

### Contents
<a name="API_MouseScrollResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-MouseScrollResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-MouseScrollResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_MouseScrollResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseScrollResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseScrollResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseScrollResult) 

## MppPaymentInput
<a name="API_MppPaymentInput"></a>

Contains the payment challenge from a 402 Payment Required response. Forward the raw `WWW-Authenticate: Payment` header value verbatim. In response, you receive a payment credential that satisfies the challenge. Provide exactly one challenge per request.

### Contents
<a name="API_MppPaymentInput_Contents"></a>

 ** version **   <a name="BedrockAgentCore-Type-MppPaymentInput-version"></a>
The MPP protocol version, for example "1" or "2".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10.  
Pattern: `[0-9]+`   
Required: Yes

 ** wwwAuthenticateHeaders **   <a name="BedrockAgentCore-Type-MppPaymentInput-wwwAuthenticateHeaders"></a>
The raw `WWW-Authenticate: Payment` header value from the 402 response, passed verbatim. Provide exactly one entry. The service uses this value to generate the payment credential.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 16384.  
Required: Yes

 ** buyerPaysGasFees **   <a name="BedrockAgentCore-Type-MppPaymentInput-buyerPaysGasFees"></a>
Authorizes the service to sign a payment whose blockchain network (gas) fees are charged to your wallet, on top of the payment amount.  
The challenge indicates who sponsors the network fees. When the challenge does not sponsor them, the service signs the payment only if this field is `true`. Otherwise it returns a validation error, so you can decide whether to pay the fees or obtain a challenge that sponsors them.  
Optional. When omitted or `false`, you decline to pay network fees. This field has no effect on challenges that already sponsor the fees.  
Type: Boolean  
Required: No

### See Also
<a name="API_MppPaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MppPaymentInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MppPaymentInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MppPaymentInput) 

## MppPaymentOutput
<a name="API_MppPaymentOutput"></a>

Contains the payment credential, ready to retry the request.

### Contents
<a name="API_MppPaymentOutput_Contents"></a>

 ** paymentCredential **   <a name="BedrockAgentCore-Type-MppPaymentOutput-paymentCredential"></a>
Ready-to-send value for the `Authorization` header, in the form "Payment <base64url-token>". Attach this header and retry the original request. To inspect the full credential, base64url-decode the token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: Yes

 ** selectedPaymentId **   <a name="BedrockAgentCore-Type-MppPaymentOutput-selectedPaymentId"></a>
The id of the challenge that was paid, echoed from the input challenge so you can correlate the result without decoding the credential.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-MppPaymentOutput-version"></a>
The MPP protocol version, for example "1" or "2".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10.  
Pattern: `[0-9]+`   
Required: Yes

### See Also
<a name="API_MppPaymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MppPaymentOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MppPaymentOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MppPaymentOutput) 

## OAuth2Authentication
<a name="API_OAuth2Authentication"></a>

OAuth2 authentication information for third-party providers.

### Contents
<a name="API_OAuth2Authentication_Contents"></a>

 ** sub **   <a name="BedrockAgentCore-Type-OAuth2Authentication-sub"></a>
The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** emailAddress **   <a name="BedrockAgentCore-Type-OAuth2Authentication-emailAddress"></a>
The email address from the OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 254.  
Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`   
Required: No

 ** name **   <a name="BedrockAgentCore-Type-OAuth2Authentication-name"></a>
The user's name from the OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** username **   <a name="BedrockAgentCore-Type-OAuth2Authentication-username"></a>
The username from the OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_OAuth2Authentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OAuth2Authentication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OAuth2Authentication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OAuth2Authentication) 

## OAuthCredentialProvider
<a name="API_OAuthCredentialProvider"></a>

Configuration for an OAuth 2.0 credential provider used to authenticate tool calls.

### Contents
<a name="API_OAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-providerArn"></a>
The ARN of the OAuth 2.0 credential provider in AgentCore Identity.  
Type: String  
Pattern: `arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)`   
Required: Yes

 ** scopes **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-scopes"></a>
The OAuth 2.0 scopes to request when obtaining an access token.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** customParameters **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-customParameters"></a>
Additional custom parameters to include in the OAuth 2.0 token request.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Value Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** defaultReturnUrl **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-defaultReturnUrl"></a>
The default return URL for the OAuth 2.0 authorization flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\w+:(\/?\/?)[^\s]+`   
Required: No

 ** grantType **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-grantType"></a>
The OAuth 2.0 grant type to use for authentication.  
Type: String  
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | TOKEN_EXCHANGE`   
Required: No

### See Also
<a name="API_OAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OAuthCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OAuthCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OAuthCredentialProvider) 

## OnlineEvaluationConfigSource
<a name="API_OnlineEvaluationConfigSource"></a>

A reference to an existing online evaluation configuration to use as the data source for batch evaluation.

### Contents
<a name="API_OnlineEvaluationConfigSource_Contents"></a>

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-OnlineEvaluationConfigSource-onlineEvaluationConfigArn"></a>
The Amazon Resource Name (ARN) of the online evaluation configuration to use as the session source.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** timeRange **   <a name="BedrockAgentCore-Type-OnlineEvaluationConfigSource-timeRange"></a>
Optional session filter configuration to narrow down which sessions from the online evaluation configuration to include.  
Type: [SessionFilterConfig](#API_SessionFilterConfig) object  
Required: No

### See Also
<a name="API_OnlineEvaluationConfigSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OnlineEvaluationConfigSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OnlineEvaluationConfigSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OnlineEvaluationConfigSource) 

## OnlineEvaluationTraceConfig
<a name="API_OnlineEvaluationTraceConfig"></a>

Contains the configuration for reusing agent traces from an online evaluation configuration for recommendation analysis. Because online evaluation is a continuous stream, a time range specifies which evaluated sessions the recommendation includes.

### Contents
<a name="API_OnlineEvaluationTraceConfig_Contents"></a>

 ** endTime **   <a name="BedrockAgentCore-Type-OnlineEvaluationTraceConfig-endTime"></a>
The end time of the time range. Only sessions evaluated before this timestamp are included.  
Type: Timestamp  
Required: Yes

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-OnlineEvaluationTraceConfig-onlineEvaluationConfigArn"></a>
The ARN of the online evaluation configuration to reuse sessions from.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** startTime **   <a name="BedrockAgentCore-Type-OnlineEvaluationTraceConfig-startTime"></a>
The start time of the time range. Only sessions evaluated at or after this timestamp are included.  
Type: Timestamp  
Required: Yes

### See Also
<a name="API_OnlineEvaluationTraceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OnlineEvaluationTraceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OnlineEvaluationTraceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OnlineEvaluationTraceConfig) 

## OutputConfig
<a name="API_OutputConfig"></a>

Output destination configuration.

### Contents
<a name="API_OutputConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudWatchConfig **   <a name="BedrockAgentCore-Type-OutputConfig-cloudWatchConfig"></a>
The CloudWatch Logs configuration for writing evaluation results.  
Type: [CloudWatchOutputConfig](#API_CloudWatchOutputConfig) object  
Required: No

### See Also
<a name="API_OutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OutputConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OutputConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OutputConfig) 

## PayloadType
<a name="API_PayloadType"></a>

Contains the payload content for an event.

### Contents
<a name="API_PayloadType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** blob **   <a name="BedrockAgentCore-Type-PayloadType-blob"></a>
The binary content of the payload.  
Type: JSON value  
Required: No

 ** conversational **   <a name="BedrockAgentCore-Type-PayloadType-conversational"></a>
The conversational content of the payload.  
Type: [Conversational](#API_Conversational) object  
Required: No

 ** json **   <a name="BedrockAgentCore-Type-PayloadType-json"></a>
The JSON content of the payload. Use this type to store non-conversational, JSON-formatted data, such as behavioral events, activity logs, or system events.  
Type: [MemoryJsonData](#API_MemoryJsonData) object  
Required: No

### See Also
<a name="API_PayloadType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PayloadType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PayloadType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PayloadType) 

## PaymentInput
<a name="API_PaymentInput"></a>

The payment input details, which vary by payment type.

### Contents
<a name="API_PaymentInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cryptoX402 **   <a name="BedrockAgentCore-Type-PaymentInput-cryptoX402"></a>
Input for a crypto X402 payment.  
Type: [CryptoX402PaymentInput](#API_CryptoX402PaymentInput) object  
Required: No

 ** mpp **   <a name="BedrockAgentCore-Type-PaymentInput-mpp"></a>
Contains the payment challenge from a 402 Payment Required response. Forward the raw `WWW-Authenticate: Payment` header value verbatim. In response, you receive a payment credential that satisfies the challenge. Provide exactly one challenge per request.  
Type: [MppPaymentInput](#API_MppPaymentInput) object  
Required: No

### See Also
<a name="API_PaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentInput) 

## PaymentInstrument
<a name="API_PaymentInstrument"></a>

Represents a payment instrument.

### Contents
<a name="API_PaymentInstrument_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentInstrument-createdAt"></a>
The timestamp when this payment instrument was created.  
Type: Timestamp  
Required: Yes

 ** paymentConnectorId **   <a name="BedrockAgentCore-Type-PaymentInstrument-paymentConnectorId"></a>
The ID of the payment connector associated with this instrument.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** paymentInstrumentDetails **   <a name="BedrockAgentCore-Type-PaymentInstrument-paymentInstrumentDetails"></a>
The details specific to the payment instrument type.  
Type: [PaymentInstrumentDetails](#API_PaymentInstrumentDetails) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** paymentInstrumentId **   <a name="BedrockAgentCore-Type-PaymentInstrument-paymentInstrumentId"></a>
The unique identifier for this payment instrument.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** paymentInstrumentType **   <a name="BedrockAgentCore-Type-PaymentInstrument-paymentInstrumentType"></a>
The type of payment instrument (e.g., EMBEDDED\_CRYPTO\_WALLET).  
Type: String  
Valid Values: `EMBEDDED_CRYPTO_WALLET`   
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentInstrument-paymentManagerArn"></a>
The ARN of the payment manager that owns this payment instrument.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-PaymentInstrument-status"></a>
The current status of this payment instrument.  
Type: String  
Valid Values: `INITIATED | ACTIVE | FAILED | DELETED | BLOCKED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentInstrument-updatedAt"></a>
The timestamp when this payment instrument was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentInstrument-userId"></a>
The user ID associated with this payment instrument.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

### See Also
<a name="API_PaymentInstrument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentInstrument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentInstrument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentInstrument) 

## PaymentInstrumentDetails
<a name="API_PaymentInstrumentDetails"></a>

Details specific to the instrument type.

### Contents
<a name="API_PaymentInstrumentDetails_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** embeddedCryptoWallet **   <a name="BedrockAgentCore-Type-PaymentInstrumentDetails-embeddedCryptoWallet"></a>
Embedded crypto wallet managed directly by end user.  
Type: [EmbeddedCryptoWallet](#API_EmbeddedCryptoWallet) object  
Required: No

### See Also
<a name="API_PaymentInstrumentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentInstrumentDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentInstrumentDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentInstrumentDetails) 

## PaymentInstrumentSummary
<a name="API_PaymentInstrumentSummary"></a>

Summary of a payment instrument for list operations.

### Contents
<a name="API_PaymentInstrumentSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-createdAt"></a>
The timestamp when this payment instrument was created.  
Type: Timestamp  
Required: Yes

 ** paymentConnectorId **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentConnectorId"></a>
The ID of the payment connector associated with this instrument.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** paymentInstrumentId **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentInstrumentId"></a>
The unique identifier for this payment instrument.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** paymentInstrumentType **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentInstrumentType"></a>
The type of payment instrument (e.g., EMBEDDED\_CRYPTO\_WALLET).  
Type: String  
Valid Values: `EMBEDDED_CRYPTO_WALLET`   
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentManagerArn"></a>
The ARN of the payment manager that owns this payment instrument.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-status"></a>
The current status of this payment instrument.  
Type: String  
Valid Values: `INITIATED | ACTIVE | FAILED | DELETED | BLOCKED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-updatedAt"></a>
The timestamp when this payment instrument was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-userId"></a>
The user ID associated with this payment instrument.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

### See Also
<a name="API_PaymentInstrumentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentInstrumentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentInstrumentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentInstrumentSummary) 

## PaymentOutput
<a name="API_PaymentOutput"></a>

The payment output details, which vary by payment type.

### Contents
<a name="API_PaymentOutput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cryptoX402 **   <a name="BedrockAgentCore-Type-PaymentOutput-cryptoX402"></a>
Output from a crypto X402 payment.  
Type: [CryptoX402PaymentOutput](#API_CryptoX402PaymentOutput) object  
Required: No

 ** mpp **   <a name="BedrockAgentCore-Type-PaymentOutput-mpp"></a>
Contains the payment credential, ready to retry the request.  
Type: [MppPaymentOutput](#API_MppPaymentOutput) object  
Required: No

### See Also
<a name="API_PaymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentOutput) 

## PaymentSession
<a name="API_PaymentSession"></a>

A payment session for managing payment transactions.

### Contents
<a name="API_PaymentSession_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentSession-createdAt"></a>
The timestamp when the session was created.  
Type: Timestamp  
Required: Yes

 ** expiryTimeInMinutes **   <a name="BedrockAgentCore-Type-PaymentSession-expiryTimeInMinutes"></a>
The session expiry time in minutes.  
Type: Integer  
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentSession-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** paymentSessionId **   <a name="BedrockAgentCore-Type-PaymentSession-paymentSessionId"></a>
The unique identifier of the payment session.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentSession-updatedAt"></a>
The timestamp when the session was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentSession-userId"></a>
The user ID associated with this session.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

 ** availableLimits **   <a name="BedrockAgentCore-Type-PaymentSession-availableLimits"></a>
The current available spending limits.  
Type: [AvailableLimits](#API_AvailableLimits) object  
Required: No

 ** limits **   <a name="BedrockAgentCore-Type-PaymentSession-limits"></a>
The spending limits for the payment session.  
Type: [SessionLimits](#API_SessionLimits) object  
Required: No

### See Also
<a name="API_PaymentSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentSession) 

## PaymentSessionSummary
<a name="API_PaymentSessionSummary"></a>

Summary information about a payment session.

### Contents
<a name="API_PaymentSessionSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-createdAt"></a>
The timestamp when the session was created.  
Type: Timestamp  
Required: Yes

 ** expiryTimeInMinutes **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-expiryTimeInMinutes"></a>
The session expiry time in minutes.  
Type: Integer  
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** paymentSessionId **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-paymentSessionId"></a>
The unique identifier of the payment session.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-updatedAt"></a>
The timestamp when the session was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-userId"></a>
The user ID associated with this session.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

### See Also
<a name="API_PaymentSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentSessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentSessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentSessionSummary) 

## PaymentTokenRequestInput
<a name="API_PaymentTokenRequestInput"></a>

Vendor-specific token request configuration.

### Contents
<a name="API_PaymentTokenRequestInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCdpTokenRequest **   <a name="BedrockAgentCore-Type-PaymentTokenRequestInput-coinbaseCdpTokenRequest"></a>
The Coinbase CDP token request.  
Type: [CoinbaseCdpTokenRequestInput](#API_CoinbaseCdpTokenRequestInput) object  
Required: No

 ** stripePrivyTokenRequest **   <a name="BedrockAgentCore-Type-PaymentTokenRequestInput-stripePrivyTokenRequest"></a>
The Stripe Privy token request.  
Type: [StripePrivyTokenRequestInput](#API_StripePrivyTokenRequestInput) object  
Required: No

### See Also
<a name="API_PaymentTokenRequestInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentTokenRequestInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentTokenRequestInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentTokenRequestInput) 

## PaymentTokenResponseOutput
<a name="API_PaymentTokenResponseOutput"></a>

Vendor-specific token response configuration.

### Contents
<a name="API_PaymentTokenResponseOutput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCdpTokenResponse **   <a name="BedrockAgentCore-Type-PaymentTokenResponseOutput-coinbaseCdpTokenResponse"></a>
The Coinbase CDP token response.  
Type: [CoinbaseCdpTokenResponseOutput](#API_CoinbaseCdpTokenResponseOutput) object  
Required: No

 ** stripePrivyTokenResponse **   <a name="BedrockAgentCore-Type-PaymentTokenResponseOutput-stripePrivyTokenResponse"></a>
The Stripe Privy token response.  
Type: [StripePrivyTokenResponseOutput](#API_StripePrivyTokenResponseOutput) object  
Required: No

### See Also
<a name="API_PaymentTokenResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentTokenResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentTokenResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentTokenResponseOutput) 

## PerVariantOnlineEvaluationConfig
<a name="API_PerVariantOnlineEvaluationConfig"></a>

An online evaluation configuration associated with a specific A/B test variant.

### Contents
<a name="API_PerVariantOnlineEvaluationConfig_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-PerVariantOnlineEvaluationConfig-name"></a>
The name of the variant this evaluation configuration applies to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2.  
Pattern: `(C|T1)`   
Required: Yes

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-PerVariantOnlineEvaluationConfig-onlineEvaluationConfigArn"></a>
The Amazon Resource Name (ARN) of the online evaluation configuration for this variant.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

### See Also
<a name="API_PerVariantOnlineEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PerVariantOnlineEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PerVariantOnlineEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PerVariantOnlineEvaluationConfig) 

## Proxy
<a name="API_Proxy"></a>

Union type representing different proxy configurations. Currently supports external customer-managed proxies.

### Contents
<a name="API_Proxy_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** externalProxy **   <a name="BedrockAgentCore-Type-Proxy-externalProxy"></a>
Configuration for an external customer-managed proxy server.  
Type: [ExternalProxy](#API_ExternalProxy) object  
Required: No

### See Also
<a name="API_Proxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Proxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Proxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Proxy) 

## ProxyBypass
<a name="API_ProxyBypass"></a>

Configuration for domains that should bypass all proxies and connect directly to the internet. These bypass rules take precedence over all proxy routing rules.

### Contents
<a name="API_ProxyBypass_Contents"></a>

 ** domainPatterns **   <a name="BedrockAgentCore-Type-ProxyBypass-domainPatterns"></a>
Array of domain patterns that should bypass the proxy. Supports `.amazonaws.com` for subdomain matching or `amazonaws.com` for exact domain matching. Requests to these domains connect directly without using any proxy. Maximum 253 characters per pattern.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\.)?[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`   
Required: No

### See Also
<a name="API_ProxyBypass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProxyBypass) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProxyBypass) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProxyBypass) 

## ProxyConfiguration
<a name="API_ProxyConfiguration"></a>

Configuration for routing browser traffic through customer-managed proxy servers. Supports 1-5 proxy servers for domain-based routing and proxy bypass rules.

### Contents
<a name="API_ProxyConfiguration_Contents"></a>

 ** proxies **   <a name="BedrockAgentCore-Type-ProxyConfiguration-proxies"></a>
An array of 1-5 proxy server configurations for domain-based routing. Each proxy can specify which domains it handles via `domainPatterns`, enabling flexible routing of different traffic through different proxies based on destination domain.  
Type: Array of [Proxy](#API_Proxy) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** bypass **   <a name="BedrockAgentCore-Type-ProxyConfiguration-bypass"></a>
Optional configuration for domains that should bypass all proxies and connect directly to their destination, like the internet. Takes precedence over all proxy routing rules.  
Type: [ProxyBypass](#API_ProxyBypass) object  
Required: No

### See Also
<a name="API_ProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProxyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProxyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProxyConfiguration) 

## ProxyCredentials
<a name="API_ProxyCredentials"></a>

Union type representing different proxy authentication methods. Currently supports HTTP Basic Authentication (username and password).

### Contents
<a name="API_ProxyCredentials_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** basicAuth **   <a name="BedrockAgentCore-Type-ProxyCredentials-basicAuth"></a>
HTTP Basic Authentication credentials (username and password) stored in AWS Secrets Manager.  
Type: [BasicAuth](#API_BasicAuth) object  
Required: No

### See Also
<a name="API_ProxyCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProxyCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProxyCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProxyCredentials) 

## RecommendationConfig
<a name="API_RecommendationConfig"></a>

The configuration for a recommendation, varying by recommendation type.

### Contents
<a name="API_RecommendationConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** systemPromptRecommendationConfig **   <a name="BedrockAgentCore-Type-RecommendationConfig-systemPromptRecommendationConfig"></a>
The configuration for a system prompt recommendation.  
Type: [SystemPromptRecommendationConfig](#API_SystemPromptRecommendationConfig) object  
Required: No

 ** toolDescriptionRecommendationConfig **   <a name="BedrockAgentCore-Type-RecommendationConfig-toolDescriptionRecommendationConfig"></a>
The configuration for a tool description recommendation.  
Type: [ToolDescriptionRecommendationConfig](#API_ToolDescriptionRecommendationConfig) object  
Required: No

### See Also
<a name="API_RecommendationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationConfig) 

## RecommendationEvaluationConfig
<a name="API_RecommendationEvaluationConfig"></a>

The evaluation configuration for assessing recommendation quality.

### Contents
<a name="API_RecommendationEvaluationConfig_Contents"></a>

 ** evaluators **   <a name="BedrockAgentCore-Type-RecommendationEvaluationConfig-evaluators"></a>
The list of evaluators to use for assessing recommendation quality.  
Type: Array of [RecommendationEvaluatorReference](#API_RecommendationEvaluatorReference) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

### See Also
<a name="API_RecommendationEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationEvaluationConfig) 

## RecommendationEvaluatorReference
<a name="API_RecommendationEvaluatorReference"></a>

A reference to an evaluator used for recommendation assessment.

### Contents
<a name="API_RecommendationEvaluatorReference_Contents"></a>

 ** evaluatorArn **   <a name="BedrockAgentCore-Type-RecommendationEvaluatorReference-evaluatorArn"></a>
The Amazon Resource Name (ARN) of the evaluator.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/(Builtin|ThirdParty)\.[a-zA-Z0-9._-]+`   
Required: Yes

### See Also
<a name="API_RecommendationEvaluatorReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationEvaluatorReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationEvaluatorReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationEvaluatorReference) 

## RecommendationResult
<a name="API_RecommendationResult"></a>

The result of a recommendation, containing the optimized output.

### Contents
<a name="API_RecommendationResult_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** systemPromptRecommendationResult **   <a name="BedrockAgentCore-Type-RecommendationResult-systemPromptRecommendationResult"></a>
The result of a system prompt recommendation.  
Type: [SystemPromptRecommendationResult](#API_SystemPromptRecommendationResult) object  
Required: No

 ** toolDescriptionRecommendationResult **   <a name="BedrockAgentCore-Type-RecommendationResult-toolDescriptionRecommendationResult"></a>
The result of a tool description recommendation.  
Type: [ToolDescriptionRecommendationResult](#API_ToolDescriptionRecommendationResult) object  
Required: No

### See Also
<a name="API_RecommendationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationResult) 

## RecommendationResultConfigurationBundle
<a name="API_RecommendationResultConfigurationBundle"></a>

A configuration bundle reference in a recommendation result.

### Contents
<a name="API_RecommendationResultConfigurationBundle_Contents"></a>

 ** bundleArn **   <a name="BedrockAgentCore-Type-RecommendationResultConfigurationBundle-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** versionId **   <a name="BedrockAgentCore-Type-RecommendationResultConfigurationBundle-versionId"></a>
The version identifier of the configuration bundle containing the recommendation.  
Type: String  
Required: Yes

### See Also
<a name="API_RecommendationResultConfigurationBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationResultConfigurationBundle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationResultConfigurationBundle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationResultConfigurationBundle) 

## RecommendationSummary
<a name="API_RecommendationSummary"></a>

Summary information about a recommendation.

### Contents
<a name="API_RecommendationSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-RecommendationSummary-createdAt"></a>
The timestamp when the recommendation was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-RecommendationSummary-name"></a>
The name of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`   
Required: Yes

 ** recommendationArn **   <a name="BedrockAgentCore-Type-RecommendationSummary-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

 ** recommendationId **   <a name="BedrockAgentCore-Type-RecommendationSummary-recommendationId"></a>
The unique identifier of the recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-RecommendationSummary-status"></a>
The current status of the recommendation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING`   
Required: Yes

 ** type **   <a name="BedrockAgentCore-Type-RecommendationSummary-type"></a>
The type of recommendation.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-RecommendationSummary-updatedAt"></a>
The timestamp when the recommendation was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-RecommendationSummary-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Required: No

### See Also
<a name="API_RecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationSummary) 

## RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

 Summary information about a registry record.

### Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-createdAt"></a>
 The date and time when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** descriptors **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-descriptors"></a>
 The descriptor configurations for this registry record.  
Type: [Descriptors](#API_Descriptors) object  
Required: Yes

 ** descriptorType **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-descriptorType"></a>
 The type of descriptor associated with this registry record.  
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS`   
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-name"></a>
 The name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-recordArn"></a>
 The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-recordId"></a>
 The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** registryArn **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-registryArn"></a>
 The Amazon Resource Name (ARN) of the registry that this record belongs to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-status"></a>
 The current status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-updatedAt"></a>
 The date and time when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-version"></a>
 The version of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-description"></a>
 A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

### See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RegistryRecordSummary) 

## ResourceContent
<a name="API_ResourceContent"></a>

Contains information about resource content.

### Contents
<a name="API_ResourceContent_Contents"></a>

 ** type **   <a name="BedrockAgentCore-Type-ResourceContent-type"></a>
The type of resource content.  
Type: String  
Valid Values: `text | blob`   
Required: Yes

 ** blob **   <a name="BedrockAgentCore-Type-ResourceContent-blob"></a>
The binary resource content.  
Type: Base64-encoded binary data object  
Required: No

 ** mimeType **   <a name="BedrockAgentCore-Type-ResourceContent-mimeType"></a>
The MIME type of the resource content.  
Type: String  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-ResourceContent-text"></a>
The text resource content.  
Type: String  
Required: No

 ** uri **   <a name="BedrockAgentCore-Type-ResourceContent-uri"></a>
The URI of the resource content.  
Type: String  
Required: No

### See Also
<a name="API_ResourceContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ResourceContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ResourceContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ResourceContent) 

## ResourceLocation
<a name="API_ResourceLocation"></a>

The location of the browser extension.

### Contents
<a name="API_ResourceLocation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="BedrockAgentCore-Type-ResourceLocation-s3"></a>
The Amazon S3 location of the resource. Use this when the resource is stored in an Amazon S3 bucket.  
Type: [S3Location](#API_S3Location) object  
Required: No

### See Also
<a name="API_ResourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ResourceLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ResourceLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ResourceLocation) 

## ResponseChunk
<a name="API_ResponseChunk"></a>

A structure representing a response chunk that contains exactly one of the possible event types: `contentStart`, `contentDelta`, or `contentStop`.

### Contents
<a name="API_ResponseChunk_Contents"></a>

 ** contentDelta **   <a name="BedrockAgentCore-Type-ResponseChunk-contentDelta"></a>
An event containing incremental output (stdout or stderr) from the command execution. These are the middle chunks.  
Type: [ContentDeltaEvent](#API_ContentDeltaEvent) object  
Required: No

 ** contentStart **   <a name="BedrockAgentCore-Type-ResponseChunk-contentStart"></a>
An event indicating the start of content streaming from the command execution. This is the first chunk received.  
Type: [ContentStartEvent](#API_ContentStartEvent) object  
Required: No

 ** contentStop **   <a name="BedrockAgentCore-Type-ResponseChunk-contentStop"></a>
An event indicating the completion of the command execution, including the exit code and final status. This is the last chunk received.  
Type: [ContentStopEvent](#API_ContentStopEvent) object  
Required: No

### See Also
<a name="API_ResponseChunk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ResponseChunk) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ResponseChunk) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ResponseChunk) 

## RightExpression
<a name="API_RightExpression"></a>

Right expression of the `eventMetadata`filter.

### Contents
<a name="API_RightExpression_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** metadataValue **   <a name="BedrockAgentCore-Type-RightExpression-metadataValue"></a>
Value associated with the key in `eventMetadata`.  
Type: [MetadataValue](#API_MetadataValue) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_RightExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RightExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RightExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RightExpression) 

## RootCauseCluster
<a name="API_RootCauseCluster"></a>

A cluster of similar root causes identified within a failure subcategory.

### Contents
<a name="API_RootCauseCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-RootCauseCluster-affectedSessionCount"></a>
The number of sessions affected by this root cause.  
Type: Integer  
Required: Yes

 ** affectedSessions **   <a name="BedrockAgentCore-Type-RootCauseCluster-affectedSessions"></a>
The list of sessions affected by this root cause.  
Type: Array of [AffectedSession](#API_AffectedSession) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-RootCauseCluster-clusterId"></a>
The unique identifier of the root cause cluster.  
Type: Integer  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-RootCauseCluster-name"></a>
The name of the root cause cluster.  
Type: String  
Required: Yes

 ** recommendation **   <a name="BedrockAgentCore-Type-RootCauseCluster-recommendation"></a>
The recommended fix for this root cause.  
Type: String  
Required: Yes

 ** rootCause **   <a name="BedrockAgentCore-Type-RootCauseCluster-rootCause"></a>
The root cause explanation for this cluster of failures.  
Type: String  
Required: Yes

### See Also
<a name="API_RootCauseCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RootCauseCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RootCauseCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RootCauseCluster) 

## S3FilesConfiguration
<a name="API_S3FilesConfiguration"></a>

The configuration for mounting an Amazon Simple Storage Service (Amazon S3) Files access point that you own into a session.

### Contents
<a name="API_S3FilesConfiguration_Contents"></a>

 ** accessPointArn **   <a name="BedrockAgentCore-Type-S3FilesConfiguration-accessPointArn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Storage Service (Amazon S3) Files access point to mount.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`   
Required: Yes

 ** fileSystemArn **   <a name="BedrockAgentCore-Type-S3FilesConfiguration-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Storage Service (Amazon S3) Files file system that owns the access point.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:s3files:[a-z0-9-]+:[0-9]{12}:file-system/fs-[0-9a-f]{17,40}`   
Required: Yes

 ** mountPath **   <a name="BedrockAgentCore-Type-S3FilesConfiguration-mountPath"></a>
The absolute path within the session at which the access point is mounted, for example `/mnt/s3data`. Each mount path must be unique across all file system configurations in the session.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 200.  
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`   
Required: Yes

### See Also
<a name="API_S3FilesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/S3FilesConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/S3FilesConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/S3FilesConfiguration) 

## S3Location
<a name="API_S3Location"></a>

The Amazon S3 location configuration of a resource.

### Contents
<a name="API_S3Location_Contents"></a>

 ** bucket **   <a name="BedrockAgentCore-Type-S3Location-bucket"></a>
The name of the Amazon S3 bucket where the resource is stored.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`   
Required: Yes

 ** prefix **   <a name="BedrockAgentCore-Type-S3Location-prefix"></a>
The name of the Amazon S3 prefix/key where the resource is stored.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** versionId **   <a name="BedrockAgentCore-Type-S3Location-versionId"></a>
The name of the Amazon S3 version ID where the resource is stored (Optional).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

### See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/S3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/S3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/S3Location) 

## ScreenshotArguments
<a name="API_ScreenshotArguments"></a>

Arguments for a screenshot action.

### Contents
<a name="API_ScreenshotArguments_Contents"></a>

 ** format **   <a name="BedrockAgentCore-Type-ScreenshotArguments-format"></a>
The image format for the screenshot. Defaults to `PNG`.  
Type: String  
Valid Values: `PNG`   
Required: No

### See Also
<a name="API_ScreenshotArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ScreenshotArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ScreenshotArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ScreenshotArguments) 

## ScreenshotResult
<a name="API_ScreenshotResult"></a>

The result of a screenshot action.

### Contents
<a name="API_ScreenshotResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-ScreenshotResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** data **   <a name="BedrockAgentCore-Type-ScreenshotResult-data"></a>
The base64-encoded image data. Present only when the action succeeded.  
Type: Base64-encoded binary data object  
Required: No

 ** error **   <a name="BedrockAgentCore-Type-ScreenshotResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

### See Also
<a name="API_ScreenshotResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ScreenshotResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ScreenshotResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ScreenshotResult) 

## SearchCriteria
<a name="API_SearchCriteria"></a>

Contains search criteria for retrieving memory records.

### Contents
<a name="API_SearchCriteria_Contents"></a>

 ** searchQuery **   <a name="BedrockAgentCore-Type-SearchCriteria-searchQuery"></a>
The search query to use for finding relevant memory records.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10000.  
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-SearchCriteria-memoryStrategyId"></a>
The memory strategy identifier to filter memory records by.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** metadataFilters **   <a name="BedrockAgentCore-Type-SearchCriteria-metadataFilters"></a>
Filters to apply to metadata associated with a memory.  
Type: Array of [MemoryMetadataFilterExpression](#API_MemoryMetadataFilterExpression) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

 ** topK **   <a name="BedrockAgentCore-Type-SearchCriteria-topK"></a>
The maximum number of top-scoring memory records to return. This value is used for semantic search ranking.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

### See Also
<a name="API_SearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SearchCriteria) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SearchCriteria) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SearchCriteria) 

## SecretsManagerLocation
<a name="API_SecretsManagerLocation"></a>

The AWS Secrets Manager location configuration.

### Contents
<a name="API_SecretsManagerLocation_Contents"></a>

 ** secretArn **   <a name="BedrockAgentCore-Type-SecretsManagerLocation-secretArn"></a>
The ARN of the AWS Secrets Manager secret containing the certificate.  
Type: String  
Pattern: `arn:aws(-[a-z-]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`   
Required: Yes

### See Also
<a name="API_SecretsManagerLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SecretsManagerLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SecretsManagerLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SecretsManagerLocation) 

## ServerDefinition
<a name="API_ServerDefinition"></a>

 The MCP server definition with a schema version and inline content. The `schemaVersion` identifies the version of the MCP server configuration schema.

### Contents
<a name="API_ServerDefinition_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-ServerDefinition-inlineContent"></a>
 The inline content of the server definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

 ** schemaVersion **   <a name="BedrockAgentCore-Type-ServerDefinition-schemaVersion"></a>
 The schema version of the MCP server configuration. The schema version identifies the format of the server definition content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_ServerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ServerDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ServerDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ServerDefinition) 

## SessionFilter
<a name="API_SessionFilter"></a>

Contains filter criteria for listing sessions.

### Contents
<a name="API_SessionFilter_Contents"></a>

 ** eventFilter **   <a name="BedrockAgentCore-Type-SessionFilter-eventFilter"></a>
The event filter condition to apply. Use this to filter sessions based on event presence.  
Type: String  
Valid Values: `HAS_EVENTS`   
Required: No

### See Also
<a name="API_SessionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionFilter) 

## SessionFilterConfig
<a name="API_SessionFilterConfig"></a>

A time range filter for selecting sessions. Specifies the start and end times to narrow down which sessions are included.

### Contents
<a name="API_SessionFilterConfig_Contents"></a>

 ** endTime **   <a name="BedrockAgentCore-Type-SessionFilterConfig-endTime"></a>
The end time of the time range. Only sessions with activity before this timestamp are included.  
Type: Timestamp  
Required: No

 ** startTime **   <a name="BedrockAgentCore-Type-SessionFilterConfig-startTime"></a>
The start time of the time range. Only sessions with activity at or after this timestamp are included.  
Type: Timestamp  
Required: No

### See Also
<a name="API_SessionFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionFilterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionFilterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionFilterConfig) 

## SessionLimits
<a name="API_SessionLimits"></a>

The spending limits configuration for a payment session.

### Contents
<a name="API_SessionLimits_Contents"></a>

 ** maxSpendAmount **   <a name="BedrockAgentCore-Type-SessionLimits-maxSpendAmount"></a>
The maximum amount that can be spent in the session.  
Type: [Amount](#API_Amount) object  
Required: Yes

### See Also
<a name="API_SessionLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionLimits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionLimits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionLimits) 

## SessionMetadataShape
<a name="API_SessionMetadataShape"></a>

Metadata for a specific session in a batch evaluation, including ground truth data and test scenario identifiers.

### Contents
<a name="API_SessionMetadataShape_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SessionMetadataShape-sessionId"></a>
The unique identifier of the session this metadata applies to.  
Type: String  
Required: Yes

 ** groundTruth **   <a name="BedrockAgentCore-Type-SessionMetadataShape-groundTruth"></a>
The ground truth data for this session, including expected responses and assertions.  
Type: [GroundTruthSource](#API_GroundTruthSource) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-SessionMetadataShape-metadata"></a>
Additional key-value metadata associated with this session.  
Type: String to string map  
Required: No

 ** testScenarioId **   <a name="BedrockAgentCore-Type-SessionMetadataShape-testScenarioId"></a>
An optional test scenario identifier for categorizing and tracking evaluation results.  
Type: String  
Required: No

### See Also
<a name="API_SessionMetadataShape_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionMetadataShape) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionMetadataShape) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionMetadataShape) 

## SessionSummary
<a name="API_SessionSummary"></a>

Contains summary information about a session in an AgentCore Memory resource.

### Contents
<a name="API_SessionSummary_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-SessionSummary-actorId"></a>
The identifier of the actor associated with the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-SessionSummary-createdAt"></a>
The timestamp when the session was created.  
Type: Timestamp  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-SessionSummary-sessionId"></a>
The unique identifier of the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

### See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionSummary) 

## SessionTraceIds
<a name="API_SessionTraceIds"></a>

A pairing of a session with the specific trace IDs to evaluate within that session. Use this to evaluate individual traces rather than an entire session.

### Contents
<a name="API_SessionTraceIds_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SessionTraceIds-sessionId"></a>
The unique identifier of the session that contains the traces to evaluate.  
Type: String  
Required: Yes

 ** traceIds **   <a name="BedrockAgentCore-Type-SessionTraceIds-traceIds"></a>
The list of trace IDs within the session to evaluate.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Fixed length of 32.  
Required: Yes

### See Also
<a name="API_SessionTraceIds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionTraceIds) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionTraceIds) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionTraceIds) 

## SkillDefinition
<a name="API_SkillDefinition"></a>

 The structured skill definition with a schema version and inline content.

### Contents
<a name="API_SkillDefinition_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-SkillDefinition-inlineContent"></a>
 The inline content of the skill definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

 ** schemaVersion **   <a name="BedrockAgentCore-Type-SkillDefinition-schemaVersion"></a>
 The schema version of the skill definition. If you don't specify a version, the service detects it automatically.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_SkillDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SkillDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SkillDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SkillDefinition) 

## SkillMdDefinition
<a name="API_SkillMdDefinition"></a>

 The skill markdown definition for agent skills descriptors.

### Contents
<a name="API_SkillMdDefinition_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-SkillMdDefinition-inlineContent"></a>
 The inline markdown content of the skill definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

### See Also
<a name="API_SkillMdDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SkillMdDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SkillMdDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SkillMdDefinition) 

## SpanContext
<a name="API_SpanContext"></a>

 The contextual information that uniquely identifies a span within the distributed tracing system. Contains session, trace, and span identifiers used to correlate evaluation results with specific agent execution points. 

### Contents
<a name="API_SpanContext_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SpanContext-sessionId"></a>
 The unique identifier of the session containing this span. Sessions represent complete conversation flows and are detected using configurable `SessionTimeoutMinutes` (default 15 minutes).   
Type: String  
Required: Yes

 ** spanId **   <a name="BedrockAgentCore-Type-SpanContext-spanId"></a>
 The unique identifier of the specific span being referenced. Spans represent individual operations like tool calls, model invocations, or other discrete actions within the agent's execution.   
Type: String  
Required: No

 ** traceId **   <a name="BedrockAgentCore-Type-SpanContext-traceId"></a>
 The unique identifier of the trace containing this span. Traces represent individual request-response interactions within a session and group related spans together.   
Type: String  
Required: No

### See Also
<a name="API_SpanContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SpanContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SpanContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SpanContext) 

## StreamUpdate
<a name="API_StreamUpdate"></a>

Contains information about an update to a stream.

### Contents
<a name="API_StreamUpdate_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** automationStreamUpdate **   <a name="BedrockAgentCore-Type-StreamUpdate-automationStreamUpdate"></a>
The update to an automation stream.  
Type: [AutomationStreamUpdate](#API_AutomationStreamUpdate) object  
Required: No

### See Also
<a name="API_StreamUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StreamUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StreamUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StreamUpdate) 

## StripePrivyTokenRequestInput
<a name="API_StripePrivyTokenRequestInput"></a>

Stripe Privy token request parameters.

### Contents
<a name="API_StripePrivyTokenRequestInput_Contents"></a>

 ** requestBody **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-requestBody"></a>
Request body JSON for the Privy API call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16384.  
Pattern: `[\u0009\u000A\u000D\u0020-\u007E]+`   
Required: Yes

 ** requestPath **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-requestPath"></a>
The path of the Stripe Privy API request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `/[a-zA-Z0-9/_\-\.~%?=&]+`   
Required: Yes

 ** includeAuthorizationSignature **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-includeAuthorizationSignature"></a>
Set to true to generate privy-authorization-signature.  
Type: Boolean  
Required: No

 ** requestHost **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-requestHost"></a>
The host for the Privy API request. Defaults to "api.privy.io".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\-\.]+`   
Required: No

### See Also
<a name="API_StripePrivyTokenRequestInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StripePrivyTokenRequestInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StripePrivyTokenRequestInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StripePrivyTokenRequestInput) 

## StripePrivyTokenResponseOutput
<a name="API_StripePrivyTokenResponseOutput"></a>

Stripe Privy token response containing appId, basicAuthToken, and optionally authorizationSignature.

### Contents
<a name="API_StripePrivyTokenResponseOutput_Contents"></a>

 ** appId **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-appId"></a>
The Privy app ID for the privy-app-id header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** basicAuthToken **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-basicAuthToken"></a>
Base64-encoded Basic Auth token (appId:appSecret) for the Authorization header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: Yes

 ** authorizationSignature **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-authorizationSignature"></a>
Base64-encoded ECDSA P-256 authorization signature (only present when includeAuthorizationSignature is true).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

 ** requestExpiry **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-requestExpiry"></a>
Unix timestamp in milliseconds when the authorization signature expires.  
Type: Long  
Required: No

### See Also
<a name="API_StripePrivyTokenResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StripePrivyTokenResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StripePrivyTokenResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StripePrivyTokenResponseOutput) 

## SystemPromptConfig
<a name="API_SystemPromptConfig"></a>

The system prompt input, either as inline text or from a configuration bundle.

### Contents
<a name="API_SystemPromptConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBundle **   <a name="BedrockAgentCore-Type-SystemPromptConfig-configurationBundle"></a>
The system prompt sourced from a configuration bundle version.  
Type: [SystemPromptConfigurationBundle](#API_SystemPromptConfigurationBundle) object  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-SystemPromptConfig-text"></a>
The system prompt text provided inline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Required: No

### See Also
<a name="API_SystemPromptConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SystemPromptConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SystemPromptConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SystemPromptConfig) 

## SystemPromptConfigurationBundle
<a name="API_SystemPromptConfigurationBundle"></a>

A system prompt sourced from a configuration bundle version.

### Contents
<a name="API_SystemPromptConfigurationBundle_Contents"></a>

 ** bundleArn **   <a name="BedrockAgentCore-Type-SystemPromptConfigurationBundle-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** systemPromptJsonPath **   <a name="BedrockAgentCore-Type-SystemPromptConfigurationBundle-systemPromptJsonPath"></a>
The JSON path within the configuration bundle that contains the system prompt.  
Type: String  
Required: Yes

 ** versionId **   <a name="BedrockAgentCore-Type-SystemPromptConfigurationBundle-versionId"></a>
The version identifier of the configuration bundle.  
Type: String  
Required: Yes

### See Also
<a name="API_SystemPromptConfigurationBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SystemPromptConfigurationBundle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SystemPromptConfigurationBundle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SystemPromptConfigurationBundle) 

## SystemPromptRecommendationConfig
<a name="API_SystemPromptRecommendationConfig"></a>

Configuration for generating system prompt optimization recommendations.

### Contents
<a name="API_SystemPromptRecommendationConfig_Contents"></a>

 ** agentTraces **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationConfig-agentTraces"></a>
The agent traces to analyze for generating recommendations.  
Type: [AgentTracesConfig](#API_AgentTracesConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** systemPrompt **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationConfig-systemPrompt"></a>
The current system prompt to optimize.  
Type: [SystemPromptConfig](#API_SystemPromptConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** evaluationConfig **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationConfig-evaluationConfig"></a>
The evaluation configuration specifying which evaluator to use for assessing recommendation quality.  
Type: [RecommendationEvaluationConfig](#API_RecommendationEvaluationConfig) object  
Required: No

### See Also
<a name="API_SystemPromptRecommendationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SystemPromptRecommendationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SystemPromptRecommendationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SystemPromptRecommendationConfig) 

## SystemPromptRecommendationResult
<a name="API_SystemPromptRecommendationResult"></a>

The result of a system prompt recommendation, containing the optimized prompt.

### Contents
<a name="API_SystemPromptRecommendationResult_Contents"></a>

 ** configurationBundle **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationResult-configurationBundle"></a>
The configuration bundle containing the recommended system prompt, if the input was sourced from a configuration bundle.  
Type: [RecommendationResultConfigurationBundle](#API_RecommendationResultConfigurationBundle) object  
Required: No

 ** errorCode **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationResult-errorCode"></a>
The error code if the recommendation failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationResult-errorMessage"></a>
The error message if the recommendation failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** explanation **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationResult-explanation"></a>
An explanation of why the recommendation was generated and what patterns were identified in the agent traces.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Required: No

 ** recommendedSystemPrompt **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationResult-recommendedSystemPrompt"></a>
The optimized system prompt text generated by the recommendation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Required: No

### See Also
<a name="API_SystemPromptRecommendationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SystemPromptRecommendationResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SystemPromptRecommendationResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SystemPromptRecommendationResult) 

## TargetRef
<a name="API_TargetRef"></a>

A reference to a gateway target.

### Contents
<a name="API_TargetRef_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-TargetRef-name"></a>
The name of the gateway target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

### See Also
<a name="API_TargetRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/TargetRef) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/TargetRef) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/TargetRef) 

## TokenBalance
<a name="API_TokenBalance"></a>

A single token balance entry.

### Contents
<a name="API_TokenBalance_Contents"></a>

 ** amount **   <a name="BedrockAgentCore-Type-TokenBalance-amount"></a>
Raw balance in the smallest denomination (e.g., USDC base units where 1 USDC = 1000000).  
Type: String  
Required: Yes

 ** chain **   <a name="BedrockAgentCore-Type-TokenBalance-chain"></a>
The specific blockchain chain.  
Type: String  
Valid Values: `BASE | BASE_SEPOLIA | ETHEREUM | SOLANA | SOLANA_DEVNET`   
Required: Yes

 ** decimals **   <a name="BedrockAgentCore-Type-TokenBalance-decimals"></a>
Number of decimal places for the token (e.g., 6 for USDC).  
Type: Integer  
Required: Yes

 ** network **   <a name="BedrockAgentCore-Type-TokenBalance-network"></a>
The blockchain network family (ETHEREUM or SOLANA).  
Type: String  
Valid Values: `ETHEREUM | SOLANA`   
Required: Yes

 ** token **   <a name="BedrockAgentCore-Type-TokenBalance-token"></a>
The supported token for this balance.  
Type: String  
Valid Values: `USDC`   
Required: Yes

### See Also
<a name="API_TokenBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/TokenBalance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/TokenBalance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/TokenBalance) 

## TokenUsage
<a name="API_TokenUsage"></a>

 The token consumption statistics for language model operations during evaluation. Provides detailed breakdown of input, output, and total tokens used for cost tracking and performance monitoring. 

### Contents
<a name="API_TokenUsage_Contents"></a>

 ** inputTokens **   <a name="BedrockAgentCore-Type-TokenUsage-inputTokens"></a>
 The number of tokens consumed for input processing during the evaluation. Includes tokens from the evaluation prompt, agent traces, and any additional context provided to the evaluator model.   
Type: Integer  
Required: No

 ** outputTokens **   <a name="BedrockAgentCore-Type-TokenUsage-outputTokens"></a>
 The number of tokens generated by the evaluator model in its response. Includes tokens for the score, explanation, and any additional output produced during the evaluation process.   
Type: Integer  
Required: No

 ** totalTokens **   <a name="BedrockAgentCore-Type-TokenUsage-totalTokens"></a>
 The total number of tokens consumed during the evaluation, calculated as the sum of input and output tokens. Used for cost calculation and rate limiting within the service limits.   
Type: Integer  
Required: No

### See Also
<a name="API_TokenUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/TokenUsage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/TokenUsage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/TokenUsage) 

## ToolArguments
<a name="API_ToolArguments"></a>

The collection of arguments that specify the operation to perform and its parameters when invoking a tool in Amazon Bedrock AgentCore. Different tools require different arguments, and this structure provides a flexible way to pass the appropriate arguments to each tool type.

### Contents
<a name="API_ToolArguments_Contents"></a>

 ** clearContext **   <a name="BedrockAgentCore-Type-ToolArguments-clearContext"></a>
Whether to clear the context for the tool.  
Type: Boolean  
Required: No

 ** code **   <a name="BedrockAgentCore-Type-ToolArguments-code"></a>
The code to execute in a code interpreter session. This is the source code in the specified programming language that will be executed by the code interpreter.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** command **   <a name="BedrockAgentCore-Type-ToolArguments-command"></a>
The command to execute with the tool.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** content **   <a name="BedrockAgentCore-Type-ToolArguments-content"></a>
The content for the tool operation.  
Type: Array of [InputContentBlock](#API_InputContentBlock) objects  
Required: No

 ** directoryPath **   <a name="BedrockAgentCore-Type-ToolArguments-directoryPath"></a>
The directory path for the tool operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** language **   <a name="BedrockAgentCore-Type-ToolArguments-language"></a>
The programming language of the code to execute. This tells the code interpreter which language runtime to use for execution.  
Type: String  
Valid Values: `python | javascript | typescript`   
Required: No

 ** path **   <a name="BedrockAgentCore-Type-ToolArguments-path"></a>
The path for the tool operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** paths **   <a name="BedrockAgentCore-Type-ToolArguments-paths"></a>
The paths for the tool operation.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** runtime **   <a name="BedrockAgentCore-Type-ToolArguments-runtime"></a>
The runtime environment to use for code execution. If not specified, defaults to `deno` for JavaScript and TypeScript.  
Type: String  
Valid Values: `nodejs | deno | python`   
Required: No

 ** taskId **   <a name="BedrockAgentCore-Type-ToolArguments-taskId"></a>
The identifier of the task for the tool operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

### See Also
<a name="API_ToolArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolArguments) 

## ToolDescriptionConfig
<a name="API_ToolDescriptionConfig"></a>

The tool description content.

### Contents
<a name="API_ToolDescriptionConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="BedrockAgentCore-Type-ToolDescriptionConfig-text"></a>
The tool description as inline text.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Required: No

### See Also
<a name="API_ToolDescriptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionConfig) 

## ToolDescriptionConfigurationBundle
<a name="API_ToolDescriptionConfigurationBundle"></a>

Tool descriptions sourced from a configuration bundle version.

### Contents
<a name="API_ToolDescriptionConfigurationBundle_Contents"></a>

 ** bundleArn **   <a name="BedrockAgentCore-Type-ToolDescriptionConfigurationBundle-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** tools **   <a name="BedrockAgentCore-Type-ToolDescriptionConfigurationBundle-tools"></a>
The list of tool entries mapping tool names to their JSON paths within the bundle.  
Type: Array of [ConfigurationBundleToolEntry](#API_ConfigurationBundleToolEntry) objects  
Required: Yes

 ** versionId **   <a name="BedrockAgentCore-Type-ToolDescriptionConfigurationBundle-versionId"></a>
The version identifier of the configuration bundle.  
Type: String  
Required: Yes

### See Also
<a name="API_ToolDescriptionConfigurationBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionConfigurationBundle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionConfigurationBundle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionConfigurationBundle) 

## ToolDescriptionInput
<a name="API_ToolDescriptionInput"></a>

A tool description input containing the tool name and its current description.

### Contents
<a name="API_ToolDescriptionInput_Contents"></a>

 ** toolDescription **   <a name="BedrockAgentCore-Type-ToolDescriptionInput-toolDescription"></a>
The current description of the tool to optimize.  
Type: [ToolDescriptionConfig](#API_ToolDescriptionConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** toolName **   <a name="BedrockAgentCore-Type-ToolDescriptionInput-toolName"></a>
The name of the tool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_\-\.]+`   
Required: Yes

### See Also
<a name="API_ToolDescriptionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionInput) 

## ToolDescriptionOutput
<a name="API_ToolDescriptionOutput"></a>

The output for a single tool description recommendation.

### Contents
<a name="API_ToolDescriptionOutput_Contents"></a>

 ** toolName **   <a name="BedrockAgentCore-Type-ToolDescriptionOutput-toolName"></a>
The name of the tool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_\-\.]+`   
Required: Yes

 ** explanation **   <a name="BedrockAgentCore-Type-ToolDescriptionOutput-explanation"></a>
An explanation of why the recommendation was generated for this tool and what patterns were identified in the agent traces.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Required: No

 ** recommendedToolDescription **   <a name="BedrockAgentCore-Type-ToolDescriptionOutput-recommendedToolDescription"></a>
The optimized tool description text generated by the recommendation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Required: No

### See Also
<a name="API_ToolDescriptionOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionOutput) 

## ToolDescriptionRecommendationConfig
<a name="API_ToolDescriptionRecommendationConfig"></a>

Configuration for generating tool description optimization recommendations.

### Contents
<a name="API_ToolDescriptionRecommendationConfig_Contents"></a>

 ** agentTraces **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationConfig-agentTraces"></a>
The agent traces to analyze for generating tool description recommendations.  
Type: [AgentTracesConfig](#API_AgentTracesConfig) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** toolDescription **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationConfig-toolDescription"></a>
The current tool descriptions to optimize.  
Type: [ToolDescriptionSource](#API_ToolDescriptionSource) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_ToolDescriptionRecommendationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationConfig) 

## ToolDescriptionRecommendationResult
<a name="API_ToolDescriptionRecommendationResult"></a>

The result of a tool description recommendation, containing optimized descriptions.

### Contents
<a name="API_ToolDescriptionRecommendationResult_Contents"></a>

 ** configurationBundle **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-configurationBundle"></a>
The configuration bundle containing the recommended tool descriptions, if the input was sourced from a configuration bundle.  
Type: [RecommendationResultConfigurationBundle](#API_RecommendationResultConfigurationBundle) object  
Required: No

 ** errorCode **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-errorCode"></a>
The error code if the recommendation failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-errorMessage"></a>
The error message if the recommendation failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** tools **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-tools"></a>
The list of tools with their recommended descriptions.  
Type: Array of [ToolDescriptionOutput](#API_ToolDescriptionOutput) objects  
Required: No

### See Also
<a name="API_ToolDescriptionRecommendationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationResult) 

## ToolDescriptionSource
<a name="API_ToolDescriptionSource"></a>

The source of tool descriptions, either inline text or from a configuration bundle.

### Contents
<a name="API_ToolDescriptionSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBundle **   <a name="BedrockAgentCore-Type-ToolDescriptionSource-configurationBundle"></a>
Tool descriptions sourced from a configuration bundle version.  
Type: [ToolDescriptionConfigurationBundle](#API_ToolDescriptionConfigurationBundle) object  
Required: No

 ** toolDescriptionText **   <a name="BedrockAgentCore-Type-ToolDescriptionSource-toolDescriptionText"></a>
Tool descriptions provided as inline text.  
Type: [ToolDescriptionTextInput](#API_ToolDescriptionTextInput) object  
Required: No

### See Also
<a name="API_ToolDescriptionSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionSource) 

## ToolDescriptionTextInput
<a name="API_ToolDescriptionTextInput"></a>

Inline tool description input containing a list of tools.

### Contents
<a name="API_ToolDescriptionTextInput_Contents"></a>

 ** tools **   <a name="BedrockAgentCore-Type-ToolDescriptionTextInput-tools"></a>
The list of tool descriptions to optimize.  
Type: Array of [ToolDescriptionInput](#API_ToolDescriptionInput) objects  
Required: Yes

### See Also
<a name="API_ToolDescriptionTextInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionTextInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionTextInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionTextInput) 

## ToolResultStructuredContent
<a name="API_ToolResultStructuredContent"></a>

Contains structured content from a tool result.

### Contents
<a name="API_ToolResultStructuredContent_Contents"></a>

 ** executionTime **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-executionTime"></a>
The execution time of the tool operation in milliseconds.  
Type: Double  
Required: No

 ** exitCode **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-exitCode"></a>
The exit code from the tool execution.  
Type: Integer  
Required: No

 ** stderr **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-stderr"></a>
The standard error output from the tool execution.  
Type: String  
Required: No

 ** stdout **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-stdout"></a>
The standard output from the tool execution.  
Type: String  
Required: No

 ** taskId **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-taskId"></a>
The identifier of the task that produced the result.  
Type: String  
Required: No

 ** taskStatus **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-taskStatus"></a>
The status of the task that produced the result.  
Type: String  
Valid Values: `submitted | working | completed | canceled | failed`   
Required: No

### See Also
<a name="API_ToolResultStructuredContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolResultStructuredContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolResultStructuredContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolResultStructuredContent) 

## ToolsDefinition
<a name="API_ToolsDefinition"></a>

 The MCP tools definition with a protocol version and inline content. The `protocolVersion` identifies the MCP protocol version that the tools conform to. This differs from `schemaVersion` in the server definition, which identifies the server configuration schema format.

### Contents
<a name="API_ToolsDefinition_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-ToolsDefinition-inlineContent"></a>
 The inline content of the tools definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

 ** protocolVersion **   <a name="BedrockAgentCore-Type-ToolsDefinition-protocolVersion"></a>
 The MCP protocol version that the tools conform to. This differs from the `schemaVersion` field in the server definition, which identifies the server configuration schema format.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_ToolsDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolsDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolsDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolsDefinition) 

## ToolsFileSystemConfiguration
<a name="API_ToolsFileSystemConfiguration"></a>

Specifies a file system to mount into the session by providing exactly one of the following:
+  `s3FilesConfiguration` - Mounts an Amazon Simple Storage Service (Amazon S3) Files access point.
+  `efsConfiguration` - Mounts an Amazon Elastic File System (Amazon EFS) access point.

### Contents
<a name="API_ToolsFileSystemConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** efsConfiguration **   <a name="BedrockAgentCore-Type-ToolsFileSystemConfiguration-efsConfiguration"></a>
The configuration for mounting your own Amazon Elastic File System (Amazon EFS) access point into the session.  
Type: [EfsConfiguration](#API_EfsConfiguration) object  
Required: No

 ** s3FilesConfiguration **   <a name="BedrockAgentCore-Type-ToolsFileSystemConfiguration-s3FilesConfiguration"></a>
The configuration for mounting your own Amazon Simple Storage Service (Amazon S3) Files access point into the session.  
Type: [S3FilesConfiguration](#API_S3FilesConfiguration) object  
Required: No

### See Also
<a name="API_ToolsFileSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolsFileSystemConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolsFileSystemConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolsFileSystemConfiguration) 

## UserIdentifier
<a name="API_UserIdentifier"></a>

The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.

### Contents
<a name="API_UserIdentifier_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** userId **   <a name="BedrockAgentCore-Type-UserIdentifier-userId"></a>
The ID of the user for whom you have retrieved a workload access token for  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** userToken **   <a name="BedrockAgentCore-Type-UserIdentifier-userToken"></a>
The OAuth2.0 token issued by the user’s identity provider that was used to generate the workload access token  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`   
Required: No

### See Also
<a name="API_UserIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UserIdentifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UserIdentifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UserIdentifier) 

## UserIntentAffectedSession
<a name="API_UserIntentAffectedSession"></a>

A session associated with a user intent cluster.

### Contents
<a name="API_UserIntentAffectedSession_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-UserIntentAffectedSession-sessionId"></a>
The unique identifier of the session.  
Type: String  
Required: Yes

 ** userMessages **   <a name="BedrockAgentCore-Type-UserIntentAffectedSession-userMessages"></a>
The user messages from this session that contributed to the intent cluster.  
Type: Array of strings  
Required: Yes

### See Also
<a name="API_UserIntentAffectedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UserIntentAffectedSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UserIntentAffectedSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UserIntentAffectedSession) 

## UserIntentCluster
<a name="API_UserIntentCluster"></a>

A cluster of similar user intents identified across sessions.

### Contents
<a name="API_UserIntentCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-UserIntentCluster-affectedSessionCount"></a>
The number of sessions with this user intent.  
Type: Integer  
Required: Yes

 ** affectedSessions **   <a name="BedrockAgentCore-Type-UserIntentCluster-affectedSessions"></a>
The list of sessions with this user intent.  
Type: Array of [UserIntentAffectedSession](#API_UserIntentAffectedSession) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-UserIntentCluster-clusterId"></a>
The unique identifier of the user intent cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-UserIntentCluster-description"></a>
A description of the user intent pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-UserIntentCluster-name"></a>
The name of the user intent cluster.  
Type: String  
Required: Yes

### See Also
<a name="API_UserIntentCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UserIntentCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UserIntentCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UserIntentCluster) 

## UserIntentClusteringResultContent
<a name="API_UserIntentClusteringResultContent"></a>

The user intent clustering result containing grouped user intents identified across evaluated sessions.

### Contents
<a name="API_UserIntentClusteringResultContent_Contents"></a>

 ** userIntents **   <a name="BedrockAgentCore-Type-UserIntentClusteringResultContent-userIntents"></a>
The list of user intent clusters identified across analyzed sessions.  
Type: Array of [UserIntentCluster](#API_UserIntentCluster) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

### See Also
<a name="API_UserIntentClusteringResultContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UserIntentClusteringResultContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UserIntentClusteringResultContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UserIntentClusteringResultContent) 

## ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Stores information about a field passed inside a request that resulted in an exception.

### Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** message **   <a name="BedrockAgentCore-Type-ValidationExceptionField-message"></a>
A message describing why this field failed validation.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-ValidationExceptionField-name"></a>
The name of the field.  
Type: String  
Required: Yes

### See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ValidationExceptionField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ValidationExceptionField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ValidationExceptionField) 

## Variant
<a name="API_Variant"></a>

A variant in an A/B test, representing either the control (C) or treatment (T1) configuration.

### Contents
<a name="API_Variant_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-Variant-name"></a>
The name of the variant. Must be `C` for control or `T1` for treatment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2.  
Pattern: `(C|T1)`   
Required: Yes

 ** variantConfiguration **   <a name="BedrockAgentCore-Type-Variant-variantConfiguration"></a>
The configuration for this variant, including the configuration bundle or target reference.  
Type: [VariantConfiguration](#API_VariantConfiguration) object  
Required: Yes

 ** weight **   <a name="BedrockAgentCore-Type-Variant-weight"></a>
The percentage of traffic to route to this variant. Weights across all variants must sum to 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: Yes

### See Also
<a name="API_Variant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Variant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Variant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Variant) 

## VariantConfiguration
<a name="API_VariantConfiguration"></a>

The configuration for an A/B test variant.

### Contents
<a name="API_VariantConfiguration_Contents"></a>

 ** configurationBundle **   <a name="BedrockAgentCore-Type-VariantConfiguration-configurationBundle"></a>
A reference to a configuration bundle version to use for this variant.  
Type: [ConfigurationBundleRef](#API_ConfigurationBundleRef) object  
Required: No

 ** target **   <a name="BedrockAgentCore-Type-VariantConfiguration-target"></a>
A reference to a gateway target to route traffic to for this variant.  
Type: [TargetRef](#API_TargetRef) object  
Required: No

### See Also
<a name="API_VariantConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/VariantConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/VariantConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/VariantConfiguration) 

## VariantResult
<a name="API_VariantResult"></a>

Statistical results for a treatment variant compared against the control.

### Contents
<a name="API_VariantResult_Contents"></a>

 ** isSignificant **   <a name="BedrockAgentCore-Type-VariantResult-isSignificant"></a>
Whether the observed difference is statistically significant.  
Type: Boolean  
Required: Yes

 ** mean **   <a name="BedrockAgentCore-Type-VariantResult-mean"></a>
The mean evaluation score for this variant.  
Type: Double  
Required: Yes

 ** sampleSize **   <a name="BedrockAgentCore-Type-VariantResult-sampleSize"></a>
The number of sessions evaluated for this variant.  
Type: Integer  
Required: Yes

 ** variantName **   <a name="BedrockAgentCore-Type-VariantResult-variantName"></a>
The name of the treatment variant.  
Type: String  
Required: Yes

 ** absoluteChange **   <a name="BedrockAgentCore-Type-VariantResult-absoluteChange"></a>
The absolute change in mean score compared to the control variant.  
Type: Double  
Required: No

 ** confidenceInterval **   <a name="BedrockAgentCore-Type-VariantResult-confidenceInterval"></a>
The confidence interval for the observed difference.  
Type: [ConfidenceInterval](#API_ConfidenceInterval) object  
Required: No

 ** percentChange **   <a name="BedrockAgentCore-Type-VariantResult-percentChange"></a>
The percentage change in mean score compared to the control variant.  
Type: Double  
Required: No

 ** pValue **   <a name="BedrockAgentCore-Type-VariantResult-pValue"></a>
The p-value indicating the statistical significance of the observed difference.  
Type: Double  
Required: No

### See Also
<a name="API_VariantResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/VariantResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/VariantResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/VariantResult) 

## ViewPort
<a name="API_ViewPort"></a>

The configuration that defines the dimensions of a browser viewport in a browser session. The viewport determines the visible area of web content and affects how web pages are rendered and displayed. Proper viewport configuration ensures that web content is displayed correctly for the agent's browsing tasks.

### Contents
<a name="API_ViewPort_Contents"></a>

 ** height **   <a name="BedrockAgentCore-Type-ViewPort-height"></a>
The height of the viewport in pixels. This value determines the vertical dimension of the visible area. Valid values range from 600 to 1080 pixels.  
Type: Integer  
Valid Range: Minimum value of 240. Maximum value of 2160.  
Required: Yes

 ** width **   <a name="BedrockAgentCore-Type-ViewPort-width"></a>
The width of the viewport in pixels. This value determines the horizontal dimension of the visible area. Valid values range from 800 to 1920 pixels.  
Type: Integer  
Valid Range: Minimum value of 320. Maximum value of 3840.  
Required: Yes

### See Also
<a name="API_ViewPort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ViewPort) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ViewPort) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ViewPort) 

# Common Parameters
<a name="CommonParameters"></a>

The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string. Any action-specific parameters are listed in the topic for that action. For more information about Signature Version 4, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

 **X-Amz-Algorithm**   <a name="CommonParameters-X-Amz-Algorithm"></a>
The hash algorithm that you used to create the request signature.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Valid Values: `AWS4-HMAC-SHA256`   
Required: Conditional

 **X-Amz-Credential**   <a name="CommonParameters-X-Amz-Credential"></a>
The credential scope value, which is a string that includes your access key, the date, the region you are targeting, the service you are requesting, and a termination string ("aws4\_request"). The value is expressed in the following format: *access\_key*/*YYYYMMDD*/*region*/*service*/aws4\_request.  
For more information, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the *IAM User Guide*.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

 **X-Amz-Date**   <a name="CommonParameters-X-Amz-Date"></a>
The date that is used to create the signature. The format must be ISO 8601 basic format (YYYYMMDD'T'HHMMSS'Z'). For example, the following date time is a valid X-Amz-Date value: `20120325T120000Z`.  
Condition: X-Amz-Date is optional for all requests; it can be used to override the date used for signing requests. If the Date header is specified in the ISO 8601 basic format, X-Amz-Date is not required. When X-Amz-Date is used, it always overrides the value of the Date header. For more information, see [Elements of an AWS API request signature](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-signing-elements.html) in the *IAM User Guide*.  
Type: string  
Required: Conditional

 **X-Amz-Security-Token**   <a name="CommonParameters-X-Amz-Security-Token"></a>
The temporary security token that was obtained through a call to AWS Security Token Service (AWS STS). For a list of services that support temporary security credentials from AWS STS, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.  
Condition: If you're using temporary security credentials from AWS STS, you must include the security token.  
Type: string  
Required: Conditional

 **X-Amz-Signature**   <a name="CommonParameters-X-Amz-Signature"></a>
Specifies the hex-encoded signature that was calculated from the string to sign and the derived signing key.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

 **X-Amz-SignedHeaders**   <a name="CommonParameters-X-Amz-SignedHeaders"></a>
Specifies all the HTTP headers that were included as part of the canonical request. For more information about specifying signed headers, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the *IAM User Guide*.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

# Common Error Types
<a name="CommonErrors"></a>

This section lists common error types that this AWS service may return. Not all services return all error types listed here. For errors specific to an API action for this service, see the topic for that API action.

 **AccessDeniedException**   <a name="CommonErrors-AccessDeniedException"></a>
You don't have permission to perform this action. Verify that your IAM policy includes the required permissions.  
HTTP Status Code: 403

 **ExpiredTokenException**   <a name="CommonErrors-ExpiredTokenException"></a>
The security token included in the request has expired. Request a new security token and try again.  
HTTP Status Code: 403

 **IncompleteSignature**   <a name="CommonErrors-IncompleteSignature"></a>
The request signature doesn't conform to AWS standards. Verify that you're using valid AWS credentials and that your request is properly formatted. If you're using an SDK, ensure it's up to date.  
HTTP Status Code: 403

 **InternalFailure**   <a name="CommonErrors-InternalFailure"></a>
The request can't be processed right now because of an internal server issue. Try again later. If the problem persists, contact AWS Support.  
HTTP Status Code: 500

 **MalformedHttpRequestException**   <a name="CommonErrors-MalformedHttpRequestException"></a>
The request body can't be processed. This typically happens when the request body can't be decompressed using the specified content encoding algorithm. Verify that the content encoding header matches the compression format used.  
HTTP Status Code: 400

 **NotAuthorized**   <a name="CommonErrors-NotAuthorized"></a>
You don't have permissions to perform this action. Verify that your IAM policy includes the required permissions.  
HTTP Status Code: 401

 **OptInRequired**   <a name="CommonErrors-OptInRequired"></a>
Your AWS account needs a subscription for this service. Verify that you've enabled the service in your account.  
HTTP Status Code: 403

 **RequestAbortedException**   <a name="CommonErrors-RequestAbortedException"></a>
The request was aborted before a response could be returned. This typically happens when the client closes the connection.  
HTTP Status Code: 400

 **RequestEntityTooLargeException**   <a name="CommonErrors-RequestEntityTooLargeException"></a>
The request entity is too large. Reduce the size of the request body and try again.  
HTTP Status Code: 413

 **RequestTimeoutException**   <a name="CommonErrors-RequestTimeoutException"></a>
The request timed out. The server didn't receive the complete request within the expected time frame. Try again.  
HTTP Status Code: 408

 **ServiceUnavailable**   <a name="CommonErrors-ServiceUnavailable"></a>
The service is temporarily unavailable. Try again later.  
HTTP Status Code: 503

 **ThrottlingException**   <a name="CommonErrors-ThrottlingException"></a>
Your request rate is too high. The AWS SDKs automatically retry requests that receive this exception. Reduce the frequency of requests.  
HTTP Status Code: 400

 **UnknownOperationException**   <a name="CommonErrors-UnknownOperationException"></a>
The action or operation isn't recognized. Verify that the action name is spelled correctly and that it's supported by the API version you're using.  
HTTP Status Code: 404

 **UnrecognizedClientException**   <a name="CommonErrors-UnrecognizedClientException"></a>
The X.509 certificate or AWS access key ID you provided doesn't exist in our records. Verify that you're using valid credentials and that they haven't expired.  
HTTP Status Code: 403

 **ValidationError**   <a name="CommonErrors-ValidationError"></a>
The input doesn't meet the required format or constraints. Check that all required parameters are included and that values are valid.  
HTTP Status Code: 400