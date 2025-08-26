# Environment Variables

RedLite uses several environment variables for configuration. This document lists all environment variables used throughout the project and when they are needed.

## Core RedLite Variables

### REDLITE_DATA_DIR

**Purpose**: Specifies the directory where RedLite stores its data files, including run metadata and cached results.

**Default**: `~/.cache/redlite` (user's home cache directory)

**When needed**: Optional. Only set this if you want to change the default data storage location.

### PORT

**Purpose**: Specifies the port number for the RedLite Web UI.

**Default**: `8000`

**When needed**: Optional. Only needed when running the RedLite Web UI and you want to use a different port than the default.

## API Keys for AI Models

### OPENAI_API_KEY

**Purpose**: API key for accessing OpenAI models (GPT-3.5, GPT-4, etc.)

**When needed**: Required when using `OpenAIModel` for text generation tasks.

### GEMINI_API_KEY

**Purpose**: API key for accessing Gogole Gemini models

**When needed**: Required when using `GeminiModel` for text generation tasks.

### HF_TOKEN

**Purpose**: Hugging Face authentication token for accessing models and datasets from the Hugging Face Hub.

**When needed**: Required when using `HFModel` with private models or models that require authentication. Also needed for higher rate limits.

### NGC_API_KEY

**Purpose**: NVIDIA NGC (NVIDIA GPU Cloud) API key for accessing NVIDIA's LLaMA NIM (NVIDIA Inference Microservice) models.

**When needed**: Required when using NVIDIA's LLaMA NIM service for text generation.

## AWS Credentials

### AWS_ACCESS_KEY_ID

**Purpose**: AWS access key ID for authenticating with AWS Bedrock services.

**When needed**: Required when using `AwsBedrockModel` for accessing AWS Bedrock text generation models.

### AWS_SECRET_ACCESS_KEY

**Purpose**: AWS secret access key for authenticating with AWS Bedrock services.

**When needed**: Required when using `AwsBedrockModel` for accessing AWS Bedrock text generation models.

## Zeno Integration

### ZENO_API_KEY

**Purpose**: API key for uploading evaluation results to Zeno platform for visualization and analysis.

**When needed**: Required when using the Zeno upload functionality (`redlite upload` command or `redlite.zeno.upload()` function).





