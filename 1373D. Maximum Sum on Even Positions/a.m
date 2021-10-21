sobrante = 2e5;
clc
it = 0;
while true
    it = it + 1;
    T = 1;
    data = [];
    for i = 1:randi(10)
        [val, sobrante] = getRand(sobrante);
        %
        % if sobrante < 0
        %     break
        % end
        
        data = [data val];
    end
    
    disp(numel(data))
    disp(data)
    fid = fopen('a.txt', 'w');
    fprintf(fid, '1\n');
    fprintf(fid, '%d\n',numel(data));
    fprintf(fid, '%d ',data');
    fprintf(fid, '\n');
    fclose(fid);
    drawnow
    !python go2.py <a.txt >b.txt
    drawnow
    data2 = fileread('b.txt');
    resp = strsplit(data2, '\r\n');
    
    [bR data2R] = solve(data);
    if str2double(resp{1}) ~= bR
        it
        beep
        break
        
    end
end
function [val, sobrante] = getRand(sobrante)
% maxVal = uint64(1e9);
maxVal = 10;
val = randi(maxVal);
% sobrante = sobrante - val;
end

function [maxResp data2R] = solve(data)
n = numel(data);
maxResp  = 0;
for i = 1:n
    for j = i:n
        data2 = data;
        data2(i:j) = data2(j:-1:i);
        
        resp = sum(data2(1:2:end));
        if resp > maxResp
            maxResp = resp;
            data2R = data2;
        end
    end
end

disp(data2R);
end