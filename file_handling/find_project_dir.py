import os


def find_project_root(markers=("requirements.txt", ".gitignore", "venv", ".venv", ".idea")):
    # Auto-convert string to tuple if single marker is passed
    if isinstance(markers, str):
        markers = (markers,)

    current_path = os.path.abspath(os.path.dirname(__file__))

    while current_path != os.path.dirname(current_path):  # Until root of filesystem
        for marker in markers:
            marker_path = os.path.join(current_path, marker)
            if os.path.exists(marker_path):  # Works for files or directories
                return current_path
        current_path = os.path.dirname(current_path)

    raise FileNotFoundError(f"Project root not found using markers: {', '.join(markers)}")