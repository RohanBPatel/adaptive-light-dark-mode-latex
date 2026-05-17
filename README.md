# Adaptive Light/Dark Mode for LaTeX

After spending many hours in VSCode typing up homework assignments, I found the constant white background of default LaTeX documents annoying. I created this script as a simple solution to dynamically adjust document aesthetics for a more comfortable experience.

The `Color.tex` script provides a one-line include for LaTeX documents to automatically adjust their background and text colors based on the hour and minute of day. By default, it transitions from light, paper-like tones during the day to high-contrast, warm dark modes at night.

**[Interactive Version in Desmos](https://www.desmos.com/calculator/spybafvetz)**

## File Structure

- `Color.tex`: The core logic file that calculates color weights and HSV values.
- `Color_Example.tex` and `Color_Example.pdf`: A demonstration of basic usage and manual hour setting.
- `generate_hours.py`: A Python script that automates the generation of 25 PDFs (one for each hour) in `hourly_pdfs/` to test the transition logic.
- `template.tex`: The LaTeX template used by the generator script.

## How to Use

A full working example is provided in `Color_Example.tex`.

First, import the `xcolor`, `xfp`, and `datetime2` packages.

### Automatic Mode
Place `Color.tex` in an accessible directory and add the following to your preamble:
```latex
\input{<path to Color.tex>}
```

If  `Color.tex` is in your project directory:
```latex
\input{Color.tex}
```

The document will now use the current system time to determine its color scheme.

### Manual Mode

To force a page/document to adapt to a hardcoded time, 9:00 PM (hour 21), define the hour before inputting the color file:
```latex
\def\currenthour{<time as decimal between 0.00 and 24.00>}
\input{<path to Color.tex>}
```

## Making Adjustments
To customize the behavior of the adaptive theme, modify these variables within `Color.tex`:

| Variable | Description | Effect |
| --- | --- | --- |
| `\wake` | The midpoint (hour) where the mode transitions from dark to light. | Sets the start of the "daytime" profile. |
| `\sleep` | The midpoint (hour) where the mode transitions from light to dark. | Sets the start of the "nighttime" profile. If not exactly \wake + 12, a (minor) color jump will occur at midnight. |
| `\contrastradius` | Minimum normalized contrast difference (0.0-0.5). | 0.0 gives a smooth transition over time (cosine). 0.5 creates a sharp, instant step between day and night modes. |
| `\yellowfactor` | Strength of the blue light filter (0.0-1.0). | 0.0 maintains original hues. 1.0 applies maximum yellow tint to the background. |
| `\mypaperhue` | Base hue for the paper background (0-360). | Adjusts the color cast of the page. [Reference Image](https://en.wikipedia.org/wiki/HSL_and_HSV#/media/File:Hsl-hsv_models.svg) for finer control. |
| `\mypapersat` | Saturation (0-1) of paper. | Lower saturation to 0 for pure grayscale/white paper during daytime. |
| `\mypaperval` | Value (0-1) of paper. | Lowering this slightly limits the peak brightness of whiter pages. |

The text color is automatically calculated to maximize contrast between page and text.