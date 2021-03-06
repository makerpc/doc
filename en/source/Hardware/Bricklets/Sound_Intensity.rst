
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Sound Intensity Bricklet
:shoplink: ../../../shop/bricklets/sound-intensity-bricklet.html

.. include:: Sound_Intensity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _sound_intensity_bricklet:

Sound Intensity Bricklet
========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_sound_intensity_tilted_350.jpg",
	               "Bricklets/bricklet_sound_intensity_tilted_600.jpg",
	               "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_vertical_100.jpg",
	             "Bricklets/bricklet_sound_intensity_vertical_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_horizontal_100.jpg",
	             "Bricklets/bricklet_sound_intensity_horizontal_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_tilted_back_100.jpg",
	             "Bricklets/bricklet_sound_intensity_tilted_back_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_sound_intensity_case_tilted_100.jpg",
	             "Cases/bricklet_sound_intensity_case_tilted_600.jpg",
	             "Sound Intensity Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_brickv_100.jpg",
	             "Bricklets/bricklet_sound_intensity_brickv.jpg",
	             "Sound Intensity Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/sound_intensity_bricklet_dimensions_100.png",
	             "Dimensions/sound_intensity_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures sound intensity
* 12bit resolution
* Usable as clapping switch, alarm system sensor, etc.


.. _sound_intensity_bricklet_description:

Description
-----------

The Sound Intensity :ref:`Bricklet <primer_bricklets>` is equipped
with a microphone capsule and can be used to measure loudness by
:ref:`Bricks <primer_bricks>`. The returned value corresponds to the 
`upper envelop <http://en.wikipedia.org/wiki/Envelope_(waves)>`__
of the signal of the microphone capsule.

It is possible to configure events that are triggered if a specified
threshold of loudness is exceeded.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        12bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 30 x 9mm (0.98 x 1.18 x 0.35")
Weight                            4g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/sound-intensity-bricklet/raw/master/hardware/sound-intensity-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/sound_intensity_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/sound-intensity-bricklet/zipball/master>`__)


.. _sound_intensity_bricklet_test:

Test your Sound Intensity Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the changing sound
intensity.

.. image:: /Images/Bricklets/bricklet_sound_intensity_brickv.jpg
   :scale: 100 %
   :alt: Sound Intensity Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_intensity_brickv.jpg

|test_pi_ref|

.. _sound_intensity_bricklet_case:

Case
----

A `laser-cut case for the Sound Intensity Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-sound-intensity-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_sound_intensity_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_sound_intensity_case_tilted_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw Bricklet to top plate with spacers at the bottom and long screws from the top,
* build up side plates,
* plug side plates into top plate and
* screw bottom plate to bottom spacers.

Below you can see an exploded assembly drawing of the Temperature IR Bricklet case:

.. image:: /Images/Exploded/sound_intensity_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Exploded/sound_intensity_exploded.png

|bricklet_case_hint|


.. _sound_intensity_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Sound_Intensity_hlpi.table
