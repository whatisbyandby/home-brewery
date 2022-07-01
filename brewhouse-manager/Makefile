target: dependency1
	recipes
		

test:
	docker build -t brewery-manager:test --target test .
	docker run -v $$PWD/cover:/code/cover \
		brewery-manager:test pytest \
		--cov=app \
		--cov-report=term \
		--cov-report=html:cover/cov_html \
		--ignore=./tests/on_device

run:
	docker build -t brewery-manager:latest --target production .
	docker run brewery-manager:latest uvicorn app.main:app --host 0.0.0.0 --port 80
