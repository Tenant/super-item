源码：
```c++
# include <cstdio>

FILE* fp;
float _imu_rot[3], _imu_shv[3];
fp = fopen("imu.calib", "r");
fscanf(fp, "%*s %f %f %f", &_imu_rot[0], &_imu_rot[1], &_imu_rot[2]);
fscanf(fp, "%*s %f %f %f", &_imu_shv[0], &_imu_shv[1], &_imu_shv[2]);
fclose(fp);

fp = fopen(setting->value("Calib/velo_calib").toString().toStdString().c_str(), "r");
fscanf(fp, "%*s %f %f %f", &_velo_rot[0], &_velo_rot[1], &_velo_rot[2]);
fscanf(fp, "%*s %f %f %f", &_velo_shv[0], &_velo_shv[1], &_velo_shv[2]);
fclose(fp);
```

数据文件：
```bash
rot 0.00 0.00 0.00
shv -0.50 0.07 1.98
```

```c++
#include <QSettings>

float dd[3];
int tt[3];

QSetting* setting = new QSettings(filename, QSettings::IniFormat, this);
QString item0 = setting->value("/Category0/item0", "").toString();
QStringList colorValue = setting->value("Category1/item1").toStringList();
float dd = item1[0].toFloat();
tt[0] = item1[1].toInt();
```

```bash
[Category0]
item0=""
[Category1]
item1=3.13,0,0
```
