all: $(patsubst page_%.py,out/page_%.png,$(wildcard page_*.py))

out/page_%.png: out/page_%.svg
	inkscape $< -o $@ -b white

out/page_%.svg: page_%.py
	poetry run python $< > $@

watch:
	reflex --decoration=none -s -r '\.py' -- make all

fmt:
	poetry run black *.py
