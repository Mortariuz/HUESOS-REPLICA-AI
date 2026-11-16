#!/usr/bin/env python3
"""Valida el esquema y los valores de templates/features.csv (stdlib only)."""
import csv
import sys
from pathlib import Path

REQUIRED = {"id", "feature", "priority", "status", "evidence", "acceptance_criteria", "notes"}
PRIORITIES = {"MUST", "SHOULD", "COULD", "WONT"}
STATUSES = {"unknown", "not_started", "in_progress", "partial", "complete", "blocked", "excluded"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = set(reader.fieldnames or [])
            missing = sorted(REQUIRED - headers)
            if missing:
                return [f"Faltan columnas obligatorias: {', '.join(missing)}"]

            seen_ids: set[str] = set()
            for line, row in enumerate(reader, start=2):
                feature_id = (row.get("id") or "").strip()
                feature = (row.get("feature") or "").strip()
                priority = (row.get("priority") or "").strip().upper()
                status = (row.get("status") or "").strip().lower()

                if not feature_id:
                    errors.append(f"Línea {line}: id vacío.")
                elif feature_id in seen_ids:
                    errors.append(f"Línea {line}: id duplicado '{feature_id}'.")
                seen_ids.add(feature_id)

                if not feature:
                    errors.append(f"Línea {line}: feature vacío.")
                if priority not in PRIORITIES:
                    errors.append(
                        f"Línea {line}: priority '{priority or '(vacío)'}' no válido "
                        f"(usa {', '.join(sorted(PRIORITIES))})."
                    )
                if status not in STATUSES:
                    errors.append(
                        f"Línea {line}: status '{status or '(vacío)'}' no válido "
                        f"(usa {', '.join(sorted(STATUSES))})."
                    )
    except FileNotFoundError:
        return [f"No existe el archivo: {path}"]
    except UnicodeError as exc:
        return [f"No se pudo decodificar el CSV: {exc}"]
    except csv.Error as exc:
        return [f"CSV inválido: {exc}"]

    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("templates/features.csv")
    errors = validate(path)
    if errors:
        print("Matriz de funciones: ERROR")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Matriz de funciones: OK ({path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
