---
name: generate-test-cases-junos
description: "Use when source code changes under ansible_collections/juniper/device/plugins and the user wants unit tests created or updated under ansible_collections/junipernetworks/junos/tests/unit."
allowed-tools:
  - read_file
  - file_search
  - grep_search
  - run_in_terminal
  - apply_patch
  - get_errors
context: fork
---

# Generate Unit Tests For Junos Collection Changes

## Goal
Create or update unit tests for code changes under:
- ansible_collections/juniper/device/plugins/module_utils/network/junos
- ansible_collections/juniper/device/plugins/modules

Match the existing test style under:
- ansible_collections/junipernetworks/junos/tests/unit

## Use This Skill When
- The user asks to write unit tests for modified Junos collection source files.
- The requested scope is under ansible_collections/juniper/device/plugins.
- The user expects actual test file edits, not only planning.

## Do Not Use This Skill When
- The task is test planning only (no code edits requested).
- The task is integration/functional testing under tests/integration.

## Required Workflow

### 1) Detect changed source files
Collect changed files and keep only these roots:
- ansible_collections/juniper/device/plugins/module_utils/network/junos
- ansible_collections/juniper/device/plugins/modules

Preferred commands:
- git diff --name-only -- ansible_collections/juniper/device/plugins/module_utils/network/junos ansible_collections/juniper/device/plugins/modules
- git diff --name-only --cached -- ansible_collections/juniper/device/plugins/module_utils/network/junos ansible_collections/juniper/device/plugins/modules

If both are empty, ask for exact files or compare branch heads:
- git diff --name-only origin/master...HEAD -- ansible_collections/juniper/device/plugins/module_utils/network/junos ansible_collections/juniper/device/plugins/modules

### 2) Map source file to unit test path
Use these conventions first, then adjust to existing repository layout:

- ansible_collections/juniper/device/plugins/modules/junos_<name>.py
  -> ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos/test_junos_<name>.py

- ansible_collections/juniper/device/plugins/module_utils/network/junos/config/<name>/<name>.py
  -> ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos/test_junos_<name>.py

- ansible_collections/juniper/device/plugins/module_utils/network/junos/argspec/<name>/<name>.py
  -> ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos/test_junos_<name>.py

- ansible_collections/juniper/device/plugins/module_utils/network/junos/config/<name>/
  + ansible_collections/juniper/device/plugins/module_utils/network/junos/argspec/<name>/
  + ansible_collections/juniper/device/plugins/modules/junos_<name>.py
  -> prefer updating one existing test file test_junos_<name>.py

If no matching test file exists, create one at:
- ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos/test_junos_<name>.py

### 3) Learn local style before writing tests
Read nearby tests and follow conventions:
- unittest-style classes inheriting from TestJunosModule.
- setUp patches for lock/unlock/load/commit and facts collection.
- set_module_args(...) + execute_module(...) pattern.
- fixture usage via load_fixture(...).

### 4) Implement behavior-focused tests only for changed behavior
Cover only behavior changed by source diff.

Typical scenarios for these modules:
- New parameter accepted by module args and not rejected.
- Parameter passed to commit_configuration kwargs when changed config commits.
- Default behavior path if parameter omitted.
- Error/edge path only if the source diff changed validation behavior.

Do not over-assert internal details unrelated to observable behavior.

### 5) Keep edits minimal and scoped
- Do not refactor unrelated tests.
- Do not reformat unrelated files.
- Reuse existing fixtures/helpers first.

### 6) Validate with targeted runs first
Run only updated/generated test files first.

Preferred commands:
- python -m pytest -q ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos/test_junos_<name>.py
- python -m pytest -q ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos/test_junos_<name>.py -k <new_test_name>

Then optionally run broader subset:
- python -m pytest -q ansible_collections/junipernetworks/junos/tests/unit/modules/network/junos

### 7) Report results
Summarize:
- changed source files detected
- source-to-test mapping used
- test files created/updated
- scenarios covered
- command(s) run and pass/fail outcome
- residual risks or uncovered branches

## Output Contract
Final response must include:
1. Source-to-test mapping used.
2. Exact test files modified.
3. Behavior each new/updated test verifies.
4. Validation command summary and outcomes.
5. Test output excerpt (at least test status lines + final summary).
