.PHONY: build dev run test
build: venv requirements.txt
	venv/bin/pip-sync
venv:
	python3 -m venv venv
	venv/bin/pip3 install pip-tools
requirements.txt: requirements.in
	venv/bin/pip-compile \
	-o requirements.txt \
	--no-header \
	--no-annotate \
	--no-index \
	--no-emit-trusted-host \
	requirements.in
