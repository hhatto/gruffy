:tocdepth: 2

Welcome to Gruffy
=================


What is Gruffy
==============
Gruffy is a yet another Python Graphing Library.
re-implementation to `Gruff`_ (Ruby Graphing Library).

This module using `pgmagick`_ (GraphicsMagick) .

.. _`Gruff`: http://nubyonrails.com/pages/gruff
.. _`Gruffy`: http://pypi.python.org/pypi/gruffy/
.. _`pgmagick`: http://pypi.python.org/pypi/pgmagick/


Documentation
=============
.. toctree::
   :maxdepth: 1

   intro
   api


ScreenShots
===========

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


Code Sample
===========

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


Getting the source
==================
Gruffy's soucecode managed on github_ .

.. _github: http://github.com/hhatto/gruffy

.. code-block:: bash

    git clone git://github.com/hhatto/gruffy.git

- `Gruffy on github`_
- `Gruffy on PyPI`_

.. _`Gruffy on github`: http://github.com/hhatto/gruffy
.. _`Gruffy on PyPI`: http://pypi.python.org/pypi/gruffy/


Other Graph Libraries
=====================

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


Infomation
===========

Contact
-------
Gruffy is written by `Hideo Hattori`_ .
contact the author by e-mail to hhatto.jp@gmail.com .

.. _`Hideo Hattori`: http://www.hexacosa.net/

License
----------
Gruffy is under the MIT License.
see the :file:`LICENSE` file.
