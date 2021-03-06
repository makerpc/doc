
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Debug Brick
:shoplink: ../../../shop/bricks/debug-brick.html

.. _debug_brick:

Debug Brick
===========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_debug_tilted_front_350.jpg",
	               "Bricks/brick_debug_tilted_front_600.jpg",
	               "Debug Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_debug_tilted_back_100.jpg",
	             "Bricks/brick_debug_tilted_back_600.jpg",
	             "Debug Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_debug_top_100.jpg",
	             "Bricks/brick_debug_top_600.jpg",
	             "Debug Brick top")
	}}
	{{
	    tfdocimg("Bricks/brick_debug_bottom_100.jpg",
	             "Bricks/brick_debug_bottom_600.jpg",
	             "Debug Brick bottom")
	}}
	{{
	    tfdocimg("Dimensions/debug_brick_dimensions_100.png",
	             "Dimensions/debug_brick_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* For Firmware Developers
* JTAG and serial console


.. _debug_brick_description:

Description
-----------

The Debug Brick can be used to add JTAG and serial console debug capabilities
to :ref:`Bricks <primer_bricks>`,
:ref:`Bricklets <primer_bricklets>` and :ref:`stacks <primer_stack>`.

.. note::
 You only need the Debug Brick if you want to debug the low level C firmware
 of Bricks or Bricklets. It does not add any features for PC based programming.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions (W x D x H)            40 x 40 x 8mm (1.57 x 1.57 x 0.31")*
Weight                            18g
================================  ============================================================

\* without connectors


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/debug-brick/raw/master/hardware/debug-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/debug_brick_dimensions.png>`__)
* Design files (`Download <https://github.com/Tinkerforge/debug-brick/zipball/master>`__)


Known Bugs
----------

Debug Brick Hardware Version 1.1 has a design flaw. GND pins of the JTAG 
connector are not connected. This can lead to debug problems when using the
JTAG interface. The serial console is not affected. The problem can be fixed
by soldering a wire from a GND pin of the JTAG connector to a GND pad on the
board. This issue will be fixed with the next hardware version. 

.. image:: /Images/Bricks/brick_debug_wire_fix_350.jpg
   :scale: 100 %
   :alt: Debug Brick with Wire
   :align: center
   :target: ../../_images/Bricks/brick_debug_wire_fix_1000.jpg


