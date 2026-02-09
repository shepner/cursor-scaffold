#!/usr/bin/env bash
# Prepare an existing project for use in the knowledge-hub: run bootstrap and show next steps.
#
# Usage:
#   prepare-project-for-hub.sh <project_path> [--install-packs pack1 pack2 ...] [--apply]
#
# Runs cursor-scaffold's bootstrap-project.py on project_path. Without --apply, shows dry-run.
# See .cursor/notes/importing-projects.md for where to place the project and workspace options.

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
BOOTSTRAP="$REPO_ROOT/.cursor/helpers/bootstrap-project.py"

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <project_path> [--install-packs pack1 pack2 ...] [--enable-packs pack1 ...] [--apply]"
  echo ""
  echo "Prepares a project for the hub: runs bootstrap (AGENTS.md, .cursor/, git)."
  echo "See: $REPO_ROOT/.cursor/notes/importing-projects.md"
  exit 1
fi

PROJECT_PATH="$1"
shift
ARGS=("$@")

# Ensure --apply is present for actual changes
if [[ " ${ARGS[*]} " != *" --apply "* ]]; then
  echo "Dry run (no --apply). Add --apply to make changes."
  echo ""
fi

"$BOOTSTRAP" "$PROJECT_PATH" "${ARGS[@]}"

echo ""
echo "Next steps (optional):"
echo "  - If the project is under personal/ or work/, it is already indexed when that root is in the workspace."
echo "  - To add as a named workspace root: edit knowledge-hub.code-workspace and AGENTS.md (see importing-projects note)."
echo "  - To install more packs later: python3 $REPO_ROOT/.cursor/helpers/install_cursor_packs.py --target <path> --packs core git ..."
