def magic_square(n):
  magicSquare = [[0 for x in range(n)]
                      for y in range(n)]
  
  i = n//2
  j = n-1
  
  num = 1
  while num <= n*n:
    if i == -1 and j == n:
      j = n-2
      i = 0
    else:
      if j == n:
        j = 0
      if i < 0:
        i = n-1
        
    if magicSquare[i][j]:
      j -= 2
      i += 1
      continue
    else:
      magicSquare[i][j] = num
      num += 1
      
    j += 1
    i -= 1
  
  return magicSquare


n = int(input("마방진의 크기를 선택하세요 : "))
print("마방진 크기", n, "x", n, "은: ")
for i in magic_square(n):
    print(*i)