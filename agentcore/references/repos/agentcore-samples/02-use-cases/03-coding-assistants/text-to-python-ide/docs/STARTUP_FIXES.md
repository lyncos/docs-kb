---
title: ✅ Startup Script Fixes Applied
description: 'The application is now ready to start with:'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/03-coding-assistants/text-to-python-ide/docs/STARTUP_FIXES.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# ✅ Startup Script Fixes Applied

## 🔧 **Issues Fixed**

### 1. **AWS Credentials Check**
- **Problem**: `start.sh` required AWS Access Key + Secret Key even when profile was set
- **Solution**: Updated `diagnose_backend.py` to make AWS keys optional when `AWS_PROFILE` is configured
- **Result**: Now supports both authentication methods:
  - ✅ **AWS Profile** (recommended): `AWS_PROFILE=default`
  - ✅ **Access Keys** (fallback): `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY`

### 2. **Package Check**
- **Problem**: Looking for `strands` instead of `strands-agents`
- **Solution**: Confirmed that `strands-agents` package correctly imports as `strands`
- **Result**: Dependencies check is working correctly

### 3. **Diagnostic Handling**
- **Problem**: Script failed on port conflicts (normal during startup)
- **Solution**: Updated `start.sh` to handle expected warnings gracefully
- **Result**: Only fails on real issues, not expected port conflicts

## ✅ **Current Status**

### **Environment Variables (.env)**
```bash
# AWS Configuration
AWS_REGION=us-east-1
AWS_PROFILE=default  # ✅ Profile-based auth (recommended)

# Backend Configuration  
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Frontend Configuration
REACT_APP_API_URL=http://localhost:8000
```

### **Authentication Priority**
1. **AWS Profile** (`AWS_PROFILE`) - ✅ **PREFERRED**
2. **Access Keys** (`AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY`) - ✅ Fallback

### **Diagnostic Results**
```bash
✅ Virtual environment activated
✅ All dependencies available (strands-agents ✓)
✅ AWS profile authentication working
✅ Strands-Agents framework working
✅ AgentCore permissions working
✅ Backend initialization successful
⚠️  Port conflicts (expected during startup)
```

## 🚀 **Ready to Start**

The application is now ready to start with:

```bash
./start.sh
```

**Features Working:**
- ✅ AWS Profile authentication
- ✅ Real strands-agents framework
- ✅ Real AgentCore code execution
- ✅ No simulation fallbacks
- ✅ Proper error handling
- ✅ Graceful startup diagnostics

**Architecture:**
- **Code Generator**: Strands-Agents + Claude Haiku 4.5
- **Code Executor**: Strands-Agents + AgentCore CodeInterpreter
- **Authentication**: AWS Profile (nmurich_dev with BedrockAgentCoreFullAccess)
- **Execution**: Real AWS sandbox environment
