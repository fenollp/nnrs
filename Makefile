SOURCES = $(shell find src/ -name *.rs)

all: $(SOURCES)
	cargo build

test: $(SOURCES)
	cargo test

clean:
	cargo clean
