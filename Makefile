help:
	@echo ""
	@echo "Options:"
	@echo ""
	@echo "- install  Install development dependencies"
	@echo "- help     Show this help"
	@echo "- test     Run full test suite (flake8 and unit tests)"
	@echo ""

install:
	@bin/install_dependencies

test:
	@bin/run_test_suite
