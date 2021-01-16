def in_common(a: str, b: str) -> str:
    shared: List[str] = []

    splatted_a = a.split()
    splatted_b = b.split()

    for item in splatted_a:
        if item in splatted_b:
            shared.append(item)

    return ' '.join(shared)


a: str = 'Hot Chicks Realize The Deep Dark Fantasies And Shows Their Pussies'
b: str = 'Finger In My Ass Deep Dark Fantasies With Leather Man'

print(in_common(a, b))
