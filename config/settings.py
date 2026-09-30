import os

class ConfigurationError(RuntimeError): pass

def get_runtime_config():
    level=os.getenv("TEST_AGENT_LOG_LEVEL")
    max_cases=os.getenv("TEST_AGENT_MAX_CASES")
    missing=[name for name,val in (("TEST_AGENT_LOG_LEVEL",level),("TEST_AGENT_MAX_CASES",max_cases)) if not val]
    if missing: raise ConfigurationError("missing required environment variables: "+", ".join(missing))
    try: limit=int(max_cases)
    except ValueError as exc: raise ConfigurationError("TEST_AGENT_MAX_CASES must be an integer") from exc
    if limit<1: raise ConfigurationError("TEST_AGENT_MAX_CASES must be >= 1")
    return {"log_level":level,"max_cases":limit}
