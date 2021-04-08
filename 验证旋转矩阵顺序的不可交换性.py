import numpy as np

def construct_R(rot_x, rot_y, rot_z):
    sa, ca = np.sin(rot_x), np.cos(rot_x)
    sb, cb = np.sin(rot_y), np.cos(rot_y)
    sg, cg = np.sin(rot_z), np.cos(rot_z)

    cc_r1 = cb * cg
    cc_r2 = cg * sa * sb - ca * sg
    cc_r3 = sa * sg + ca * cg * sb
    cc_r4 = cb * sg
    cc_r5 = sa * sb * sg + ca * cg
    cc_r6 = ca * sb * sg - cg * sa
    cc_r7 = -sb
    cc_r8 = cb * sa
    cc_r9 = ca * cb

    return np.array([cc_r1, cc_r2, cc_r3, cc_r4, cc_r5, cc_r6, cc_r7, cc_r8, cc_r9]).reshape(3, 3)

def rotate_with_R(pt, R):
    return np.matmul(R, pt)

def demo_1():
    '''
    空间中同一个点在不同坐标系下的坐标经由同一个旋转矩阵变换后所得坐标不一定对应同一个点
    说明旋转矩阵的表达与坐标系的定义有关

    其数学证明为 R1 * (R0 * pt) != R0 * (R1 * pt) 矩阵乘法不满足交换律
    '''
    pt = [3, 5, 2]
    pt1 = np.array(pt).reshape(3,1)
    R0 = construct_R(1.57, 0.98, 1.02)
    t0 = np.array([0, 0, 0]).reshape(3,1)
    pt2 = rotate_with_R(pt1, R0)

    R = construct_R(0.5 * np.pi, 1.34, 0.24)
    pt1_d = rotate_with_R(pt1, R)
    pt2_d = rotate_with_R(pt2, R)
    
    pt1_dd = rotate_with_R(pt1_d, R0)
    print(pt2_d - pt1_dd)

if __name__ == '__main__':
    demo_1()

