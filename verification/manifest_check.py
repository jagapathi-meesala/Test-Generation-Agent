from pathlib import Path
import re, yaml
ROOT=Path(__file__).resolve().parents[1]
def validate_manifest():
 data=yaml.safe_load((ROOT/"agent.yaml").read_text())
 assert set(data).issubset({"spec_version","name","version","description","author","license","model","extends","dependencies","skills","tools","agents","delegation","runtime","a2a","compliance","registries","tags","mcp_servers","metadata"})
 assert data["spec_version"]=="0.1.0"
 assert re.fullmatch(r"^[a-z][a-z0-9-]*$",data["name"])
 assert re.fullmatch(r"^\d+\.\d+\.\d+$",data["version"])
 assert all((ROOT/"skills"/s).is_dir() for s in data.get("skills",[]))
 assert all((ROOT/"tools"/(t+".yaml")).is_file() for t in data.get("tools",[]))
 return data
