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

StackedMixinオブジェクト
------------------------
データを積み重ねて表示するグラフを作成したい場合は、このオブジェクトを
他のグラフオブジェクトと一緒に継承してください。
このオブジェクトはデータセットの合計値を算出する
:func:`get_maximum_by_stack` メソッドのみを提供します。

.. autoclass:: gruffy.base.StackedMixin
   :members:
   :inherited-members:


Areaグラフオブジェクト
----------------------
Areaオブジェクトは面グラフを作成するグラフオブジェクトです。

.. autoclass:: Area
   :members:


Barグラフオブジェクト
---------------------
棒グラフを作成するためのオブジェクトです。

.. autoclass:: Bar
   :members:


Dotグラフオブジェクト
---------------------
点グラフを作成するためのオブジェクトです。

.. autoclass:: Dot
   :members:


Lineグラフオブジェクト
----------------------
折れ線グラフを作成するためのオブジェクトです。

.. autoclass:: Line
   :members:


Pieグラフオブジェクト
---------------------
パイグラフを作成するためのオブジェクトです。

.. autoclass:: Pie
   :members:


SideBarグラフオブジェクト
-------------------------
横棒グラフを作成するためのオブジェクトです。

.. autoclass:: SideBar
   :members:

