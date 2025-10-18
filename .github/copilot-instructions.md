# cat-jekyll-config-generator AI Coding Instructions

## Project Overview
This is a Python CLI tool that automatically generates Jekyll `_config.yml` files for GitHub Pages across multiple repository directories. The tool scans a parent directory for repositories (identified by having a `README.md`) and generates standardized Jekyll configuration files using a TOML template.

## Architecture & Key Components

### Core Module Structure
- `src/cat_jekyll_config_generator.py` - Single-file CLI application with clear functional separation
- Configuration via TOML files (see `examples/config_example.toml`)
- Batch script launcher (`cat_jekyll_config_generator.bat`) for Windows convenience

### Data Flow
1. Load TOML configuration → 2. Discover repositories (has `README.md`) → 3. Generate `_config.yml` per repo using template substitution

## Critical Development Workflows

### Running the Tool
```bash
# Windows batch launcher
cat_jekyll_config_generator.bat

# Direct Python execution
python -m src.cat_jekyll_config_generator --config-filename=secrets/cat_jekyll_config_generator.toml
```

### Configuration Pattern
All settings in TOML format with template strings:
- `config_template` uses `.format()` substitution with: `{repo_name}`, `{description}`, `{username}`, `{theme}`
- `description_template` allows customization of repository descriptions
- `base_dir` points to parent directory containing repositories

## Project-Specific Conventions

### File Detection Logic
Repository discovery: directories with `README.md` files (excludes dotfiles automatically)
```python
repo_dirs = [d for d in base_path.iterdir()
             if d.is_dir() and not d.name.startswith(".") and (d / "README.md").exists()]
```

### Error Handling Pattern
Uses `sys.exit(1)` for fatal errors with Japanese error messages:
```python
if not path.exists():
    print(f"エラー: 設定ファイル '{config_path}' が見つかりません")
    sys.exit(1)
```

### Configuration Validation
Required TOML fields: `["github_username", "base_dir", "theme", "description_template", "config_template"]`

## Development Environment

### Dependencies
- `tomli` for TOML parsing (with import error handling and user guidance)
- Python 3.9+ (uses `pathlib` and type hints)

### Code Quality Tools
- **Ruff**: Line length 120, E/F/W/I rules enabled, double quotes preferred
- **Pytest**: Configured but no tests implemented yet
- Code uses Japanese comments and error messages

### Key Files to Reference
- `secrets/cat_jekyll_config_generator.toml` - Live configuration (gitignored)
- `examples/config_example.toml` - Template for new configurations
- `ruff.toml` - Linting configuration with project-specific settings

## Integration Points
- **Output**: Writes to `_config.yml` files in discovered repository directories
- **Input**: TOML configuration files with template string substitution
- **GitHub Pages**: Generated configs are specifically for Jekyll/GitHub Pages deployment

When modifying this tool, maintain the single-file architecture, preserve the Japanese error messaging, and ensure template string compatibility with existing configurations.
