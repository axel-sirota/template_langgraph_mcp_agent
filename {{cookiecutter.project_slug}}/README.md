# {{cookiecutter.project_name}}

> **Fork origin:** 
[cbardyn/ai-swiss-workflows](https://github.com/cbardyn/ai-swiss-workflows)  
> Completely rebuilt for **LangGraph**, **MCP tools**, and **TDD-first** 
development.  
> This repo is a **GitHub Template** + **Cookiecutter** skeleton — click 
“Use this template” or run
> `cookiecutter gh:axel-sirota/template_langgraph_mcp_agent`.

## How this repo does TDD

* Write feature scenarios as markdown bullet-points under `tests/specs/`.
* Run `pytest -q` – it will fail.
* Ask Cursor to “Generate tests from specs”, then “Make code pass the 
tests”.

Rules live in `.cursor/rules/best-practices.mdc`; **asserts must never be
commented out** – fix failing tests instead.
