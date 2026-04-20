#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_SKILLS_DIR="${SCRIPT_DIR}/Skills/research-skills"
CODEX_HOME_DIR="${CODEX_HOME:-${HOME}/.codex}"
CODEX_SKILLS_DIR="${CODEX_HOME_DIR}/skills"
COMMAND="${1:-install}"
RESTORE_SOURCE="${2:-}"

SKILLS=(
  "btc-eth-news-digest"
  "comprehensive-equity-research-analysis"
  "cross-asset-weekly-outlook"
  "daily-trading-insights"
  "global-macro-intelligence"
  "qqq-daily-outlook"
  "sector-company-discovery"
  "company-valuation-analyst"
  "screening-compounders"
  "upcoming-themes-discovery"
)

mkdir -p "${CODEX_SKILLS_DIR}"

restore_from_backup() {
  local source_dir="$1"

  if [[ ! -d "${source_dir}" ]]; then
    echo "Restore source is not a directory: ${source_dir}" >&2
    exit 1
  fi

  shopt -s nullglob
  local entries=("${source_dir}"/*)
  shopt -u nullglob

  if [[ ${#entries[@]} -eq 0 ]]; then
    echo "Restore source is empty: ${source_dir}" >&2
    exit 1
  fi

  for entry in "${entries[@]}"; do
    local name
    name="$(basename "${entry}")"
    local target_path="${CODEX_SKILLS_DIR}/${name}"

    if [[ -L "${target_path}" || -e "${target_path}" ]]; then
      rm -rf "${target_path}"
    fi

    mv "${entry}" "${target_path}"
    echo "Restored ${target_path} from ${source_dir}/${name}"
  done
}

if [[ "${COMMAND}" == "--restore" ]]; then
  if [[ -z "${RESTORE_SOURCE}" ]]; then
    RESTORE_SOURCE="$(ls -1dt "${CODEX_HOME_DIR}"/skill-backups/* 2>/dev/null | head -n 1 || true)"
  fi

  if [[ -z "${RESTORE_SOURCE}" ]]; then
    echo "No skill backups found in ${CODEX_HOME_DIR}/skill-backups" >&2
    exit 1
  fi

  restore_from_backup "${RESTORE_SOURCE}"
  echo "Restore complete."
  exit 0
fi

BACKUP_DIR="${CODEX_HOME_DIR}/skill-backups/$(date +%Y%m%d-%H%M%S)"
mkdir -p "${BACKUP_DIR}"

backup_existing_target() {
  local target_path="$1"

  if [[ -L "${target_path}" || -e "${target_path}" ]]; then
    local target_name
    target_name="$(basename "${target_path}")"
    local backup_path="${BACKUP_DIR}/${target_name}"

    if [[ -e "${backup_path}" || -L "${backup_path}" ]]; then
      rm -rf "${backup_path}"
    fi

    mv "${target_path}" "${backup_path}"
    echo "Backed up ${target_path} -> ${backup_path}"
  fi
}

for skill in "${SKILLS[@]}"; do
  source_path="${REPO_SKILLS_DIR}/${skill}"
  target_path="${CODEX_SKILLS_DIR}/${skill}"

  if [[ ! -d "${source_path}" ]]; then
    echo "Missing repo skill directory: ${source_path}" >&2
    exit 1
  fi

  backup_existing_target "${target_path}"

  ln -s "${source_path}" "${target_path}"
  echo "Linked ${target_path} -> ${source_path}"
done

echo "Symlink install complete."
echo "Backups stored in ${BACKUP_DIR}"
echo "Restore latest backup with: ${SCRIPT_DIR}/symlink-install.sh --restore"
echo "Restore specific backup with: ${SCRIPT_DIR}/symlink-install.sh --restore <backup-dir>"
