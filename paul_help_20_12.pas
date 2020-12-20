var f,g:text;
s:string;
i:byte;

procedure del(var s:string; i:byte; var f,g:text);
begin
while not eof(f) do
begin
readln(f,s);
i:=length(s);
while (length(s) > 0) and (s[i]<>' ') do
begin
delete(s,i,1);
i:=i-1;
end;
delete(s,length(s),1);
writeln(g,s);
end;
end;

begin
var inputFilename := 'file1.txt';

if not FileExists(inputFilename) then
begin
  writeln('Ошибка! Файл ', inputFilename, ' не существует');
  halt();  
end;

assign(f, inputFilename);
reset(f);
assign(g,'file2.txt');
rewrite(g);

del(s,i,f,g);

close(f);
close(g);

write('Файл преобразован');
readln
end.
