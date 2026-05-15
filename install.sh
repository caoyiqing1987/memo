#!/bin/bash
# install.sh — Install `memo` CLI

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_DIR="${HOME}/.local/bin"
INSTALL_PATH="${BIN_DIR}/memo"

mkdir -p "$BIN_DIR"

# Create the wrapper script
cat > "$INSTALL_PATH" << 'WRAPPER'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
exec python3 "${SCRIPT_DIR}/../lib/memo/memo.py" "$@"
WRAPPER

# Copy the library
mkdir -p "${BIN_DIR}/../lib/memo"
cp "$SCRIPT_DIR/memo.py" "${BIN_DIR}/../lib/memo/"

chmod +x "$INSTALL_PATH"

# Detect shell and suggest PATH update
SHELL_NAME="$(basename "${SHELL}")"
RC_FILE=""
case "$SHELL_NAME" in
  zsh) RC_FILE="${HOME}/.zshrc" ;;
  bash) RC_FILE="${HOME}/.bashrc" ;;
esac

echo "✓ Installed memo to ${INSTALL_PATH}"

if [[ ":$PATH:" != *":${BIN_DIR}:"* ]]; then
  echo ""
  echo "⚠  ${BIN_DIR} is not in your PATH."
  echo "   Add this to your ${RC_FILE:-shell config}:"
  echo "   export PATH=\"\$PATH:${BIN_DIR}\""
  echo "   Then run: source ${RC_FILE:-your shell config}"
fi

echo ""
echo "  Try: memo init"
