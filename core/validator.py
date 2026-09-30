REQUIRED_KEYS=("id","target","category","inputs","expected","rationale","provenance")


def validate_cases(cases: list[dict]) -> dict:
    errors=[]; warnings=[]; seen=set()
    if not isinstance(cases,list): return {"valid":False,"errors":["cases must be a list"],"warnings":[]}
    for i,case in enumerate(cases):
        if not isinstance(case,dict): errors.append(f"case[{i}] must be an object"); continue
        missing=[k for k in REQUIRED_KEYS if k not in case]
        if missing: errors.append(f"case[{i}] missing keys: {', '.join(missing)}")
        cid=case.get("id")
        if cid in seen: errors.append(f"duplicate case id: {cid}")
        if cid is not None: seen.add(cid)
        if not isinstance(case.get("inputs"),dict): errors.append(f"case[{i}].inputs must be an object")
        if isinstance(case.get("expected"),str) and not case["expected"].strip(): errors.append(f"case[{i}].expected must be non-empty")
    if not cases: warnings.append("no test cases were supplied")
    return {"valid":not errors,"errors":errors,"warnings":warnings,"count":len(cases)}
