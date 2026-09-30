import pytest
from config.settings import get_runtime_config, ConfigurationError
def test_required_runtime_config(monkeypatch):
 monkeypatch.delenv("TEST_AGENT_LOG_LEVEL",raising=False); monkeypatch.delenv("TEST_AGENT_MAX_CASES",raising=False)
 with pytest.raises(ConfigurationError): get_runtime_config()
