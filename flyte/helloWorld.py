from flytekit import task, workflow

@task
def say_hello() -> str:
    return "Hello world"

@workflow
def my_wf() -> str:
    res = say_hello()
    return res

if __name__=="__main__":
    print(f"running my_wf() {my_wf()}")