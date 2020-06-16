INPUT_STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
tar_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}

arr = INPUT_STR.split()
for (i, _) in enumerate(arr):
    j = i + 1
    if j in tar_num:
        ans[arr[i][0:1]] = j
    else:
        ans[arr[i][0:2]] = j
print(ans)
