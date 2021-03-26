% 加载数据并获取数据信息
nums = size(GPS, 1);

ixes = [];
iyes = [];
xes = [];
yes = [];
for idx = 1:10:nums
    [x, y] = lb2xy(GPS.longitude(idx), GPS.latitude(idx));
    [ix, iy] = xy2fig(x, y);
    xes = [xes, x];
    yes = [yes, y];
    ixes = [ixes, ix];
    iyes = [iyes, iy];    
end

map = geotiffread('map.tif');

figure
set(gcf, 'color', 'w', 'position',[100 100 500 625])
set(gca, 'position',[0 0 1 1])
hold on
axis off
box on
axis equal
axis([1000 5800 500 6500])

imshow(map)
patch([1000, 1000, 5800, 5800], [500, 6500,  6500, 500], 'white', 'FaceAlpha', 0.7)
plot(ixes, iyes, 'r-', 'LineWidth', 1.5)