# OctoPrint-PrusaSlowPurgeTower

Slows down the purge wipe on the colour change tower to help with toothpaste stripe smearing or issues with bridging and failed wipe towers.

I was getting a clean looking result before the melt zone was properly purged printing at the high speed prusa uses as only the core of the filament is extruding.  Printing slower tries to allow the whole melt zone pool to be purged more easily.

Also if you are having trouble with failing prime towers because of the speed this will help.

The plugin will limit the feedrates on the X and Y axis for the purge of the new colour into the purge tower.  It sets the limit after the tool change and only during the extrusion of the new filament.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/BoyStot/OctoPrint-PrusaSlowPurgeTower/archive/master.zip

## Configuration

Add the following into PrusaSlicer->Printer Settings->Custom GCode->Start-Gcode.

    ;PURGESPEED:[external_perimeter_speed]

Any of your speed tags can be used or you can enter your own number.

    ;PURGESPEED:30
