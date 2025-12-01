Last updated: 2025-12-02


# プロジェクト概要生成プロンプト（来訪者向け）

## 生成するもの：
- projectを3行で要約する
- プロジェクトで使用されている技術スタックをカテゴリ別に整理して説明する
- プロジェクト全体のファイル階層ツリー（ディレクトリ構造を図解）
- プロジェクト全体のファイルそれぞれの説明
- プロジェクト全体の関数それぞれの説明
- プロジェクト全体の関数の呼び出し階層ツリー

## 生成しないもの：
- Issues情報（開発者向け情報のため）
- 次の一手候補（開発者向け情報のため）
- ハルシネーションしそうなもの（例、存在しない機能や計画を勝手に妄想する等）

## 出力フォーマット：
以下のMarkdown形式で出力してください：

```markdown
# Project Overview

## プロジェクト概要
[以下の形式で3行でプロジェクトを要約]
- [1行目の説明]
- [2行目の説明]
- [3行目の説明]

## 技術スタック
[使用している技術をカテゴリ別に整理して説明]
- フロントエンド: [フロントエンド技術とその説明]
- 音楽・オーディオ: [音楽・オーディオ関連技術とその説明]
- 開発ツール: [開発支援ツールとその説明]
- テスト: [テスト関連技術とその説明]
- ビルドツール: [ビルド・パース関連技術とその説明]
- 言語機能: [言語仕様・機能とその説明]
- 自動化・CI/CD: [自動化・継続的統合関連技術とその説明]
- 開発標準: [コード品質・統一ルール関連技術とその説明]

## ファイル階層ツリー
```
[プロジェクトのディレクトリ構造をツリー形式で表現]
```

## ファイル詳細説明
[各ファイルの役割と機能を詳細に説明]

## 関数詳細説明
[各関数の役割、引数、戻り値、機能を詳細に説明]

## 関数呼び出し階層ツリー
```
[関数間の呼び出し関係をツリー形式で表現]
```
```


以下のプロジェクト情報を参考にして要約を生成してください：

## プロジェクト情報
名前: 
説明: # cat-jekyll-config-generator

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


依存関係:
{}

## ファイル階層ツリー
📄 .editorconfig
📄 .gitignore
📁 .vscode/
  📊 settings.json
📄 LICENSE
📖 README.md
📄 _config.yml
📁 examples/
  📄 config_example.toml
📁 generated-docs/
🌐 googled947dc864c270e07.html
📄 pytest.ini
📄 ruff.toml
📁 src/
  📄 cat_jekyll_config_generator.py
📁 tests/
  📄 __init__.py
  📄 test_cat_jekyll_config_generator.py

## ファイル詳細分析
**googled947dc864c270e07.html** (1行, 53バイト)
  - 関数: なし
  - インポート: なし

## 関数呼び出し階層
関数呼び出し階層を分析できませんでした

## プロジェクト構造（ファイル一覧）
.vscode/settings.json
README.md
googled947dc864c270e07.html

上記の情報を基に、プロンプトで指定された形式でプロジェクト概要を生成してください。
特に以下の点を重視してください：
- 技術スタックは各カテゴリごとに整理して説明
- ファイル階層ツリーは提供された構造をそのまま使用
- ファイルの説明は各ファイルの実際の内容と機能に基づく
- 関数の説明は実際に検出された関数の役割に基づく
- 関数呼び出し階層は実際の呼び出し関係に基づく


---
Generated at: 2025-12-02 07:01:44 JST
