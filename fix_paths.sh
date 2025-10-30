#!/usr/bin/env bash
set -euo pipefail

for f in docs/plot*.md; do
  if [[ -f "$f" ]]; then
    if grep -q "../api/" "$f"; then
      # Note: '' right after -i means "no backup file"
      sed -i '' -e 's|\.\./api/|\.\./api-reference/|g' "$f"
      echo "Updated: $f"
    else
      echo "No change: $f"
    fi
  fi
done

find docs -type f -name "*.md" -exec sed -E -i '' 's/\(([^()]*)\.md#/(\1#/g' {} +

