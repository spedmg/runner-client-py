SPEC_ARGS := --format documentation
SPECS := spec
.PHONY: test install

install:
	@echo Installing 'pipenv'
	@pip3 install --user pipenv
	@echo Installing test dependencies
	@pipenv install

test:
	@echo "Testing"
	@ENVIRONMENT=test pipenv run mamba $(SPEC_ARGS) $(SPECS)
