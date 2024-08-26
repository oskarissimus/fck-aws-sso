release:
	poetry version patch
	git commit -m "Bump version" pyproject.toml
	git push
	git tag -a v`poetry version -s` -m "Release v`poetry version -s`"
	git push --tags
	gh release create v`poetry version -s` --generate-notes
