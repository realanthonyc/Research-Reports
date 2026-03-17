#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_SKILLS_DIR="${SCRIPT_DIR}/skills"
CODEX_HOME_DIR="${CODEX_HOME:-${HOME}/.codex}"
CODEX_SKILLS_DIR="${CODEX_HOME_DIR}/skills"

SKILLS=(
  "btc-eth-news-digest"
  "comprehensive-equity-research-analysis"
  "cross-asset-weekly-outlook"
  "global-macro-intelligence"
  "qqq-daily-outlook"
)

mkdir -p "${CODEX_SKILLS_DIR}"

for skill in "${SKILLS[@]}"; do
  source_path="${REPO_SKILLS_DIR}/${skill}"
  target_path="${CODEX_SKILLS_DIR}/${skill}"

  if [[ ! -d "${source_path}" ]]; then
    echo "Missing repo skill directory: ${source_path}" >&2
    exit 1
  fi

  if [[ -L "${target_path}" ]]; then
    rm "${target_path}"
  elif [[ -e "${target_path}" ]]; then
    rm -rf "${target_path}"
  fi

  ln -s "${source_path}" "${target_path}"
  echo "Linked ${target_path} -> ${source_path}"
done

echo "Symlink install complete."
