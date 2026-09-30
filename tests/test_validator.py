from core.validator import validate_cases

def valid(i): return {"id":i,"target":"f","category":"baseline","inputs":{},"expected":"works","rationale":"baseline","provenance":{"source_line":1,"method":"deterministic-ast-analysis"}}

def test_valid_cases(): assert validate_cases([valid("a")])["valid"]
def test_duplicate_ids():
 r=validate_cases([valid("a"),valid("a")]); assert not r["valid"]; assert any("duplicate" in x for x in r["errors"])
def test_missing_key():
 c=valid("a"); del c["expected"]; assert not validate_cases([c])["valid"]
