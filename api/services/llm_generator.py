from transformers import pipeline

# Lightweight open model (swap with better later)
_generator = None

def get_generator():
    global _generator
    if _generator is None:
        _generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2", device=-1)
    return _generator

PROMPT_TEMPLATE = """
You are an electronics engineer. Generate a SPICE netlist for the following requirement.
Include components, values, and .op analysis.
Requirement: {req}
Only output SPICE netlist.
"""

def generate_netlist_llm(req: str) -> str:
    gen = get_generator()
    prompt = PROMPT_TEMPLATE.format(req=req)
    out = gen(prompt, max_length=300, do_sample=True)[0]["generated_text"]
    # crude cleanup
    return out.split("Requirement:")[-1].strip()
