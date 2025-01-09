all: $(patsubst page_%.py,out/%.png,$(wildcard page_*.py))

out/%.png: out/%.svg
	inkscape $< -o $@ -b white --export-png-color-mode=Gray_16

out/%.svg: page_%.py supernote_nomad.py utils.py
	poetry run python $< > $@

watch:
	reflex --decoration=none -s -r '\.py' -- make all

fmt:
	poetry run black *.py
