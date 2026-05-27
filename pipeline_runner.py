import subprocess

steps = [
    ("EXTRACT", "python etl/extract.py"),
    ("TRANSFORM", "python etl/transform.py"),
    ("LOAD", "python etl/load.py"),
    ("ANALYTICS", "python analytics/query_data.py")
]

for step_name, command in steps:
    print(f"\n==========={step_name}===========\n")

    result =subprocess.run(command, shell=True)

    if result.returncode !=0:
        print(f"Erro na etapa:{step_name}")
        break

print(f"\nPipeline finalizado!")