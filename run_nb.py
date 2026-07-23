import nbformat
from nbclient import NotebookClient
from pathlib import Path

nb_path = Path('notebooks/00_core.ipynb')
nb = nbformat.read(nb_path, as_version=4)
client = NotebookClient(nb, timeout=600, kernel_name='python3')
try:
    client.execute()
    nbformat.write(nb, Path('notebooks/00_core.executed.ipynb'))
    print('EXECUTION_OK')
except Exception as e:
    print('EXECUTION_FAILED')
    import traceback
    traceback.print_exc()
