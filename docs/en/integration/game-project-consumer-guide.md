# Game Project Consumer Guide

A private game project can call ArtifactWeaver after it has already produced a render manifest, Markdown narrative, report JSON, and linked evidence JSON.

For a private Unity game project, Unity, Jenkins, Codex, QA logic, video capture, and project-specific adapters stay outside ArtifactWeaver. ArtifactWeaver does not run the game, evaluate gameplay, discover reports, upload files, or call external services.

Keep game-specific adapters in the private downstream repository. This open-source repository should only contain generic examples with fake data.
