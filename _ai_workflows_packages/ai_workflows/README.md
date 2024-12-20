<div align="center">
  <h1>🤖 AI Workflows Framework</h1>
  <p><i>Transform AI Assistant Chats into Powerful Python Code</i></p>
</div>

## 🎯 Why This Framework?

You love working with AI assistants - writing instructions in plain text, having natural conversations, getting quick results. But sometimes you need more:

- 🔄 Want to run the same workflow reliably, again and again?
- 📊 Need to process data from multiple sources first?
- 🎮 Want precise control over how the AI thinks?
- 🤝 Need to integrate with your existing tools?

That's where this framework comes in. It helps you transform your text-based AI workflows into Python code that:
- 🚀 Runs independently of any AI assistant
- 🛠️ Uses proven open-source libraries
- 🎯 Gives you complete control over execution
- 📈 Adapts to your needs

## ⚡ Quick Example

```python
from ai_workflows import Workflow

# Transform your text instructions into code
workflow = Workflow(
    config_path='config.yaml',             # Choose your AI tools
    instructions_path='instructions.yaml'  # Define your workflow
)

# Run it anywhere!
result = workflow.run()
```

## 🧩 Core Components

### 1. Instructions File (tasks.yaml)
Your workflow, structured but still readable:
```yaml
goal: "Analyze customer feedback"
tasks:
  - key: 'extract_topics'
    description: 'Find main topics in feedback'
    inputs:
      - from_context: ['feedback.csv']
    outputs:
      - key: 'topics'
        file: 'topics.md'
```

### 2. AI Tools Config (config.yaml)
Choose your preferred AI models and settings:
```yaml
llm:
  type: "langchain_groq.ChatGroq"
  model_name: "llama-3.3-70b-versatile"
  temperature: 0  # Precise outputs

embeddings:
  type: "langchain_huggingface.HuggingFaceEmbeddings"
  model_name: "all-MiniLM-L6-v2"
```

## 🚀 Getting Started

### 1. Install Requirements
- Python 3.10+
- Poetry (package manager)

### 2. Set Up the Framework
```bash
# Get the code
git clone https://github.com/cbardyn/ai-swiss-workflows
cd _ai_workflows_packages/ai_workflows

# Install dependencies
poetry install

# Activate environment
source .venv/bin/activate  # (or .\.venv\Scripts\activate on Windows)
```

### 3. Create Your First Workflow

1. **Write Instructions** (tasks.yaml):
```yaml
goal: "Summarize meeting notes"
tasks:
  - key: 'extract_key_points'
    description: 'Identify main decisions and action items'
    inputs:
      - from_context: ['meeting_notes.md']
    outputs:
      - key: 'summary'
        file: 'summary.md'
```

2. **Configure AI** (config.yaml):
```yaml
llm:
  type: "langchain_groq.ChatGroq"
  model_name: "llama-3.3-70b-versatile"
  temperature: 0
```

3. **Run It** (run.py):
```python
from ai_workflows import setup_logging, Workflow

# Enable helpful logging
setup_logging()

# Create and run your workflow
workflow = Workflow('config.yaml', 'tasks.yaml')
result = workflow.run()
```

## 🛠️ Framework Features

### Smart Context Management
- 📂 Automatic file loading
- 🔍 Vector search for relevant info
- 🧠 Memory across tasks

### Robust Task Orchestration
- ⛓️ Sequential task execution
- 📊 Data passing between tasks
- 📈 Progress tracking

### Professional Error Handling
- 🚫 Missing file detection
- 🔄 API failure recovery
- ⚠️ Configuration validation

## 🎯 When to Use This Framework

### Perfect For:
- 🔄 Repeatable AI workflows
- 🎯 Systematic processes
- 🤝 Team knowledge sharing
- 🔧 Tool integration

### Maybe Not For:
- 🤔 One-off creative tasks
- 💭 Exploratory conversations
- 🎨 Highly iterative design
- 📝 Simple text completions

## 🚀 Next Steps

1. Check examples in `_ai_workflows/code_based/*/`
2. Try the FAQ analyzer demo
3. Convert your own text workflows
4. Share improvements!

## 🛠️ Roadmap

We're working on:
- 🔌 More external connectors (Dropbox, Google Drive)
- ✅ Automated testing suite
- 🔒 Enhanced security features
- ⚡ Parallel task execution
- 🔄 Backup AI models
- 💾 Automatic data backups
- 📊 Performance monitoring

---

<div align="center">
  <sub>Built with ❤️ by AI Swiss</sub>
</div>
