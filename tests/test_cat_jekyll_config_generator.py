"""
Tests for cat_jekyll_config_generator
"""

import tempfile
from pathlib import Path

import pytest

from src.cat_jekyll_config_generator import generate_config


@pytest.fixture
def sample_config():
    """サンプル設定を返すフィクスチャ"""
    return {
        "github_username": "testuser",
        "theme": "jekyll-theme-slate",
        "description_template": "{repo_name}",
        "config_template": """title: "{repo_name}"
description: "{description}"
theme: {theme}
github:
  is_project_page: true
  repository_url: https://github.com/{username}/{repo_name}
""",
    }


def test_generate_config_creates_new_file(sample_config):
    """新規に_config.ymlを生成できることをテスト"""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "test-repo"
        repo_path.mkdir()
        (repo_path / "README.md").touch()

        result = generate_config(repo_path, sample_config)

        assert result is True
        config_file = repo_path / "_config.yml"
        assert config_file.exists()
        content = config_file.read_text()
        assert "test-repo" in content
        assert "testuser" in content


def test_generate_config_overwrites_small_file(sample_config):
    """1024バイト未満の既存ファイルは上書きされることをテスト"""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "test-repo"
        repo_path.mkdir()
        (repo_path / "README.md").touch()

        # 小さい既存ファイルを作成（100バイト）
        config_file = repo_path / "_config.yml"
        small_content = "x" * 100
        config_file.write_text(small_content)
        assert config_file.stat().st_size < 1024

        result = generate_config(repo_path, sample_config)

        assert result is True
        assert config_file.exists()
        new_content = config_file.read_text()
        assert new_content != small_content
        assert "test-repo" in new_content


def test_generate_config_skips_large_file(sample_config, capsys):
    """1024バイト以上の既存ファイルはスキップされることをテスト"""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "test-repo"
        repo_path.mkdir()
        (repo_path / "README.md").touch()

        # 1024バイト以上の既存ファイルを作成
        config_file = repo_path / "_config.yml"
        large_content = "x" * 1024
        config_file.write_text(large_content)
        assert config_file.stat().st_size >= 1024

        result = generate_config(repo_path, sample_config)

        assert result is False
        assert config_file.exists()
        # ファイルは変更されていないことを確認
        assert config_file.read_text() == large_content

        # スキップメッセージが出力されていることを確認
        captured = capsys.readouterr()
        assert "⏭️" in captured.out
        assert "1024バイト以上のためスキップしました" in captured.out
        assert "test-repo" in captured.out


def test_generate_config_skips_exactly_1024_bytes(sample_config):
    """ちょうど1024バイトのファイルもスキップされることをテスト"""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "test-repo"
        repo_path.mkdir()
        (repo_path / "README.md").touch()

        # ちょうど1024バイトの既存ファイルを作成
        config_file = repo_path / "_config.yml"
        exact_content = "x" * 1024
        config_file.write_text(exact_content)
        assert config_file.stat().st_size == 1024

        result = generate_config(repo_path, sample_config)

        assert result is False
        assert config_file.read_text() == exact_content


def test_generate_config_processes_1023_bytes(sample_config):
    """1023バイトのファイルは処理されることをテスト"""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "test-repo"
        repo_path.mkdir()
        (repo_path / "README.md").touch()

        # 1023バイトの既存ファイルを作成
        config_file = repo_path / "_config.yml"
        content_1023 = "x" * 1023
        config_file.write_text(content_1023)
        assert config_file.stat().st_size == 1023

        result = generate_config(repo_path, sample_config)

        assert result is True
        new_content = config_file.read_text()
        assert new_content != content_1023
        assert "test-repo" in new_content
