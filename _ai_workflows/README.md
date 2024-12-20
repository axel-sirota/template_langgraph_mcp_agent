<div align="center">
  <h1>🏭 AI Workflows Library</h1>
  <p><i>Transform chaotic AI interactions into reliable, repeatable processes</i></p>
</div>

## 🎯 What's This?

This library contains battle-tested workflows that turn complex AI tasks into systematic processes. Think of them as recipes that:
- ✨ Work reliably every time
- 📈 Scale across teams
- 🔄 Improve with each use
- 🎓 Anyone can learn and use

## 📁 Library Structure

```
_ai_workflows/
├── factory/              # Create new workflows & instructions
│   ├── new_workflow/     # Bootstrap a complete workflow
│   └── new_instructions/ # Generate instructions files
├── templates/            # Reusable workflow templates
└── [use_case]/          # Purpose-specific workflows
    ├── instructions/     # AI collaboration guidelines
    └── run.md           # Ready-to-use execution script
```

## 🚀 Quick Start

### Using a Workflow
1. Open Cursor AI's Composer (CMD/CTRL + I)
2. Copy any `run.md` file content
3. Fill in your specific inputs
4. Press Enter and watch the magic happen!

### Creating a Workflow
Best option: Use our factory workflow
1. Go to `factory/new_workflow/`
2. Follow `run.md`
3. Get a professional workflow structure in seconds

## 💡 Two Ways to Use This Library

### 1. Generic Workflows (in this folder)
Perfect for common tasks that work across projects:
```
_ai_workflows/
├── communication/    # Email templates, posts...
├── documentation/    # Technical writing, guides...
└── code_review/     # Code analysis, improvements...
```

### 2. Project-Specific Workflows
Create a `_ai_workflows/` folder in your project:
```
your_project/
├── _ai_workflows/   # Your custom workflows
│   ├── data_prep/
│   └── analysis/
└── src/
```

## 🎓 Understanding Workflow Types

### Complete Workflows
For repeatable processes:
```
workflow_name/
├── instructions/    # AI guidelines
│   └── instructions_v1.0.0.md
└── run.md          # Execution script
```

### Single Instructions
For one-time complex tasks:
```
project_name/
└── instructions_v1.0.0.md
```

## ⚡ Best Practices

### Version Control
- Use semantic versioning (v1.0.0)
- Document changes clearly
- Keep previous versions for reference

### Quality Assurance
- Files get `__validation_required` suffix
- Always validate outputs
- Remove suffix after validation
- Test with various inputs

### Design Principles
- One clear purpose per workflow
- Standardized inputs/outputs
- Clear validation criteria
- Regular improvements

## 🛠️ Current Limitations & Roadmap

### File-Based System
Current limitations:
- Manual version control
- Basic collaboration features
- No built-in branching

### Coming Soon
We're working on:
- Git integration
- Automated validation
- Collaborative editing
- Change tracking

## 📚 Learn More

- 📖 Full tutorial: `_ai_tutorials/2_ai_workflows/tutorial_en.md`
- 🏭 Start with: `factory/new_workflow/run.md`
- 📺 Watch: [AI Workflows Tutorial](https://youtu.be/YRzHOVCkmA0)

## 🤝 Contributing

1. Master existing workflows first
2. Test in your projects
3. Document thoroughly
4. Share improvements

---

<div align="center">
  <sub>Built with ❤️ by AI Swiss</sub>
</div>
