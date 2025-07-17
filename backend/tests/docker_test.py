import pytest
import subprocess
import os

@pytest.mark.skipif(
    os.getenv("RUN_DOCKER_TEST", "false").lower() != "true",
    reason="Docker build test skipped unless RUN_DOCKER_TEST=true"
)
def test_docker_build():
    result = subprocess.run(
        ["docker", "build", "-t", "quote-searcher", "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    assert result.returncode == 0, f"Docker build failed:\n{result.stderr.decode()}"
