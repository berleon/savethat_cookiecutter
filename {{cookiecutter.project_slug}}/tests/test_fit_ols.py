#!/usr/bin/env python
"""Tests for `{{ cookiecutter.pkg_name }}` package."""

from pathlib import Path

import pytest
import savethat
from savethat import io

from {{ cookiecutter.pkg_name }} import fit_ols

# ensure the project dir is set to the repo root
savethat.set_project_dir(Path(__file__).parent.parent)


@pytest.fixture
def storage(tmp_path: Path) -> savethat.Storage:

    fake_b2 = io.SimulatedB2API()
    return io.B2Storage(
        local_path=tmp_path,
        remote_path=Path("test"),
        b2_bucket=fake_b2.bucket_name,
        b2_key_id=fake_b2.application_key_id,
        b2_key=fake_b2.master_key,
        _bucket=fake_b2.bucket,
    )


def test_fit_ols(storage: savethat.Storage) -> None:
    args = fit_ols.FitOLSArgs(
        dataset="california_housing",
        target="MedHouseVal",
    )
    node = fit_ols.FitOLS("unique_node_key", args, storage)
    result = node.run()

    assert result.mse < 1.0
