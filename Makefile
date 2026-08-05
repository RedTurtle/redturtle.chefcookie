STATIC_DIR = src/redturtle/chefcookie/browser/static
ESBUILD = npx --yes esbuild@0.28.1

JS_SOURCES = \
	$(STATIC_DIR)/redturtle_chefcookie.js \
	$(STATIC_DIR)/redturtle_chefcookie_tech.js
JS_MINIFIED = $(JS_SOURCES:.js=.min.js)

CSS_SOURCES = $(STATIC_DIR)/styles.css
CSS_MINIFIED = $(CSS_SOURCES:.css=.min.css)

.PHONY: minify minify-js minify-css check-minified

minify: minify-js minify-css

minify-js:
	@for src in $(JS_SOURCES); do \
		out="$${src%.js}.min.js"; \
		echo "minifying $$src -> $$out"; \
		$(ESBUILD) $$src --minify --outfile=$$out; \
	done

minify-css:
	@for src in $(CSS_SOURCES); do \
		out="$${src%.css}.min.css"; \
		echo "minifying $$src -> $$out"; \
		$(ESBUILD) $$src --minify --outfile=$$out; \
	done

# Regenerates the minified assets and fails if that changes anything that
# is not already committed: catches the case where someone edited a source
# file (redturtle_chefcookie.js, redturtle_chefcookie_tech.js, styles.css)
# without regenerating its .min counterpart.
# NOTE: this compares file *content* (git diff), not modification times:
# git does not preserve mtimes on checkout, so an mtime-based check would
# always "pass" right after a fresh clone/checkout in CI regardless of
# which file was actually edited last.
check-minified: minify
	git diff --exit-code -- $(JS_MINIFIED) $(CSS_MINIFIED)
