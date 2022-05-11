from pathlib import Path
{% if cookiecutter._collect_coverage == "y" %}
import coverage{% endif %}
import savethat

if __name__ == "__main__":
    {% if cookiecutter._collect_coverage == "y" %}# ensures coverage is also collected for subprocesses
    coverage.process_startup()
    {% endif %}repro_dir = Path(__file__).parent.parent

    savethat.run_main(
        "{{cookiecutter.pkg_name}}",
        env_file=repro_dir / "savethat.toml",
    )
