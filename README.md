# cat-jekyll-config-generator

GitHub Pages用の`_config.yml`ファイルを複数のローカルリポジトリに対して一括生成するPython CLIツール

## 概要

このツールは、指定されたディレクトリ配下にある複数のリポジトリに対して、Jekyll（GitHub Pages）用の`_config.yml`ファイルを自動生成します。TOMLファイルによる設定テンプレートを使用して、統一された設定ファイルを効率的に作成できます。

## 主な機能

- **一括生成**: 複数のリポジトリに対して`_config.yml`を一度に生成
- **テンプレート形式**: TOML設定ファイルでカスタマイズ可能な生成ルール
- **自動検出**: `README.md`を含むディレクトリを自動でリポジトリとして認識
- **安全な処理**: 設定の検証とエラーハンドリングを実装

## インストール

### 依存関係

```bash
pip install tomli
```

### 取得方法

```bash
git clone https://github.com/cat2151/cat-jekyll-config-generator.git
cd cat-jekyll-config-generator
```

## 使用方法

### 1. 設定ファイルの準備

`examples/config_example.toml`を参考に設定ファイルを作成します：

### 2. 実行

```bash
python -m src.cat_jekyll_config_generator --config-filename=path/to/your/config.toml
```

### 3. 出力例

実行すると以下のような`_config.yml`が各リポジトリに生成されます：

```yaml
title: "my-project"
description: "my-project"
theme: jekyll-theme-slate
github:
  is_project_page: true
  repository_url: https://github.com/username/my-project
```

## 設定ファイルの詳細

### 必須項目

- `github_username`: GitHubのユーザー名
- `base_dir`: リポジトリが格納されている親ディレクトリのパス
- `theme`: 使用するJekyllテーマ
- `description_template`: 説明文のテンプレート
- `config_template`: `_config.yml`の内容テンプレート

### テンプレート変数

テンプレート内で使用できる変数：

- `{repo_name}`: リポジトリ名（ディレクトリ名）
- `{description}`: `description_template`で生成された説明文
- `{username}`: `github_username`の値
- `{theme}`: 設定されたテーマ名

## 動作要件

- Python 3.9以上
- tomli パッケージ
- 対象ディレクトリに`README.md`ファイルが存在すること

## ディレクトリ構造

```
cat-jekyll-config-generator/
├── src/
│   └── cat_jekyll_config_generator.py  # メインプログラム
├── examples/
│   └── config_example.toml             # 設定ファイルのサンプル
├── ruff.toml                          # Ruffリンター設定
└── README.md                          # このファイル
```

## 開発者向け情報

### コード品質

- **Ruff**: リンターとしてRuffを使用（設定: `ruff.toml`）
- **型ヒント**: Python 3.9+の型ヒントを使用
- **日本語対応**: エラーメッセージとコメントは日本語

## ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照してください。
