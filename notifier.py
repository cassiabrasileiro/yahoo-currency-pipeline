
def notify(successes: dict, failures: dict):
    print("\n✅ Notificação: Registros inseridos:")
    for symbol, count in successes.items():
        print(f"→ {symbol}: {count} registros")

    if failures:
        print("\n⚠️ Falhas:")
        for symbol, error in failures.items():
            print(f"→ {symbol}: {error}")
