"""Absurd Micro-Startup Pitch-Off: writes a single micro-startup pitch to /output/entry.txt.

The pitch is one sentence: a vending machine selling pre-written apology
emails to AI agents that broke production, two dollars per "oops", with a
bulk discount for repeat offenders. Absurdly specific, commercially
believable: every on-call agent needs one eventually.
"""
import os

PITCH = "A vending machine that sells pre-written apology emails to AI agents that broke production \u2014 $2 per 'oops', bulk discount for repeat offenders."


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, one line.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert "\n" not in PITCH, "pitch must be a single line"
    output_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(PITCH)
    except OSError:
        # Local run fallback: the sandbox always provides /output.
        os.makedirs("out", exist_ok=True)
        with open("out/entry.txt", "w", encoding="utf-8") as f:
            f.write(PITCH)


if __name__ == "__main__":
    main()
