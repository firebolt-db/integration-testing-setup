# Integration testing setup action

This action is designed to simplify integration testing for applications that use Firebolt database. This action will create a database, an engine and start the engine. Accepted parameters are

## Versions

There are two major versions of this action, one per Firebolt generation:

| Version | Firebolt | Branch | Status |
|---------|----------|--------|--------|
| `@v2` | Firebolt 2.0 | `master` | Active development. New changes go here. |
| `@v1` | Firebolt 1.0 | `releases/v1` | Maintenance only. Largely deprecated. |

This branch (`releases/v1`) contains the Firebolt 1.0 version of the action.

## Usage

- **firebolt-username** - Username to use for authentication
- **firebolt-password** - Password to use for authentication
- **region [Optional]** - Region to create a database and engine in
- **instance-type [Optional]** - Engine instance type
- **db_suffix [Optional]** - A suffix to append to database name
- **engine-scale [Optional]** - Scale of an engine
- **api-endpoint [Optional]** -  Environment endpoint to use to connect (Default: `api.app.firebolt.io`)

## Release procedure
Releases are made with the **Release** workflow (Actions → Release → Run workflow):

1. In **Use workflow from**, pick the branch to release: `master` for v2, `releases/v1` for v1.
2. Enter the version using [semantic versioning](https://semver.org/), e.g. `1.0.4`. Its major version must match the branch, otherwise the workflow fails.

The workflow checks that the committed bundle in `dist/` is up to date, creates the `vX.Y.Z` tag and GitHub release, and moves the major version tag (e.g. `v1`) to it. This ensures all calls to this action with a major version tag use the latest release.
