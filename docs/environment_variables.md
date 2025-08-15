# Environment Variables

RedLite uses several environment variables for configuration. This document lists all environment variables used throughout the project, when they are needed, and how to set them on different operating systems.

## Core RedLite Variables

### REDLITE_DATA_DIR

**Purpose**: Specifies the directory where RedLite stores its data files, including run metadata and cached results.

**Default**: `~/.cache/redlite` (user's home cache directory)

**When needed**: Optional. Only set this if you want to change the default data storage location.

**Usage in code**: `redlite/_util.py` - Used by the `redlite_data_dir()` function to determine where to store run data and cache files.

#### Setting REDLITE_DATA_DIR:

**Linux/macOS (Bash/Zsh):**
```bash
export REDLITE_DATA_DIR="/path/to/your/data/directory"
```

**Windows (Command Prompt):**
```cmd
set REDLITE_DATA_DIR=C:\path\to\your\data\directory
```

**Windows (PowerShell):**
```powershell
$env:REDLITE_DATA_DIR="C:\path\to\your\data\directory"
```

## API Keys for AI Models

### OPENAI_API_KEY

**Purpose**: API key for accessing OpenAI models (GPT-3.5, GPT-4, etc.)

**When needed**: Required when using `OpenAIModel` for text generation tasks.

**Usage in code**: Used in examples (`samples/gpt3_5_turbo.py`, `README.md`) when creating OpenAI model instances.

#### Setting OPENAI_API_KEY:

**Linux/macOS (Bash/Zsh):**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-openai-api-key-here"
```

### HF_TOKEN

**Purpose**: Hugging Face authentication token for accessing models and datasets from the Hugging Face Hub.

**When needed**: Required when using `HFModel` with private models or models that require authentication. Also needed for higher rate limits.

**Usage in code**: Used in multiple sample files (`samples/gemma2-8bit.py`, `samples/gemma2-half.py`, `samples/gemma3.py`, `samples/eagle.py`, `samples/openchat.py`, `samples/llama.py`, `samples/mistral.py`) when creating HuggingFace model instances.

#### Setting HF_TOKEN:

**Linux/macOS (Bash/Zsh):**
```bash
export HF_TOKEN="your-huggingface-token-here"
```

**Windows (Command Prompt):**
```cmd
set HF_TOKEN=your-huggingface-token-here
```

**Windows (PowerShell):**
```powershell
$env:HF_TOKEN="your-huggingface-token-here"
```

### NGC_API_KEY

**Purpose**: NVIDIA NGC (NVIDIA GPU Cloud) API key for accessing NVIDIA's LLaMA NIM (NVIDIA Inference Microservice) models.

**When needed**: Required when using NVIDIA's LLaMA NIM service for text generation.

**Usage in code**: Used in `samples/nvidia_llama_nim.py` for accessing NVIDIA's hosted LLaMA models.

#### Setting NGC_API_KEY:

**Linux/macOS (Bash/Zsh):**
```bash
export NGC_API_KEY="your-nvidia-ngc-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set NGC_API_KEY=your-nvidia-ngc-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:NGC_API_KEY="your-nvidia-ngc-api-key-here"
```

## AWS Credentials

### AWS_ACCESS_KEY_ID

**Purpose**: AWS access key ID for authenticating with AWS Bedrock services.

**When needed**: Required when using `AwsBedrockModel` for accessing AWS Bedrock text generation models.

**Usage in code**: Used in `samples/aws_bedrock.py` when creating AWS Bedrock model instances.

#### Setting AWS_ACCESS_KEY_ID:

**Linux/macOS (Bash/Zsh):**
```bash
export AWS_ACCESS_KEY_ID="your-aws-access-key-id"
```

**Windows (Command Prompt):**
```cmd
set AWS_ACCESS_KEY_ID=your-aws-access-key-id
```

**Windows (PowerShell):**
```powershell
$env:AWS_ACCESS_KEY_ID="your-aws-access-key-id"
```

### AWS_SECRET_ACCESS_KEY

**Purpose**: AWS secret access key for authenticating with AWS Bedrock services.

**When needed**: Required when using `AwsBedrockModel` for accessing AWS Bedrock text generation models.

**Usage in code**: Used in `samples/aws_bedrock.py` when creating AWS Bedrock model instances.

#### Setting AWS_SECRET_ACCESS_KEY:

**Linux/macOS (Bash/Zsh):**
```bash
export AWS_SECRET_ACCESS_KEY="your-aws-secret-access-key"
```

**Windows (Command Prompt):**
```cmd
set AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
```

**Windows (PowerShell):**
```powershell
$env:AWS_SECRET_ACCESS_KEY="your-aws-secret-access-key"
```

## Zeno Integration

### ZENO_API_KEY

**Purpose**: API key for uploading evaluation results to Zeno platform for visualization and analysis.

**When needed**: Required when using the Zeno upload functionality (`redlite upload` command or `redlite.zeno.upload()` function).

**Usage in code**: Used in `redlite/zeno/upload.py` for authenticating with the Zeno platform to upload evaluation results.

#### Setting ZENO_API_KEY:

**Linux/macOS (Bash/Zsh):**
```bash
export ZENO_API_KEY="your-zeno-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set ZENO_API_KEY=your-zeno-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:ZENO_API_KEY="your-zeno-api-key-here"
```

## Development/Testing

### PORT

**Purpose**: Specifies the port number for the RedLite test server.

**Default**: `8000`

**When needed**: Optional. Only needed when running the RedLite test server and you want to use a different port than the default.

**Usage in code**: Used in `redlite/server/test/__main__.py` when starting the development/test server.

#### Setting PORT:

**Linux/macOS (Bash/Zsh):**
```bash
export PORT=3000
```

**Windows (Command Prompt):**
```cmd
set PORT=3000
```

**Windows (PowerShell):**
```powershell
$env:PORT=3000
```

## Persistent Environment Variables

To make environment variables persistent across terminal sessions, you can add the export commands to your shell configuration file:

### Linux/macOS:
- **Bash**: Add to `~/.bashrc` or `~/.bash_profile`
- **Zsh**: Add to `~/.zshrc`
- **Fish**: Add to `~/.config/fish/config.fish`

Example for `~/.bashrc` or `~/.zshrc`:
```bash
# RedLite configuration
export REDLITE_DATA_DIR="/path/to/your/data/directory"
export OPENAI_API_KEY="your-openai-api-key-here"
export HF_TOKEN="your-huggingface-token-here"
export ZENO_API_KEY="your-zeno-api-key-here"
```

### Windows:
You can set persistent environment variables through:
1. **System Properties** → **Advanced** → **Environment Variables**
2. **PowerShell** (as Administrator):
   ```powershell
   [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-api-key", "User")
   ```
