# Author: shahzad15
# Description: Generates the 3D Parametric CAD Model of Waveshare ESP32-S3-Zero in Autodesk Fusion 360

import adsk.core
import adsk.fusion
import traceback
import os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active Fusion 360 design! Please open or create a design first.')
            return

        rootComp = design.rootComponent

        # Create occurrences / component
        trans = adsk.core.Matrix3D.create()
        occ = rootComp.occurrences.addNewComponent(trans)
        newComp = occ.component
        newComp.name = "Waveshare_ESP32_S3_Zero"

        sketches = newComp.sketches
        xyPlane = newComp.xYConstructionPlane
        xzPlane = newComp.xZConstructionPlane

        # 1. PCB Base Sketch (18.0 mm x 23.5 mm)
        pcbSketch = sketches.add(xyPlane)
        lines = pcbSketch.sketchCurves.sketchLines
        # Centered on X: -9.0 to +9.0 mm; Y: 0.0 to 23.5 mm (Fusion uses cm: -0.9 to 0.9, 0.0 to 2.35)
        rect = lines.addTwoPointRectangle(
            adsk.core.Point3D.create(-0.9, 0.0, 0.0),
            adsk.core.Point3D.create(0.9, 2.35, 0.0)
        )

        # 2. Add Header Through-Hole Circles (9 on Left, 9 on Right, pitch 2.54 mm = 0.254 cm)
        circles = pcbSketch.sketchCurves.sketchCircles
        y_start = 0.254
        pitch = 0.254
        hole_rad = 0.05 # 1.0 mm drill dia = 0.05 cm radius
        for i in range(9):
            y = y_start + i * pitch
            # Left pin hole
            circles.addByCenterRadius(adsk.core.Point3D.create(-0.762, y, 0.0), hole_rad)
            # Right pin hole
            circles.addByCenterRadius(adsk.core.Point3D.create(0.762, y, 0.0), hole_rad)

        # Extrude PCB Base (thickness 1.2 mm = 0.12 cm)
        prof = pcbSketch.profiles.item(0)
        extrudes = newComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(0.12)
        extInput.setDistanceExtent(False, distance)
        pcbExtrude = extrudes.add(extInput)
        pcbBody = pcbExtrude.bodies.item(0)
        pcbBody.name = "PCB_Substrate"

        # 3. USB-C Receptacle (Width 8.94 mm, Length 7.35 mm, Height 3.2 mm)
        # Sits on top of PCB at Y=23.5 mm, extends to Y=24.5 mm
        usbSketch = sketches.add(xyPlane)
        usbSketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(-0.447, 1.715, 0.12),
            adsk.core.Point3D.create(0.447, 2.45, 0.12)
        )
        usbProf = usbSketch.profiles.item(0)
        usbExtInput = extrudes.createInput(usbProf, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        usbHeight = adsk.core.ValueInput.createByReal(0.32)
        usbExtInput.setDistanceExtent(False, usbHeight)
        usbExt = extrudes.add(usbExtInput)
        usbBody = usbExt.bodies.item(0)
        usbBody.name = "USB_C_Receptacle"

        # 4. ESP32-S3 SoC / Shield (7.0 mm x 7.0 mm x 0.9 mm)
        socSketch = sketches.add(xyPlane)
        socSketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(-0.35, 0.8, 0.12),
            adsk.core.Point3D.create(0.35, 1.5, 0.12)
        )
        socProf = socSketch.profiles.item(0)
        socExtInput = extrudes.createInput(socProf, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        socHeight = adsk.core.ValueInput.createByReal(0.09)
        socExtInput.setDistanceExtent(False, socHeight)
        socExt = extrudes.add(socExtInput)
        socBody = socExt.bodies.item(0)
        socBody.name = "ESP32_S3_SoC"

        # 5. Ceramic RF Antenna (3.2 mm x 1.6 mm x 1.2 mm at bottom edge)
        antSketch = sketches.add(xyPlane)
        antSketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(-0.16, 0.05, 0.12),
            adsk.core.Point3D.create(0.16, 0.21, 0.12)
        )
        antProf = antSketch.profiles.item(0)
        antExtInput = extrudes.createInput(antProf, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        antHeight = adsk.core.ValueInput.createByReal(0.12)
        antExtInput.setDistanceExtent(False, antHeight)
        antExt = extrudes.add(antExtInput)
        antBody = antExt.bodies.item(0)
        antBody.name = "Ceramic_Antenna"

        # 6. BOOT and RESET Tactile Buttons
        # BOOT (Left)
        btn1Sketch = sketches.add(xyPlane)
        btn1Sketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(-0.68, 1.95, 0.12),
            adsk.core.Point3D.create(-0.48, 2.15, 0.12)
        )
        btn1Prof = btn1Sketch.profiles.item(0)
        btn1ExtInput = extrudes.createInput(btn1Prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        btn1Height = adsk.core.ValueInput.createByReal(0.10)
        btn1ExtInput.setDistanceExtent(False, btn1Height)
        btn1Ext = extrudes.add(btn1ExtInput)
        btn1Body = btn1Ext.bodies.item(0)
        btn1Body.name = "BOOT_Button"

        # RESET (Right)
        btn2Sketch = sketches.add(xyPlane)
        btn2Sketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(0.48, 1.95, 0.12),
            adsk.core.Point3D.create(0.68, 2.15, 0.12)
        )
        btn2Prof = btn2Sketch.profiles.item(0)
        btn2ExtInput = extrudes.createInput(btn2Prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        btn2Height = adsk.core.ValueInput.createByReal(0.10)
        btn2ExtInput.setDistanceExtent(False, btn2Height)
        btn2Ext = extrudes.add(btn2ExtInput)
        btn2Body = btn2Ext.bodies.item(0)
        btn2Body.name = "RESET_Button"

        # 7. WS2812B RGB LED (2.0 mm x 2.0 mm x 0.8 mm)
        ledSketch = sketches.add(xyPlane)
        ledSketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(-0.45, 1.55, 0.12),
            adsk.core.Point3D.create(-0.25, 1.75, 0.12)
        )
        ledProf = ledSketch.profiles.item(0)
        ledExtInput = extrudes.createInput(ledProf, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ledHeight = adsk.core.ValueInput.createByReal(0.08)
        ledExtInput.setDistanceExtent(False, ledHeight)
        ledExt = extrudes.add(ledExtInput)
        ledBody = ledExt.bodies.item(0)
        ledBody.name = "WS2812B_RGB_LED"

        # Export STEP automatically if export manager available
        try:
            exportMgr = design.exportManager
            out_folder = r"C:\Users\shahzad\Documents\ai forlder\EaglePCB\my designed lib\ESP32-S3-Zero"
            if os.path.exists(out_folder):
                step_file = os.path.join(out_folder, "ESP32-S3-Zero.step")
                stepOptions = exportMgr.createSTEPExportOptions(step_file, newComp)
                exportMgr.execute(stepOptions)
        except:
            pass

        ui.messageBox('Waveshare ESP32-S3-Zero 3D Model created successfully in Fusion 360!')

    except Exception:
        if ui:
            ui.messageBox('Failed to create model:\n{}'.format(traceback.format_exc()))
