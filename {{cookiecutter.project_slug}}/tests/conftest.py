"""Fixtures for pytest."""

from pathlib import Path

import pytest


@pytest.fixture
def env_file(tmp_path: Path) -> Path:
    """Environment file fixture.

    Using this fixture ensure that local files are saved to the pytest tmpdir.
    """

    data_path = tmp_path / "data"
    with open(tmp_path / "savethat.toml", 'w') as f:
        print(f'local_path="${data_path}"', file=f)
        print('b2_prefix="test"', file=f)
        print("use_b2_simulation=true", file=f)

    return tmp_path / "savethat.toml"
