---
title: BedrockAgentCore[¶](#bedrockagentcore "Link to this heading")
description: Welcome to the Amazon Bedrock AgentCore Data Plane API reference. Data Plane actions process and handle data or workloads within Amazon Web Services services.
product: Amazon Bedrock AgentCore
section: References / boto3.amazonaws.com
source_url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore.html
fetched: '2026-09-26'
tags:
- agentcore
- boto3-amazonaws-com
- core
- reference
referenced_by:
- aws-sdk-memory.md
- memory-get-started.md
conversion: pandoc
---

# BedrockAgentCore[¶](#bedrockagentcore "Link to this heading")

## Client[¶](#client "Link to this heading")

*class* BedrockAgentCore.Client[¶](#BedrockAgentCore.Client "Link to this definition")  
A low-level client representing Amazon Bedrock AgentCore

Welcome to the Amazon Bedrock AgentCore Data Plane API reference. Data Plane actions process and handle data or workloads within Amazon Web Services services.

    import boto3

    client = boto3.client('bedrock-agentcore')

These are the available methods:

- [batch_create_memory_records](bedrock-agentcore/client/batch_create_memory_records.html)
- [batch_delete_memory_records](bedrock-agentcore/client/batch_delete_memory_records.html)
- [batch_update_memory_records](bedrock-agentcore/client/batch_update_memory_records.html)
- [can_paginate](bedrock-agentcore/client/can_paginate.html)
- [close](bedrock-agentcore/client/close.html)
- [complete_resource_token_auth](bedrock-agentcore/client/complete_resource_token_auth.html)
- [create_ab_test](bedrock-agentcore/client/create_ab_test.html)
- [create_event](bedrock-agentcore/client/create_event.html)
- [create_payment_instrument](bedrock-agentcore/client/create_payment_instrument.html)
- [create_payment_session](bedrock-agentcore/client/create_payment_session.html)
- [delete_ab_test](bedrock-agentcore/client/delete_ab_test.html)
- [delete_batch_evaluation](bedrock-agentcore/client/delete_batch_evaluation.html)
- [delete_capacity_provider_session](bedrock-agentcore/client/delete_capacity_provider_session.html)
- [delete_event](bedrock-agentcore/client/delete_event.html)
- [delete_memory_record](bedrock-agentcore/client/delete_memory_record.html)
- [delete_payment_instrument](bedrock-agentcore/client/delete_payment_instrument.html)
- [delete_payment_session](bedrock-agentcore/client/delete_payment_session.html)
- [delete_recommendation](bedrock-agentcore/client/delete_recommendation.html)
- [evaluate](bedrock-agentcore/client/evaluate.html)
- [get_ab_test](bedrock-agentcore/client/get_ab_test.html)
- [get_agent_card](bedrock-agentcore/client/get_agent_card.html)
- [get_batch_evaluation](bedrock-agentcore/client/get_batch_evaluation.html)
- [get_browser_session](bedrock-agentcore/client/get_browser_session.html)
- [get_code_interpreter_session](bedrock-agentcore/client/get_code_interpreter_session.html)
- [get_event](bedrock-agentcore/client/get_event.html)
- [get_memory_record](bedrock-agentcore/client/get_memory_record.html)
- [get_paginator](bedrock-agentcore/client/get_paginator.html)
- [get_payment_instrument](bedrock-agentcore/client/get_payment_instrument.html)
- [get_payment_instrument_balance](bedrock-agentcore/client/get_payment_instrument_balance.html)
- [get_payment_session](bedrock-agentcore/client/get_payment_session.html)
- [get_recommendation](bedrock-agentcore/client/get_recommendation.html)
- [get_resource_api_key](bedrock-agentcore/client/get_resource_api_key.html)
- [get_resource_oauth2_token](bedrock-agentcore/client/get_resource_oauth2_token.html)
- [get_resource_payment_token](bedrock-agentcore/client/get_resource_payment_token.html)
- [get_waiter](bedrock-agentcore/client/get_waiter.html)
- [get_workload_access_token](bedrock-agentcore/client/get_workload_access_token.html)
- [get_workload_access_token_for_jwt](bedrock-agentcore/client/get_workload_access_token_for_jwt.html)
- [get_workload_access_token_for_user_id](bedrock-agentcore/client/get_workload_access_token_for_user_id.html)
- [ingest_data](bedrock-agentcore/client/ingest_data.html)
- [invoke_agent_runtime](bedrock-agentcore/client/invoke_agent_runtime.html)
- [invoke_agent_runtime_command](bedrock-agentcore/client/invoke_agent_runtime_command.html)
- [invoke_browser](bedrock-agentcore/client/invoke_browser.html)
- [invoke_code_interpreter](bedrock-agentcore/client/invoke_code_interpreter.html)
- [invoke_harness](bedrock-agentcore/client/invoke_harness.html)
- [list_ab_tests](bedrock-agentcore/client/list_ab_tests.html)
- [list_actors](bedrock-agentcore/client/list_actors.html)
- [list_batch_evaluations](bedrock-agentcore/client/list_batch_evaluations.html)
- [list_browser_sessions](bedrock-agentcore/client/list_browser_sessions.html)
- [list_code_interpreter_sessions](bedrock-agentcore/client/list_code_interpreter_sessions.html)
- [list_events](bedrock-agentcore/client/list_events.html)
- [list_memory_extraction_jobs](bedrock-agentcore/client/list_memory_extraction_jobs.html)
- [list_memory_records](bedrock-agentcore/client/list_memory_records.html)
- [list_payment_instruments](bedrock-agentcore/client/list_payment_instruments.html)
- [list_payment_sessions](bedrock-agentcore/client/list_payment_sessions.html)
- [list_recommendations](bedrock-agentcore/client/list_recommendations.html)
- [list_sessions](bedrock-agentcore/client/list_sessions.html)
- [process_payment](bedrock-agentcore/client/process_payment.html)
- [retrieve_memory_records](bedrock-agentcore/client/retrieve_memory_records.html)
- [save_browser_session_profile](bedrock-agentcore/client/save_browser_session_profile.html)
- [search_registry_records](bedrock-agentcore/client/search_registry_records.html)
- [start_batch_evaluation](bedrock-agentcore/client/start_batch_evaluation.html)
- [start_browser_session](bedrock-agentcore/client/start_browser_session.html)
- [start_code_interpreter_session](bedrock-agentcore/client/start_code_interpreter_session.html)
- [start_memory_extraction_job](bedrock-agentcore/client/start_memory_extraction_job.html)
- [start_recommendation](bedrock-agentcore/client/start_recommendation.html)
- [stop_batch_evaluation](bedrock-agentcore/client/stop_batch_evaluation.html)
- [stop_browser_session](bedrock-agentcore/client/stop_browser_session.html)
- [stop_code_interpreter_session](bedrock-agentcore/client/stop_code_interpreter_session.html)
- [stop_runtime_session](bedrock-agentcore/client/stop_runtime_session.html)
- [update_ab_test](bedrock-agentcore/client/update_ab_test.html)
- [update_browser_stream](bedrock-agentcore/client/update_browser_stream.html)

## Paginators[¶](#paginators "Link to this heading")

Paginators are available on a client instance via the `get_paginator` method. For more detailed instructions and examples on the usage of paginators, see the paginators [user guide](https://docs.aws.amazon.com/boto3/latest/guide/paginators.html).

The available paginators are:

- [ListABTests](bedrock-agentcore/paginator/ListABTests.html)
- [ListActors](bedrock-agentcore/paginator/ListActors.html)
- [ListBatchEvaluations](bedrock-agentcore/paginator/ListBatchEvaluations.html)
- [ListEvents](bedrock-agentcore/paginator/ListEvents.html)
- [ListMemoryExtractionJobs](bedrock-agentcore/paginator/ListMemoryExtractionJobs.html)
- [ListMemoryRecords](bedrock-agentcore/paginator/ListMemoryRecords.html)
- [ListPaymentInstruments](bedrock-agentcore/paginator/ListPaymentInstruments.html)
- [ListPaymentSessions](bedrock-agentcore/paginator/ListPaymentSessions.html)
- [ListRecommendations](bedrock-agentcore/paginator/ListRecommendations.html)
- [ListSessions](bedrock-agentcore/paginator/ListSessions.html)
- [RetrieveMemoryRecords](bedrock-agentcore/paginator/RetrieveMemoryRecords.html)
