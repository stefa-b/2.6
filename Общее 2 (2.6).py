def foo(items):
    return {v: k for k, v in items}
n = 10
d = {i: f'{i}' for i in range(n)}
new_d = foo(d.items())
print(d)
print(new_d)