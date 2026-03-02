"""
Batch 6 Acceptance Test: Add physics isolation smoke test.
"""
import subprocess
import sys

def test_physics_has_no_streamlit_dependency():
    """Ensures core.physics can be imported without streamlit."""
    script = "import sys; sys.modules['streamlit']=None; import core.physics"
    result = subprocess.run([sys.executable, "-c", script], capture_output=True)
    assert result.returncode == 0, \
        f"core.physics failed to import without streamlit: {result.stderr.decode()}"