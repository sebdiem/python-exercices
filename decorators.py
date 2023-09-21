"""
Create a decorator that logs the execution time of any function it wraps.

@timeit
def mytest_function():
    print("running…")
    sleep(1)
    print("done")

running this function should print:

    running…
    done
    function "mytest_function" ran in 1.003s
"""
