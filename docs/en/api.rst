API Reference
=============

.. module:: gruffy

This is a Gruffy API Reference.


Base Graph Object
-----------------
Baseオブジェクトはすべてのグラフオブジェクトの基本オブジェクトになります。
通常、グラフ作成をする場合には使用することはありません。新しいグラフオブジェクトを作成したい場合に継承して使用してください。

このオブジェクトはグラフのカラーテーマの設定、データの設定、グラフの描画設定、グラフの描画を行います。

.. autoclass:: gruffy.base.Base
   :members:
   :inherited-members:
   :undoc-members:

StackedMixin Object
------------------------
データを積み重ねて表示するグラフを作成したい場合は、このオブジェクトを
他のグラフオブジェクトと一緒に継承してください。
このオブジェクトはデータセットの合計値を算出する
:func:`get_maximum_by_stack` メソッドのみを提供します。

.. autoclass:: gruffy.base.StackedMixin
   :members:


Area Graph Object
----------------------
Areaオブジェクトは面グラフを作成するグラフオブジェクトです。

.. autoclass:: Area
   :members:
   :inherited-members:


Bar Graph Object
---------------------
棒グラフを作成するためのオブジェクトです。

.. autoclass:: Bar
   :members:
   :inherited-members:


Dot Graph Object
---------------------
点グラフを作成するためのオブジェクトです。

.. autoclass:: Dot
   :members:
   :inherited-members:


Line Graph Object
----------------------
折れ線グラフを作成するためのオブジェクトです。

.. autoclass:: Line
   :members:
   :inherited-members:


Pie Graph Object
---------------------
パイグラフを作成するためのオブジェクトです。

.. autoclass:: Pie
   :members:
   :inherited-members:


SideBar Graph Object
-------------------------
横棒グラフを作成するためのオブジェクトです。

.. autoclass:: SideBar
   :members:
   :inherited-members:


Bezier Graph Object
-------------------------
ベジェ曲線グラフを作成するためのオブジェクトです。

.. autoclass:: Bezier
   :members:

AccumulatorBar Graph Object
-------------------------
アキュムレーターグラフを作成するためのオブジェクトです。

.. autoclass:: AccumulatorBar
   :members:

