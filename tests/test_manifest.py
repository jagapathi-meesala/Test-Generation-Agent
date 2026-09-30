from verification.manifest_check import validate_manifest
def test_manifest_and_references():
 d=validate_manifest(); assert d["name"]=="test-generation-agent"
