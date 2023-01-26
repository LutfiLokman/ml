import pandas as pd
import json

df = pd.DataFrame(
    {
        "procedure_name": ["Appendectomy", "Cesarean Section", "Nephrectomy"],
        "supply_name": ["Ligasure", "Ligasure", "Antibax"],
        "op_note": [
            "Laparoscopic converted to open",
            "Normal delivery converted to C-section",
            "Uncomplicated",
        ],
    }
)

json_str = """
{
"procedure_name" : ".*append.*",
"supply_name" : ".*ligasure",
"op_note" : ".*convert.*"
}
"""
query_dict = json.loads(json_str)

query_str = " & ".join(
    [f"{k}.str.match('{v}', case=False)" for k, v in query_dict.items()]
)

print(query_str)

df.query(query_str)
