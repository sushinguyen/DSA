def sap_xep_hoc_sinh(ds):
    n = len(ds)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if ds[j][1] < ds[min_idx][1]:
                min_idx = j
        ds[i], ds[min_idx] = ds[min_idx], ds[i]
    return ds

hoc_sinh = [('An', 8), ('Ba', 5), ('Ca', 7), ('Da', 3)]
print(sap_xep_hoc_sinh(hoc_sinh))

