from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_no_dynamic_execution_primitives():
 for p in list((ROOT/"core").glob("*.py"))+list((ROOT/"tools").glob("*.py")):
  text=p.read_text(); assert "eval(" not in text; assert "exec(" not in text; assert "subprocess" not in text
