#!/usr/bin/env python3
"""
GitHub Pages _config.yml Generator

指定ディレクトリ配下の各リポジトリフォルダに_config.ymlを自動生成する
"""

import argparse
import sys
from pathlib import Path

try:
    import tomli
except ImportError:
    print("エラー: tomliがインストールされていません")
    print("以下のコマンドでインストールしてください:")
    print("  pip install tomli")
    sys.exit(1)


def load_config(config_path: str) -> dict:
    """TOMLファイルから設定を読み込む"""
    path = Path(config_path)
    if not path.exists():
        print(f"エラー: 設定ファイル '{config_path}' が見つかりません")
        sys.exit(1)

    try:
        with open(path, "rb") as f:
            return tomli.load(f)
    except Exception as e:
        print(f"エラー: 設定ファイルの読み込みに失敗しました - {e}")
        sys.exit(1)


def generate_config(repo_path: Path, config: dict):
    """指定されたリポジトリディレクトリに_config.ymlを生成する"""
    repo_name = repo_path.name
    config_path = repo_path / "_config.yml"

    # 既存の_config.ymlが1024バイト以上の場合はスキップ
    if config_path.exists():
        file_size = config_path.stat().st_size
        if file_size >= 1024:
            print(f"⏭️  {repo_name}: _config.ymlが1024バイト以上のためスキップしました ({file_size}バイト)")
            return False

    # descriptionの処理
    description = config["description_template"].format(repo_name=repo_name)

    # _config.ymlを生成
    config_content = config["config_template"].format(
        repo_name=repo_name, description=description, username=config["github_username"], theme=config["theme"]
    )

    try:
        config_path.write_text(config_content, encoding="utf-8")
        print(f"✅ {repo_name}: _config.ymlを生成しました")
        return True
    except Exception as e:
        print(f"❌ {repo_name}: エラーが発生しました - {e}")
        return False


def parse_arguments():
    """コマンドライン引数を解析する"""
    parser = argparse.ArgumentParser(description="GitHub Pages _config.yml自動生成ツール")
    parser.add_argument("--config-filename", type=str, required=True, help="設定ファイル（TOML形式）のパス")
    return parser.parse_args()


def validate_config(config: dict):
    """設定ファイルの必須項目をチェックする"""
    required_fields = ["github_username", "base_dir", "theme", "description_template", "config_template"]
    for field in required_fields:
        if field not in config:
            print(f"エラー: 設定ファイルに '{field}' が指定されていません")
            sys.exit(1)


def get_repository_directories(base_dir: str) -> list[Path]:
    """対象となるリポジトリディレクトリの一覧を取得する"""
    base_path = Path(base_dir)

    if not base_path.exists():
        print(f"エラー: ディレクトリ '{base_dir}' が存在しません")
        sys.exit(1)

    # ディレクトリ一覧を取得（README.mdがあるもののみ）
    repo_dirs = [
        d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith(".") and (d / "README.md").exists()
    ]

    if not repo_dirs:
        print(f"エラー: '{base_dir}' 配下にリポジトリディレクトリが見つかりません")
        sys.exit(1)

    return sorted(repo_dirs)


def process_repositories(repo_dirs: list[Path], config: dict):
    """リポジトリディレクトリに対して_config.ymlを生成する"""
    print(f"対象リポジトリ数: {len(repo_dirs)}\n")

    success_count = 0
    for repo_dir in repo_dirs:
        if generate_config(repo_dir, config):
            success_count += 1

    print(f"\n完了: {success_count}/{len(repo_dirs)} 件の_config.ymlを生成しました")


def main():
    """メインエントリポイント"""
    # コマンドライン引数の解析
    args = parse_arguments()

    # 設定ファイルを読み込む
    config = load_config(args.config_filename)

    # 設定の検証
    validate_config(config)

    # 対象ディレクトリの取得
    repo_dirs = get_repository_directories(config["base_dir"])

    # 処理の実行
    process_repositories(repo_dirs, config)


if __name__ == "__main__":
    main()
