# Least-squares-method

## Description

Python及びMATLABによる最小二乗法。

排ガス規制対応のため、A/Fを計測することになったのだが、以下の課題有り。

・LAFセンサの物理値(A/F)そのものがECUからゲットできない。
	(ECU側で物理値変換していない？)
・LAFセンサの特性はリニアと思いきや、それほどリニアではない。
・LAF(Linear Air Fuel ratio)という名前がついている割には全然リニアじゃない
・複数のセンサ特性が存在。
・特性テーブルはあるので、線形補間型のテーブル変換でも良いが、使用している計測器の変換テーブル点数がそれほど多くなく・・・。つまり点数が全然足りない。。。

というわけで、LAFセンサの特性を2次関数で同定してみて、なんとか辻褄を合わせる。
※ 2次関数の変換式を挟むことはできる。

## Detailed description

Python版の詳細説明
https://www.simulationroom999.com/blog/python-laf-sensor-characteristic/

MATLAB版の詳細説明
https://www.simulationroom999.com/blog/matlab-laf-sensor-characteristic/
