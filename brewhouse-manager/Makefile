target: dependency1
	recipes


dev:
	docker build -t brewery-manager:development --target development .
	docker run \
		-p 5000:5000 \
		-v $$PWD/app:/code/app \
		-v $$PWD/tests:/code/tests \
		-v $$PWD/log:/code/log \
		--privileged \
		brewery-manager:development

test:
	docker build -t brewery-manager:test --target test .
	docker run -v $$PWD/cover:/code/cover \
		brewery-manager:test pytest \
		--cov=app \
		--cov-report=term \
		--cov-report=html:cover/cov_html


test_plugins: 
	docker build -t brewery-manager:test_plugins --target test_plugins .
	docker run \
		--privileged \
		-v $$PWD/cover:/code/cover \
		brewery-manager:test_plugins \
		pytest ./plugins \
		--cov=plugins \
		--cov-report=term \
		--cov-report=html:cover/plugins_html

run:
	docker build -t brewery-manager:latest --target production .
	docker run brewery-manager:latest uvicorn app.main:app --host 0.0.0.0 --port 80