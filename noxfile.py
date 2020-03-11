import nox


@nox.session(python=['3.7'])
def tests(session):
    args = session.postargs or ['--cov']
    session.run('poetry', 'install', external=True)
    session.run('pytest', *args)
