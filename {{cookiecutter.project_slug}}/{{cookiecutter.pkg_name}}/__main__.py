import coverage
import savethat

# ensures coverage is also collected for subprocesses
coverage.process_startup()

savethat.run_main("{{cookiecutter.pkg_name}}")
