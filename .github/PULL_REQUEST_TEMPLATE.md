## Description

<!-- A concise summary of the changes in this PR. Reference related issues where applicable. -->

Closes #<!-- issue number -->

---

## Collection Namespace

<!-- Identify which collection(s) this PR affects -->

- **Collection namespace:** <!-- e.g. juniper.device or junipernetworks.junos -->
- **Collection version (bumped to):** <!-- e.g. 3.2.0 — update galaxy.yml if applicable -->
- **Module(s) / plugin(s) changed:** <!-- e.g. juniper.device.config, junipernetworks.junos.junos_command -->

---

## Type of Change

<!-- Check all that apply -->

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] Feature / new module or plugin (non-breaking change that adds functionality)
- [ ] Enhancement (improvement to existing module or plugin behaviour)
- [ ] Breaking change (fix or feature that would cause existing playbooks / roles to behave differently)
- [ ] Task / Chore (refactor, dependency update, CI, docs, etc.)

---

## Fix Details

<!-- Describe the root cause and what was changed to fix it. Be specific. -->

### Root Cause

<!-- What was the underlying problem? -->

### Solution

<!-- How does this PR address it? List the key changes. -->

- 
- 
- 

---

## Versions Tested

<!-- Fill in the versions you tested against. Add or remove rows as needed. -->

| Item | Version |
|------|---------|
| Collection namespace & version | <!-- e.g. juniper.device 3.2.0 --> |
| Ansible / ansible-core | <!-- e.g. ansible-core 2.15.3 --> |
| Python | <!-- e.g. 3.10.12 --> |
| OS | <!-- e.g. Ubuntu 22.04 --> |
| Junos version | <!-- e.g. 22.2R1.9 --> |
| Junos platform | <!-- e.g. MX480, vMX, QFX5100 --> |
| junos-eznc | <!-- e.g. 2.7.1 --> |
| ncclient | <!-- e.g. 0.6.15 --> |

---

## Sanity Test Results

<!-- Run sanity tests and paste the summary output below. -->

- [ ] Sanity tests pass with no new errors

```bash
ansible-test sanity
```

<details>
<summary>Sanity test output</summary>

```
<paste sanity test output here>
```

</details>

---

## Unit Test Results

<!-- Run unit tests and paste the summary output below. -->

- [ ] New or updated unit tests added under `tests/unit/`
- [ ] All unit tests pass locally

```bash
python3.12 -m pytest
```

<details>
<summary>Unit test output</summary>

```
<paste unit test output here>
```

</details>

- [ ] Code coverage has not decreased

---

## Integration Test Results

<!-- Run integration tests against a real or virtual Junos device and paste the summary. -->

- [ ] Integration tests reviewed for impact
- [ ] Affected integration tests pass (requires a live Junos device or vMX)

```bash
ansible-test network-integration --python 3.12 --inventory /root/pyez_ansible_release_validation1/ansible-junos-stdlib/ansible_collections/juniper/device/tests/integration/inventory.networking
```

<details>
<summary>Integration test output</summary>

```
<paste integration test output here>
```

</details>

---

## Checklist

### Code Quality

- [ ] Code follows the project's style guidelines
- [ ] `ansible-lint` passes with no new errors

```bash
ansible-lint
```

- [ ] `flake8` / `ruff` reports no new errors (for Python files)

```bash
flake8 plugins/
# or
ruff check plugins/
```

### Documentation

- [ ] Module documentation (DOCUMENTATION, EXAMPLES, RETURN blocks) updated if parameters changed
- [ ] `CHANGELOG.rst` / `changelogs/fragments/` entry added
- [ ] `galaxy.yml` version bumped if releasing

### General

- [ ] No hardcoded credentials, IP addresses, or sensitive data introduced
- [ ] `requirements.txt` updated if new Python packages are required
- [ ] Backward-compatible: existing playbooks will not break

---

## Additional Notes

<!-- Anything else reviewers should know: deployment considerations, follow-up tasks, known limitations, related PRs, etc. -->
