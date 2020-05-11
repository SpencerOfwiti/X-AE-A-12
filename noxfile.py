import nox


@nox.session(python=["3.8", "3.7"])
def test(session):
	"""
	Run the test suite.
	:param session:
	:return:
	"""
	args = session.posargs or ["--cov", "-m", "not e2e"]
	session.run("poetry", "install", external=True)
	session.run("pytest", *args)
