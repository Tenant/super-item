% Data Interface Demo
% Variable Definitions:
%   lon: trajectory longtitude, or trajectory global x, size [1, nums]
%   lat: trajecotry latitude, or trajectory global y, size [1, nums]
%   val: point lables, size [1, nums]
%   You can use your data, as well as the above format is satisfied
  
data = readtable("F:/KYXZ2020/G/data/data_20201011/data-6/Camera/光照条件复杂度标注结果文件.csv");
gps = readtable("F:/KYXZ2020/G/data/data_20201011/data-6/Camera/GPS定位复杂度标注结果文件.csv");
lon = gps.longitude';
lat = gps.latitude';
val = data.label';
lab = calc_label(val);

% You dont need to modify the following code
  
alt = zeros(size(lon));

figure; hold on; box on; axis equal; axis off

surface([lon;lon], [lat;lat], [alt;alt], [lab;lab], ...
    'facecolor', 'none',...
    'EdgeColor', 'interp',...
    'LineWidth', 6)
colormap('JET')
caxis([0 12])

% 设置绘图参数
set(gcf, 'Position', [100, 100, 800, 600], 'color', [1, 1, 1])
set(gca, 'Fontname', 'Times New Roman', 'FontSize',20, 'position', [0.1,0.1,0.9,0.9])

% 保存绘图结果
% saveas(gcf, 'result.png')

function label = calc_label(value)
    if min(value) ~= max(value)
        min_value = min(value);
        max_value = max(value);
        label = (value - min_value) ./ (max_value - min_value) * 10;
    else
        label = value;
    end
end
