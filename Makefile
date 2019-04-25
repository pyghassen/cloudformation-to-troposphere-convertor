clean:
	./scripts/clean.sh

test:
	./scripts/clean.sh
	./scripts/test.sh

lint:
	./scripts/lint.sh

run:
	./scripts/run.sh $(input) $(output)
