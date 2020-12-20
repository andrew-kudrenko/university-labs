Program lab6z;
const n1=20;
var
  input: array [1..n1] of integer;
  a: array[1..n1,1..n1] of integer;
  n,i,j,c,k: integer;
begin
  repeat
    write('Введите размер матрицы n: ');
    readln(n);
  until n<=20; 
  
  for i := 1 to n * n do
  begin
    write('> ');
    readln(input[i]);
  end;
  
  i:=1; j:=1; c:=0; k:=0;
  repeat   
    while (k<n*n)and(j<=n-c) do
    begin
      a[i,j]:=input[k + 1];
      inc(j);
      inc(k);
    end;    
    inc(i); dec(j);
    while (k<n*n)and(i<=n-c) do
    begin
      a[i,j]:=input[k + 1];
      inc(i);
      inc(k);
    end;   
    dec(j); dec(i);
    while (k<=n*n)and(j>=1+c) do
    begin
      a[i,j]:=input[k + 1];
      dec(j);
      inc(k);
    end;   
    inc(c); inc(j); dec(i);
    while (k<=n*n)and(i>=1+c) do
    begin
      a[i,j]:=input[k + 1];
      dec(i);
      inc(k);
    end;
    inc(j); inc(i);
  until k>=n*n;
  for i:=1 to n do
  begin
    for j:=1 to n do
      write(a[i,j]:4);
    writeln;
  end;
end.
