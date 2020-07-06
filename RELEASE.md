To release a new version of dbsession:
1. git fetch upstream && git checkout upstream/master
2. Close milestone on GitHub
3. git clean -xfdi
4. Update CHANGELOG.md with loghub
5. git add -A && git commit -m "Update Changelog"
6. Update release version in ``__init__.py`` (set release version, remove 'dev0')
7. git add -A && git commit -m "Release vX.X.X"
8. git tag -a vX.X.X -m "Release vX.X.X"
9. python setup.py sdist
10. python setup.py bdist_wheel
11. twine upload
12. Update development version in ``__init__.py`` (add '.dev0' and increment minor)
13. git add -A && git commit -m "Back to work"
14. git push upstream master
15. git push upstream --tags
16. Draft a new release in GitHub
17. Compute SHA256 checksum for `.tar.gz` source
18. Update version and sha256 for the latest version.
19. Bump build version to 0.
20. conda-build recipe/
21. anaconda upload ... --user treble
