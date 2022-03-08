# 3D Magnetic Lines with blender

Does this:

![First time getting it working](./3DMagneticLines.png)

<video controls width="100%">
<source src="./animation.avi" type="video/avi"> 
</video>

[On Youtube](https://youtu.be/B3bTxSRhlVY)

## How to use
Run the `AddUIPanel.py` script in the text editor of the example `.blend` file -- then use the magnetic lines panel added to the object properties (object properties is the cube icon amongst the buttons screen-division, as shown in the screenshot above). To use with a new blender project, open all the `.py` files in the text editor, then run `AddUIPanel.py` to add the magnetic lines panel to the object properties.

[How It Works](./howItWorks.md)

## Disclaimer
The math is not the scientifically accurate math for magnets. This project is primarily just for visualization. The project just uses the inverse _square_ law. I learned after making the project that it would probably be more appropriate if it used the inverse _cube_ law.