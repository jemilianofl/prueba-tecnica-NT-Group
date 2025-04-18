import subprocess

print("\n🔄 Verificando conexión con la base de datos...\n")
# Espera a que la base esté lista
subprocess.run(["python", "wait_for_db.py"], check=True)

scripts = [
    "load_data.py",
    "extract_data.py",
    "transform_data.py",
    "db_setup.py",
    "create_view.py"
]

print("\n📦 Iniciando flujo completo de procesamiento de datos...\n")

for script in scripts:
    print(f"\n🚀 Ejecutando: {script}\n")
    try:
        result = subprocess.run(["python", script], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar {script}: {e}")
        print(f"📜 STDOUT:\n{e.stdout}")
        print(f"📜 STDERR:\n{e.stderr}")
        break

print("\n✅ Proceso completo terminado.")