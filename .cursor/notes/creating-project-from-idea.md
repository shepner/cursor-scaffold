# Creating a new project from an idea in another root

When you **create or expand a project** from an idea that originated elsewhere (e.g. a note in an Obsidian vault, another repo in the workspace), keep the new project **self-contained** so it can be moved or cloned later.

## Do not edit the source root

- Do not edit files in the vault (or other root) unless the user explicitly asks. Do not add a "Project" section or link there pointing to the new project.
- The idea may have come from that root; the implementation and all documentation belong in the new project only.

## Keep the project self-contained

- **No cross-project links.** Do not reference the source note or repo by path or URL in the new project's README or docs. Use only public, external references (upstream docs, specs, APIs).
- **All documentation inside the project.** Describe the idea and context in the project's own README or `.cursor/notes/` so the project stands alone.
- Rationale: the project can then be moved, cloned, or shared without broken links or dependency on another root.

## In the new project

- Add a **self-contained rule** (e.g. `.cursor/rules/self-contained.mdc`) so future sessions in that project also avoid editing other roots and avoid cross-project links.

This convention applies when the user says "expand this into a project", "create a project from this note", or "document and learn" after a correction like "don't edit Obsidian / don't link between projects."
