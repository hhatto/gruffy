:tocdepth: 2

Gruffyへようこそ
================


Gruffyとは？
============
`Gruffy`_ はPythonのグラフ作成モジュールの一つです。
Rubyで実装された `Gruff`_ のPythonによる実装です。

Gruffy を使用するには `pgmagick`_ モジュールが必要です。

.. _`Gruff`: http://nubyonrails.com/pages/gruff
.. _`Gruffy`: http://pypi.python.org/pypi/gruffy/
.. _`pgmagick`: http://pypi.python.org/pypi/pgmagick/


ドキュメント
============
.. toctree::
   :maxdepth: 1

   intro
   api


グラフの作成例
==============
.. gruffy::
   :title: Gruffy's Graph
   :width: 500
   :type: Area

    transparent = True
    data("Apples", [1, 2, 3, 4, 4, 3])
    data("Oranges", [4, 8, 7, 9, 8, 9])
    data("Watermelon", [2, 3, 1, 5, 6, 8])
    data("Peaches", [9, 9, 10, 8, 7, 9])
    labels = {0: '2003', 2: '2004', 4: '2005.09'}

.. gruffy::
   :title: Gruffy's Graph
   :width: 500
   :type: StackedSideBar

    theme_pastel()
    transparent = True
    data("Apples", [1, 2, 3, 4, 4, 3])
    data("Oranges", [4, 8, 7, 9, 8, 9])
    data("Watermelon", [2, 3, 1, 5, 6, 8])
    data("Peaches", [9, 9, 10, 8, 7, 9])
    labels = {0: '2003', 2: '2004', 4: '2005.09'}




サンプルコード
==============

.. code-block:: python

    from gruffy import Area

    g = Area()
    g.title = "Gruffy's Graph"
    g.transparent = True

    g.data("Apples", [1, 2, 3, 4, 4, 3])
    g.data("Oranges", [4, 8, 7, 9, 8, 9])
    g.data("Watermelon", [2, 3, 1, 5, 6, 8])
    g.data("Peaches", [9, 9, 10, 8, 7, 9])

    g.labels = {0: '2003', 2: '2004', 4: '2005.09'}

    g.write()


ソースコード
============
Gruffyのソースコードは github_ で管理しています。

.. _github: http://github.com/

- `Gruffy Source Code via Git`_
- `Gruffy on PyPI`_

.. _`Gruffy Source Code via Git`: http://github.com/hhatto/gruffy
.. _`Gruffy on PyPI`: http://pypi.python.org/pypi/gruffy/


他のグラフモジュール
====================
Gruffy以外の選択肢として以下のモジュールがありますので、
もし必要であれば試してみてください。

- matplotlib_
- pyOFC2_
- Graphy_
- `Python Google Chart`_
- Pycha_
- Pychart_
- RPy_

.. _matplotlib: http://matplotlib.sourceforge.net/
.. _pyOFC2: http://btbytes.github.com/pyofc2/
.. _Graphy: http://zovirl.com/2009/05/26/graphy-a-chart-library-for-python/
.. _Pycha: http://bitbucket.org/lgs/pycha/wiki/Home
.. _Pychart: http://home.gna.org/pychart/
.. _`Python Google Chart`: http://pygooglechart.slowchop.com/
.. _RPy: http://rpy.sourceforge.net/


その他の情報
============

連絡先
------
Gruffyは服部 英夫(Hideo Hattori)が作成しました。

Gruffyに関する質問、問題報告等があれば hhatto.jp@gmail.com にメールを送付してください。

ライセンス
----------
GruffyはMITライセンスのもとに使用が可能です。

