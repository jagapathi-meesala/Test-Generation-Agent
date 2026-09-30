from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_explainability_structure():
    t=(ROOT/"EXPLAINABILITY.md").read_text()
    required=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
    assert all(h in t for h in required)
    assert "## Inputs\n" not in t and "## Decision\n" not in t and "## Limits\n" not in t
    for h in required:
        section=t.split(h,1)[1].split("\n## ",1)[0]
        sentences=[x for x in section.replace("\n"," ").split(". ") if x.strip()]
        assert len(sentences)>=2

def test_required_files():
    for p in ["agent.yaml","SOUL.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md","README.md",".env.example"]:
        assert (ROOT/p).exists()
