function [x, y] = lb2xy(l, b)

    x = l * 20037508.3427892 / 180;
    y  = log(tan((90 + b) * pi / 360)) / (pi / 180);
    y = y * 20037508.3427892 / 180;

end