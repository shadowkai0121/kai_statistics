# Phase 01: User Setup Required

**Generated:** 2026-04-22
**Phase:** 01-library-infrastructure
**Status:** Incomplete

Complete these items before the first real PyPI release. The repository-side automation is already in place; these steps require maintainer access to external dashboards.

## Environment Variables

No local environment variables are required for the trusted-publishing path in this phase.

## Account Setup

- [ ] **Create or access the `kai_statistics` PyPI project**
  - URL: https://pypi.org/
  - Skip if: The package already exists under your maintainer account

## Dashboard Configuration

- [ ] **Confirm the `kai_statistics` project is ready for uploads**
  - Location: PyPI dashboard -> Your projects
  - Notes: Make sure the package name is owned by the intended maintainer account before the first release upload.

- [ ] **Register GitHub Actions trusted publishing for this repository**
  - Location: PyPI dashboard -> `kai_statistics` -> Publishing
  - Notes: Authorize the GitHub repository and the `.github/workflows/publish.yml` workflow so tagged releases can publish without storing a PyPI API token in the repo.

## Verification

After completing setup, verify the dashboard state before creating the first release tag:

```bash
# No local CLI verification is required for this dashboard-only setup.
# Before the first real release, confirm in PyPI that the GitHub repository
# and publish.yml workflow are listed as an approved trusted publisher.
```

Expected results:
- The `kai_statistics` project exists in PyPI under the correct maintainer account.
- PyPI lists the repository workflow as an approved trusted publisher.

---

**Once all items complete:** Mark status as "Complete" at top of file.
