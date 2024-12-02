# 🚀 Workflows library

> "Workflows turn complex AI tasks into reliable, repeatable processes."

This folder contains generic, reusable workflows that can be used across different projects.

⚠️ For project-specific workflows, create a `_ai_workflows` folder in your project directory instead.

## 📁 Structure

```
_ai_workflows/            # Generic, reusable workflows
├── factory/              # Workflows for creating new workflows
│   ├── new_workflow/     # Creates a new workflow
│   └── new_instructions/ # Creates a new instructions file
├── templates/            # Templates for workflows or instructions files
└── [use_case]/           # Workflows organized by use case (e.g., communication/)
    ├── instructions/
    │   └── instructions_v1.0.0.md
    └── run.md
```

## 🎯 Generic vs project-specific workflows

### Generic workflows
Located in the root `_ai_workflows/` folder, these are reusable across different projects:
```
_ai_workflows/
├── factory/
├── templates/
└── communication/      # Example: generic communication workflows
    ├── event_invite/
    ├── linkedin_post/
    ├── ...
```

### Project-specific workflows
Located in a `_ai_workflows/` folder within your project, these are tailored to project needs:
```
my_project/
├── _ai_workflows/      # Project-specific workflows
│   ├── data_curation/
│   ├── paper_writing/
│   ├── ...
```

## 💡 Workflows vs instructions files

### Workflows
- For **repeated tasks** that follow the same pattern
- Example: Writing bug ticket instructions
- Has both `instructions/` folder and `run.md`
- Is refined over time through multiple uses
- Version controlled (v1.0.0, v1.1.0, etc.)

### Instructions files
- For **one-time complex projects**
- Example: Resolving a specific bug ticket
- Single file: `instructions_v1.0.0.md`
- Also is refined and version controlled, but usually stops evolving after the project is complete

**Example:**
```
project/
├── _ai_workflows/
│   └── ticket_resolution/  # Workflow for generic ticket resolution
│       ├── instructions/
│       │   └── instructions_v1.0.0.md
│       └── run.md
└── ticket_resolutions/
    └── ticket_number_123/
        └── instructions_v1.0.0.md  # Instructions that evolve with the ticket, until its resolution
```

## 🚀 Getting started

### Using an existing workflow

1. Open Composer (CMD + I (MacOS) or CTRL + I (Windows))
2. Copy-paste the content of the workflow's `run.md`
3. Adapt the inputs to your needs
4. Press Enter

For more details, see the tutorials in `_ai_tutorials`.

### Creating a new workflow

#### Option 1: Using factory workflow (recommended)
1. Navigate to `_ai_workflows/factory/new_workflow/`
2. Follow the instructions in `run.md`
3. The factory will bootstrap a new workflow structure

#### Option 2: Manual creation
1. Create your workflow folder:
```
your_workflow/
├── instructions/
│   └── instructions_v1.0.0.md
└── run.md
```
2. Copy an existing workflow or use templates from `_ai_workflows/templates/`
3. Customize for your needs

## 🛠️ Maintenance

### Version control
- Use semantic versioning (vX.Y.Z)
- Document changes in version history
- Keep previous versions for reference

### Quality control
- Generated files should include a `__validation_required` suffix (see the `.cursorrules` file specifying this)
- Always validate generated files (and remove the suffix after validation)
- Test workflows with various inputs
- Collect and incorporate feedback

### Best practices
- One purpose per workflow
- Clear instructions file
- Standardized inputs
- Clear validation criteria
- Regular reviews and updates

## 📚 Resources

- See the full tutorial in `_ai_tutorials/2_ai_workflows/tutorial_en.md`
- Use factory workflows in `factory/` to get started

## 🤝 Contributing

1. Follow the existing structure
2. Add workflows to your project (in a `_ai_workflows/` subfolder)
3. Document usage and provide examples in a README.md file if needed
4. Contribute to generic workflows in `_ai_workflows/` only when you've mastered the process

## ⚠️ Current limitations

### File-based versioning
The current system relies on a shared file structure on a server, which has some limitations:
- No built-in change history
- Manual version management
- Limited collaboration features
- No branching capabilities
- Risk of concurrent modifications

### Future improvements
Ideally, this system should be enhanced with:
- A Git repository for proper version control
- Branch-based workflow development
- Pull request reviews for quality control
- Automated validation checks
- Proper conflict resolution
- Change history and traceability

Until then, be extra careful when modifying shared workflows and always:
- Communicate changes to the team
- Keep backup copies of critical workflows
- Document all modifications in version history
- Test changes thoroughly before deployment

---

**Note**: This is a living document! Share your feedback and improvements to help our workflow library grow and evolve.