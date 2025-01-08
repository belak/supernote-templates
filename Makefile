all: $(patsubst page_%.py,out/page_%.png,$(wildcard page_*.py))

out/page_%.png: out/page_%.svg
	inkscape $< -o $@ -b white --export-png-color-mode=Gray_16

out/page_%.svg: page_%.py utils.py
	poetry run python $< > $@

watch:
	reflex --decoration=none -s -r '\.py' -- make all

fmt:
	poetry run black *.py
