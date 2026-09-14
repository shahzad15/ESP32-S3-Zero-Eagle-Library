# Waveshare ESP32-S3-Zero Autodesk EAGLE PCB Library (.lbr)

[![EAGLE Compatible](https://img.shields.io/badge/Autodesk%20EAGLE-9.x%20%7C%208.x%20%7C%207.x-blue.svg)](https://www.autodesk.com/products/eagle/overview)
[![Fusion 360 Compatible](https://img.shields.io/badge/Autodesk%20Fusion%20360-Electronics%20Ready-orange.svg)](https://www.autodesk.com/products/fusion-360/overview)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hardware: Waveshare](https://img.shields.io/badge/Hardware-ESP32--S3--Zero-red.svg)](https://docs.waveshare.com/ESP32-S3-Zero)

Official, verified **Autodesk EAGLE** and **Autodesk Fusion 360 Electronics** component library (`.lbr`) for the **Waveshare ESP32-S3-Zero** mini development board.

This library includes a clear schematic symbol with functional pin grouping and two industry-standard PCB footprints: **Through-Hole (TH)** and **Castellated Surface-Mount (SMD)**.

---

## 📸 Component Overview

The **ESP32-S3-Zero** is an ultra-compact mini development board powered by the **Espressif ESP32-S3FH4R2** dual-core Xtensa LX7 processor (240MHz, 2.4GHz Wi-Fi + Bluetooth 5 LE, 4MB Flash, 2MB PSRAM). 

* **Board Dimensions**: 23.50 mm × 18.00 mm
* **Header Pitch**: 2.54 mm (0.1 inch standard breadboard spacing)
* **USB Interface**: Onboard Type-C USB with native USB OTG & USB CDC / JTAG
* **Status Indication**: Onboard WS2812 addressable RGB LED controlled via GPIO 21
* **Antenna**: Ceramic RF chip antenna with ground keepout boundary

---

## 📦 Included Packages & Footprints

| Footprint Variant | EAGLE Package Name | Description & Typical Usage |
| :--- | :--- | :--- |
| **Through-Hole** | `ESP32-S3-ZERO-TH` | Standard 2.54 mm pitch 1.0 mm drill holes with 1.78 mm copper pads. Ideal for pin headers, female socket headers, or breadboard carrier boards. |
| **Castellated SMD** | `ESP32-S3-ZERO-SMD` | Precision castellated edge pads (2.0 mm × 1.4 mm) allowing the ESP32-S3-Zero to be soldered directly flat as a surface-mount daughterboard/module onto custom host PCBs. |

---

## 📍 Pinout & Signal Mapping

| Physical Pin | EAGLE Pin Name | Hardware Description / Alternative Functions |
| :---: | :--- | :--- |
| **1** | `5V` | 5V Power Input (from USB VBUS or External 5V Supply) |
| **2** | `GND` | System Ground Reference |
| **3** | `3V3` | 3.3V Regulated Output (from onboard LDO) |
| **4** | `GP1` | GPIO 1 / ADC1_CH0 / Touch 1 |
| **5** | `GP2` | GPIO 2 / ADC1_CH1 / Touch 2 |
| **6** | `GP3` | GPIO 3 / Strapping Pin |
| **7** | `GP4` | GPIO 4 / ADC1_CH3 / Touch 4 |
| **8** | `GP5` | GPIO 5 / ADC1_CH4 / Touch 5 |
| **9** | `GP6` | GPIO 6 / ADC1_CH5 / Touch 6 |
| **10** | `GP7` | GPIO 7 / ADC1_CH6 / Touch 7 |
| **11** | `GP8` | GPIO 8 / ADC1_CH7 / Touch 8 |
| **12** | `GP9` | GPIO 9 / Strapping Pin |
| **13** | `GP10` | GPIO 10 |
| **14** | `GP11` | GPIO 11 |
| **15** | `GP12` | GPIO 12 |
| **16** | `GP13` | GPIO 13 |
| **17** | `GP14` | GPIO 14 |
| **18** | `GP15` | GPIO 15 / ADC2_CH4 / Touch 14 |
| **19** | `GP16` | GPIO 16 / ADC2_CH5 |
| **20** | `GP17` | GPIO 17 / ADC2_CH6 |
| **21** | `GP18` | GPIO 18 / ADC2_CH7 |
| **22** | `GP19/USB_D-` | GPIO 19 / Native USB D- (Differential Data Negative) |
| **23** | `GP20/USB_D+` | GPIO 20 / Native USB D+ (Differential Data Positive) |
| **24** | `GP21/RGB_LED` | GPIO 21 / Onboard WS2812 Addressable RGB LED Data Pin |
| **25** | `GP38` | GPIO 38 |
| **26** | `GP39` | GPIO 39 |
| **27** | `GP40` | GPIO 40 |
| **43** | `GP43/TXD0` | UART0 Serial Transmit (TXD) Test Pad |
| **44** | `GP44/RXD0` | UART0 Serial Receive (RXD) Test Pad |

---

## 🚀 How to Install & Use

### In Autodesk EAGLE (Version 7.x, 8.x, 9.x):
1. Download or clone this repository:
   ```bash
   git clone https://github.com/shahzad15/ESP32-S3-Zero-Eagle-Library.git
   ```
2. Copy `ESP32-S3-Zero.lbr` to your EAGLE libraries directory:
   * **Windows**: `C:\Users\<YourUsername>\Documents\EAGLE\libraries\`
   * **macOS / Linux**: `~/Documents/EAGLE/libraries/`
3. Open Autodesk EAGLE Control Panel:
   * Go to **Libraries** -> right click `ESP32-S3-Zero.lbr` -> click **Use** (turns dot green).
   * Or type in the EAGLE command bar:
     ```text
     USE ESP32-S3-Zero.lbr;
     ```
4. In your schematic editor, click **Add Component** (`Shift + A` or type `ADD *ESP32-S3-ZERO*`):
   * Select `ESP32-S3-ZERO`
   * Choose variant:
     * **`-TH`**: For standard header pin assembly
     * **`-SMD`**: For surface-mount carrier board soldering

### In Autodesk Fusion 360 (Electronics Workspace):
1. In Fusion 360 Electronics, open **Library Manager**.
2. Click **Add from disk / In Use** tab -> browse and select `ESP32-S3-Zero.lbr`.
3. Add the part into your schematic design.

---

## 📐 PCB Layout & Routing Best Practices

1. **RF Antenna Keepout**:
   * Do **NOT** route copper traces, polygon ground pours, or component pads directly underneath the ceramic chip antenna region at the bottom edge of the board.
   * Keep this zone free of ground planes across all PCB layers to avoid RF signal attenuation.
2. **Decoupling Capacitors**:
   * While the ESP32-S3-Zero includes onboard regulation, place a `10µF` and `0.1µF` ceramic capacitor close to the `5V` and `3V3` power pins on your carrier board for maximum power rail stability.
3. **Thermal Considerations**:
   * If running dual-core 240MHz with Wi-Fi transmitting at peak power (+20dBm), ensure adequate air circulation or thermal vias beneath the carrier PCB.

---

## 📄 License

This library is open-sourced under the **[MIT License](LICENSE)**. You are free to use it in personal, educational, and commercial PCB designs without restriction.

---

## 🤝 Contributing & Bug Reports

Contributions, pinout enhancements, and 3D step model integrations are welcome! Feel free to open an Issue or submit a Pull Request.

*Maintained by [@shahzad15](https://github.com/shahzad15).*
