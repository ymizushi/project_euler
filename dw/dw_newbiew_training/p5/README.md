# Problem 5

```
Expedition
トラックで距離Lの道を移動します。はじめトラックにはガゾリンがP積まれています。このトラックは距離1走るとガソリンが1消費されます。途中でガソリンが0になってしまうとトラックは停止してしまい、移動に失敗してしまいます。途中にはN個ガソリンスタンドがあります。各ガソリンスタンドiは道のスタート地点から距離Aiの地点にあって、Biだけガソリンを補給することができます。トラックの燃料タンクの容量に制限はなく、いくらでもガソリンを補給することができます。トラックは移動を完了できるでしょうか？またそのその際、最小で何回のガソリンの補給が必要でしょうか？完了できる場合は最小の補給回数を、出きない場合は-1を出力して下さい。

制約
1 ≦ N ≦ 10000
1 ≦ L ≦ 1000000, 1 ≦ P ≦ 1000000
1 ≦ Ai < L, 1 ≦ Bi ≦ 100
入力
N = 4
L = 25
P = 10
A = {10, 14, 20, 21}
B = {10, 5, 2, 4}
出力
2 (１つめと2つめのガソリンスタンドで補給)



計算チャレンジ
N = 100
L = 5000
P = 100
A = {1, 76, 138, 155, 243, 260, 335, 435, 498, 536, 564, 594, 602, 636, 695, 744, 750, 838, 869, 966, 1053, 1072, 1108, 1184, 1225, 1271, 1342, 1376, 1391, 1432, 1487, 1541, 1635, 1697, 1755, 1794, 1799, 1812, 1822, 1836, 1860, 1951, 1964, 1997, 2015, 2056, 2057, 2123, 2132, 2187, 2213, 2284, 2373, 2412, 2451, 2530, 2610, 2657, 2734, 2760, 2856, 2912, 3003, 3050, 3070, 3098, 3148, 3223, 3302, 3400, 3432, 3510, 3586, 3604, 3607, 3622, 3713, 3754, 3807, 3848, 3920, 4012, 4085, 4091, 4159, 4227, 4260, 4354, 4360, 4388, 4406, 4426, 4441, 4535, 4623, 4687, 4760, 4824, 4854, 4880}
B = {70, 31, 45, 45, 48, 61, 87, 52, 89, 26, 2, 51, 24, 91, 2, 11, 46, 82, 78, 26, 85, 81, 100, 64, 70, 19, 71, 8, 52, 87, 36, 73, 38, 63, 55, 87, 52, 91, 25, 58, 10, 47, 9, 21, 81, 27, 56, 58, 70, 74, 42, 85, 58, 85, 99, 79, 4, 85, 68, 71, 11, 60, 40, 53, 49, 4, 37, 73, 24, 28, 95, 60, 67, 81, 31, 9, 39, 81, 91, 74, 39, 42, 81, 73, 100, 37, 16, 53, 98, 17, 52, 29, 75, 20, 67, 62, 26, 11, 29, 71}
```
