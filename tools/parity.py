#!/usr/bin/env python3
"""Calcula paridad ponderada desde features.csv (stdlib only)."""
import csv
import sys
from pathlib import Path

WEIGHTS = {"MUST": 5, "SHOULD": 3, "COULD": 1}
DONE = {"complete", "completed", "done", "completo", "completado"}
PARTIAL = {"partial", "parcial"}

def main(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    total = earned = 0
    missing = []
    for row in rows:
        priority = row.get("priority", "").strip().upper()
        status = row.get("status", "").strip().lower()
        if priority not in WEIGHTS:
            continue
        weight = WEIGHTS[priority]
        total += weight
        if status in DONE:
            earned += weight
        elif status in PARTIAL:
            earned += weight / 2
        else:
            missing.append((priority, row.get("feature", row.get("id", "Sin nombre")), status or "unknown"))
    if not total:
        print("No hay funcionalidades ponderables.")
        return
    print(f"Paridad ponderada: {earned / total * 100:.1f}% ({earned:g}/{total})")
    print("Pendientes:")
    for priority, feature, status in missing:
        print(f"- [{priority}] {feature} — {status}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python parity.py templates/features.csv")
    main(sys.argv[1])
