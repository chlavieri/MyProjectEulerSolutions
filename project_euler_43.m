clc; clear;
format long g
string_num = '0123456789';
permuts_str = perms(string_num);

permuts_str = permuts_str(permuts_str(:,1) ~= '0', :);
%disp(permuts_str);
pandigital = [];

for i = 1:length(permuts_str)
    num = permuts_str(i, :);
    num2to4 = str2double(num(2:4));
    num3to5 = str2double(num(3:5));
    num4to6 = str2double(num(4:6));
    num5to7 = str2double(num(5:7));
    num6to8 = str2double(num(6:8));
    num7to9 = str2double(num(7:9));
    num8to10 = str2double(num(8:10));
    nums = [num2to4 num3to5 num4to6 num5to7 num6to8 num7to9 num8to10];
    if (mod(nums(1),2) == 0 && mod(nums(2),3) == 0 && ...
            mod(nums(3),5) == 0 && mod(nums(4), 7) == 0 && ...
            mod(nums(5), 11) == 0 && mod(nums(6), 13) == 0 && ...
            mod(nums(7), 17) == 0)
        pandigital = [pandigital str2double(num)];
    end

end

disp(sum(pandigital));