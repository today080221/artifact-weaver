# Downstream Consumer Contract

Private downstream projects generate artifacts. ArtifactWeaver renders them.

Recommended artifact root:

```text
artifact-root/
  render_manifest.json
  report.md
  report.json
  linked_evidence.json
  screenshots/
    placeholder-or-real-private-file.png
```

Render command:

```bash
python -m artifact_weaver render --manifest artifact-root/render_manifest.json --out artifact-root/html
```

The downstream project remains responsible for collecting evidence assets, writing JSON, and deciding what the report means. ArtifactWeaver only receives already-generated artifacts.

Do not commit private artifacts to this repository. Do not include Steam AppID or DepotID values. Do not include Jenkins internal URLs. Do not include actual local or company paths. Do not include actual skill IDs or synergy IDs.
