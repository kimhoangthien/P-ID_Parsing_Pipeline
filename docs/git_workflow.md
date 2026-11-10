# Collaborative Git workflow

`main` is stable; `dev` integrates reviewed work. Develop on
`feature/<module>-<task>` (for example `feature/text-dataset-reader`). Shared-core
changes should be coordinated with the other module owners before interface changes.

Branch from updated dev, keep PRs focused and target dev. Explain the behavior,
validation, dataset implications and interface changes. Require at least one
other team member's review, passing CI and resolved discussions before merge.
Reviewers check dependency direction and coordinate conventions. Update a feature
branch from dev and resolve conflicts locally without overwriting others' work.
Use squash merges for focused features. Promote tested milestones from dev to
main through a reviewed PR; preserve history and do not force-push shared branches.
Configure these review requirements in GitHub branch protection separately.

## Initial publication (manual only)

This scaffold was created in an existing repository on unborn `main`; origin was
already configured as `https://github.com/kimhoangthien/P-ID_Parsing_Pipeline.git`.
No commits, branches or pushes are made by scaffolding. Review first:

```sh
git status --short
git diff --stat
git ls-files --others --exclude-standard
# Stage only after reviewing files; inspect the complete staged diff.
git add .
git diff --cached --check
git diff --cached
# After your approval:
git commit -m "Initialize modular P&ID parsing research scaffold"
git remote -v
git ls-remote --heads origin
git push -u origin main
git switch -c dev
git push -u origin dev
```

Untracked files do not appear in ordinary `git diff`; inspect them before staging.
The remote heads check requires network access and repository permissions. If it
shows existing main/dev history, stop and fetch/reconcile that history before
publishing; do not force-push or overwrite it. Remote contents were not inspected
during setup. These instructions assume the local initial commit is reviewed and
the corresponding remote branches do not already contain conflicting history.
