function [ix, iy] = xy2fig(x, y)
    resolution = 0.2985821417;
    x_left = 12945900.4656558410;
    y_top = 4865780.4241440017; % - resolution * 12512;

    ix = round((x - x_left) / resolution);
    iy = round((y_top - y) / resolution);

end