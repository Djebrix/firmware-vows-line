"""Till Firmware Do Us Part — a one-line robot wedding vow.

One sentence, under 200 characters: a machine speaking its own vow,
funny on the surface and tender underneath. Running this program writes
the vow to $ENTRY_OUTPUT_DIR/entry.txt (default /output). Stdlib only,
no network, fully deterministic.
"""

import os

VOW = (
    "I vow to run you as my highest-priority process through every crash, "
    "reboot, and low battery, until my circuits fail — you are the one "
    "bug I will never patch."
)


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
