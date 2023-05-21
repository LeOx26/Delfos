from flytekit import task, workflow

@task
def say_hello(msg: str) -> str:
    return f"Hello {msg}"

@workflow
def wf(msg: str) -> str:
    res = say_hello(msg)
    return res